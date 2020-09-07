from date import date

class entry(object):
	def __init__ (self, inp):
		self.traits = inp.split(",")
		#print(self.getstart())
	def getfirstname(self):
		name = self.traits[0]
		name = name[0:name.index(" ")]
		return name
	def getlastname(self):
		name = self.traits[0]
		name = name[name.index(" "):]
		return name
	def getstart(self):
		return date(self.traits[2])
	def getleft(self):
		return date(self.traits[3])
	def gettime(self):
		return int(self.traits[4][:-1])