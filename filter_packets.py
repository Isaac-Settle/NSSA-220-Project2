import re
def filter():
	filename = "Captures/example.txt"
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

filter()
