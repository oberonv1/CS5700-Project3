import os

tcp_types = ["reno_reno", "new_reno_reno", "new_reno_vegas", "vegas_vegas"]

for tcp in tcp_types:
    for n in range(1,11):
        output_file = tcp + "_" + str(n) + "mb_exp2"
        command = "ns " + tcp + "_exp2.tcl " + str(n) + "Mb " + output_file
        os.system(command)