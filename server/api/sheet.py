from flask import Blueprint, current_app as app, request

import match
import re
import team

from decorators import api_wrapper, WebException
from models import db, Sheets

blueprint = Blueprint("sheet", __name__)

@blueprint.route("/new", methods=["POST"])
@api_wrapper
def new_sheet_request():
    form = request.form
    tid = form.get("tid").lstrip("0")
    mid = form.get("mid").strip().upper()
    alliance = form.get("alliance")

    if not validate_match(mid):
        # Match id does not match the regex
        raise WebException("Invalid match id.")

    _match = match.get_match(mid=mid).first()
    if _match is None:
        # Match does not exist yet, so create one
        match.add_match(mid)

    _team = team.get_team(tid=tid).first()
    if _team is None:
        # Team does not exist yet, so create one
        team.add_team(tid)

    sheet = get_sheet(tid=tid, mid=mid, alliance=alliance).first()
    if sheet is not None:
        # Duplicate sheet exists, so alert the user
        raise WebException("Sheet already exists.")

    # Create a new sheet
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
    mid = form.get("mid").strip().upper()
    tid = form.get("tid").lstrip("0")
    alliance = form.get("alliance")

    if not validate_match(mid):
        # Match id does not match the regex
        raise WebException("Invalid match id.")

    _match = match.get_match(mid=mid).first()
    if _match is None:
        # Match does not exist yet, so create one
        match.add_match(mid)

    _team = team.get_team(tid=tid).first()
    if _team is None:
        # Team does not exist yet, so create one
        team.add_team(tid)

    update_sheet(sid, mid, tid, alliance)
    return {"success": 1, "message": "Sheet updated."}

def new_sheet(tid, mid, alliance):
    sheet = Sheets(mid, tid, alliance)
    with app.app_context():
        db.session.add(sheet)
        db.session.commit()

def delete_sheet(sid):
    sheet = get_sheet(sid=sid).first()
    with app.app_context():
        db.session.delete(sheet)
        db.session.commit()

def update_sheet(sid, mid, tid, alliance):
    sheet = get_sheet(sid=sid).first()
    sheet.mid = mid
    sheet.tid = tid
    sheet.alliance = alliance
    with app.app_context():
        db.session.add(sheet)
        db.session.commit()

def get_sheet(sid=None, mid=None, tid=None, alliance=None):
    match = {}
    if sid is not None:
        match.update({"sid": sid})
    if mid is not None:
        match.update({"mid": mid})
    if tid is not None:
        match.update({"tid": tid})
    if alliance is not None:
        match.update({"alliance": alliance})
    sheet = Sheets.query.filter_by(**match)
    return sheet

def validate_match(mid):
    return re.match("^(P|Q)\d+$", mid) is not None
