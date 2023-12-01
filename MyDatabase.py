import sqlite3
class MyDatabase:
    def __init__(self):
        self.conn = sqlite3.connect('calculator.db')
        self.cursor = self.conn.cursor()

        self.create_users_table()
        self.create_history_table()

    def create_users_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS User (
                               Username TEXT PRIMARY KEY,
                               Password TEXT)''')
        self.conn.commit()

    def create_history_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS HistoryRecord (
                               RecordId INTEGER PRIMARY KEY AUTOINCREMENT,
                               Username TEXT,
                               Calculation TEXT,
                               Result TEXT,
                               FOREIGN KEY (Username) REFERENCES User(Username))''')
        self.conn.commit()

    def add_user(self, username, password):
        self.cursor.execute("INSERT INTO User (Username, Password) VALUES (?, ?)", (username, password))
        self.conn.commit()

    def verify_user(self, username, password):
        self.cursor.execute("SELECT Password FROM User WHERE Username=?", (username,))
        fetched_password = self.cursor.fetchone()
        if fetched_password and fetched_password[0] == password:
            return True
        else:
            return False

    def add_to_history(self, username, calculation, result):
        self.cursor.execute("INSERT INTO HistoryRecord (Username, Calculation, Result) VALUES (?, ?, ?)", (username, calculation, result))
        self.conn.commit()

    def get_user_history(self, username):
        self.cursor.execute("SELECT Calculation, Result FROM HistoryRecord WHERE Username=?", (username,))
        return self.cursor.fetchall()