from PyQt5.QtGui import QPainter, QColor, QBrush, QPen, QFont, QPainterPath, QPixmap, QDrag
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlRelationalTableModel, QSqlQueryModel, QSqlQuery
from PyQt5 import QtCore
from PyQt5.QtCore import QAbstractTableModel, QEvent, Qt, QRect, QMimeData, pyqtSignal, QDir, QSize
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
from reservation.ReservationActionLayout import ReservationActionLayout
from reservation.RoomingListWidget import RoomingListWidget


class ReservationEdit(QWidget):
    def __init__(self, parent=None, db=None, res=None):
        if db is None:
            self.db = Connection().db
        else:
            self.db = db
        if res is None:
            res = Reservation()
        else:
            self.reservation = res
        self.reservation = Reservation('210002').fetch_by_id(self.db)  # DEBUG: init reservation
        super(ReservationEdit, self).__init__()

        self.parent = parent
        self.setMinimumWidth(800)

        main_layout = QGridLayout()
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(5, 5, 5, 5)

        res_details = ReservationDetailWidget()
        res_details.guest_id_signal.connect(self.populate_guest_info)
        res_details.reservation_valid.connect(self.push_res)
        rooming_list = RoomingListWidget()

        self.res_ordered = ReservationOrderedWidget()

        res_details.init_res_details(self.reservation)
        rooms_avel = ReservationAvelRooms()
        action_lay = ReservationActionLayout()

        action_lay.search_guest_btn.clicked.connect(self.search_guest_btn_clicked)
        action_lay.new_res_btn.clicked.connect(self.new_res_btn_clicked)

        tab = QTabWidget()
        tab.addTab(QPushButton(), "All reservations")
        tab.addTab(res_details, "Basic")
        tab.addTab(rooming_list, "Rooming List")

        tab.setCurrentIndex(1)  # DEBUG: focuses on rooming list
        main_layout.addWidget(self.res_ordered, 0, 0)
        main_layout.addWidget(rooms_avel, 0, 1)
        main_layout.addWidget(tab, 1, 0, 1, 3)
        main_layout.addLayout(action_lay, 0, 2, 3, 1)
        res_details.guest_id_signal.connect(self.choose_guest_on_click)

        self.setLayout(main_layout)

    def res_inited(self, e):
        # Gather info from res details -
        print('sss', e)

    def new_res_btn_clicked(self):
        '''Triggered by new_btn'''
        # TODO: insert to db logic
        print('create')

    def populate_guest_info(self, i):
        # Fills forms in guest field (ordered_widget)
        guest = Guest()
        guest.fetch_by_id(self.db, i)
        self.res_ordered.init_guest(guest)
        print('kaka')

    def search_guest_btn_clicked(self):
        ''' Opens new sub window in parent MDI with search_guest window'''
        self._dialog = SearchGuest()
        self.parent.addSubWindow(self._dialog)
        self._dialog.chosen_guest.connect(self.choose_guest_on_click)
        self._dialog.show()

    def choose_guest_on_click(self, int):
        '''Triggered by choose guest in search_btn_dialog'''
        guest = Guest() # Init guest
        guest.fetch_by_id(self.db, int) # Fetch from db
        self.res_ordered.init_guest(guest) # Populate res_ordered widget

    def check_obligatories(self):

        pass


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        lay = QVBoxLayout()
        self.mdi_area = QMdiArea()
        res_edit = ReservationEdit(self)

        self.mdi_area.addSubWindow(res_edit)

        lay.addWidget(self.mdi_area)
        self.setLayout(lay)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    win = ReservationEdit()
    win.move(200, 200)
    # win.resize(600, 600)
    win.show()
    app.exec_()
