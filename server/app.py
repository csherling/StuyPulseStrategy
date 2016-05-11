import sys

import api

from flask import Flask, render_template

app = Flask(__name__)

# Load api route blueprints
app.register_blueprint(api.team.blueprint, url_prefix="/api/team")
app.register_blueprint(api.sheet.blueprint, url_prefix="/api/sheet")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///strategy.db"

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
        # View all teams
        teams = api.team.get_team().all()
        return render_template("teams.html", teams=teams)
    else:
        # Overview for a specific team
        team = api.team.get_team(tid=tid).first()
        return render_template("view_team.html", team=team)

@app.route("/matches", methods=["GET", "POST"])
@app.route("/matches/<tid>", methods=["GET", "POST"])
def matches(tid=None):
    if tid is None:
        # View all matches
        matches = api.match.get_match().all()
        return render_template("matches.html", matches=matches)
    else:
        # View all matches played by a specific team
        team = api.team.get_team(tid=tid).first()
        return render_template("matches.html", team=team, matches=team.get_matches().all())

@app.route("/sheets", methods=["GET", "POST"])
@app.route("/sheets/<tid>/", methods=["GET", "POST"])
@app.route("/sheets/<tid>/<sid>/", methods=["GET", "POST"])
def sheets(tid=None, sid=None):
    if tid is None and sid is None:
        # View all sheets
        return render_template("sheets.html", sheets=api.sheet.get_sheet().all())

    if sid is None:
        # View all sheets belonging to a specific team
        team = api.team.get_team(tid=tid).first()
        return render_template("view_sheet.html", team=team, sheets=team.sheets)
    else:
        # View one sheet belonging to a specific team for a specific match
        team = api.team.get_team(tid=tid).first()
        sheet = api.sheet.get_sheet(sid=sid).first()
        return render_template("view_sheet.html", team=team, sheets=[sheet])

if __name__ == "__main__":
    # Enable debug mode if the flag is present
    app.debug = "--debug" in sys.argv

    # Run the application
    app.run(host="0.0.0.0", port=6940)
