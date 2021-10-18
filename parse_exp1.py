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



with open(args.data_file) as file:
    contents = file.readlines()
    for line in contents:
        event, time,from_node,to_node,pkt_typ,pkt_sze,flags,fid,src_adr,dst_adr,seq_num,pkt_id = line.split(' ')
        if pkt_typ == 'tcp':
            # pkt_id will route through several node pairs on the way to TCP sink
            # make map key neighboring node path + pkt_id, garaunteed unique
            if event == 'r':
                recMap[from_node + ":" + to_node + ":" + pkt_id] = time
            elif event == '-':
                dequeueMap[from_node + ":" + to_node + ":" + pkt_id] = time
            elif event == 'd':
                drops += 1

sum_latency = 0
for key, dequeue_time in dequeueMap.items():
    if key in recMap:
        sum_latency += float(recMap[key]) - float(dequeue_time)
avg_latency = sum_latency/len(recMap)

# TCP flow ran from 0.6 to 9.5 seconds
# only count recieved TCP packets / second
avg_thput = float(len(recMap)) / 8.9

print(avg_latency)
print(avg_thput)
print(drops)