from flask import Flask, render_template, request, redirect, url_for
import hashlib

app = Flask(__name__)

#home page
@app.route("/", methods = ["GET", "POST"])
def index():
	#create new post
	if request.method == "POST":
		#get form results
		postText = request.form["text"]
		#generate hash ID for post
		postId = hashlib.md5(postText.encode("utf-8")).hexdigest()
		#write to database
		#go to post page
		return redirect(url_for("viewPost", postId = postId))
	return render_template("index.html")

#view post page
@app.route("/p/<postId>")
def viewPost(postId):
	return render_template("post.html", postId = postId)

if __name__ == "__main__":
	app.run()