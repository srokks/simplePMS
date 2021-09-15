import sqlite3

from PyQt5.QtSql import QSqlDatabase
from PyQt5.QtCore import QStandardPaths,QDir

class Connection:
    __database_name = r'test_db.db'

    def __init__(self):
        db = QSqlDatabase()
        db_name = r'test_db.db'
        db.setDatabaseName(db_name)
        db.open()
        # print(db.isOpen())
        # print(db.tables())


