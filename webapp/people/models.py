
from webapp.model import db


class People(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, index = True, nullable = False)
    group_id = db.Column(db.Integer, index = True, nullable = False)
    name = db.Column(db.String, nullable = False)
    date_of_birth = db.Column(db.Date, nullable = False)
    phone = db.Column(db.String)
    profile = db.Column(db.String)
    hobbies = db.Column(db.String)
    reminder_rule = db.Column(db.Integer)

    def __repr__(self):
        return '<People {}>'.format(self.id)