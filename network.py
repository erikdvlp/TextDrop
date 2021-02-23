import sqlite3
import datetime

dbDir = "db/textdrop.db"

def init():
	try:
		with open(dbDir) as f:
			pass
	except IOError:
		conn = sqlite3.connect(dbDir)
		c = conn.cursor()
		c.execute("create table posts (id varchar(32), text varchar, timestamp datetime)")
		conn.commit()
		conn.close()

def createPost(postId, postText):
	conn = sqlite3.connect(dbDir)
	c = conn.cursor()
	c.execute("insert into posts values (?, ?, ?)", (postId, postText, datetime.datetime.now()))
	conn.commit()
	conn.close()

def getPost(postId):
	conn = sqlite3.connect(dbDir)
	c = conn.cursor()
	c.execute("select text, timestamp from posts where id=?", (postId,))
	row = c.fetchone()
	post = {"text": row[0], "timestamp": row[1]}
	conn.close()
	return post