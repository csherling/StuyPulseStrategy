from flask import Blueprint, current_app as app, request

from decorators import api_wrapper
from models import db, Matches, Sheets

def get_match(mid=None):
    match = {}
    if mid is not None:
        match.update({"mid": mid})
    match = Matches.query.filter_by(**match)
    return match

def add_match(mid):
    match = Matches(mid)
    with app.app_context():
        db.session.add(match)
        db.session.commit()
