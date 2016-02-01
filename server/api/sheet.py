from flask import Blueprint, current_app as app, request

import match
import re
import team

from decorators import api_wrapper, WebException
from models import db, Sheet

blueprint = Blueprint("sheet", __name__)

@blueprint.route("/new", methods=["POST"])
@api_wrapper
def new_sheet_request():
    """Handle api request for creating a new sheet."""
    form = request.form
    tid = form.get("tid").lstrip("0")
    mid = form.get("mid").strip()
    alliance = form.get("alliance")

    if not validate_match(mid):
        raise WebException("Invalid match id.")

    if not match.match_exists(mid):
        match.add_match(mid)

    if not team.team_exists(tid):
        team.add_team(tid)

    if sheet_exists(tid, mid, alliance):
        raise WebException("Sheet already exists.")

    new_sheet(tid, mid, alliance)

    return {"success": 1, "message": "Sheet created."}

@blueprint.route("/delete", methods=["POST"])
@api_wrapper
def delete_sheet_request():
    """Handle api request for deleting a sheet."""
    form = request.form
    sid = form.get("sid")
    delete_sheet(sid)
    return {"success": 1, "message": "Sheet deleted."}

@blueprint.route("/update", methods=["POST"])
@api_wrapper
def update_sheet_request():
    """Handle api request for updating a sheet."""
    form = request.form
    sid = form.get("sid")
    mid = form.get("mid")
    if not validate_match(mid):
        raise WebException("Invalid match id.")

    tid = form.get("tid")
    alliance = form.get("alliance")
    update_sheet(sid, mid, tid, alliance)
    return {"success": 1, "message": "Sheet updated."}

def new_sheet(tid, mid, alliance):
    """
    Create a new sheet and add it to the database.

    Parameters
    ----------
    tid : int
        Team number.
    mid : str
        Id of the match (i.e: Q1 or P2).
    alliance : str
        Team alliance for match (i.e: Blue Alliance).
    """
    sheet = Sheet(mid, tid, alliance)
    with app.app_context():
        db.session.add(sheet)
        db.session.commit()

def delete_sheet(sid):
    """
    Remove a sheet from the database.

    Parameters
    ----------
    sid : int
        Id of the sheet to be removed.
    """
    sheet = get_sheet(sid)
    with app.app_context():
        db.session.delete(sheet)
        db.session.commit()

def update_sheet(sid, mid, tid, alliance):
    """
    Update a sheet in the database.

    Parameters
    ----------
    sid : int
        Id of the sheet to be updated.
    mid : str
        Value of the new match id of the sheet.
    tid : int
        Value of the new team number of the sheet. Essentially changes
        ownership of the sheet.
    alliance : str
        Value of the new alliance of the team for the match.
    """
    sheet = get_sheet(sid)
    sheet.mid = mid
    sheet.tid = tid
    sheet.alliance = alliance
    with app.app_context():
        db.session.add(sheet)
        db.session.commit()

def get_sheets():
    """Return all Sheet in the database"""
    sheets = Sheet.query.all()
    return sheets

def get_sheet(sid):
    """
    Return Sheet specified by its sheet id.

    Parameters
    ----------
    sid : int
        Id of the sheet to be returned.
    """
    sheet = Sheet.query.filter_by(sid=sid).first()
    return sheet

def sheet_exists(tid, mid, alliance):
    """
    Check for an existing sheet.

    Parameters
    ----------

    tid : int
        Team number.
    mid : str
        Match id.
    alliance : str
        Alliance.
    """
    sheet = Sheet.query.filter_by(tid=tid, mid=mid, alliance=alliance).first()
    return sheet is not None

def validate_match(mid):
    return re.match("^(P|Q)\d+$", mid) is not None
