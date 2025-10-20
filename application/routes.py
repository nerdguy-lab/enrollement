
from application import app
# import render template
from flask import render_template

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")
