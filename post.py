from datetime import datetime
import hashlib
import time

#timeFormat = "%d-%m-%Y %H:%M:%S"

class Post:
	id = None
	text = None
	time = None
	duration = None
	public = True

	def __init__(self, text, duration=3600, id=None, time=None, public=True):
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