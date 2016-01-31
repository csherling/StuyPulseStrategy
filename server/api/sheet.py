from flask import Blueprint, current_app as app, request

from decorators import api_wrapper
from models import db, Sheets

blueprint = Blueprint("sheet", __name__)

@blueprint.route("/new", methods=["POST"])
@api_wrapper
def new_sheet_request():
    form = request.form
    tid = form.get("tid")
    mid = form.get("mid")
    new_sheet(tid, mid)
    return {"success": 1, "message": "Sheet created."}

@blueprint.route("/delete", methods=["POST"])
@api_wrapper
def delete_sheet_request():
    form = request.form
    sid = form.get("sid")
    delete_sheet(sid)
    return {"success": 1, "message": "Sheet deleted."}

def new_sheet(tid, mid):
    sheet = Sheets(mid, tid)
    with app.app_context():
        db.session.add(sheet)
        db.session.commit()

def delete_sheet(sid):
    sheet = get_sheet(sid)
    with app.app_context():
        db.session.delete(sheet)
        db.session.commit()

def get_sheets():
    sheets = Sheets.query.all()
    return sheets

def get_sheet(sid):
    sheet = Sheets.query.filter_by(sid=sid).first()
    return sheet
