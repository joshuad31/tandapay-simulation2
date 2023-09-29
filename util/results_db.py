import os
import sqlite3
from datetime import datetime

class Results_DB:
    def __init__(self, db_path='data/history.db'):
        db_dir = os.path.dirname(db_path)
        if not os.path.exists(db_dir):
            os.makedirs(db_dir)

        self.conn = sqlite3.connect(db_path)
        self.remote_conn = None
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
        if self.remote_conn:
            with self.remote_conn.cursor() as cursor:
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS results (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        date_time TEXT,
                        title TEXT,
                        version TEXT,
                        contents TEXT
                    );
                """)

    def set_remote_db(self, host, user, password, database):
        self.remote_conn = pymysql.connect(host=host, user=user, password=password, database=database)
        self.create_table()

    def add_result(self, title, version, contents):
        date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with self.conn:
            self.conn.execute("""
                INSERT INTO results (date_time, title, version, contents)
                VALUES (?, ?, ?, ?);
            """, (date_time, title, version, contents))
        if self.remote_conn:
            with self.remote_conn.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO results (date_time, title, version, contents)
                    VALUES (%s, %s, %s, %s);
                """, (date_time, title, version, contents))
            self.remote_conn.commit()

    def get_results(self):
        sqlite_results = []
        with self.conn:
            cursor = self.conn.execute("""
                SELECT id, date_time, title, version
                FROM results
                ORDER BY date_time DESC;
            """)
            sqlite_results = cursor.fetchall()

        remote_results = []
        if self.remote_conn:
            with self.remote_conn.cursor() as cursor:
                cursor.execute("""
                    SELECT id, date_time, title, version
                    FROM results
                    ORDER BY date_time DESC;
                """)
                remote_results = cursor.fetchall()

        return (sqlite_results + remote_results)

    def get_result_by_id(self, result_id):
        result = None
        with self.conn:
            cursor = self.conn.execute("""
                SELECT contents
                FROM results
                WHERE id = ?;
            """, (result_id,))
            result = cursor.fetchone()

        if result is None and self.remote_conn:
            with self.remote_conn.cursor() as cursor:
                cursor.execute("""
                    SELECT contents
                    FROM results
                    WHERE id = %s;
                """, (result_id,))
                result = cursor.fetchone()

        if result:
            return result[0]
        else:
            return None

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

