from flask import Flask, render_template, request, redirect, url_for
import post
import network
import helpers

app = Flask(__name__)

#home page
@app.route("/", methods = ["GET", "POST"])
def index():
	#create new post
	if request.method == "POST":
		p = helpers.createPostFromForm(request.form)
		network.createPost(p)
		return redirect(url_for("viewPost", postId = p.id))
	#get index page
	else:
		posts = network.getRecentPosts()
		return render_template("index.html", posts = posts)

#main post page
@app.route("/<postId>")
def viewPost(postId):
	#query database
	p = network.getPost(postId)
	if (p == None):
		return redirect(url_for("noPage"))
	#manipulate strings for display
	strs = helpers.getDisplayStrings(p)
	#return post page
	return render_template("post.html", postId = p.id, postTextByLine = strs["postTextByLine"], postSize = strs["postSize"], postTime = strs["postTime"])

#raw post page
@app.route("/raw/<postId>")
def viewRawPost(postId):
	#query database
	p = network.getPost(postId)
	if (p == None):
		return redirect(url_for("noPage"))
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