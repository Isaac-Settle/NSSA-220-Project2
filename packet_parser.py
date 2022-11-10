import re
from Packet import Packet

def get_ip_string(hex_bytes):
	IP = ""
	for i in range(len(hex_bytes)):
		IP += str(int(hex_bytes[i],16)) 
		if (i < 3): IP += "."
	return IP

def convert_hex_to_int(hex_bytes):
	full_bytes = ""
	for byte in hex_bytes:
		full_bytes += byte
	value = int(full_bytes,16)
	return value

def parse(filename):
	packets = []
	f = open(filename)
	line = f.readline()
	while line:
		if (line[:3] == "No."):
			line = f.readline().strip()
			# split whenever there is 2 or more spaces
			split = re.split(' {2,}', line) 

			time = float(split[0].split(' ')[1])

			f.readline()
			line = f.readline().strip()


			# reads the hex data into a list
			hex_bytes = []
			while line:
				split = re.split(' {2,}', line)
				hex_bytes += split[1].split(' ')
				line = f.readline().strip()

			ip_length = convert_hex_to_int(hex_bytes[16:18])
			ttl = convert_hex_to_int(hex_bytes[22])
			source_ip = get_ip_string(hex_bytes[26:30])
			dest_ip = get_ip_string(hex_bytes[30:34])
			icmp_type = convert_hex_to_int(hex_bytes[34])
			sequence_num = convert_hex_to_int(hex_bytes[40:42])
			data_size = len(hex_bytes[42:])

			p = Packet(
				time,
				ip_length,
				ttl,
				source_ip,
				dest_ip,
				icmp_type,
				sequence_num,
				data_size
			)
			packets.append(p)

		line = f.readline()
	return packets

#parse()
