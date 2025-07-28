from app import db

class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, nullable=False)
    description = db.Column(db.String(128), nullable=True)  

    def _repr_(self):
        return '<Menu {}>'.format(self.name)
