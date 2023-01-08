import sqlite3


class Database:
    def __init__(self):
        self.conn = sqlite3.connect('mydatabase.db', check_same_thread=False)
        self.cursor = self.conn.cursor()

    def create_database(self):
        self.cursor.execute(
            '''CREATE TABLE people (vk_id integer, photo text, name text, date text, age integer, description text, connection text)''')
        self.cursor.execute('''CREATE TABLE admins (vk_id integer, name text, surname text)''')

    def insert_values(self, url, name, date, age, descr, connection, vk_id, username, surname):
        if not self.get_people_by_vk_id(vk_id):
            self.cursor.execute('''INSERT INTO admins (vk_id, name, surname) VALUES (?, ?, ?)''',
                                (vk_id, username, surname))

        self.cursor.execute(
            '''INSERT INTO people (photo, name, date, age, description, connection, vk_id) VALUES (?, ?, ?, ?, ?, ?, ?)''',
            (url, name, date, age, descr, connection, vk_id))
        self.conn.commit()

    def get_people_by_vk_id(self, vk_id):
        self.cursor.execute('''SELECT * FROM people WHERE vk_id = ?''', (vk_id,))
        rows = self.cursor.fetchall()
        return rows

    def get_admins_list(self):
        self.cursor.execute('''SELECT * FROM admins''')
        rows = self.cursor.fetchall()
        return rows

