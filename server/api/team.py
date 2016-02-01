from flask import Blueprint, current_app as app, request

import sheet

from decorators import api_wrapper, WebException
from models import db, Match, Sheet, Team

blueprint = Blueprint("team", __name__)

@blueprint.route("/add", methods=["POST"])
@api_wrapper
def add_team_request():
    """Handle api request for adding a new team to the database."""
    form = request.form
    tid = form.get("tid").lstrip("0")

    if team_exists(tid):
        # Team with that number already exists in the database
        raise WebException("Team already exists.")

    add_team(tid)
    return {"success": 1, "message" : "Team added."}

@blueprint.route("/delete", methods=["POST"])
@api_wrapper
def delete_team_request():
    """Handle api request for deleting a team from the database."""
    form = request.form
    tid = form.get("tid")
    delete_team(tid)
    return {"success": 1, "message" : "Team deleted."}

def add_team(tid):
    """
    Add a new team to the database.

    Parameters
    ----------
    tid : int
        Number of the team to add.
    """
    team = Team(tid)
    with app.app_context():
        db.session.add(team)
        db.session.commit()

def delete_team(tid):
    """
    Delete a team from the database.

    Parameters
    ----------
    tid : int
        Number of the team to delete.
    """
    team = get_team(tid)
    sheets = get_sheets(tid)
    with app.app_context():
        db.session.delete(team)
        db.session.commit()

    # Remove all sheets belonging to the now deleted team
    for sheet in sheets:
        with app.app_context():
            db.session.delete(sheet)
            db.session.commit()

def get_teams():
    """Retrieve all teams in the database."""
    teams = Team.query.all();
    return teams

def get_team(tid):
    """
    Retrieve a team with a given team id from the database.

    Parameters
    ----------
    tid : int
        Number of the desired Team
    """
    team = Team.query.filter_by(tid=tid).first()
    return team

def team_exists(tid):
    """
    Check if a team with a given id exists in the database.

    Parameters
    ----------
    tid : int
        Number of the team.
    """
    team = get_team(tid)
    return team is not None

def get_sheets(tid):
    """
    Retrieve all sheets belonging to a team.

    Parameters
    ----------
    tid : int
        Number of the team.
    """
    sheets = Sheet.query.filter_by(tid=tid).all()
    return sheets

def get_matches(tid):
    """
    Retrieve all matches played by a team.

    Parameters
    ----------
    tid : int
        Number of the team.
    """
    sheets = get_sheets(tid)
    mids = []

    # Get the match ids for all sheets belonging to the team
    for sheet in sheets:
        mids.append(sheet.mid)

    # Retrieve all matches where the mid is in the list of mids
    matches = Match.query.filter(Match.mid.in_(mids)).all()
    return matches
