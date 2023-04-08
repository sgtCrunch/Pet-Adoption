
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime

db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""
    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """Pets Model"""

    __tablename__ = "pets"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.String(50),
                     nullable=False)
    species = db.Column(db.String(50),
                     nullable=False)
    photo_url = db.Column(db.String(), nullable=True, default="profile.png")
    age = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.String(), nullable=True)
    available = db.Column(db.Boolean, nullable=False, default=True)
    
