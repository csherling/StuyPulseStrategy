from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Teams(db.Model):
    tid = db.Column(db.Integer, unique=True, primary_key=True) # Team number
    sheets = db.relationship("Sheets", backref="teams", lazy="dynamic")

    def __init__(self, tid):
        self.tid = tid;

    def get_matches(self):
        matches = []
        for sheet in self.sheets:
            match = Matches.query.filter_by(mid=sheet.mid).first()
            matches.append(match)
        return matches

class Matches(db.Model):
    mid = db.Column(db.String(16), unique=True, primary_key=True) # Match id (Q1, Q2, etc)
    sheets = db.relationship("Sheets", backref="matches", lazy="dynamic")

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
