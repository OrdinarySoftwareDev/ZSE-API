from flask import Flask, redirect, jsonify, abort
from flask_httpauth import HTTPBasicAuth
from modules.pot import *
import modules.news
import modules.zastepstwa
import modules.plan
import cacher

import re

app = Flask(__name__)

# dokumentacja
readme = "https://github.com/OrdinarySoftwareDev/ZSE-API/blob/main/README.md"

group_hrefs = cacher.group_hrefs

@app.route("/")
@app.route("/docs")
def index():
    return redirect(readme)

@app.route("/zastepstwa")
def zastepstwa():
    response = modules.zastepstwa.run()
    return jsonify(pot.zipify(response))

@app.route("/news")
def news():
    response = modules.news.run()
    return jsonify(pot.zipify(response))

@app.route("/groups")
def groupslist():
    return jsonify(group_hrefs)

@app.route("/plan/<group>")
def plan(group):
    link = None

    if group in group_hrefs:
        link = group_hrefs[group]
        response = modules.plan.run(link)
        return response
    else:
        abort(404)

if __name__ == "__main__":
    app.run("0.0.0.0")