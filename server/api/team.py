from flask import Blueprint, current_app as app, request

import sheet

from decorators import api_wrapper, WebException
from models import db, Matches, Sheets, Teams

blueprint = Blueprint("team", __name__)

@blueprint.route("/add", methods=["POST"])
@api_wrapper
def add_team_request():
    form = request.form
    tid = form.get("tid").lstrip("0")

    team = get_team(tid=tid).first()
    if team is not None:
        # Team with that number already exists in the database
        raise WebException("Team already exists.")

    add_team(tid)
    return {"success": 1, "message" : "Team added."}

@blueprint.route("/delete", methods=["POST"])
@api_wrapper
def delete_team_request():
    form = request.form
    tid = form.get("tid")
    delete_team(tid)
    return {"success": 1, "message" : "Team deleted."}

def add_team(tid):
    team = Teams(tid)
    with app.app_context():
        db.session.add(team)
        db.session.commit()

def delete_team(tid):
    team = get_team(tid=tid).first()
    sheets = team.sheets
    with app.app_context():
        db.session.delete(team)
        db.session.commit()

    # Remove all sheets belonging to the now deleted team
    for sheet in sheets:
        with app.app_context():
            db.session.delete(sheet)
            db.session.commit()

def get_team(tid=None):
    match = {}
    if tid is not None:
        match.update({"tid": tid})
    team = Teams.query.filter_by(**match)
    return team
