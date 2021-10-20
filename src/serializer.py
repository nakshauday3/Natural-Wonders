from flask_marshmallow import Marshmallow
from flask import current_app
from .models import *

"""
ma : Marshmallow,
object serialization/deserialization schema
integrated with Flask-SQLAlchemy models
"""
ma = Marshmallow()

def init_marshmallow(app):
    with app.app_context():
        ma.init_app(current_app)

class LocationsSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Locations
    id = ma.auto_field()
    name = ma.auto_field()
    about = ma.auto_field()
    pic = ma.auto_field()
    country = ma.auto_field()
    datetime = ma.auto_field()


class GeographySchema(ma.SQLAlchemySchema):
    class Meta:
        model = Geography
    lat_long = ma.auto_field()
    climate = ma.auto_field()
    landscape = ma.auto_field()


class StatsSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Stats
    rank = ma.auto_field()
    stars = ma.auto_field()
    yearly_visitors = ma.auto_field()
    unesco_heritage = ma.auto_field()


class SpeciesSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Species
    species_name = ma.auto_field()
    locations_id = ma.auto_field()
