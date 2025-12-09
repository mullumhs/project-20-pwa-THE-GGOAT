from flask import render_template, request, redirect, url_for, flash, jsonify
from models import db, Pokemon # Also import your database model here
import requests

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



    @app.route('/delete/<id>', methods=['POST'])
    def delete_item(id):
        # This route should handle deleting an existing item identified by the given ID.
        item = Pokemon.query.get(id)  # Fetch item by ID
        if item is None:
            flash("Item not found", "error")
            return redirect(url_for("index"))
        db.session.delete(item)  	# Delete item

        db.session.commit()  		# Commit changes
        return redirect(url_for('view_team'))
    
    
    @app.route('/test', methods=['GET'])
    def view_team():
        url = "https://pokeapi.co/api/v2/pokemon/pikachu"  # example with Pikachu
        response = requests.get(url)
        data = response.json()
        print(data.keys())  # shows top-level keys in the JSON
        return render_template('single.html', data=data)
    
    @app.route('/team', methods=['GET'])
    
    def view_pokemon():
        collection1 = ''
        type1 = request.args.get('type1', '')
        type2 = request.args.get('type2', '')
        print(type1, type2)
        if not type1 and not type2:
            print("empty")                     
            collection1 = Pokemon.query.all()
        elif not type2:
            collection1 = Pokemon.query.filter(Pokemon.type1 == type1)
        elif not type1:
            collection1 = Pokemon.query.filter(Pokemon.type2 == type2)
        else:
            collection1 = Pokemon.query.filter(Pokemon.type2 == type2, Pokemon.type1 == type1)
        meow = []
        for item in collection1:
            #Main Data
            url = f"https://pokeapi.co/api/v2/pokemon/{item.name}"
            r = requests.get(url)
            print(r)
            data=r.json()

            # Species data for flavor text
            species_url = f"https://pokeapi.co/api/v2/pokemon-species/{item.name}"
            r2 = requests.get(species_url)
            species_data = r2.json()

            # Get the first English flavor text entry
            entry = next(
                e['flavor_text'] for e in species_data['flavor_text_entries']
                if e['language']['name'] == 'en'
            )

            # Attach flavor text to the Pokémon dict
            data['flavor_text'] = entry
            data['db_id'] = item.id 
            
            meow.append(data)
        return render_template('team.html', meow=meow)