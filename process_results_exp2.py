import os
from parse_exp2 import get_metrics2


tcp_types = ["reno_reno", "new_reno_reno", "new_reno_vegas", "vegas_vegas"]

output_file = open("experiment2_results", "w")

for tcp in tcp_types:
    output_file.write("########## " + tcp + " ##########\n")
    for n in range(1,11):
        input_filename = tcp + "_" + str(n) + "mb_exp2"
        (avg_latency, avg_thput, pkt_loss_rate,
        avg_latency2,avg_thput2,pkt_loss_rate2) = get_metrics2("experiment2/"+ input_filename)

        output_file.write("Average Latency for TCP flow 1: " + ("%.5f" % avg_latency) + "\n")
        output_file.write("Average Thoroughput for TCP flow 1 (packets/s):" + ("%.2f" % avg_thput) + "\n")
        output_file.write("Packet Loss Rate for TCP flow1:" + ("%.3f" % pkt_loss_rate) + "\n")

        output_file.write("Average Latency for TCP flow 2 (seconds): " + ("%.5f" % avg_latency2) + "\n")
        output_file.write("Average Thoroughput for TCP flow 2 (packets/s):" + ("%.3f" % avg_thput2) + "\n")
        output_file.write("Packet Loss Rate for TCP flow 2:" + ("%.3f" % pkt_loss_rate2) + "\n")
        output_file.write("\n\n")

output_file.close()