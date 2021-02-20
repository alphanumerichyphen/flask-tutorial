from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
	return render_template("index.html")

@app.route("/<name>")
def user(name):
	return render_template("user.html", content=name)


@app.route("/admin")
def admin():
	return redirect(url_for("user", name="Admin"))


@app.route("/test")
def test(name="test"):
	return f"<h1>If life is a {name}, take and A+ to the graveyard</h1>"

if __name__ == "__main__":
	app.run(debug = True)