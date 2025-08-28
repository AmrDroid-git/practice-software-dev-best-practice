import sqlite3
from config import DB_PATH

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS persons (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def add_person(name, age):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO persons (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    conn.close()

def get_all_persons():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM persons")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete_person(person_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM persons WHERE id=?", (person_id,))
    conn.commit()
    conn.close()
