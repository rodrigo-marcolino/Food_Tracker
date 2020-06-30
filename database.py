from flask import g
import sqlite3
import os

app_dir = os.path.abspath(os.path.dirname(__file__))
database = os.path.join(app_dir, "data.db")

def connect_db():
    sql = sqlite3.connect(database)
    sql.row_factory = sqlite3.Row
    return sql


def get_db():
    sql = sqlite3.connect(database)
    sql.row_factory = sqlite3.Row
    return sql