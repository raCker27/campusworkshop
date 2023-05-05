"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaafqbhp8u791gttn0g-a.oregon-postgres.render.com",
        database="todo_3d09",
        user="todo_3d09_user",
        password="whDhNFNvshO1DeDacDAMjb90qop16OML")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
