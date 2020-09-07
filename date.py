class date (object):
	def __init__(self, str):
		self.traits = str[str.index(" ") + 1:].split(":")
		self.traits[2] = self.traits[2][0:2]
		if str[-2] == 'P':
			self.traits[0] = int(self.traits[0]) + 12
		print(self.traits)
	def hour(self):
		return int(self.traits[0])
	def minute(self):
		return int(self.traits[1])
	def second(self):
		return int(self.traits[2])
	def compareto(self, fles): #returns 1 for greater, 0 for equal, -1 for less than
		if (self.hour() > fles.hour()) 
			return 1
		else if (self.hour() < fles.hour()) 
			return -1
		else:
			if self.minute() > fles.minute():
				return 1
			else if self.minute() < fles.minute():
				return -1
			else:
				if self.second() > fles.second():
					return 1
				else if self.second() < fles.second():
					return -1
		return 0



