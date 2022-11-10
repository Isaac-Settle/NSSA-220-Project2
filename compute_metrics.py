from Packet import Packet


def calc_num_echo_req_replies_sent(node_list, source_node_ip):
    num_requests = 0
    num_replies = 0
    for packet in node_list:
        if (packet.source_ip == source_node_ip and packet.icmp_type == 8):
            num_requests += 1
        elif (packet.source_ip == source_node_ip and packet.icmp_type == 0):
            num_replies += 1
    return num_requests, num_replies






def compute(node1_list, node2_list, node3_list, node4_list):
    #Compute method take in 4 lists, each corresponding to a node. This function will compute metrics for each of the node files using the list passed in.
    
    #Variables
    node1_ip = "192.168.100.1" 
    node2_ip = "192.168.100.2"
    node3_ip = "192.168.200.1"
    node4_ip = "192.168.200.2"
  
    
    # Do computations for each node
    # Node 1

    n1_requests, n1_replies = calc_num_echo_req_replies_sent(node1_list, node1_ip)
    print(n1_requests,n1_replies,sep="\t")



    # Node 2
    # Node 3
    # Node 4
    
        #Output to a CSV file
