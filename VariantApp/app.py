#import libraries
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request)

# # # # # # #
# FLASK SETUP
# # # # # # #
app = Flask(__name__)

# # # # # # # # #
# DATABASE SETUP
# # # # # # # # #

from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///db.sqlite"

# remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create database variable
db = SQLAlchemy(app)

# import function
from .variant import find_variants

# create route that renders index.html template
@app.route("/")
def index():
     
    return render_template("index.html")

# Create api route that returns desired info

@app.route("/api/info", methods=["GET"])
def api():
      
    user_name = request.args.get("userName")
    user_year = request.args.get("userYear", type=str)
    
    return jsonify(find_variants(user_name, user_year))
  
        
if __name__ == "__main__":
    app.run(debug=True)