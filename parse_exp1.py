''' input file format: 
event|time|from_node|to_node|pkt_typ|pkt_sze|flags|fid|src_adr|dst_adr|seq#|pkt_id
r 4.498 1 2 cbr 1000 ------- 2 1.0 3.1 548 1030
+ 4.498 2 3 cbr 1000 ------- 2 1.0 3.1 548 1030
- 4.498 2 3 cbr 1000 ------- 2 1.0 3.1 548 1030

r: revcieve (at to_node)
+: enqueue
-: dequeue
d: drop


'''

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("data_file", type=str, help="Output file from ns simulation")

args = parser.parse_args()

# to calculate average latency
recMap = {}
drops = 0
dequeueMap = {}

#total dequeued from TCP source
total_dequeued = 0


with open(args.data_file) as file:
    contents = file.readlines()
    for line in contents:
        vars = line.split(' ')
        if len(vars) == 12:
            event, time,from_node,to_node,pkt_typ,pkt_sze,flags,fid,src_adr,dst_adr,seq_num,pkt_id = vars
        if pkt_typ == 'tcp':
            # pkt_id will route through several node pairs on the way to TCP sink
            # count time from dequeue from node 0 to recieved on node 4
            if event == 'r' and from_node == "3" and to_node == "4":
                recMap[pkt_id] = time
            elif event == '-' and from_node == "0" and to_node == "2":
                dequeueMap[pkt_id] = time
        if event == 'd': # packet could be dropped at tcp or cbr flows
            drops += 1

sum_latency = 0
for key, dequeue_time in dequeueMap.items():
    if key in recMap:
        sum_latency += float(recMap[key]) - float(dequeue_time)
    total_dequeued += 1
avg_latency = sum_latency/len(recMap) if len(recMap) != 0 else 0

# TCP flow ran from 0.5 to 9.5 seconds
# only count recieved TCP packets / second
avg_thput = len(recMap) / 9.0
pkt_loss_rate = drops/total_dequeued

print("Average Latency (seconds): ","%.5f" % avg_latency)
print("Average Thoroughput(packets/s):","%.2f" % avg_thput)
print("Packet Loss Rate:","%.2f" % pkt_loss_rate)