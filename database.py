import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect("visionqc.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS predictions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        image_name TEXT,
        prediction TEXT,
        confidence REAL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()

def save_prediction(image_name, prediction, confidence):

    conn = sqlite3.connect("visionqc.db")
    cursor = conn.cursor()

    # Get current local time (your PC time)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
    INSERT INTO predictions(image_name,prediction,confidence,created_at)
    VALUES(?,?,?,?)
    """,(
        image_name,
        prediction,
        confidence,
        current_time
    ))

    conn.commit()
    conn.close()


def get_predictions():
    conn = sqlite3.connect("visionqc.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT image_name,prediction,confidence,created_at
    FROM predictions
    ORDER BY id DESC
    """)

    data = cursor.fetchall()

    conn.close()

    return data
def clear_history():
    conn = sqlite3.connect("visionqc.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM predictions")

    conn.commit()
    conn.close()