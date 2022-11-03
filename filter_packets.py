import re
def filter():
	filename = r"Captures\Node1.txt"
	with open(filename) as file:
		for line in file:
			if re.findall("Echo (ping) Request", line):
				print(line)
			# do things

filter()
