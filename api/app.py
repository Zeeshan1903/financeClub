from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/meettheteam")
def team():
    return render_template("team.html")