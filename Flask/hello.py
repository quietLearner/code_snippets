from flask import Flask, render_template, url_for


# https://stackoverflow.com/questions/23327293/flask-raises-templatenotfound-error-even-though-template-file-exists
app = Flask(__name__)
app = Flask(__name__, template_folder="template")  # still relative to module


posts = [
    {
        "author": "Corey Schafer",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "April 20, 2018",
    },
    {
        "author": "Jane Doe",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "April 21, 2018",
    },
    {
        "author": "Jane Doe",
        "title": "Blog Post 3",
        "content": "Third post content",
        "date_posted": "April 22, 2018",
    },
    {
        "author": "Jane Doe",
        "title": "Blog Post 4",
        "content": "Fourth post content",
        "date_posted": "April 23, 2018",
    },
    {
        "author": "Jane Doe",
        "title": "Blog Post 5",
        "content": "Fifth post content",
        "date_posted": "April 24, 2018",
    },
]


@app.route("/")
@app.route("/home")
def hello_world():
    return render_template("home.html", posts=posts)


# https://jinja.palletsprojects.com/en/stable/


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/login")
@app.route("/register")
def login():
    return render_template("home.html", posts=posts)


# Run the app
# flask --app hello run --debug
