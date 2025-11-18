from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(32), nullable=False)
    Type1 = db.Column(db.String(16), nullable=False)
    Type2 = db.Column(db.String(16), nullable=True)
    Classification = db.Column(db.String(64), nullable=True)
    Ability = db.Column(db.String(32), nullable=True)
    BST = db.Column(db.Integer, nullable=True)
    HP = db.Column(db.Integer, nullable=True)
    DEF = db.Column(db.Integer, nullable=True)
    SP_ATK = db.Column(db.Integer, nullable=True)
    SP_DEF = db.Column(db.Integer, nullable=True)
    SPE = db.Column(db.Integer, nullable=True)
    Held_item = db.Column(db.String(32), nullable=True)
    Level = db.Column(db.Integer, nullable=True)
    Primary_Clrs = db.Column(db.String(32), nullable=True)
    Gen = db.Column(db.Integer, nullable=False)
    Favourite_nba_team = db.Column(db.String(32), nullable=False)

    def __repr__(self):

        return f'<Pokemon {self.title}>'
# Define your database model here
# Example: class Item(db.Model):    