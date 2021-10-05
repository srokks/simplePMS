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
    ''' Reservation Edit widget'''
    def __init__(self, parent=None, db=None, res=None):
        if db is None:  # if parent widget don't pass database
            self.db = Connection().db  # init new connection
        else:
            self.db = db
        if res is None:  # if parent widget don't pass reservation
            self.reservation = None  # init Null reservation
        else:
            self.reservation = res

        # self.reservation = Reservation('210002').fetch_by_id(self.db)  # DEBUG: init reservation
        super(ReservationEdit, self).__init__()

        self.parent = parent
        self.setMinimumWidth(800)
        # ----
        main_layout = QGridLayout()  # main layout - grid
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(5, 5, 5, 5)
        # ----

        # --- Init main widgets
        # --- Init main widgets
        self.res_details = ReservationDetailWidget()
        self.guest_info = ReservationOrderedWidget()
        rooming_list = RoomingListWidget()
        rooms_avel = ReservationAvelRooms()
        self.action_lay = ReservationActionLayout()
        # -----
        self.res_details.init_res_details(self.reservation) # inits res_details with reservation
        self.guest_info.init_guest()
        self.action_lay.search_guest_btn.clicked.connect(self.search_guest_btn_clicked) # connect search_btn to popup window in MDI
        self.action_lay.new_res_btn.clicked.connect(self.new_res_btn_clicked) # connect event of pushing new reservation
        # -----
        tab = QTabWidget()
        #TODO: fix mac os tab positioning
        tab.addTab(QPushButton(), "All reservations")
        tab.addTab(self.res_details, "Basic")
        tab.addTab(rooming_list, "Rooming List")
        # -----
        tab.setCurrentIndex(1)  # DEBUG: focuses on rooming list
        # ----- Main layout widgets push logic
        main_layout.addWidget(self.guest_info, 0, 0)
        main_layout.addWidget(rooms_avel, 0, 1)
        main_layout.addWidget(tab, 1, 0, 1, 3)
        main_layout.addLayout(self.action_lay, 0, 2, 3, 1)
        # -----
        self.res_details.reservation_valid.connect(self.on_valid_reservation) # catches signal if form is valid filled
        # -----
        self.setLayout(main_layout)



    def on_valid_reservation(self, e):
        '''Checks if all things are filled and turn enable new_btn'''
        #TODO: somehow catch singals from two widgget and
        self.action_lay.new_res_btn.setDisabled(e)
        print('sss')

    def new_res_btn_clicked(self):
        '''Triggered by new_bt, pushes reservation data into db'''
        # TODO: insert to db logic
        self.reservation = self.res_details.gather_res_details()

        print('create')

    def populate_guest_info(self, i):
        ''' Fills forms in guest field (guest_info)'''
        guest = Guest()
        guest.fetch_by_id(self.db, i) # fetch guest from db
        self.guest_info.init_guest(guest) # populate guest_info

    def search_guest_btn_clicked(self):
        ''' Opens new sub window in parent MDI with search_guest window'''
        self._dialog = SearchGuest()
        self.parent.addSubWindow(self._dialog) # adds to parent MDI new window
        self._dialog.chosen_guest.connect(self.populate_guest_info) # signal passes choosen guest id
        self._dialog.show()






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
