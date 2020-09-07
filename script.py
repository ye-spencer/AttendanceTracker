from entry import entry

def run(inFileName, outFileName):
	print(inFileName)
	print(outFileName)
	inFile = open(inFileName, "r")
	outFile = open(outFileName, "w")
	#print(inFile.readline())
	firstLine = True
	for inp in inFile.readlines():
		if firstLine:
			firstLine = False
			continue
		else:
			entry(inp)
		#print(inp)
