from flask import Flask, render_template, request, redirect, url_for
import hashlib
import network
import sys

app = Flask(__name__)

#home page
@app.route("/", methods = ["GET", "POST"])
def index():
	#create new post
	if request.method == "POST":
		#get form results
		postText = request.form["text"]
		#generate hash ID for post
		postId = str(hashlib.md5(postText.encode("utf-8")).hexdigest())
		#write to database
		network.createPost(postId, postText)
		#go to post page
		return redirect(url_for("viewPost", postId = postId))
	#return index page
	return render_template("index.html")

#view post page
@app.route("/p/<postId>")
def viewPost(postId):
	#query database
	post = network.getPost(postId)
	#string manipulation
	postSize = len(post["text"].encode("utf-8"))
	postTextByLine = post["text"].split("\n")
	#return post page
	return render_template("post.html", postId = postId, postTextByLine = postTextByLine, postSize = postSize, postTime = post["timestamp"])

if __name__ == "__main__":
	network.init()
	app.run()