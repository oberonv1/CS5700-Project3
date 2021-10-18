import os

tcp_types = ["tahoe", "reno", "new_reno", "vegas"]

for tcp in tcp_types:
    for n in range(1,11):
        output_file = tcp + "_" + str(n) + "mb_exp1"
        command = "ns " + tcp + "_exp1.tcl " + str(n) + "Mb " + output_file
        os.system(command)