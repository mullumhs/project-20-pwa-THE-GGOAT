from flask import render_template, request, redirect, url_for, flash
from models import db, Pokemon # Also import your database model here

# Define your routes inside the 'init_routes' function
# Feel free to rename the routes and functions as you see fit
# You may need to use multiple methods such as POST and GET for each route
# You can use render_template or redirect as appropriate
# You can also use flash for displaying status messages

def init_routes(app):

    @app.route('/', methods=['GET'])
    def index():
        collection = Pokemon.query.all()

        # This route should retrieve all items from the database and display them on the page.
        return render_template('index.html', collection=collection)



    @app.route('/add', methods=['GET', 'POST'])
    def create_item():
        if request.method == 'POST':
            new_pokemon = Pokemon(
                name=request.form['name'],
                type1=request.form['type1'],
                type2=request.form['type2'],
                gen=int(request.form['gen'])
            )
            db.session.add(new_pokemon)
            db.session.commit()

            return redirect(url_for('index'))
        return render_template('add.html')        
            # This route should handle adding a new item to the database.
       



    @app.route('/update', methods=['POST'])
    def update_item():
        # This route should handle updating an existing item identified by the given ID.
        return render_template('index.html', message=f'Item updated successfully')



    @app.route('/delete', methods=['POST'])
    def delete_item():
        # This route should handle deleting an existing item identified by the given ID.
        return render_template('index.html', message=f'Item deleted successfully')
    
    @app.route('/team', methods=['GET'])
    def view_team():
        collection = Pokemon.query.all()
        return render_template('team.html', collection=collection )