''' input file format: 
event|time|from_node|to_node|pkt_typ|pkt_sze|flags|fid|src_adr|dst_adr|seq#|pkt_id
r 4.498 1 2 cbr 1000 ------- 2 1.0 3.1 548 1030
+ 4.498 2 3 cbr 1000 ------- 2 1.0 3.1 548 1030
- 4.498 2 3 cbr 1000 ------- 2 1.0 3.1 548 1030

r: revcieve (at to_node)
+: enqueue
-: dequeue
d: drop


'''