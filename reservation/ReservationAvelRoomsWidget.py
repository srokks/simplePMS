from PyQt5.QtGui import QPainter, QColor, QBrush, QPen, QFont, QPainterPath, QPixmap, QDrag
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlRelationalTableModel, QSqlQueryModel, QSqlQuery
from PyQt5 import QtCore
from PyQt5.QtCore import QAbstractTableModel, QEvent, Qt, QRect, QMimeData, pyqtSignal, QDir,QSize
from PyQt5.QtWidgets import (
    QDialog,
QMdiArea,
    QSizeGrip,
    QScrollArea,
    QCompleter,
    QWidget,
    QSizePolicy,
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
    QGroupBox,
    QFrame,
QFormLayout,
)
from guest.SearchGuestWidget import SearchGuest
from db.Connection import Connection
class ReservationAvelRooms(QWidget):
    def __init__(self):
        super(ReservationAvelRooms, self).__init__()
        self.setMinimumSize(200,200)
        main_layout = QHBoxLayout()
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0,0,0,0)
        self.tab_widget = QTabWidget()
        self.tab_widget.addTab(QWidget(),'Criteria')
        self.tab_widget.addTab(QWidget(),'Avel rooms')
        self.tab_widget.setCurrentIndex(1)
        main_layout.addWidget(self.tab_widget)
        self.setLayout(main_layout)
    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setRenderHint(painter.Antialiasing)
        path = QPainterPath()
        rect = QRect(0, 0, self.width(), self.height())
        pen = QPen(QColor('green'), 1)
        painter.setPen(pen)
        painter.drawRect(rect)