import post
from datetime import datetime

def createPostFromForm(form):
	formText = form["text"]
	duration = form["duration"]
	public = form.get("public")
	if (public != None):
		public = 1
	else:
		public = 0
	p = post.Post(formText, duration, public)
	return p

def getDisplayStrings(p):
	postSize = len(p.text.encode("utf-8"))
	postTextByLine = p.text.split("\n")
	postTime = datetime.utcfromtimestamp(p.time).strftime("%d-%m-%Y %H:%M:%S") + " UTC"
	return {"postSize": postSize, "postTextByLine": postTextByLine, "postTime": postTime}