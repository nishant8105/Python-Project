from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def calculator ():
    return render_template('index.html')

@app.route("/about")
def about():
    return "On about page"

@app.route("/contact")
def contact():
    return "on contact page"