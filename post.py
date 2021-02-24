from datetime import datetime
import hashlib

timeFormat = "%d-%m-%Y %H:%M:%S"

class Post:
	id = None
	text = None
	time = None

	def __init__(self, text, id=None, time=None):
		self.text = text
		if (id == None):
			self.id = self.generateId()
		else:
			self.id = id
		if (time == None):
			self.time = self.generateTime()
		else:
			self.time = datetime.strptime(time, timeFormat)

	def generateId(self):
		return str(hashlib.md5(self.text.encode("utf-8")).hexdigest())

	def generateTime(self):
		return datetime.now().strftime(timeFormat)