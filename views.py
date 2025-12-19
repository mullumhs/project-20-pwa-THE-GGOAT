from flask import render_template, request, redirect, url_for, flash, jsonify
from models import db, Pokemon # Also import your database model here
import requests
from urllib.parse import quote

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
            shiny_val=request.form['shiny']

            shiny_bool = True if shiny_val == 'true' else False
            
            new_pokemon = Pokemon(
                name=request.form['name'],
                type1=request.form['type1'],
                type2=request.form['type2'],
                nick=request.form['nickname'],
                shiny=shiny_bool, 
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
        return redirect(url_for('view_pokemon'))
    
    
    @app.route('/pokemon/<name>', methods=['GET'])
    def pokemon_details(name):
        encoded = quote(name.lower(), safe='-')

        # Fetch Pokémon data
        url = f"https://pokeapi.co/api/v2/pokemon/{encoded}"
        r = requests.get(url)
        data = r.json()

        # Fetch species data (for flavor text)
        species_url = f"https://pokeapi.co/api/v2/pokemon-species/{encoded}"
        r2 = requests.get(species_url)
        species_data = r2.json()

        entry = next(
            e['flavor_text'] for e in species_data['flavor_text_entries']
            if e['language']['name'] == 'en'
        )

        data['flavor_text'] = entry

        #  Look up nickname from  database
        db_pokemon = Pokemon.query.filter_by(name=name).first()
        data['nickname'] = db_pokemon.nick if db_pokemon and db_pokemon.nick else None
        data['shiny'] = db_pokemon.shiny if db_pokemon else False
        return render_template('taken.html', data=data)
    
    @app.route('/team', methods=['GET'])
    
    def view_pokemon():
        collection1 = ''
        type1 = request.args.get('type1', '')
        type2 = request.args.get('type2', '')
        
        print(type1, type2)
        if not type1 and not type2:                     
            collection1 = Pokemon.query.all()
        elif not type2:
            print(type2)
            collection1 = Pokemon.query.filter(Pokemon.type1 == type1).all()
        elif not type1:
            collection1 = Pokemon.query.filter(Pokemon.type2 == type2).all()
        else:
            collection1 = Pokemon.query.filter(Pokemon.type2 == type2, Pokemon.type1 == type1).all()
        meow = []
        for item in collection1:
            name = (item.name or "").strip().lower()
            encoded = quote(name, safe='-')
            url = f"https://pokeapi.co/api/v2/pokemon/{encoded}"
            r = requests.get(url)
            data = r.json()

            species_url = f"https://pokeapi.co/api/v2/pokemon-species/{encoded}"
            r2 = requests.get(species_url)
            species_data = r2.json()
            entry = next(e['flavor_text'] for e in species_data['flavor_text_entries'] if e['language']['name'] == 'en')

            # Attach DB fields and chosen sprite
            data['flavor_text'] = entry
            data['db_id'] = item.id
            data['shiny'] = bool(item.shiny)            # ensure a boolean
            # optional: precompute a single sprite URL
            data['sprite'] = data['sprites']['front_shiny'] if data['shiny'] else data['sprites']['front_default']

            meow.append(data)
        return render_template('team.html', meow=meow)