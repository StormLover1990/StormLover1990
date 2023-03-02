from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select, text, create_engine
from flask import Flask

db = SQLAlchemy()


def create_app(app):
    db.app = app
    db.init_app(app)


class Pet(db.Model):
    __tablename__ = "pets"

    @classmethod
    def get_by_species(cls, species):
        result = db.session.execute(select(cls).where(cls.species == species))
        res = [x[0] for x in result]
        return res

    @classmethod
    def get_all_hungry(cls):
        result = db.session.execute(select(cls).where(cls.hunger > 20))
        res = [x[0] for x in result]
        return res

    def __repr__(self):
        p = self
        return f"<Pet id={p.id} name={p.name} species={p.species} hunger={p.hunger}>"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.String(50),
                     nullable=False,
                     unique=True)
    species = db.Column(db.String(30), nullable=True)

    hunger = db.Column(db.Integer, nullable=False, default=20)

    def greet(self):
        return f"Hi, I am {self.name} the {self.species}."

    def feed(self, amt=20):
        '''Update hunger based off of amt'''
        self.hunger -= amt
        self.hunger = max(self.hunger, 0)
