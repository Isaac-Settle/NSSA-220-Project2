# NSSA 220 - Project 2 - Packet Capture Analysis Tool
# Riley Basile-Benson, Isaac Settle, and Jose Nunez


from filter_packets import *
from packet_parser import *
from compute_metrics import *

#filter()
node1_list = parse("Captures\\Node1_filtered.txt")
node2_list = parse("Captures\\Node2_filtered.txt")
node3_list = parse("Captures\\Node3_filtered.txt")
node4_list = parse("Captures\\Node4_filtered.txt")
compute(node1_list, node2_list, node3_list, node4_list)
