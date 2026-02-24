import sqlite3
from pathlib import Path

DB_FILE = Path("data") / "countries.db"

def run_query(query: str):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute(query)
    results = cursor.fetchall()

    conn.close()
    return results


if __name__ == "__main__":

    query = """
    SELECT name_common, population
    FROM countries
    WHERE population > 100000000
    ORDER BY population DESC;
    """

    results = run_query(query)

    for row in results:
        print(row)