from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Team(db.Model):
    """
    Model representing a team being scouted.

    Attributes
    ----------
    tid : int
        Number of the team being scouted.
    sheets : list of Sheets
        Sheets belonging to the team.
    """
    tid = db.Column(db.Integer, unique=True, primary_key=True) # Team number
    sheets = db.relationship("Sheet", backref="team", lazy="dynamic")

    def __init__(self, tid):
        self.tid = tid;

class Match(db.Model):
    """
    Model representing a match.

    Attributes
    ----------
    mid : str
        Id of the match.
    sheets : list of Sheets
        Sheets for the match.
    """
    mid = db.Column(db.String(16), unique=True, primary_key=True) # Match id (Q1, Q2, etc)
    sheets = db.relationship("Sheet", backref="match", lazy="dynamic")

    def __init__(self, mid):
        self.mid = mid;

class Sheet(db.Model):
    """
    Model representing a scouting sheet.

    Attributes
    ----------
    sid : int
        Id of the sheet.
    mid : str
        Id of the match being scouted.
    tid : int
        Id of the team being scouted.
    alliance : str
        Alliance of the team being scouted.
    """
    sid = db.Column(db.Integer, unique=True, primary_key=True)
    mid = db.Column(db.String(16), db.ForeignKey("match.mid"))
    tid = db.Column(db.Integer, db.ForeignKey("team.tid"))
    alliance = db.Column(db.String(16))

    def __init__(self, mid, tid, alliance):
        self.mid = mid
        self.tid = tid
        self.alliance = alliance
