set ns [new Simulator]

# Experiment 1 setup
#
#        n1                 n4
#         \                /
# 10Mb TCP \  10Mb CBR    / 10Mb TCP
#           n2 --------- n3
#          /               \
#         /                 \
#        n5                 n6 
#

# Output tracing
set f [open reno_10mb_exp1.txt w]
$ns trace-all $f

set n1 [$ns node]
set n5 [$ns node]
set n2 [$ns node]
set n3 [$ns node]
set n4 [$ns node]
set n6 [$ns node]


$ns duplex-link $n1 $n2 10Mb 10ms DropTail 
$ns duplex-link $n5 $n2 10Mb 10ms DropTail 
$ns duplex-link $n2 $n3 10Mb 20ms DropTail 
$ns duplex-link $n4 $n3 10Mb 10ms DropTail 
$ns duplex-link $n6 $n3 10Mb 10ms DropTail 
$ns queue-limit $n2 $n3 25
$ns queue-limit $n3 $n2 25


#Create a UDP agent and attach it to node n0
set udp0 [new Agent/UDP]
$ns attach-agent $n2 $udp0

# Create a CBR traffic source and attach it to udp0
set cbr0 [new Application/Traffic/CBR]
$cbr0 set packetSize_ 1000
$cbr0 set rate_ 10MB
$cbr0 attach-agent $udp0

set null0 [new Agent/Null] 
$ns attach-agent $n3 $null0 
$ns connect $udp0 $null0 
$udp0 set fid_ 0



# A FTP over TCP/Reno from $n1 to $n4
set tcp [$ns create-connection TCP/Reno $n1 TCPSink $n4 1]
$tcp set packetSize_ 1000
set ftp [$tcp attach-source FTP]

$ns at 0.5 "$cbr0 start"
$ns at 0.6 "$ftp start"
$ns at 9.4 "$ftp stop"
$ns at 9.5 "$cbr0 stop"
$ns at 10.0 "finish"

proc finish {} {
        global ns f 
        $ns flush-trace
        close $f

        puts "Experiment 1 simulation completed."
        exit 0
}

$ns run