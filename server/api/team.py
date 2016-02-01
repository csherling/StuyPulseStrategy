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
    sheets = get_sheets(tid)
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

def get_sheets(tid):
    sheets = Sheets.query.filter_by(tid=tid).all()
    return sheets

def get_matches(tid):
    sheets = get_sheets(tid)
    mids = []
    for sheet in sheets:
        mids.append(sheet.mid)
    return Matches.query.filter(Matches.mid.in_(mids)).all()
