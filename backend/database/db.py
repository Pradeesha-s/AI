import sqlite3

DB_NAME = "AI.db"

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def create_user_table():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()

def create_task_table():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            role TEXT NOT NULL,
            day INTEGER NOT NULL,
            title TEXT NOT NULL,
            description TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()

def insert_sample_tasks():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM tasks")
    count = cursor.fetchone()[0]

    if count == 0:
        sample_tasks = [
            ("react", 1, "Intro to React", "Learn what React is and why it is used"),
            ("react", 2, "JSX Basics", "Understand JSX syntax"),
            ("prompt", 1, "Intro to Prompts", "Learn how prompts guide AI"),
            ("app", 1, "App Dev Basics", "Understand mobile app development")
        ]

        cursor.executemany(
            "INSERT INTO tasks (role, day, title, description) VALUES (?, ?, ?, ?)",
            sample_tasks
        )

        conn.commit()

    conn.close()
