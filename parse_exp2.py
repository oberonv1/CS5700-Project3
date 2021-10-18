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
recMap1 = {}
recMap2 = {}
drops1 = 0
drops2 = 0
dequeueMap1 = {}
dequeueMap2 = {}

total_dequeued1 = 0
total_dequeued2 = 0


with open(args.data_file) as file:
    contents = file.readlines()
    for line in contents:
        vars = line.split(' ')
        if len(vars) == 12:
            event, time,from_node,to_node,pkt_typ,pkt_sze,flags,fid,src_adr,dst_adr,seq_num,pkt_id = vars
        if pkt_typ == 'tcp' and fid == "1":
            # pkt_id will route through several node pairs on the way to TCP sink
            # count time from dequeue from node 0 to recieved on node 4
            if event == 'r' and from_node == "3" and to_node == "4":
                recMap1[pkt_id] = time
            elif event == '-' and from_node == "0" and to_node == "2":
                dequeueMap1[pkt_id] = time
            elif event == 'd': # packet could be dropped at tcp or cbr flows
                drops1 += 1
        if pkt_typ == 'tcp' and fid == "2":
            if event == 'r' and from_node == "3" and to_node == "5":
                recMap2[pkt_id] = time
            elif event == '-' and from_node == "1" and to_node == "2":
                dequeueMap2[pkt_id] = time
            elif event == 'd':
                drops2 += 1


sum_latency = 0
for key, dequeue_time in dequeueMap1.items():
    if key in recMap1:
        sum_latency += float(recMap1[key]) - float(dequeue_time)
    total_dequeued1 += 1
avg_latency = sum_latency/len(recMap1) if len(recMap1) != 0 else 0

# TCP flow ran from 0.6 to 9.5 seconds
# only count recieved TCP packets / second
avg_thput = len(recMap1) / 9.0
pkt_loss_rate = drops1/total_dequeued1

print("Average Latency for TCP flow 1: ","%.5f" % avg_latency)
print("Average Thoroughput for TCP flow 1 (packets/s):","%.2f" % avg_thput)
print("Packet Loss Rate for TCP flow1:","%.2f" % pkt_loss_rate)


# repeat analysis for tcp flow 2
sum_latency = 0
for key, dequeue_time in dequeueMap2.items():
    if key in recMap2:
        sum_latency += float(recMap2[key]) - float(dequeue_time)
    total_dequeued2 += 1
avg_latency2 = sum_latency/len(recMap2) if len(recMap2) != 0 else 0

avg_thput2 = len(recMap2) / 9.0
pkt_loss_rate2 = drops2/total_dequeued2

print("Average Latency for TCP flow 2 (seconds): ","%.5f" % avg_latency2)
print("Average Thoroughput for TCP flow 2 (packets/s):","%.2f" % avg_thput2)
print("Packet Loss Rate for TCP flow 2:","%.2f" % pkt_loss_rate2)