"""
A module to filter through packets and output only request and replies to a file.

@author Isaac Settle
"""
import re
import sys
def filter(filename):
	"""
	Filters through packets and anytime a request or reply packet 
	is found it writes to a file with the entire packet.
	"""
	length = len(filename)
	write = open(filename[0:length-4] + "_filtered.txt", 'w')
	sys.stdout = write
	with open(filename) as file:
		prevLine = ""
		for line in file:

			# Uses regex to search for if a line contains 'Echo'. If the line does contain it the line will not be None. 
			if re.search('Echo', line) != None:
				print(prevLine.strip("\n"))
				print(line.strip("\n"))
				var = True
				increment = 0
				while(var and increment<1):
					line = file.readline()

					# Specifically adds functionality to remove the new line from the first line of a packet.
					if(re.search('No.', line) == None):
						print(line.strip("\n"))
					else:
						var = False
					if(line==""):
						increment+=1

			# Used to store the previous line in the scenario where the packet is a request / reply 
			# and needs to print the entire packet INCLUDING the first line.
			prevLine = line 
			
	write.close()

def main():
	filter("Captures/Node1.txt")
	filter("Captures/Node2.txt")
	filter("Captures/Node3.txt")
	filter("Captures/Node4.txt")

if __name__ == "__main__":
	main()
