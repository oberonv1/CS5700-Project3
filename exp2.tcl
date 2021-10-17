set ns [new Simulator]


# Output tracing
set f [open out_exp1.txt w]
$ns trace-all $f

# Experiment 1 setup
#
#        n1                 n4
#         \                /
# 10Mb TCP \  10 CBR      / 10Mb TCP
#           n2 --------- n3
# 10Mb TCP /               \ 10Mb TCP
#         /                 \
#        n5                 n6 
#

set n1 [$ns node]
set n5 [$ns node]
set n2 [$ns node]
set n3 [$ns node]
set n4 [$ns node]
set n6 [$ns node]

$ns duplex-link $n1 $n2 10Mb 2ms DropTail 
$ns duplex-link $n5 $n2 10Mb 3ms DropTail 
$ns duplex-link $n2 $n3 1.5Mb 20ms RED 
$ns queue-limit $n2 $n3 25
$ns queue-limit $n3 $n2 25
$ns duplex-link $n4 $n3 10Mb 4ms DropTail 
$ns duplex-link $n6 $n3 10Mb 5ms DropTail 

$ns duplex-link-op $n1 $n2 orient right-down
$ns duplex-link-op $n5 $n2 orient right-up
$ns duplex-link-op $n2 $n3 orient right
$ns duplex-link-op $n2 $n3 queuePos 0
$ns duplex-link-op $n3 $n2 queuePos 0
$ns duplex-link-op $n4 $n3 orient left-down
$ns duplex-link-op $n6 $n3 orient left-up



$ns at 20.0 "finish"

proc finish {} {
        global ns f 
        $ns flush-trace
        close $f

        puts "Experiment 1 simulation completed."
        exit 0
}

$ns run