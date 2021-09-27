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

import reservation.ResEdit
from guest.SearchGuestWidget import SearchGuest
from reservation.Reservation import Reservation
from db.Connection import Connection
from guest.Guest import Guest
from reservation.ReservationAvelRoomsWidget import ReservationAvelRooms
from reservation.ReservationDetailWidget import ReservationDetailWidget
from reservation.ReservationOrderedWidget import ReservationOrderedWidget

class ReservationActionLayout(QVBoxLayout):
    init_guest = pyqtSignal(int)
    create_res_signal = pyqtSignal()
    def __init__(self):
        super(ReservationActionLayout, self).__init__()

        self.search_guest_btn = QPushButton()
        self.search_guest_btn.setText("Search guest")
        self.new_res_btn = QPushButton()
        self.new_res_btn.setText("New")
        self.new_res_btn.clicked.connect(self.create_res_signal.emit)
        # self.search_guest_btn.clicked.connect(self.search_guest_btn_clicked)
        self.addWidget(self.new_res_btn)

        self.addWidget(QPushButton("Change"))
        self.addWidget(self.search_guest_btn)
        self.addWidget(QPushButton("Close"))
        self.addStretch()

    def search_guest_btn_clicked(self):
        self._dialog = SearchGuest()
        self._dialog.show()
        self._dialog.chosen_guest.connect(self.on_dialog_choosen)
