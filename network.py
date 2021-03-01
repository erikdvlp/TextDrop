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
		c.execute("create table posts (id varchar(32), text varchar, time int, duration int, public int)")
		conn.commit()
		conn.close()

def createPost(p):
	conn = sqlite3.connect(dbDir)
	c = conn.cursor()
	c.execute("insert into posts values (?, ?, ?, ?, ?)", (p.id, p.text, p.time, p.duration, p.public))
	conn.commit()
	conn.close()

def getPost(postId):
	conn = sqlite3.connect(dbDir)
	c = conn.cursor()
	c.execute("select text, duration, time, public from posts where id=?", (postId,))
	row = c.fetchone()
	if (row != None):
		p = post.Post(row[0], row[1], row[3], postId, row[2])
		conn.close()
		return p
	else:
		conn.close()
		return None

def getRecentPosts():
	conn = sqlite3.connect(dbDir)
	c = conn.cursor()
	c.execute("select id, text from posts where public = 1 and (time + duration) > ? order by time desc limit 3", (int(time.time()),))
	p = []
	rows = c.fetchall()
	if (rows != None):
		for r in rows:
			textPreview = r[1]
			if (len(textPreview) > 75):
				textPreview = r[1][0:72] + "..."
			p.append({"id": r[0], "text": textPreview})
	conn.close()
	return p

def deleteExpiredPost(postId):
	conn = sqlite3.connect(dbDir)
	c = conn.cursor()
	c.execute("select time, duration from posts where id = ?", (postId,))
	row = c.fetchone()
	if (int(row[0]) + int(row[1]) < int(time.time())):
		c.execute("delete from posts where id = ?", (postId,))
		conn.commit()
	conn.close()

def deleteAllExpiredPosts():
	conn = sqlite3.connect(dbDir)
	c = conn.cursor()
	c.execute("select id from posts where (time + duration) < ?", (int(time.time()),))
	rows = c.fetchall()
	for r in rows:
		c.execute("delete from posts where id = ?", (r[0],))
		conn.commit()
	conn.close()