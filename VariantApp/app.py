#import libraries

import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

# # # # # # #
# FLASK SETUP
# # # # # # #

app = Flask(__name__)

# # # # # # # # #
# DATABASE SETUP
# # # # # # # # #

from flask_sqlalchemy import flask_sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///db.sqlite"

# remove tracking modifications
app.confi['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from ## import ##

# create route that renders index.html template
@app.route("/")
def home():
    return redner_template("index.html")
    
# Query database and send jsonified results
@app.route("/send", methods=["GET", "POST"])
df send():
    if request.method == "POST":
        name = request.form["petName"]
        lat = request.form["petLat"]

        pet = Pet(name=name, lat=lat)
        db.session.add(pet)
        db.session.commit()
        return redirect("/", code=302)
    
    return render template("form.html")
