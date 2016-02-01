import sys

import api

from flask import Flask, render_template

app = Flask(__name__)

app.register_blueprint(api.team.blueprint, url_prefix="/api/team")
app.register_blueprint(api.sheet.blueprint, url_prefix="/api/sheet")
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:password@localhost/strategy"

with app.app_context():
    # Initialize tables/databases to be used by SQLAlchemy
    from api.models import db, Matches, Sheets, Teams
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
    return render_template("matches.html", sheets=api.sheet.get_sheets(), matches=api.match.get_matches())

@app.route("/sheets", methods=["GET", "POST"])
@app.route("/sheets/<tid>/", methods=["GET", "POST"])
@app.route("/sheets/<tid>/<sid>", methods=["GET", "POST"])
def sheets(tid=None, sid=None):
    if tid is None and sid is None:
        return render_template("sheets.html", sheets=api.sheet.get_sheets())
    elif sid is None:
        return render_template("view_sheet.html", team=api.team.get_team(tid), sheets=api.team.get_sheets(tid))
    else:
        return render_template("view_sheet.html", team=api.team.get_team(tid), sheets=[api.sheet.get_sheet(sid)])

if __name__ == "__main__":
    app.debug = "--debug" in sys.argv
    app.run(host="0.0.0.0", port=1337)
