from flask import Blueprint, current_app as app, request

import match
import team

from decorators import api_wrapper
from models import db, Sheets

blueprint = Blueprint("sheet", __name__)

@blueprint.route("/new", methods=["POST"])
@api_wrapper
def new_sheet_request():
    form = request.form
    tid = form.get("tid")
    mid = form.get("mid")
    alliance = form.get("alliance")
    if not match.match_exists(mid):
        match.add_match(mid)

    if not team.team_exists(tid):
        team.add_team(tid)

    new_sheet(tid, mid, alliance)

    return {"success": 1, "message": "Sheet created."}

@blueprint.route("/delete", methods=["POST"])
@api_wrapper
def delete_sheet_request():
    form = request.form
    sid = form.get("sid")
    delete_sheet(sid)
    return {"success": 1, "message": "Sheet deleted."}

@blueprint.route("/update", methods=["POST"])
@api_wrapper
def update_sheet_request():
    form = request.form
    sid = form.get("sid")
    mid = form.get("mid")
    tid = form.get("tid")
    alliance = form.get("alliance")
    update_sheet(sid, mid, tid, alliance)
    return {"success": 1, "message": "Sheet updated."}

def new_sheet(tid, mid, alliance):
    sheet = Sheets(mid, tid, alliance)
    with app.app_context():
        db.session.add(sheet)
        db.session.commit()

def delete_sheet(sid):
    sheet = get_sheet(sid)
    mid = sheet.mid
    with app.app_context():
        db.session.delete(sheet)
        db.session.commit()

    if len(match.get_match_sheets(mid)) == 0:
        match.delete_match(mid)

def update_sheet(sid, mid, tid, alliance):
    sheet = get_sheet(sid)
    sheet.mid = mid
    sheet.tid = tid
    sheet.alliance = alliance
    with app.app_context():
        db.session.add(sheet)
        db.session.commit()

def get_sheet(sid):
    sheet = Sheets.query.filter_by(sid=sid).first()
    return sheet

def get_sheets():
    sheets = Sheets.query.order_by("mid asc").all()
    return sheets
