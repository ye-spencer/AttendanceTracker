import sys

class date (object):
	def __init__(self, strng):
		self.string = strng
		self.traits = strng[strng.index(" ") + 1:].split(":")
		self.traits[2] = self.traits[2][0:2]
		if strng[-2] == 'P':
			self.traits[0] = int(self.traits[0]) % 12 + 12
		if strng[-2] == 'A':
			self.traits[0] = int(self.traits[0]) % 12
	def hour(self):
		return int(self.traits[0])
	def minute(self):
		return int(self.traits[1])
	def second(self):
		return int(self.traits[2])
	def compareto(self, fles):
		if (self.hour() > fles.hour()):
			return 1
		elif (self.hour() < fles.hour()):
			return -1
		else:
			if self.minute() > fles.minute():
				return 1
			elif self.minute() < fles.minute():
				return -1
			else:
				if self.second() > fles.second():
					return 1
				elif self.second() < fles.second():
					return -1
		return 0
	def tostring(self):
		return self.string

class entry(object):
	def __init__ (self, inp):
		self.traits = inp.split(",")
	def getfirstname(self):
		name = self.traits[0]
		name = name[0:name.index(" ")]
		return name
	def getlastname(self):
		name = self.traits[0]
		name = name[name.index(" ") + 1:]
		return name
	def getstart(self):
		return date(self.traits[2])
	def getleft(self):
		return date(self.traits[3])
	def gettime(self):
		return int(self.traits[4][:-1])

class studentInfo(object):
	def __init__(self):
		self.earliestStart = None
		self.latestLeft = None
		self.totalTime = 0
	def update(self, entry):
		if (self.earliestStart == None):
			self.earliestStart = entry.getstart()
		else:
			if (self.earliestStart.compareto(entry.getstart()) > 0):
				self.earliestStart = entry.getstart()
		if (self.latestLeft == None):
			self.latestLeft = entry.getleft()
		else:
			if self.latestLeft.compareto(entry.getleft()) < 0:
				self.latestLeft = entry.getleft()
		self.totalTime += entry.gettime()

	def getEarliest(self):
		return self.earliestStart
	def getLatest(self):
		return self.latestLeft
	def getTotalTime(self):
		return self.totalTime
	def tostring(self):
		return "\t%s\t\t%s\t\t%d" % (self.getEarliest().tostring(), self.getLatest().tostring(), self.getTotalTime())

def run(inFileName, outFileName):
	inFile = open(inFileName, "r")
	outFile = open(outFileName, "w")
	studentDict = {}
	firstLine = True
	for inp in inFile.readlines():
		if firstLine:
			firstLine = False
		else:
			myEntry = entry(inp)
			name = myEntry.getlastname().ljust(25, " ") + " " + myEntry.getfirstname()
			if name in studentDict:
				studentDict[name].update(myEntry)
			else:
				studentDict[name] = studentInfo()
				studentDict[name].update(myEntry)
	for name in sorted(studentDict.keys()):
		outFile.write((name.ljust(40, " ") + studentDict[name].tostring() + "\n"))

if __name__ == "__main__":
	inFile = sys.argv[1]
	outFile = sys.argv[2]
	run(sys.argv[1], sys.argv[2])