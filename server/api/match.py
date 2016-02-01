from flask import Blueprint, current_app as app, request

from decorators import api_wrapper
from models import db, Match, Sheet

def get_match_sheets(mid):
    """Get all sheets for a specific match."""
    sheets = Sheet.query.filter_by(mid=mid).all()
    return sheets

def get_match(mid):
    """Get match data from match id."""
    match = Match.query.filter_by(mid=mid).first()
    return match

def get_matches():
    """Get all matches in the database."""
    matches = Match.query.all()
    return matches

def add_match(mid):
    """Add a new match to the database."""
    match = Match(mid)
    with app.app_context():
        db.session.add(match)
        db.session.commit()

def match_exists(mid):
    """
    Check if a match with a given match id already exists in the database

    Parameters
    ----------
    mid : str
        Match id.
    """
    match = get_match(mid)
    return match is not None
