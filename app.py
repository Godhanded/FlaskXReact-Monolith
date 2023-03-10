from flask import (
    Flask,
    url_for,
    render_template,
    redirect,
    request,
    Response,
    abort,
    flash
)
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db
import json
import logging

from logging import Formatter, FileHandler

app = Flask(__name__)
app.config.from_object("config")
# app.config["secrete_key"]="foo bar"

db.init_app(app)
migrate = Migrate(app, db)


@app.route("/", methods=["GET"])
def home():
    data = json.dumps({"hello": "hello_world"})
    # flash("successfully rendered","message")
    return render_template("index.html", data=data)
