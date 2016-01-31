from flask import Blueprint, current_app as app, request

from decorators import api_wrapper
from models import db, Teams

blueprint = Blueprint("team", __name__)

@blueprint.route("/add", methods=["POST"])
@api_wrapper
def add_team_request():
    form = request.form
    tid = form.get("tid")
    add_team(tid)
    return {"success": 1, "message" : "Team added"}

@blueprint.route("/delete", methods=["POST"])
@blueprint.route("/delete/<tid>", methods=["POST"])
@api_wrapper
def delete_team_request(tid=None):
    if tid is None:
        form = request.form
        tid = form.get("tid")
    delete_team(tid)
    return {"success": 1, "message" : "Team deleted"}

def add_team(tid):
    team = Teams(tid)
    with app.app_context():
        db.session.add(team)
        db.session.commit()

def delete_team(tid):
    team = Teams.query.filter_by(tid=tid).first()
    with app.app_context():
        db.session.delete(team)
        db.session.commit()
