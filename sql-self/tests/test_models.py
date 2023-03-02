
from unittest import TestCase
from flask import Flask
from app import app
from models import db, Pet, create_app
from sqlalchemy import delete


# Use test database and don't clutter tests with SQL
# app = Flask(__name__)
# app.config.update(
#     SQLALCHEMY_DATABASE_URI='postgresql:///pet_shop_test',
#     SQLALCHEMY_ECHO=False,
#     TESTING=False
# )
# app.config['SQLALCHEMY_ECHO'] = False
# app.config['TESTING'] = True
app.app_context().push()

db.drop_all()
db.create_all()


# class SQLSelfModel(TestCase):

# @pytest.mark.fixture
# def app_ctx(self):
#     with app.app_context():
#         db.session.execute(delete(Pet))
#         yield
#     with app.app_context():
#         db.session.rollback()

# @pytest.mark.usefixtures('app_ctx')
# def test_greet(self):
#     pet = Pet(name="TestPet", species="dog", hunger=10)
#     self.assertEqual(pet.greet(), "Hi, I am TestPet the dog.")

# @pytest.mark.usefixtures('app.ctx')
# def test_feed(self):
#     pet = Pet(name="TestPet", species="dog", hunger=10)
#     pet.feed(5)
#     self.assertEqual(pet.hunger, 5)

#     pet.feed(999)
#     self.assertEqual(pet.hunger, 0)

# @pytest.mark.usefixtures('app.ctx')
# def test_get_by_species(self):
#     pet = Pet(name="TestPet", species="dog", hunger=10)
#     db.session.add(pet)
#     db.session.commit()

#     dogs = Pet.get_by_species('dog')
#     self.assertEqual(dogs, [pet])

class PetModelTestCase(TestCase):
    """Tests for model for Pets."""

    def setUp(self):
        """Clean up any existing pets."""
    with app.app_context():
        app.config.update({
            'SQLALCHEMY_DATABASE_URI': 'postgresql:///pet_shop_test',
            'TESTING': True,
            'DEBUG_TB_HOSTS': "don't-show-debug-toolbar",
            'SQLALCHEMY_ECHO': False})
        db.session.execute(delete(Pet))

    def tearDown(self):
        """Clean up any fouled transaction."""
        with app.app_context():
            db.session.rollback()

    def test_greet(self):
        pet = Pet(name="TestPet", species="dog", hunger=10)
        with app.app_context():
            self.assertEqual(pet.greet(), "Hi, I am TestPet the dog.")

    def test_feed(self):
        pet = Pet(name="TestPet", species="dog", hunger=10)
        with app.app_context():
            pet.feed(5)
            self.assertEqual(pet.hunger, 5)

            pet.feed(999)
            self.assertEqual(pet.hunger, 0)

    def test_get_by_species(self):
        pet = Pet(name="TestPet", species="dog", hunger=10)
        with app.app_context():
            db.session.add(pet)
            db.session.commit()

            dogs = Pet.get_by_species('dog')
            self.assertEqual(dogs, [pet])
