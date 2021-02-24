import sqlite3
import post
import time

dbDir = "db/textdrop.db"

def init():
	try:
		with open(dbDir) as f:
			pass
	except IOError:
		conn = sqlite3.connect(dbDir)
		c = conn.cursor()
		c.execute("create table posts (id varchar(32), text varchar, time int, duration int)")
		conn.commit()
		conn.close()

def createPost(p):
	conn = sqlite3.connect(dbDir)
	c = conn.cursor()
	c.execute("insert into posts values (?, ?, ?, ?)", (p.id, p.text, p.time, p.duration))
	conn.commit()
	conn.close()

def getPost(postId):
	conn = sqlite3.connect(dbDir)
	c = conn.cursor()
	c.execute("select text, duration, time from posts where id=?", (postId,))
	row = c.fetchone()
	if (row != None):
		p = post.Post(row[0], row[1], postId, row[2])
		conn.close()
		return p
	else:
		return None

def deleteExpiredPosts():
	conn = sqlite3.connect(dbDir)
	c = conn.cursor()
	c.execute("select id from posts where (time + duration) < ?", (int(time.time()),))
	rows = c.fetchall()
	for r in rows:
		c.execute("delete from posts where id = ?", (r[0],))
	conn.commit()
	conn.close()