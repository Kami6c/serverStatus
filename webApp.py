from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")


def index():
    list_of_servers = []
    try:
        with open("servInfo.json", "r") as srv:
            list_of_servers = json.load(srv)
    except:
        print("File doesn't exist/File not found")
    return render_template("index.html", list_of_servers=list_of_servers)

#export FLASK_APP=webApp.py
#flask run