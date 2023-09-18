import os
import sqlite3
from datetime import datetime

class Results_DB:
    def __init__(self, db_path='data/history.db'):
        db_dir = os.path.dirname(db_path)
        if not os.path.exists(db_dir):
            os.makedirs(db_dir)

        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS results (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date_time TEXT,
                    title TEXT,
                    version TEXT,
                    contents TEXT
                );
            """)

    def add_result(self, title, version, contents):
        with self.conn:
            date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.conn.execute("""
                INSERT INTO results (date_time, title, version, contents)
                VALUES (?, ?, ?, ?);
            """, (date_time, title, version, contents))

    def get_results(self):
        with self.conn:
            cursor = self.conn.execute("""
                SELECT id, date_time, title, version
                FROM results
                ORDER BY date_time DESC;
            """)
            return cursor.fetchall()

    def get_result_by_id(self, result_id):
        with self.conn:
            cursor = self.conn.execute("""
                SELECT contents
                FROM results
                WHERE id = ?;
            """, (result_id,))
            return cursor.fetchone()[0]

# Usage example
if __name__ == '__main__':
    db = Results_DB()
    db.add_result('Test Simulation', 'v3.2.0', 'Some text contents for the simulation.')

    results = db.get_results()
    print("List of Results:")
    for result in results:
        print(result)

    result_id = results[0][0]
    contents = db.get_result_by_id(result_id)
    print(f"\nContents of result with ID {result_id}:")
    print(contents)

