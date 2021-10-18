import os
import math
import scipy.stats as st
from parse_exp1 import get_metrics

sum_latency = 0
avg_latency_list = []
for n in range(0,100):
    # make CBR flow insignificantly small
    command = "ns basic_tahoe.tcl 1kb tahoe_temp"
    os.system(command)
    avg_latency, _, _ = get_metrics("tahoe_temp")
    sum_latency += avg_latency
    avg_latency_list.append(avg_latency)

# Calculate sample standard deviation
sample_avg_latency = sum_latency / 100.0
sum_variance = 0
for l in avg_latency_list:
    sum_variance += (l - sample_avg_latency)**2
std_dev = math.sqrt(sum_variance / (len(avg_latency_list) -1 ))


# preprogrammed 40 ms simulation latency
expected_avg_latency = 40

# calculate the z-test
zscore = (sample_avg_latency - expected_avg_latency) / std_dev
margin_err = st.norm.cdf(zscore)

output_file = open("stat_results", "w")
output_file.write("Standard Deviation: " + str(std_dev) + "\n")
output_file.write("Sample Average Latency: " + str(sample_avg_latency) + "\n")
output_file.write("Z-Score: " + str(zscore) + "\n")
output_file.write("Margin of Error: " + str(margin_err) + "\n")

output_file.close()