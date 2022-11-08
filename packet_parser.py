import re

def get_ip_string(hex_bytes):
	IP = ""
	for i in range(len(hex_bytes)):
		IP += str(int(hex_bytes[i],16)) 
		if (i < 3): IP += "."
	return IP



def parse() :
	ethernet2_header_length = 14

	f = open('Captures\example.txt')
	line = f.readline()
	while line:
		if (line[:3] == "No."):
			line = f.readline().strip()
			# split whenever there is 2 or more spaces
			split = re.split(' {2,}', line) 
			#num = int(split[0])

			# time = float(split[1])
			# source = split[2]
			# destination = split[3]
			# protocol = split[4]
			# length = int(split[5])
			# info_name = split[6]
			# info_data = split[7]


			f.readline()
			line = f.readline().strip()

			hex_bytes = []
			while line:
				split = re.split(' {2,}', line)
				hex_bytes += split[1].split(' ')
				line = f.readline().strip()

			sourceIP = getIPString(hex_bytes[26:30])
			destIP = getIPString(hex_bytes[30:34])

			print(sourceIP)
			print(destIP)
			#destIP = 

			print(hex_bytes)

		line = f.readline()

parse()