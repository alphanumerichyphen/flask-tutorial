from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "complicated"			#used for session
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route("/")
def homepage():
	return render_template("index.html")


@app.route("/user")
def user():
	if "user" in session:				#check if logged in
		user = session["user"]
		return render_template("user.html", content=user)
	else:
		flash("You are not logged in!")
		return redirect(url_for("login"))	#back to login if not logged in


@app.route("/login", methods=["POST", "GET"])
def login():
	if request.method == "POST":
		#session.permanent = True		#user defined time
		user = request.form["nm"]		#get user name
		session["user"] = user			#store user name in session
		flash("Login Successful!")
		return redirect(url_for("user"))
	else:
		if "user" in session:
			flash("Already logged in!")
			return redirect(url_for("user"))

		return render_template("login.html")


@app.route("/logout")
def logout():
	if "user" in session:
		user = session["user"]
		flash(f"You have been successfully logged out, {user}", "info")
		session.pop("user", None)			#removing session data
	
	return redirect(url_for("login"))


'''@app.route("/admin")
def admin():
	return redirect(url_for("user", name="Admin"))
'''

@app.route("/test")
def test(name="test"):
	return f"<h1>If life is a {name}, take an A+ to the graveyard</h1>"


if __name__ == "__main__":
	app.run(debug = True)