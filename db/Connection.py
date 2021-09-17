import dbm
import sqlite3

from PyQt5.QtSql import QSqlDatabase
from PyQt5.QtCore import QStandardPaths,QDir
a = QSqlDatabase()
class Connection:
    def __init__(self):
        app_path = QDir().absolutePath().split('/')
        app_path = '/'.join(app_path[0:-1])
        #TODO: fix path to project/program - use relative paths
        app_path ='/Users/srokks/PycharmProjects/simplePMS'
        db_path = app_path + '/db/test_db.db'
        db = QSqlDatabase('QSQLITE')
        db.setDatabaseName(db_path)
        self.db = None
        if db.open():
            self.db = db
            # return db
        else:
            print('ERROR: ',db.lastError().text())





