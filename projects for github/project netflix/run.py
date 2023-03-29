from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    # names = ["Alice", "Bob", "Charlie"]
    return render_template("home.html")

@app.route("/list")
def lists():
    return render_template("list.html")

@app.route("/movies")
def movies():
    return render_template("movies.html")

@app.route("/new")
def new():
    return render_template("new.html")

@app.route("/shows")
def shows():
    return render_template("shows.html")

@app.route("/<string:file>")
def html_file(file):
    return render_template(f"htmls/{file}")

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == "admin" and password == "123456":
            return render_template("success.html")
        # return render_template("login.html", err="Login Failed, Please try again!")
        return render_template("failed.html")
    
    return render_template("login.html")

@app.route("/auth", methods=["GET", "POST"])
def auth():

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == "admin" and password == "123456":
            return render_template("index.html")
        # return render_template("login.html", err="Login Failed, Please try again!")
        return render_template("failed.html")
    
    return render_template("login.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == "admin" and password == "123456":
            return render_template("success.html")
        # return render_template("login.html", err="Login Failed, Please try again!")
        return render_template("failed.html")
    
    return render_template("signup.html")

if __name__ == '__main__':
    app.run(debug=True) #host="0.0.0.0", port=8000