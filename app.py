import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask

CREATE_SQUAD_TABLE = (
    "CREATE TABLE IF NOT EXISTS liverpool0304 (id SERIAL PRIMARY KEY, squad_number INT, name VARCHAR(100), age INT, nation VARCHAR(100), previous_club VARCHAR(100));"
)

INSERT_INTO_SQUAD = (
    "INSERT INTO liverpool0304 (squad_number, name, age, nation, position, previous_club) VALUES (%s, %s, %s, %s, %s);"
)

load_dotenv()

app = Flask(__name__)
url = os.getenv("DATABASE_URL")
connection = psycopg2.connect(url)

@app.get("/")
def home():
    return "Hello, world!"

@app.get("/squad")
def squad():
    return "Squad goes here"