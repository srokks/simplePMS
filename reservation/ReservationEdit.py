from PyQt5.QtGui import QPainter, QColor, QBrush, QPen, QFont, QPainterPath, QPixmap, QDrag
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlRelationalTableModel, QSqlQueryModel
from PyQt5.QtCore import QAbstractTableModel, QEvent, Qt, QRect, QMimeData, pyqtSignal, QDir
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


class ReservationEdit(QWidget):
    def __init__(self):
        super(ReservationEdit, self).__init__()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    win = ReservationEdit()
    win.move(0, 0)
    win.resize(400, 400)
    win.show()
    app.exec_()
