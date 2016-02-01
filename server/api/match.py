from flask import Blueprint, current_app as app, request

from decorators import api_wrapper
from models import db, Matches, Sheets

def get_match_sheets(mid):
    sheets = Sheets.query.filter_by(mid=mid).all()
    return sheets

def get_match(mid):
    match = Matches.query.filter_by(mid=mid).first()
    return match

def get_matches():
    matches = Matches.query.all()
    return matches

def add_match(mid):
    match = Matches(mid)
    with app.app_context():
        db.session.add(match)
        db.session.commit()

def delete_match(mid):
    match = get_match(mid)
    with app.app_context():
        db.session.delete(match)
        db.session.commit()

def match_exists(mid):
    match = get_match(mid)
    return match is not None
