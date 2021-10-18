# CS5700-Project3
## General Approach:
Try out no CBR + 1 TCP flow to check inherent NS simulation delay by analyzing RTT between pairs of nodes. Consider delay when there is CBR flow, normalized when latency is averaged in the data. Add RTT of 40ms to emulate real traffic data across US for final experiment setup
Always start TCP first. Wait until TCP reaches saturation (flow reaches 10 Mbps). Check delay by checking RTT of 1 packet between nodes. We plan on using CBR as main traffic generator. (could try others if time permits, e.g. a different UDP flow )
Start with 1000 samples of randomly seeded CBR comparisons for each experiment and find median, mean, and standard deviations. Then perform a Z-Test to find statistical significance.

## Experiment 1 Procedure: 
TCP should run until saturation. Then increase CBR flow 1 Mbps and wait until TCP flow reaches saturation to collect results. Repeat until CBR reaches 10 Mbps. 
Some TCP algorithms are going to recover better in congested traffic while dropping less packets due to fast recovery or faster congestion detection.
Plan to show average bandwidth, packet drops, throughput over time, RTT (average and over time) as main variables to monitor. Sequence numbers and the congestion window size will be analyzed but will not be the main focus.

## Experiment 2 Procedure: 
- Reno/Reno = Delay one after first one saturates. Congestion affects both at the same time. Do not start at the same time as which TCP flow is affected first may be non-deterministic since they use the same congestion algorithms.
- NewReno/Reno = NewReno saturates first due to fast recovery. Run one where Reno starts first, then run the other. Take the average stats from starting NewReno first repeated 100 times, then Reno starting first repeated 100 times.
- Vegas/Vegas = Deploy one until saturation. Will have less dropped packets than Reno/Reno due to fast delay detection. Do not start at the same time as which TCP flow is affected first may be non-deterministic since they use the same congestion algorithms.
- NewReno/Vegas = Vegas always backs off congestion window first. Run 100 runs of NewReno first, then run 100 runs of Vegas first and take the average of the results. 
