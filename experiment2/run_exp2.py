import os

tcp_types = ["reno_reno", "new_reno_reno", "new_reno_vegas", "vegas_vegas"]
tcl_tcp_pairs = [("TCP/Newreno","TCP/Reno"),("TCP/Reno","TCP/Reno"),("TCP/Newreno","TCP/Vegas"),("TCP/Vegas","TCP/Vegas")]

for tcp_index in range(0,len(tcp_types)):
    for n in range(1,11):
        output_file = tcp_types[tcp_index]+ "_" + str(n) + "mb_exp2"
        command = "ns exp2.tcl " + tcl_tcp_pairs[tcp_index][0] + " " + tcl_tcp_pairs[tcp_index][1] + " " + str(n) + "Mb " + output_file
        os.system(command)
    
    for n in range(1,11):
        output_file = "rev_" + tcp_types[tcp_index]+ "_" + str(n) + "mb_exp2"
        command = "ns exp2.tcl " + tcl_tcp_pairs[tcp_index][1] + " " + tcl_tcp_pairs[tcp_index][0] + " " + str(n) + "Mb " + output_file
        os.system(command)