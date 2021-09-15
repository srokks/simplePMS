import datetime

from PyQt5.QtGui import QPainter, QColor, QBrush, QPen, QFont, QPainterPath, QPixmap, QDrag
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtCore import QAbstractTableModel, QEvent, Qt, QRect, QMimeData, pyqtSignal
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
db = QSqlDatabase('QSQLITE')
db_name = r'db\test_db.db'
db.setDatabaseName(db_name)
db.open()
print(db.isOpen())
print(db.tables())
#
# class RoomSearch(QWidget):
#     def __init__(self):
#         super(RoomSearch, self).__init__()
#         main_layout = QVBoxLayout()
#
#         self.table = QTableView()
#         self.model = QSqlTableModel(db=db)
#         self.table.setModel(self.model)
#
#         self.model.setTable('tblGuest')
#         self.model.select()
#
#         main_layout.addWidget(self.table)
#         self.setLayout(main_layout)
#
# if __name__ == "__main__":
#     import sys
#     app = QApplication(sys.argv)
#     win = RoomSearch()
#     win.move(0, 0)
#     win.resize(400, 400)
#     win.show()
#     app.exec_()