set ns [new Simulator]

if { $argc == 4 } {
    set tcpname1 [lindex $argv 0]
    set tcpname2 [lindex $argv 1]
    set argflow [lindex $argv 2]
    set file [lindex $argv 3]
} else {
    puts "Error: Requires arguments for first TCP flow, second TCP flow, CBR flow rate, and filename for output"
    exit 1
}

puts "Testing $argflow CBR flowrate, $tcpname1 starting first and $tcpname2 starting second"

# Experiment 2 setup
#
#        n1                 n4
#         \                /
# 10Mb TCP \  10Mb CBR    / 10Mb TCP
#           n2 --------- n3
#          /               \
# 10Mb TCP/                 \10Mb TCP
#        n5                 n6 
#

set n1 [$ns node]
set n5 [$ns node]
set n2 [$ns node]
set n3 [$ns node]
set n4 [$ns node]
set n6 [$ns node]

# Output tracing
set f [open $file w]
$ns trace-all $f

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
$cbr0 set rate_ $argflow
$cbr0 attach-agent $udp0

set null0 [new Agent/Null] 
$ns attach-agent $n3 $null0 
$ns connect $udp0 $null0 
$udp0 set fid_ 0



# A FTP over tcpname1 from $n1 to $n4
set tcp1 [$ns create-connection $tcpname1 $n1 TCPSink $n4 1]
$tcp1 set packetSize_ 1000
# manually tested optimal window size to take up entire 10Mb bandwidth
$tcp1 set window_ 110
set ftp1 [$tcp1 attach-source FTP]

# A competing FTP over tcpname2 from $n5 to $n6
set tcp2 [$ns create-connection $tcpname2 $n5 TCPSink $n6 2]
$tcp2 set packetSize_ 1000
# manually tested optimal window size to take up entire 10Mb bandwidth
$tcp2 set window_ 110
set ftp2 [$tcp2 attach-source FTP]

$ns at 0.5 "$cbr0 start"
$ns at 0.6 "$ftp1 start"
$ns at 1 "$ftp2 start"
$ns at 9 "$ftp2 stop"
$ns at 9.4 "$ftp1 stop"
$ns at 9.5 "$cbr0 stop"
$ns at 10.0 "finish"

proc finish {} {
        global ns f tcpname1 tcpname2
        $ns flush-trace
        close $f

        puts "$tcpname1 + $tcpname2 Experiment 2 simulation completed."
        exit 0
}

$ns run