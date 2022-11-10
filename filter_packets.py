import re
import sys
def filter(filename):
	length = len(filename)
	write = open(filename[0:length-4] + "_filtered.txt", 'w')
	sys.stdout = write
	with open(filename) as file:
		prevLine = ""
		for line in file:
			if re.search('Echo', line) != None:
				print(prevLine.strip("\n"))
				print(line.strip("\n"))
				var = True
				increment = 0
				while(var and increment<1):
					line = file.readline()
					if(re.search('No.', line) == None):
						print(line.strip("\n"))
					else:
						var = False
					if(line==""):
						increment+=1
			prevLine = line
			# do things
	write.close()

def main():
	filter("Captures/Node1.txt")
	filter("Captures/Node2.txt")
	filter("Captures/Node3.txt")
	filter("Captures/Node4.txt")

if __name__ == "__main__":
	main()
