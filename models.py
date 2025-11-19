from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=True)
    type1 = db.Column(db.String(16), nullable=True)
    type2 = db.Column(db.String(16), nullable=True)
   
    gen = db.Column(db.Integer, nullable=True)
    

    def __repr__(self):

        return f'<Pokemon {self.title}>'
# Define your database model here
# Example: class Item(db.Model):    
#  classification = db.Column(db.String(64), nullable=True)
#    ability = db.Column(db.String(32), nullable=True)
#    BST = db.Column(db.Integer, nullable=True)
#    HP = db.Column(db.Integer, nullable=True)
#    DEF = db.Column(db.Integer, nullable=True)
#    SP_ATK = db.Column(db.Integer, nullable=True)
#    SP_DEF = db.Column(db.Integer, nullable=True)
#    SPE = db.Column(db.Integer, nullable=True)
#    held_item = db.Column(db.String(32), nullable=True)
#   level = db.Column(db.Integer, nullable=True)
#    primary_clrs = db.Column(db.String(32), nullable=True)
#    favourite_nba_team = db.Column(db.String(32), nullable=True)