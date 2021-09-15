import sqlite3

from PyQt5.QtSql import QSqlDatabase


class Connection:
    __database_name = r'test_db.db'

    def __init__(self):
        db = QSqlDatabase('QSQLITE')
        db_name = r'test_db.db'
        db.setDatabaseName(db_name)
        db.open()
        # print(db.isOpen())
        # print(db.tables())
        return db



