from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(32), nullable=False)
    Type1 = db.Column(db.String(16), nullable=False)
    Type2 = db.Column(db.String(16), nullable=True)
    Classification = db.Column(db.String(64), nullable=False)
    Ability = db.Column(db.String(32), nullable=False)
    BST = db.Column(db.Integer, nullable=False)
    HP = db.Column(db.Integer, nullable=False)
    ATK = db.Column(db.Integer, nullable=False)
    DEF = db.Column(db.Integer, nullable=False)
    SP_ATK = db.Column(db.Integer, nullable=False)
    SP_DEF = db.Column(db.Integer, nullable=False)
    SPE = db.Column(db.Integer, nullable=False)
    Held_item = db.Column(db.String(32), nullable=True)
    Level = db.Column(db.Integer, nullable=False)
    Primary_Clrs = db.Column(db.String(32), nullable=False)
    Gen = db.Column(db.Integer, nullable=False)
    Favourite_nba_team = db.Column(db.String(32), nullable=False)

    def __repr__(self):

        return f'<Pokemon {self.title}>'
# Define your database model here
# Example: class Item(db.Model):    