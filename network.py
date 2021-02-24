import sqlite3

dbDir = "db/textdrop.db"

def init():
	try:
		with open(dbDir) as f:
			pass
	except IOError:
		conn = sqlite3.connect(dbDir)
		c = conn.cursor()
		c.execute("create table posts (id varchar(32), text varchar, time datetime)")
		conn.commit()
		conn.close()

def createPost(p):
	conn = sqlite3.connect(dbDir)
	c = conn.cursor()
	c.execute("insert into posts values (?, ?, ?)", (p.id, p.text, p.time))
	conn.commit()
	conn.close()

def getPost(postId):
	conn = sqlite3.connect(dbDir)
	c = conn.cursor()
	c.execute("select text, time from posts where id=?", (postId,))
	row = c.fetchone()
	post = {"text": row[0], "time": row[1]}
	conn.close()
	return post