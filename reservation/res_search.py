import datetime

from PyQt5.QtGui import QPainter, QColor, QBrush, QPen, QFont, QPainterPath, QPixmap, QDrag
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtCore import QAbstractTableModel, QEvent, Qt, QRect, QMimeData, pyqtSignal,QDir
from PyQt5.QtWidgets import (
    QDialog,
    QSizeGrip,
    QScrollArea,
    QWidget,
    QMainWindow,
    QApplication,
    QHBoxLayout,
    QLabel,
    QVBoxLayout,
    QTabWidget,
    QLineEdit,
    QPushButton,
    QBoxLayout,
    QTableWidget,
    QTableWidgetItem,
    QComboBox,
    QAbstractItemView,
    QTableView,
    QGridLayout,
    QFrame
)

#gets path of app
app_path= QDir().absolutePath().split('/')
app_path = '/'.join(app_path[0:-1])
db_path= app_path+'/db/test_db.db'

db = QSqlDatabase('QSQLITE')

db.setDatabaseName(db_path)
db.open()


class RoomSearch(QWidget):
    def __init__(self):
        super(RoomSearch, self).__init__()
        main_layout = QVBoxLayout()
        self.table = QTableView()
        self.model = QSqlTableModel(db=db)
        self.table.setModel(self.model)

        self.model.setTable('tblBookings')
        self.model.select()

        main_layout.addWidget(self.table)
        self.setLayout(main_layout)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    win = RoomSearch()
    win.move(0, 0)
    win.resize(400, 400)
    win.show()
    app.exec_()



