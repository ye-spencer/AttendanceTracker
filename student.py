from entry import entry

class studentInfo(object):
	def __init__(self):
		self.earliestStart = None
		self.latestLeft = None
		self.totalTime = 0
	def update(self, entry):
		if (self.earliestStart == None):
			self.earliestStart = entry.getstart()
		else:
			pass
		if (self.latestLeft == None):
			self.latestLeft = entry.getleft()
		else:
			pass
		self.totalTime += entry.gettime()

	def getEarliest(self):
		return self.earliestStart
	def getLatest(self):
		return self.latestLeft
	def getTotalTime(self):
		return self.totalTime
