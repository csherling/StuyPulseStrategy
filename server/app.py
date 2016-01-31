import sys

import api

from flask import Flask, render_template

app = Flask(__name__)

app.register_blueprint(api.team.blueprint, url_prefix="/api/team")
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:password@localhost/strategy"

with app.app_context():
    # Initialize tables/databases to be used by SQLAlchemy
    from api.models import db, Teams, Matches
    db.init_app(app)
    db.create_all()

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/teams", methods=["GET", "POST"])
@app.route("/teams/<tid>", methods=["GET", "POST"])
def teams(tid=None):
    if tid is None:
        return render_template("teams.html", teams=api.team.get_teams())
    else:
        return render_template("view_team.html", team=api.team.get_team(tid))

@app.route("/matches", methods=["GET", "POST"])
def matches():
    return render_template("matches.html")

@app.route("/sheets", methods=["GET", "POST"])
def sheets():
    return render_template("sheets.html")

if __name__ == "__main__":
    app.debug = "--debug" in sys.argv
    app.run(host="0.0.0.0", port=1337)
