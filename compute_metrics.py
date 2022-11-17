from Packet import Packet


def calc_num_echo_req_replies_sent(node_list, source_node_ip):
    requests = []
    replies = []
    for packet in node_list:
        if (packet.source_ip == source_node_ip and packet.icmp_type == 8):
            requests.append(packet)
        elif (packet.source_ip == source_node_ip and packet.icmp_type == 0):
            replies.append(packet)
    return requests, replies


def calc_num_echo_req_replies_recvd(node_list, node_ip):
    requests_recvd = []
    replies_recvd = []
    for packet in node_list:
        if (packet.dest_ip == node_ip and packet.icmp_type == 8):
            requests_recvd.append(packet)
        elif (packet.dest_ip == node_ip and packet.icmp_type == 0):
            replies_recvd.append(packet)
    return requests_recvd, replies_recvd


def calc_request_bytes(requests_sent, requests_recvd):
    ETHERNET_HEADER_LENGTH = 14
    bytes_requests_sent = 0
    bytes_requests_recvd = 0
    bytes_requests_data_recvd = 0
    bytes_requests_data_sent = 0

    for packet in requests_sent:
        bytes_requests_sent += (ETHERNET_HEADER_LENGTH +
                                packet.ip_length)
        bytes_requests_data_sent += packet.data_size

    for packet in requests_recvd:
        bytes_requests_recvd += (ETHERNET_HEADER_LENGTH +
                                 packet.ip_length)
        bytes_requests_data_recvd += packet.data_size

    return bytes_requests_sent, bytes_requests_data_sent, bytes_requests_recvd, bytes_requests_data_recvd


def calc_rtt(requests_sent, replies_recvd):
    total_rtt = 0
    num_trips = 0
    for request in requests_sent:
        for reply in replies_recvd:
            if (reply.sequence_num == request.sequence_num):
                total_rtt += (reply.time - request.time)
                num_trips += 1
    return (total_rtt/num_trips)*1000


def calc_reply_delay(requests_recvd, replies_sent):
    reply_delay = 0
    num_replies = 0
    for request_in in requests_recvd:
        for reply_out in replies_sent:
            if (request_in.sequence_num == reply_out.sequence_num):
                reply_delay += (reply_out.time - request_in.time)
                num_replies += 1
    return reply_delay/num_replies


def calc_average_hop_count(requests_recvd):
    STANDARD_TTL = 128
    total_ttl = 0
    num_ttl = 0
    for request in requests_recvd:
        total_ttl += (STANDARD_TTL - request.ttl) + 1
        num_ttl += 1
    return total_ttl/num_ttl


def compute(node1_list, node2_list, node3_list, node4_list):
    # Compute method take in 4 lists, each corresponding to a node. This function will compute metrics for each of the node files using the list passed in.

    # Variables
    NODE1_IP = "192.168.100.1"
    NODE2_IP = "192.168.100.2"
    NODE3_IP = "192.168.200.1"
    NODE4_IP = "192.168.200.2"

    # Do computations for each node
    # Node 1

    n1_requests_s, n1_replies_s = calc_num_echo_req_replies_sent(
        node1_list, NODE1_IP)
    n1_requests_r, n1_replies_r = calc_num_echo_req_replies_recvd(
        node1_list, NODE1_IP)

    print("Echo Requests Sent,Echo Requests Received,Echo Replies Sent,Echo Replies Received")
    print(len(n1_requests_s), len(n1_requests_r),
          len(n1_replies_s), len(n1_replies_r), sep=",")
    request_bytes_sent, request_data_sent, request_bytes_recvd, request_data_recvd = calc_request_bytes(
        n1_requests_s, n1_requests_r)

    print("Echo Request Bytes Sent (bytes),Echo Request Data Sent (bytes)")
    print(request_bytes_sent, request_data_sent, sep=',')
    print("Echo Request Bytes Received (bytes),Echo Request Data Received (bytes)")
    print(request_bytes_recvd, request_data_recvd, sep=',', end="\n\n")
    rtt = calc_rtt(n1_requests_s,n1_replies_r)
    print("Average RTT (milliseconds),{:.2f}".format(rtt))
    print("Echo Request Throughput (kB/sec),{:.1f}".format(request_bytes_sent/(rtt*len(n1_requests_s))))
    print("Echo Request Goodput (kB/sec),{:.1f}".format(request_data_sent/(rtt*len(n1_requests_s))))
    print("Average Reply Delay (microseconds),{:.2f}".format(calc_reply_delay(n1_requests_r, n1_replies_s)*(10**6)))
    print("Average Echo Request Hop Count,{:.2f}".format(calc_average_hop_count(n1_requests_r)))

    # Node 2

    # n2_requests, n2_replies = calc_num_echo_req_replies_sent(
    #     node2_list, node2_ip)
    # n3_requests, n3_replies = calc_num_echo_req_replies_sent(
    #     node3_list, node3_ip)
    # n4_requests, n4_replies = calc_num_echo_req_replies_sent(
    #     node4_list, node4_ip)
    # print(n2_requests, n2_replies, sep="\t")
    # print(n3_requests, n3_replies, sep="\t")
    # print(n4_requests, n4_replies, sep="\t")

    # Node 3
    # Node 4

    # Output to a CSV file
