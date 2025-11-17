from flask import Flask, request,
from models import db, Pokemon
from views import init_routes

# Create the Flask app and configure it
app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialise the database and routes
db.init_app(app)
init_routes(app)

app.route('/add', methods=['GET', 'POST'])




if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)