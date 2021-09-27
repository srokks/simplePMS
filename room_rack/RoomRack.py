import datetime
import sys
from PyQt5.QtGui import QPainter, QColor, QBrush, QPen, QFont, QPainterPath, QPixmap, QDrag
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtCore import QAbstractTableModel, QEvent, Qt, QRect, QMimeData, pyqtSignal
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
tile_width = 70
days_limit = 25


class RoomTile(QWidget):
    def __init__(self, room):
        super(RoomTile, self).__init__()
        self.setFixedSize(tile_width, tile_height)
        main_lay = QVBoxLayout()
        main_lay.setContentsMargins(0, 0, 0, 0)
        main_lay.setSpacing(0)
        label = QLabel()
        label.setText(room.room_no)
        label.setAlignment(Qt.AlignVCenter)
        label.setContentsMargins(5, 0, 0, 0)
        label.setToolTip(f'{room.room_no}\n{room.room_type_id}\nFloor:{room.floor}')
        main_lay.addWidget(label)

        self.setLayout(main_lay)

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setRenderHint(painter.Antialiasing)
        path = QPainterPath()
        rect = QRect(0, 0, self.width(), self.height())
        pen = QPen(QColor('red'), 1)
        painter.setPen(pen)
        painter.drawRect(rect)


class DayTile(QWidget):
    def __init__(self):
        super(DayTile, self).__init__()
        self.setFixedSize(tile_width, tile_height)
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
        rect = QRect(0, 0, self.width(), self.height())
        pen = QPen(QColor('blue'), 1)
        painter.setPen(pen)
        painter.drawRect(rect)

class BlankTile(QWidget):
    def __init__(self):
        super(BlankTile, self).__init__()
        self.setFixedSize(tile_width, tile_height)
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
        rect = QRect(0, 0, self.width(), self.height())
        pen = QPen(QColor('green'), 1)
        painter.setPen(pen)
        painter.drawRect(rect)

class BlankWidget(QWidget):
    def __init__(self, color):
        super(BlankWidget, self).__init__()
        self.color = color

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setRenderHint(painter.Antialiasing)
        path = QPainterPath()
        rect = QRect(0, 0, self.width(), self.height())
        pen = QPen(QColor(self.color), 1)
        painter.setPen(pen)
        painter.drawRect(rect)

class ResTile(QWidget):
    def __init__(self):
        super(ResTile, self).__init__()
        self.setFixedSize(tile_width/2, tile_height)
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
        rect = QRect(0, 0, self.width(), self.height())
        pen = QPen(QColor('black'), 1)
        painter.setPen(pen)
        painter.drawRect(rect)

class DaysWidget(QScrollArea):
    def __init__(self):
        super(DaysWidget, self).__init__()

        self.setMaximumHeight(2 * tile_height)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setFrameStyle(self.NoFrame)
        self.setWidgetResizable(True)
        main_widget = QWidget()
        announcer_lay = QHBoxLayout()
        announcer_lay.setContentsMargins(0, 0, 0, 0)
        announcer_lay.setSpacing(0)
        for i in range(days_limit):
            announcer_lay.addWidget(BlankTile())
        day_lay = QHBoxLayout()
        day_lay.setContentsMargins(0, 0, 0, 0)
        day_lay.setSpacing(0)
        for i in range(days_limit):
            day_lay.addWidget(DayTile())
        combo_lay = QVBoxLayout()
        combo_lay.setSpacing(0)
        combo_lay.setContentsMargins(0,0,0,0)
        combo_lay.addLayout(announcer_lay)
        combo_lay.addLayout(day_lay)
        main_widget.setLayout(combo_lay)
        self.setWidget(main_widget)



class RoomsWidget(QScrollArea):
    def __init__(self,rooms):
        super(RoomsWidget, self).__init__()
        self.setFixedWidth(tile_width)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setFrameStyle(self.NoFrame)
        self.setWidgetResizable(True)
        main_widget = QWidget()
        lay = QVBoxLayout()
        lay.setContentsMargins(0,0,0,0)
        lay.setSpacing(0)
        for room in rooms:
            lay.addWidget(RoomTile(room))
        main_widget.setLayout(lay)
        self.setWidget(main_widget)



class ReservationsWidget(QScrollArea):
    v_scroll = pyqtSignal(int)
    h_scroll = pyqtSignal(int)
    def __init__(self,rooms_count,days_count):
        super(ReservationsWidget, self).__init__()
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setFrameStyle(self.NoFrame)
        self.setWidgetResizable(True)
        main_widget = QWidget()
        lay = QGridLayout()
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(0)
        for i in range(rooms_count):
            for j in range(days_count):
                lay.addWidget(ResTile(),i,j)
        main_widget.setLayout(lay)
        self.verticalScrollBar().valueChanged.connect(self.v_scroll_emit)
        self.horizontalScrollBar().valueChanged.connect(self.v_scroll_emit)
        self.setWidget(main_widget)

    def v_scroll_emit(self,int):
        self.v_scroll.emit(int)
    def h_scroll_emit(self,int):
        self.h_scroll.emit(int)
class RoomRackWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.load_rooms()

        # ----- Test area
        # Widget declarations

        # Main layout
        lay = QHBoxLayout()
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(0)
        room_layout = QGridLayout()
        room_layout.setContentsMargins(0, 0, 0, 0)
        room_layout.setSpacing(0)
        self.filter_btn = QPushButton('Filter')

        room_layout.addWidget(BlankTile())
        room_layout.addWidget(BlankTile())
        room_layout.addWidget(RoomsWidget(self.rooms))
        days_lay = QVBoxLayout()
        days_lay.addWidget(DaysWidget())
        res_wi = ReservationsWidget(len(self.rooms),days_limit)
        res_wi.v_scroll.connect(self.scroll)
        days_lay.addWidget(res_wi)
        lay.addLayout(room_layout)
        lay.addLayout(days_lay)
        self.setLayout(lay)
    def scroll(self, int):
        print(int)
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
