import datetime

from PyQt5.QtGui import QPainter, QColor, QBrush, QPen, QFont, QPainterPath, QPixmap, QDrag
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel,QSqlRelationalTableModel,QSqlQueryModel
from PyQt5.QtCore import QAbstractTableModel, QEvent, Qt, QRect, QMimeData, pyqtSignal,QDir
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QDialog,
    QLineEdit,
    QSizeGrip,
    QScrollArea,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QTabWidget,
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

class RoomSearch(QWidget):
    def __init__(self):
        super(RoomSearch, self).__init__()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    win = RoomSearch()
    win.move(0, 0)
    win.resize(400, 400)
    win.show()
    app.exec_()



