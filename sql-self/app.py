from flask import Flask, render_template, request, redirect
from sqlalchemy import select
from models import db, create_app, Pet
from flask_debugtoolbar import DebugToolbarExtension
app = Flask(__name__)
database_url = 'postgresql:///pet_shop_db'
app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'Je171369'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

create_app(app)

app.app_context().push()


# engine = create_engine('postgresql:///movies_example', future=True)
# connection = engine.connect()


# def com(t):
#     '''Run commands in Ipython'''
#     com = connection.execute(text(t))
#     return com


@app.route('/')
def list_pets():
    '''Shows list of all pets in db'''
    result = db.session.execute(select(Pet))
    pets = [x[0] for x in result]
    return render_template('list.html', pets=pets)


@app.route('/', methods=['POST'])
def create_pet():
    name = request.form['name']
    species = request.form['species']
    hunger = request.form['hunger']
    hunger = int(hunger) if hunger else None

    new_pet = Pet(name=name, species=species, hunger=hunger)
    db.session.add(new_pet)
    db.session.commit()
    return redirect(f'/{new_pet.id}')


@app.route('/<int:pet_id>')
def show_pet(pet_id):
    '''SHow details about a single pet.'''
    # result = db.session.execute(select(Pet).where(Pet.id == pet_id))
    # res = [x[0] for x in result]
    # pet = res[0]
    pet = db.get_or_404(Pet, pet_id)
    return render_template('details.html', pet=pet)


@app.route('/species/<species_id>')
def show_pets_by_species(species_id):
    result = db.session.execute(select(Pet).where(Pet.species == species_id))
    pets = [x[0] for x in result]
    return render_template('species.html', pets=pets, species=species_id)
