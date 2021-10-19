import os
from parse_exp2 import get_metrics2


tcp_types = ["reno_reno", "new_reno_reno", "new_reno_vegas", "vegas_vegas"]
tcl_tcp_pairs = [("TCP/Newreno","TCP/Reno"),("TCP/Reno","TCP/Reno"),("TCP/Newreno","TCP/Vegas"),("TCP/Vegas","TCP/Vegas")]

output_file = open("experiment2_results", "w")

for tcp in range(0, len(tcp_types)):
    output_file.write("########## " + tcp_types[tcp] + " ##########\n")
    for n in range(1,11):
        input_filename = tcp_types[tcp] + "_" + str(n) + "mb_exp2"
        (avg_latency, avg_thput, pkt_loss_rate,
        avg_latency2,avg_thput2,pkt_loss_rate2) = get_metrics2("experiment2/"+ input_filename)

        output_file.write("Average Latency for " + tcl_tcp_pairs[tcp][0] + ": " + ("%.5f" % avg_latency) + "\n")
        output_file.write("Average Thoroughput for " + tcl_tcp_pairs[tcp][0] + " (packets/s): " + ("%.2f" % avg_thput) + "\n")
        output_file.write("Packet Loss Rate for " + tcl_tcp_pairs[tcp][0] + ": " + ("%.3f" % pkt_loss_rate) + "\n")

        output_file.write("Average Latency for " + tcl_tcp_pairs[tcp][1] + " (seconds): " + ("%.5f" % avg_latency2) + "\n")
        output_file.write("Average Thoroughput for " + tcl_tcp_pairs[tcp][1] + " (packets/s): " + ("%.3f" % avg_thput2) + "\n")
        output_file.write("Packet Loss Rate for " + tcl_tcp_pairs[tcp][1] + ": " + ("%.3f" % pkt_loss_rate2) + "\n")
        output_file.write("\n\n")

output_file.close()

rev_output_file = open("reverse_experiment2_results", "w")

for tcp in range(0, len(tcp_types)):
    rev_output_file.write("########## reversed " + tcp_types[tcp] + " ##########\n")
    for n in range(1,11):
        input_filename = "rev_" + tcp_types[tcp] + "_" + str(n) + "mb_exp2"
        (avg_latency, avg_thput, pkt_loss_rate,
        avg_latency2,avg_thput2,pkt_loss_rate2) = get_metrics2("experiment2/"+ input_filename)

        rev_output_file.write("Average Latency for " + tcl_tcp_pairs[tcp][1] + ": " + ("%.5f" % avg_latency) + "\n")
        rev_output_file.write("Average Thoroughput for " + tcl_tcp_pairs[tcp][1] + " (packets/s): " + ("%.2f" % avg_thput) + "\n")
        rev_output_file.write("Packet Loss Rate for " + tcl_tcp_pairs[tcp][1] + ": " + ("%.3f" % pkt_loss_rate) + "\n")

        rev_output_file.write("Average Latency for " + tcl_tcp_pairs[tcp][0] + " (seconds): " + ("%.5f" % avg_latency2) + "\n")
        rev_output_file.write("Average Thoroughput for " + tcl_tcp_pairs[tcp][0] + " (packets/s): " + ("%.3f" % avg_thput2) + "\n")
        rev_output_file.write("Packet Loss Rate for " + tcl_tcp_pairs[tcp][0] + ": " + ("%.3f" % pkt_loss_rate2) + "\n")
        rev_output_file.write("\n\n")

rev_output_file.close()