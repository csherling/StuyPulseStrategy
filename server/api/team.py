from flask import Blueprint, current_app as app, request

import sheet

from decorators import api_wrapper, WebException
from models import db, Sheets, Teams

blueprint = Blueprint("team", __name__)

@blueprint.route("/add", methods=["POST"])
@api_wrapper
def add_team_request():
    form = request.form
    tid = form.get("tid").lstrip("0")
    if team_exists(tid):
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
    team = get_team(tid)
    sheets = Sheets.query.filter_by(tid=tid).all()
    with app.app_context():
        db.session.delete(team)
        db.session.commit()

    for sheet in sheets:
        with app.app_context():
            db.session.delete(sheet)
            db.session.commit()

def get_teams():
    teams = Teams.query.all();
    return teams

def get_team(tid):
    team = Teams.query.filter_by(tid=tid).first()
    return team

def team_exists(tid):
    team = get_team(tid)
    return team is not None
