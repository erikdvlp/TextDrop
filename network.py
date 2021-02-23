import sqlite3

dbDir = "db/textdrop.db"

def init():
	try:
		with open(dbDir) as f:
			pass
	except IOError:
		conn = sqlite3.connect(dbDir)
		c = conn.cursor()
		c.execute("create table posts (postId varchar(32), postText varchar)")
		conn.commit()
		conn.close()

def createPost(postId, postText):
	conn = sqlite3.connect(dbDir)
	c = conn.cursor()
	c.execute("insert into posts values (?, ?)", (postId, postText))
	conn.commit()
	conn.close()

def getPost(postId):
	conn = sqlite3.connect(dbDir)
	c = conn.cursor()
	c.execute("select postText from posts where postId=?", (postId,))
	postText = c.fetchone()[0]
	conn.close()
	return postText