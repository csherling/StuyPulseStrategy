import sys

import api

from flask import Flask, render_template

app = Flask(__name__)

app.register_blueprint(api.team.blueprint, url_prefix="/api/team")

with app.app_context():
    # Initialize tables/databases to be used by SQLAlchemy
    from api.models import db
    db.init_app(app)
    db.create_all()

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/teams", methods=["GET", "POST"])
def teams():
    return render_template("teams.html")

@app.route("/sheets", methods=["GET", "POST"])
def sheets():
    return render_template("sheets.html")

if __name__ == "__main__":
    app.debug = "--debug" in sys.argv
    app.run(host="0.0.0.0", port=1337)
