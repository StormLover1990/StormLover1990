from app import app
from models import Pet, db, create_app

with app.app_context():
    db.drop_all()
    db.create_all()

tango = Pet(name='Tango', species='dog', hunger=30)
tyrian = Pet(name='Tyrian', species='cat', hunger=20)
oj = Pet(name='OJ', species='cat', hunger=80)
todd = Pet(name='Todd', species='cat', hunger=100)
milo = Pet(name='Milo', species='ghost')

db.session.add_all([tango, tyrian, oj, todd, milo])
try:
    db.session.commit()
except:
    db.session.rollback()
