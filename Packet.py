class Packet:

    def __init__(self, time, ip_length, ttl, source_ip, dest_ip, icmp_type, sequence_num, data_size):
        self.time = time,
        self.ip_length = ip_length
        self.ttl = ttl
        self.source_ip = source_ip
        self.dest_ip = dest_ip
        self.icmp_type = icmp_type
        self.sequence_num = sequence_num
        self.data_size = data_size

    
