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


class guestCompleter(QWidget):
    def __init__(self,db=None,strName=''):
        super(guestCompleter, self).__init__()
        if db==None:
            self.db = Connection().db
        else:
            self.db = db
        main_lay = QVBoxLayout()
        strName.split(',')

        model = QSqlRelationalTableModel()
        tab = QTableView()
        tab.setModel(model)
        query = QSqlQuery(db=self.db)
        query.prepare(
            "SELECT gGuestID,gFirstName,gLastName ,aCity,gPhoneNumber,gMailAddress FROM tblGuest "
            "LEFT OUTER JOIN tblAddresses ON tblGuest.gAddressID = tblAddresses.aAddressID "
            "WHERE "
            "gLastName LIKE '%' || :last_name || '%' AND "
            "gFirstName LIKE '%' || :first_name || '%' AND "
            "aCity LIKE '%' || :city || '%'"

        )
        main_lay.addWidget(tab)
        self.setLayout(main_lay)


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        lay = QVBoxLayout()
        self.mdi_area = QMdiArea()

        self.mdi_area.addSubWindow(guestCompleter())

        lay.addWidget(self.mdi_area)
        self.setLayout(lay)

2
if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    win = MainWindow()
    win.move(200, 200)
    # win.resize(600, 600)
    win.show()
    app.exec_()



