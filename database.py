import sqlite3
import json
from datetime import datetime
from pathlib import Path


# Project data directory
DATA_DIR = Path(__file__).resolve().parent / "data"

# Ensure data directory exists
DATA_DIR.mkdir(exist_ok=True)

# Database location
DATABASE_FILE = DATA_DIR / "prompttrace.db"


def get_connection():

    connection = sqlite3.connect(DATABASE_FILE)

    connection.row_factory = sqlite3.Row

    return connection


def create_table():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS experiments (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            task TEXT NOT NULL,

            prompt TEXT NOT NULL,

            prompt_version TEXT NOT NULL UNIQUE,

            model TEXT NOT NULL,

            response TEXT NOT NULL,

            score INTEGER NOT NULL CHECK(score BETWEEN 1 AND 10),

            created_at TEXT NOT NULL
        )
    """)

    connection.commit()

    connection.close()


def insert_experiment(experiment):

    connection = get_connection()

    cursor = connection.cursor()

    try:

        cursor.execute("""
            INSERT INTO experiments (
                task,
                prompt,
                prompt_version,
                model,
                response,
                score,
                created_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            experiment["task"],
            experiment["prompt"],
            experiment["prompt_version"],
            experiment["model"],
            experiment["response"],
            experiment["score"],
            experiment["created_at"]
        ))

        connection.commit()

        return True

    except sqlite3.IntegrityError:

        return False

    finally:

        connection.close()



def fetch_all_experiments():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM experiments
        ORDER BY id ASC
    """)

    rows = cursor.fetchall()

    experiments = [dict(row) for row in rows]

    connection.close()

    return experiments



def delete_experiment_from_db(prompt_version):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM experiments
        WHERE prompt_version = ?
    """, (prompt_version,))

    deleted = cursor.rowcount > 0

    connection.commit()

    connection.close()

    return deleted



def update_experiment_in_db(prompt_version, updated_data):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        UPDATE experiments
        SET
            task = ?,
            prompt = ?,
            model = ?,
            response = ?,
            score = ?
        WHERE prompt_version = ?
    """, (
        updated_data["task"],
        updated_data["prompt"],
        updated_data["model"],
        updated_data["response"],
        updated_data["score"],
        prompt_version
    ))

    updated = cursor.rowcount > 0

    connection.commit()

    connection.close()

    return updated


def migrate_json_to_sqlite():

    json_file = DATA_DIR / "experiments.json"

    if not json_file.exists():
        print("JSON file not found.")
        return

    with open(json_file, "r", encoding="utf-8") as file:
        experiments = json.load(file)

    create_table()

    imported = 0

    for experiment in experiments:

        if "created_at" not in experiment:
            experiment["created_at"] = datetime.now().isoformat(
                timespec="seconds"
            )

        if insert_experiment(experiment):
            imported += 1

    print("Total JSON experiments:", len(experiments))
    print("New experiments imported:", imported)
