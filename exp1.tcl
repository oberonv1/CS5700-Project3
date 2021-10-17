set ns [new Simulator]


# Output tracing
set f [open out_exp1.txt w]
$ns trace-all $f

# Experiment 1 setup
#
#        s1                 s3
#         \                /
# 10Mb TCP \  10 CBR      / 10Mb TCP
#           r1 --------- r2
# 10Mb TCP /               \ 110Mb TCP
#         /                 \
#        s2                 s4 
#

set s1 [$ns node]
set s2 [$ns node]
set r1 [$ns node]
set r2 [$ns node]
set s3 [$ns node]
set s4 [$ns node]

$ns duplex-link $s1 $r1 10Mb 2ms DropTail 
$ns duplex-link $s2 $r1 10Mb 3ms DropTail 
$ns duplex-link $r1 $r2 1.5Mb 20ms RED 
$ns queue-limit $r1 $r2 25
$ns queue-limit $r2 $r1 25
$ns duplex-link $s3 $r2 10Mb 4ms DropTail 
$ns duplex-link $s4 $r2 10Mb 5ms DropTail 

$ns duplex-link-op $s1 $r1 orient right-down
$ns duplex-link-op $s2 $r1 orient right-up
$ns duplex-link-op $r1 $r2 orient right
$ns duplex-link-op $r1 $r2 queuePos 0
$ns duplex-link-op $r2 $r1 queuePos 0
$ns duplex-link-op $s3 $r2 orient left-down
$ns duplex-link-op $s4 $r2 orient left-up



$ns at 20.0 "finish"

proc finish {} {
        global ns f 
        $ns flush-trace
        close $f

        puts "Experiment 1 simulation completed."
        exit 0
}

$ns run