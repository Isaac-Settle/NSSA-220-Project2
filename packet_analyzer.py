# NSSA 220 - Project 2 - Packet Capture Analysis Tool
# Riley Basile-Benson, Isaac Settle, and Jose Nunez

import filter_packets as f
import packet_parser as p
import compute_metrics as c

f.filter("Captures/Node1.txt")
f.filter("Captures/Node2.txt")
f.filter("Captures/Node3.txt")
f.filter("Captures/Node4.txt")
node1_list = p.parse("Captures\\Node1_filtered.txt")
node2_list = p.parse("Captures\\Node2_filtered.txt")
node3_list = p.parse("Captures\\Node3_filtered.txt")
node4_list = p.parse("Captures\\Node4_filtered.txt")
c.compute(node1_list, node2_list, node3_list, node4_list)
