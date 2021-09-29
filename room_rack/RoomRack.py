import datetime
import sys
from PyQt5.QtGui import QPainter, QColor, QBrush, QPen, QFont, QPainterPath, QPixmap, QDrag
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtCore import QAbstractTableModel, QEvent, Qt, QRect, QMimeData, pyqtSignal,QDate
from PyQt5.QtWidgets import (
    QDialog,
    QSizeGrip,
    QMdiSubWindow,
    QInputDialog,
    QScrollArea,
    QMdiArea,
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

import db.Connection
from room_rack.Room import Rooms

today = datetime.date.today()
DAYS = [(today + datetime.timedelta(days=x)).strftime('%d.%m') for x in range(-3, 31)]
tile_height = 25
tile_width = 80
days_limit = 10


from room_rack.rack_tiles import *

class DaysWidget(QScrollArea):
    def __init__(self,date_from:QDate,days_limit:int):
        super(DaysWidget, self).__init__()

        self.setMaximumHeight(2 * tile_height)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setFrameStyle(self.NoFrame)
        self.setWidgetResizable(True)
        main_widget = QWidget()
        announcer_lay = QHBoxLayout()
        announcer_lay.setAlignment(Qt.AlignLeft)
        announcer_lay.setContentsMargins(0, 0, 0, 0)
        announcer_lay.setSpacing(0)
        for i in range(days_limit):
            announcer_lay.addWidget(BlankTile())
        day_lay = QHBoxLayout()
        day_lay.setAlignment(Qt.AlignLeft)
        day_lay.setContentsMargins(0, 0, 0, 0)
        day_lay.setSpacing(0)
        for i in range(days_limit):
            day_lay.addWidget(DayTile(date_from.addDays(i)))
        combo_lay = QVBoxLayout()
        combo_lay.setSpacing(0)
        combo_lay.setContentsMargins(0, 0, 0, 0)
        combo_lay.addLayout(announcer_lay)
        combo_lay.addLayout(day_lay)
        main_widget.setLayout(combo_lay)
        self.setWidget(main_widget)

class RoomsWidget(QScrollArea):
    v_scroll = pyqtSignal(int)

    def __init__(self, rooms):
        super(RoomsWidget, self).__init__()
        self.setFixedWidth(tile_width)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setFrameStyle(self.NoFrame)
        self.setWidgetResizable(True)
        main_widget = QWidget()
        lay = QVBoxLayout()
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(0)
        lay.setAlignment(Qt.AlignTop or Qt.AlignLeft)
        for room in rooms:
            lay.addWidget(RoomTile(room))
        main_widget.setLayout(lay)
        self.setWidget(main_widget)
        self.verticalScrollBar().valueChanged.connect(self.v_scroll.emit)

class ResWidget(QWidget):
    def __init__(self):
        self.clicked = False
        super(ResWidget, self).__init__()
        self.setFixedHeight( tile_height)
        main_lay = QVBoxLayout()
        main_lay.setContentsMargins(0, 0, 0, 0)
        main_lay.setSpacing(0)
        label = QLabel()
        label.setAlignment(Qt.AlignVCenter)
        label.setContentsMargins(5, 0, 0, 0)

        main_lay.addWidget(label)

        self.setLayout(main_lay)

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setRenderHint(painter.Antialiasing)
        path = QPainterPath()
        rect = QRect(2, 2, self.width()-4, self.height()-4)
        pen = QPen(QColor('red'), 1)
        brush = QBrush()
        brush.setStyle(Qt.SolidPattern)
        brush.setColor(QColor('red'))
        painter.fillRect(rect,brush)
    def mousePressEvent(self, e):
        self.clicked = True
        print(self)
        self.repaint()
    def mouseReleaseEvent(self, e):
        self.clicked = False
        self.repaint()

class ReservationsWidget(QScrollArea):


    def __init__(self, rooms, days_count):
        super(ReservationsWidget, self).__init__()
        # self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.setFrameStyle(self.NoFrame)
        self.setWidgetResizable(True)
        main_widget = QWidget()
        lay = QGridLayout()
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setAlignment(Qt.AlignTop or Qt.AlignLeft)
        lay.setSpacing(0)
        for i in range(rooms):
            for j in range(days_count):
                lay.addWidget(ResTile(parent=lay,date=QDate().currentDate().addDays(int(j/2))),i,j)



        main_widget.setLayout(lay)

        self.setWidget(main_widget)

class RoomRackWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.load_rooms()
        self.date_from = QDate().currentDate()
        # ----- Test area
        # Widget declarations

        # Main layout
        lay = QHBoxLayout()
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(0)
        # ----
        room_layout = QGridLayout()
        room_layout.setContentsMargins(0, 0, 0, 0)
        room_layout.setSpacing(0)
        # ----
        self.filter_btn = QPushButton('Filter')
        # ----
        room_layout.addWidget(BlankTile())
        room_layout.addWidget(BlankTile())
        # ----
        self.rooms_wi = RoomsWidget(self.rooms)
        self.rooms_wi.verticalScrollBar().valueChanged.connect(self.res_wi_v_scroll)
        # ----
        room_layout.addWidget(self.rooms_wi)
        # ----
        days_lay = QVBoxLayout()
        # ----
        self.days_wi = DaysWidget(self.date_from,days_limit)
        self.days_wi.horizontalScrollBar().valueChanged.connect(self.res_wi_h_scroll)
        # ----
        self.res_wi = ReservationsWidget(len(self.rooms), days_limit)
        self.res_wi.horizontalScrollBar().valueChanged.connect(self.days_wi_h_scroll)
        self.res_wi.verticalScrollBar().valueChanged.connect(self.rooms_wi_v_scroll)
        # ----
        days_lay.addWidget(self.days_wi)
        days_lay.addWidget(self.res_wi)
        # ----
        lay.addLayout(room_layout)
        lay.addLayout(days_lay)
        h_lay = QVBoxLayout()
        h_lay.setContentsMargins(0,0,0,0)
        h_lay.addLayout(lay)

        butlay = QHBoxLayout()
        butlay.addWidget(QPushButton('<-'))
        butlay.addWidget(QPushButton('today'))
        butlay.addWidget(QPushButton('->'))

        h_lay.addLayout(butlay)
        self.setLayout(h_lay)

    def res_wi_v_scroll(self, int):
        self.res_wi.verticalScrollBar().setValue(int)

    def res_wi_h_scroll(self, int):
        self.res_wi.horizontalScrollBar().setValue(int)

    def rooms_wi_v_scroll(self, int):
        self.rooms_wi.verticalScrollBar().setValue(int)

    def days_wi_h_scroll(self, int):
        self.days_wi.horizontalScrollBar().setValue(int)

    def load_rooms(self):
        'Loads rooms from db and '
        self.rooms = Rooms(db.Connection.Connection().db)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        main_wi = QWidget()
        main_lay = QVBoxLayout()
        main_wi.setLayout(main_lay)

        self.mdi_area = QMdiArea()
        room_rack = RoomRackWindow()
        main_lay.addWidget(self.mdi_area)
        sub = QMdiSubWindow()
        sub.setWidget(room_rack)
        self.mdi_area.addSubWindow(sub)
        sub.showMaximized()
        self.setCentralWidget(main_wi)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.move(0, 0)
    win.resize(800, 600)
    win.show()
    app.exec_()
