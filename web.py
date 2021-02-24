from flask import Flask, render_template, request, redirect, url_for
import post
import network

app = Flask(__name__)

#home page
@app.route("/", methods = ["GET", "POST"])
def index():
	#create new post
	if request.method == "POST":
		formText = request.form["text"]
		p = post.Post(formText)
		network.createPost(p)
		return redirect(url_for("viewPost", postId = p.id))
	#return index page
	return render_template("index.html")

#main post page
@app.route("/<postId>")
def viewPost(postId):
	#query database
	resp = network.getPost(postId)
	if (resp == None):
		return redirect(url_for("noPage"))
	p = post.Post(resp["text"], postId, resp["time"])
	#manipulate strings for display
	postSize = len(p.text.encode("utf-8"))
	postTextByLine = p.text.split("\n")
	#return post page
	return render_template("post.html", postId = p.id, postTextByLine = postTextByLine, postSize = postSize, postTime = p.time)

#raw post page
@app.route("/raw/<postId>")
def viewRawPost(postId):
	#query database
	resp = network.getPost(postId)
	if (resp == None):
		return redirect(url_for("noPage"))
	p = post.Post(resp["text"], postId, resp["time"])
	#manipulate strings for display
	postTextByLine = p.text.split("\n")
	#return raw post page
	return render_template("raw.html", postTextByLine = postTextByLine)

#404
@app.route("/404")
def noPage():
	return render_template("404.html")

#catch-all
@app.errorhandler(404)
def handle_404(e):
	return redirect(url_for("noPage"))

if __name__ == "__main__":
	network.init()
	app.run()