import sqlite3


class Connection:
    __database_name = r'test_db.db'

    def __init__(self):
        self.conn = sqlite3.connect(self.__database_name)


    def get_connection(self):
        return self.conn
