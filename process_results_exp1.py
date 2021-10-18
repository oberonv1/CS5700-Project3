import os
from parse_exp1 import get_metrics


tcp_types = ["tahoe", "reno", "new_reno", "vegas"]

output_file = open("experiment1_results", "w")

for tcp in tcp_types:
    output_file.write("########## " + tcp + " ##########\n")
    for n in range(1,11):
        input_filename = tcp + "_" + str(n) + "mb_exp1"
        avg_latency, avg_thput, pkt_loss_rate = get_metrics("experiment1/"+ input_filename)
        output_file.write(input_filename + "\n")
        output_file.write("Average Latency (seconds): " + ("%.5f" % avg_latency) + "\n")
        output_file.write("Average Thoroughput(packets/s):" + ("%.3f" % avg_thput) + "\n")
        output_file.write("Packet Loss Rate:" + ("%.3f" % pkt_loss_rate) + "\n")
        output_file.write("\n\n")

output_file.close()