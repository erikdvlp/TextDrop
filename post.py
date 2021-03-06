import hashlib
import time

class Post:
	id = None
	text = None
	time = None
	duration = None
	public = 1

	def __init__(self, text, duration=3600, public=1, id=None, time=None):
		self.text = text
		self.duration = duration
		if (id == None):
			self.id = self.generateId()
		else:
			self.id = id
		if (time == None):
			self.time = self.generateTime()
		else:
			self.time = time
		self.public = public

	def generateId(self):
		return str(hashlib.md5(self.text.encode("utf-8")).hexdigest())

	def generateTime(self):
		return int(time.time())