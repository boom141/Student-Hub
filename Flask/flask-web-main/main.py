from flask import Flask, redirect,url_for,render_template,session, request
from datetime import datetime
from settings import app

@app.route("/Student_Hub")
def test():
    return render_template("base.html")


if __name__ == "__main__":
    app.run(debug=True)