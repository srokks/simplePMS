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
from reservation.ReservationActionLayout import ReservationActionLayout



class ReservationEdit(QWidget):
    def __init__(self,parent=None,db=None):
        if (db==None):
            self.db = Connection().db
        else:
            self.db = db
        super(ReservationEdit, self).__init__()
        res = Reservation('210002').fetch_by_id(self.db)

        self.parent = parent
        self.setMinimumWidth(800)

        main_layout = QGridLayout()
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(5,5,5,5)
        res_details = ReservationDetailWidget()

        self.res_ordered = ReservationOrderedWidget()
        rooms_avel = ReservationAvelRooms()
        action_lay = ReservationActionLayout()

        action_lay.search_guest_btn.clicked.connect(self.search_guest_btn_clicked)
        action_lay.new_res_btn.clicked.connect(self.new_res_btn_clicked)
        action_lay.init_guest.connect(self.choose_guest_on_click)
        tab = QTabWidget()
        tab.addTab(res_details,"Basic")
        tab.addTab(QPushButton(),"Rooming List")
        main_layout.addWidget(self.res_ordered,0,0)
        main_layout.addWidget(rooms_avel,0,1)
        main_layout.addWidget(tab,1,0,1,3)
        main_layout.addLayout(action_lay,0,2,3,1)
        res_details.guest_id_signal.connect(self.choose_guest_on_click)

        self.setLayout(main_layout)
    def res_inited(self,e):
        # Gather info from res details -
        print('sss',e)
    def new_res_btn_clicked(self):
        print('create')
    def search_guest_btn_clicked(self):
        self._dialog = SearchGuest()
        self.parent.addSubWindow(self._dialog)
        self._dialog.chosen_guest.connect(self.choose_guest_on_click)
        self._dialog.show()

    def choose_guest_on_click(self,int):
        guest = Guest()
        guest.fetch_by_id(self.db,int)
        self.res_ordered.init_guest(guest)
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
