# This function serves to take in 4 lists, each corresponding to a node. It will compute metrics for 
# each of the node files using the list passed in.

def compute(node1_list, node2_list, node3_list, node4_list):

    # Variables
    node1_ip = "192.168.100.1" 
    node2_ip = "192.168.100.2"
    node3_ip = "192.168.200.1"
    node4_ip = "192.168.200.2"

    node1_reqsent = 0 
    node1_reqrec = 0
    node1_repsent = 0
    node1_reprec = 0
    
    node1_reqbytessent = 0
    node1_reqbytesrec = 0
    node1_reqdatasent = 0
    node1_reqdatarec = 0

    node1_rttsum = 0
    node1_delaysum = 0
    node1_hopsum = 0

    node2_reqsent = 0
    node2_reqrec = 0
    node2_repsent = 0
    node2_reprec = 0
    
    node2_reqbytessent = 0
    node2_reqbytesrec = 0
    node2_reqdatasent = 0
    node2_reqdatarec = 0

    node2_rttsum = 0
    node2_delaysum = 0
    node2_hopsum = 0

    node3_reqsent = 0
    node3_reqrec = 0
    node3_repsent = 0
    node3_reprec = 0
    
    node3_reqbytessent = 0
    node3_reqbytesrec = 0
    node3_reqdatasent = 0
    node3_reqdatarec = 0

    node3_rttsum = 0
    node3_delaysum = 0
    node3_hopsum = 0

    node4_reqsent = 0
    node4_reqrec = 0
    node4_repsent = 0
    node4_reprec = 0
    
    node4_reqbytessent = 0
    node4_reqbytesrec = 0
    node4_reqdatasent = 0
    node4_reqdatarec = 0

    node4_rttsum = 0
    node4_delaysum = 0
    node4_hopsum = 0

    # Computations for each node
    
    # Node 1 --
    for packet in node1_list: #For all packets in node1_packets
        if packet[5] == "request": #if the message is a request
            if packet[2] == node1_ip:#if the source is equal to node1's ip
                node1_reqsent += 1 #add to requests send
                node1_reqbytessent += int(packet[4]) #add to bytes sent
                node1_reqdatasent += (int(packet[4]) - 42) #add to data sent
                time = float(packet[1]) #set times
                corr_packet = packet[6] #set corresponding reply packet
                for pack in node1_list: #for all packets in node1_list
                    if pack[0] == corr_packet: #if the packet id is equal to corresponding packet 
                        corr_time = float(pack[1]) #set time
                rtt = float(corr_time - time) #calc time
                node1_rttsum += rtt #add to total time sum
                if packet[3] == node2_ip: #if the dest is in the network
                    node1_hopsum += 1 #add 1
                else:
                    node1_hopsum += 3 #add 3
            else:#request received
                node1_reqrec += 1 #add to req recieved
                node1_reqbytesrec += int(packet[4]) #add to req bytes
                node1_reqdatarec += (int(packet[4]) - 42) #add to req data
                time = float(packet[1]) #add to time
                corr_packet = packet[6] #set corr_packet
                for pack in node1_list: #for all pakctes
                    if pack[0] == corr_packet: #if the packets id is equal to corresponding packet
                        corr_time = float(pack[1]) #set time
                delay = float(corr_time - time) #set delay
                node1_delaysum += delay #calc depay sum
        else:
            if packet[2] == node1_ip:#reply sent
                node1_repsent += 1 #add to reply sent
            else:#reply received
                node1_reprec += 1 #add to reply recieved

    #Calc Data size and time metrics
    node1_avgrtt = round((float(node1_rttsum / float(node1_reqsent)) * 1000.0), 2) 
    node1_through = round(((float(node1_reqbytessent) / float(node1_rttsum)) / 1000.0), 1)   
    node1_good = round(((float(node1_reqdatasent) / float(node1_rttsum)) / 1000.0), 1)   
    node1_avgdelay = round((float(node1_delaysum / float(node1_reqrec)) * 1000000.0), 2)
    node1_avghops = round(float(node1_hopsum) / float(node1_reqsent), 2)

    # Node 2 --
    for packet in node2_list:
        if packet[5] == "request":
            if packet[2] == node2_ip:
                node2_reqsent += 1
                node2_reqbytessent += int(packet[4])
                node2_reqdatasent += (int(packet[4]) - 42)
                time = float(packet[1])
                corr_packet = packet[6]
                for pack in node2_list:
                    if pack[0] == corr_packet:
                        corr_time = float(pack[1])
                rtt = float(corr_time - time)
                node2_rttsum += rtt
                if packet[3] == node1_ip:
                    node2_hopsum += 1
                else:
                    node2_hopsum += 3
            else:
                node2_reqrec += 1
                node2_reqbytesrec += int(packet[4])
                node2_reqdatarec += (int(packet[4]) - 42)
                time = float(packet[1])
                corr_packet = packet[6]
                for pack in node2_list:
                    if pack[0] == corr_packet:
                        corr_time = float(pack[1])
                delay = float(corr_time - time)
                node2_delaysum += delay
        else:
            if packet[2] == node2_ip:
                node2_repsent += 1
            else:
                node2_reprec += 1

    node2_avgrtt = round((float(node2_rttsum / float(node2_reqsent)) * 1000.0), 2) 
    node2_through = round(((float(node2_reqbytessent) / float(node2_rttsum)) / 1000.0), 1)   
    node2_good = round(((float(node2_reqdatasent) / float(node2_rttsum)) / 1000.0), 1)   
    node2_avgdelay = round((float(node2_delaysum / float(node2_reqrec)) * 1000000.0), 2)
    node2_avghops = round(float(node2_hopsum) / float(node2_reqsent), 2)

    # Node 3 --
    for packet in node3_list:
        if packet[5] == "request":
            if packet[2] == node3_ip:
                node3_reqsent += 1
                node3_reqbytessent += int(packet[4])
                node3_reqdatasent += (int(packet[4]) - 42)
                time = float(packet[1])
                corr_packet = packet[6]
                for pack in node3_list:
                    if pack[0] == corr_packet:
                        corr_time = float(pack[1])
                rtt = float(corr_time - time)
                node3_rttsum += rtt
                if packet[3] == node4_ip:
                    node3_hopsum += 1
                else:
                    node3_hopsum += 3
            else:
                node3_reqrec += 1
                node3_reqbytesrec += int(packet[4])
                node3_reqdatarec += (int(packet[4]) - 42)
                time = float(packet[1])
                corr_packet = packet[6]
                for pack in node3_list:
                    if pack[0] == corr_packet:
                        corr_time = float(pack[1])
                delay = float(corr_time - time)
                node3_delaysum += delay
        else:
            if packet[2] == node3_ip:
                node3_repsent += 1
            else:
                node3_reprec += 1

    node3_avgrtt = round((float(node3_rttsum / float(node3_reqsent)) * 1000.0), 2) 
    node3_through = round(((float(node3_reqbytessent) / float(node3_rttsum)) / 1000.0), 1)   
    node3_good = round(((float(node3_reqdatasent) / float(node3_rttsum)) / 1000.0), 1)   
    node3_avgdelay = round((float(node3_delaysum / float(node3_reqrec)) * 1000000.0), 2)
    node3_avghops = round(float(node3_hopsum) / float(node3_reqsent), 2)

    # Node 4 --
    for packet in node4_list:
        if packet[5] == "request":
            if packet[2] == node4_ip:
                node4_reqsent += 1
                node4_reqbytessent += int(packet[4])
                node4_reqdatasent += (int(packet[4]) - 42)
                time = float(packet[1])
                corr_packet = packet[6]
                for pack in node4_list:
                    if pack[0] == corr_packet:
                        corr_time = float(pack[1])
                rtt = float(corr_time - time)
                node4_rttsum += rtt
                if packet[3] == node3_ip:
                    node4_hopsum += 1
                else:
                    node4_hopsum += 3
            else:
                node4_reqrec += 1
                node4_reqbytesrec += int(packet[4])
                node4_reqdatarec += (int(packet[4]) - 42)
                time = float(packet[1])
                corr_packet = packet[6]
                for pack in node4_list:
                    if pack[0] == corr_packet:
                        corr_time = float(pack[1])
                delay = float(corr_time - time)
                node4_delaysum += delay
        else:
            if packet[2] == node4_ip:
                node4_repsent += 1
            else:
                node4_reprec += 1

    node4_avgrtt = round((float(node4_rttsum / float(node4_reqsent)) * 1000.0), 2) 
    node4_through = round(((float(node4_reqbytessent) / float(node4_rttsum)) / 1000.0), 1)   
    node4_good = round(((float(node4_reqdatasent) / float(node4_rttsum)) / 1000.0), 1)   
    node4_avgdelay = round((float(node4_delaysum / float(node4_reqrec)) * 1000000.0), 2)
    node4_avghops = round(float(node4_hopsum) / float(node4_reqsent), 2)
    
    # Output to a CSV file --
    with open("../output.csv", 'r+') as output:
        output.truncate(0)
        output.write("Node 1\n\nEcho Requests Sent,Echo Requests Received,Echo Replies Sent,Echo Replies Received\n")
        output.write(str(node1_reqsent) + "," + str(node1_reqrec) + "," + str(node1_repsent) + "," + str(node1_reprec) + "\n") 
        output.write("Echo Request Bytes Sent (bytes),Echo Request Data Sent (bytes)\n")
        output.write(str(node1_reqbytessent) + "," + str(node1_reqdatasent) + "\n")
        output.write("Echo Request Bytes Received (bytes),Echo Request Data Received (bytes)\n")
        output.write(str(node1_reqbytesrec) + "," + str(node1_reqdatarec) + "\n\n")
        output.write("Average RTT (milliseconds)," + str(node1_avgrtt) + "\n")
        output.write("Echo Request Throughput (kB/sec)," + str(node1_through) + "\n")
        output.write("Echo Request Goodput (kB/sec)," + str(node1_good) + "\n")
        output.write("Average Replay Delay (microseconds)," + str(node1_avgdelay) + "\n")
        output.write("Average Echo Request Hop Count," + str(node1_avghops) + "\n\n")

        output.write("Node 2\n\nEcho Requests Sent,Echo Requests Received,Echo Replies Sent,Echo Replies Received\n")
        output.write(str(node2_reqsent) + "," + str(node2_reqrec) + "," + str(node2_repsent) + "," + str(node2_reprec) + "\n") 
        output.write("Echo Request Bytes Sent (bytes),Echo Request Data Sent (bytes)\n")
        output.write(str(node2_reqbytessent) + "," + str(node2_reqdatasent) + "\n")
        output.write("Echo Request Bytes Received (bytes),Echo Request Data Received (bytes)\n")
        output.write(str(node2_reqbytesrec) + "," + str(node2_reqdatarec) + "\n\n")
        output.write("Average RTT (milliseconds)," + str(node2_avgrtt) + "\n")
        output.write("Echo Request Throughput (kB/sec)," + str(node2_through) + "\n")
        output.write("Echo Request Goodput (kB/sec)," + str(node2_good) + "\n")
        output.write("Average Replay Delay (microseconds)," + str(node2_avgdelay) + "\n")
        output.write("Average Echo Request Hop Count," + str(node2_avghops) + "\n\n")

        output.write("Node 3\nEcho Requests Sent,Echo Requests Received,Echo Replies Sent,Echo Replies Received\n")
        output.write(str(node3_reqsent) + "," + str(node3_reqrec) + "," + str(node3_repsent) + "," + str(node3_reprec) + "\n") 
        output.write("Echo Request Bytes Sent (bytes),Echo Request Data Sent (bytes)\n")
        output.write(str(node3_reqbytessent) + "," + str(node3_reqdatasent) + "\n")
        output.write("Echo Request Bytes Received (bytes),Echo Request Data Received (bytes)\n")
        output.write(str(node3_reqbytesrec) + "," + str(node3_reqdatarec) + "\n\n")
        output.write("Average RTT (milliseconds)," + str(node3_avgrtt) + "\n")
        output.write("Echo Request Throughput (kB/sec)," + str(node3_through) + "\n")
        output.write("Echo Request Goodput (kB/sec)," + str(node3_good) + "\n")
        output.write("Average Replay Delay (microseconds)," + str(node3_avgdelay) + "\n")
        output.write("Average Echo Request Hop Count," + str(node3_avghops) + "\n\n")

        output.write("Node 4\nEcho Requests Sent,Echo Requests Received,Echo Replies Sent,Echo Replies Received\n")
        output.write(str(node4_reqsent) + "," + str(node4_reqrec) + "," + str(node4_repsent) + "," + str(node4_reprec) + "\n") 
        output.write("Echo Request Bytes Sent (bytes),Echo Request Data Sent (bytes)\n")
        output.write(str(node4_reqbytessent) + "," + str(node4_reqdatasent) + "\n")
        output.write("Echo Request Bytes Received (bytes),Echo Request Data Received (bytes)\n")
        output.write(str(node4_reqbytesrec) + "," + str(node4_reqdatarec) + "\n\n")
        output.write("Average RTT (milliseconds)," + str(node4_avgrtt) + "\n")
        output.write("Echo Request Throughput (kB/sec)," + str(node4_through) + "\n")
        output.write("Echo Request Goodput (kB/sec)," + str(node4_good) + "\n")
        output.write("Average Replay Delay (microseconds)," + str(node4_avgdelay) + "\n")
        output.write("Average Echo Request Hop Count," + str(node4_avghops) + "\n")
    output.close()