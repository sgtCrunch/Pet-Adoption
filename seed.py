"""Seed file to make sample data for db."""

from models import Pet, db
from app import app

with app.app_context():
    # Create all tables
    db.drop_all()
    db.create_all()

    # If table isn't empty, empty it
    Pet.query.delete()

    # Add pets
    spot = Pet(name='Spot', species="Dog")
    sandra = Pet(name='Sandra', species="Bird")
    allen = Pet(name='Allen', species="Insect")

    # Add new objects to session, so they'll persist
    db.session.add(spot)
    db.session.add(sandra)
    db.session.add(allen)
    db.session.commit()