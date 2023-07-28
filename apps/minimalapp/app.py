from flask import Flask, render_template

# create Flask app
app = Flask(__name__)


# What happens on the route
# Once you create the app instance, you use it to handle incoming web requests and send
# responses to the user. @app.route is a decorator that turns a regular Python function
# into a Flask view function, which converts the function’s return value into an HTTP
# response to be displayed by an HTTP client, such as a web browser.
# You pass the value '/' to @app.route() to signify that this function will respond to
# web requests for the URL /, which is the main URL.
@app.route("/", methods=["GET", "POST"])
def index():
    return "Hello, Flaskbook!"


@app.route("/hello", methods=["GET"])
def hello():
    return "Hello!"


# Other way to define methods to use
@app.get("/hi")
@app.post("/hi")
def hi():
    return "Hi world"


# Customize the output. On the browser, type 127.0.0.1:5000/hello/marina" for
# customization
@app.route("/hello/<name>", methods=["GET", "POST"], endpoint="hello-endpoint")
def hello2(name):
    return f"Hello, {name}!"


# Design of the page on html template
@app.route("/name/<name>")
def show_name(name):
    return render_template("index.html", name=name)
