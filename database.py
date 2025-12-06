import os

import sqlite3
from datetime import datetime

# Đảm bảo thư mục data tồn tại
os.makedirs("data", exist_ok=True)

DB_PATH = "data/sentiments.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS sentiments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT,
            sentiment TEXT,
            timestamp TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_result(text, sentiment):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO sentiments (text, sentiment, timestamp) VALUES (?, ?, ?)",
              (text, sentiment, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()

# Function to retrieve history
def get_history(limit=50):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM sentiments ORDER BY timestamp DESC LIMIT ?", (limit,))
    rows = c.fetchall()
    conn.close()
    return rows

# Optional: Function to clear history (not used in main.py)
def clear_history():
    conn = sqlite3.connect("data/sentiments.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM sentiments")
    conn.commit()
    conn.close()