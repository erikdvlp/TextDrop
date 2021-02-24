import datetime
import hashlib

class Post:
	id = None
	text = None
	time = None

	def __init__(self, text, id=None, time=None):
		self.id = id
		self.text = text
		self.time = time
		if (id == None):
			self.id = self.generateId()
		if (time == None):
			self.time = self.generateTime()

	def generateId(self):
		return str(hashlib.md5(self.text.encode("utf-8")).hexdigest())

	def generateTime(self):
		return datetime.datetime.now()