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
from reservation.ReservationAvelRoomsWidget import ReservationAvelRooms
from reservation.ReservationDetailWidget import ReservationDetailWidget
from reservation.ReservationOrderedWidget import ReservationOrderedWidget

class ReservationActionLayout(QVBoxLayout):
    search_guest_signal = pyqtSignal()
    def __init__(self):
        super(ReservationActionLayout, self).__init__()

        self.search_guest_btn = QPushButton()
        self.search_guest_btn.setText("Search guest")
        self.search_guest_btn.clicked.connect(self.search_guest_btn_clicked)
        self.addWidget(QPushButton("New"))
        self.addWidget(QPushButton("Change"))
        self.addWidget(self.search_guest_btn)
        self.addWidget(QPushButton("Close"))
        self.addStretch()

    def search_guest_btn_clicked(self):
        self.search_guest_signal.emit()



class ReservationEdit(QWidget):
    def __init__(self):
        super(ReservationEdit, self).__init__()
        self.resize(200,200)
        main_layout = QGridLayout()
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(5,5,5,5)

        res_details = ReservationDetailWidget()
        res_ordered = ReservationOrderedWidget(self)
        rooms_avel = ReservationAvelRooms()
        action_lay = ReservationActionLayout()

        main_layout.addWidget(res_ordered,0,0)
        main_layout.addWidget(rooms_avel,0,1)
        main_layout.addWidget(res_details,1,0,1,2)
        main_layout.addLayout(action_lay,0,2,3,1)
        self.setLayout(main_layout)
class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        lay = QVBoxLayout()
        self.mdi_area = QMdiArea()
        res_edit = ReservationEdit()

        self.mdi_area.addSubWindow(res_edit)
        self.mdi_area.
        lay.addWidget(self.mdi_area)
        self.setLayout(lay)
if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    win = MainWindow()
    win.move(0, 0)
    win.resize(600, 600)
    win.show()
    app.exec_()
