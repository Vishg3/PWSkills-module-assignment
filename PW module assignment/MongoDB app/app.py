from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_bcrypt import Bcrypt
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = "supersecretkey"
bcrypt = Bcrypt(app)

client = MongoClient("mongodb://localhost:27017/")
db = client["user_db"]
users = db["users"]

@app.route("/")
def home():
    if "username" in session:
        return "Hello Geeks!"
    return redirect(url_for("signin"))

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        users.insert_one({"username": username, "password": hashed_password})
        flash("Signup successful! Please login.", "success")
        return redirect(url_for("signin"))
    return render_template("signup.html")

@app.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = users.find_one({"username": username})
        if user and bcrypt.check_password_hash(user["password"], password):
            session["username"] = username
            return redirect(url_for("home"))
        flash("Invalid username or password", "danger")
    return render_template("signin.html")

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("signin"))

if __name__ == "__main__":
    app.run(debug=True)
