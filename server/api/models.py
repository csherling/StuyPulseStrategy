from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# To add more fields later

class Teams(db.Model):
    tid = db.Column(db.Integer, unique=True, primary_key=True) # Team number
    matches = db.relationship("Sheets", backref="team", lazy="dynamic")

    def __init__(self, tid):
        self.tid = tid;

class Matches(db.Model):
    mid = db.Column(db.String(16), unique=True, primary_key=True) # Match id (Q1, Q2, etc)
    sheets = db.relationship("Sheets", backref="match", lazy="dynamic")

    def __init__(self, mid):
        self.mid = mid;

class Sheets(db.Model):
    sid = db.Column(db.Integer, unique=True, primary_key=True)
    mid = db.Column(db.String(16), db.ForeignKey("matches.mid"))
    tid = db.Column(db.Integer, db.ForeignKey("teams.tid"))
    alliance = db.Column(db.String(16))

    def __init__(self, mid, tid, alliance):
        self.mid = mid
        self.tid = tid
        self.alliance = alliance
