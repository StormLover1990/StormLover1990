from unittest import TestCase
from models import db, Pet, create_app
from sqlalchemy import delete
from flask import Flask
from app import app

# app = create_app(database_url='postgresql:///pet_shop_test')
# app = Flask(__name__)
# Use test database and don't clutter tests with SQL
# app.config['SQLALCHEMY_ECHO'] = False

# Make Flask errors be real errors, rather than HTML pages with error info
# app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
# app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

# app.app_context().push()

# db.drop_all()
# db.create_all()


class SQLSelf(TestCase):
    """Tests for views for Pets."""

    # @pytest.mark.fixture
    # def app_ctx(self):
    #     with app.app_context():
    #         create_app(app)
    #         app.config.update({
    #             'SQLALCHEMY_DATABASE_URI': 'postgresql:///pet_shop_test',
    #             'TESTING': True,
    #             'DEBUG_TB_HOSTS': "don't-show-debug-toolbar",
    #             'SQLALCHEMY_ECHO': False})
    #         db.session.execute(delete(Pet))
    #         pet = Pet(name="TestPet", species="dog", hunger=10)
    #         db.session.add(pet)
    #         db.session.commit()
    #         yield
    #     with app.app_context():
    #         db.session.rollback()

    def setUp(self):
        """Add sample pet."""

        with app.app_context():
            app.config.update({
                'SQLALCHEMY_DATABASE_URI': 'postgresql:///pet_shop_test',
                'TESTING': True,
                'DEBUG_TB_HOSTS': "don't-show-debug-toolbar",
                'SQLALCHEMY_ECHO': False})
            db.session.execute(delete(Pet))
            pet = Pet(name="TestPet", species="dog", hunger=10)
            db.session.add(pet)
            db.session.commit()

    def tearDown(self):
        """Clean up any fouled transaction."""
    with app.app_context():
        db.session.rollback()

    def test_list_pets(self):
        with app.test_client() as client:
            resp = client.get("/")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('TestPet', html)

    def test_show_pet(self):
        with app.test_client() as client:
            resp = client.get("/<int:1>")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1>TestPet Details</h1>', html)

    def test_add_pet(self):
        with app.test_client() as client:
            d = {"name": "TestPet2", "species": "cat", "hunger": 20}
            resp = client.post("/", data=d, follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("<h1>TestPet2 Details</h1>", html)
