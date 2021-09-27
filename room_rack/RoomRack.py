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
tile_width = 75
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
        label.setText('ss')
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


class DaysWidget(QWidget):
    def __init__(self):
        super(DaysWidget, self).__init__()
        self.setMaximumHeight(2 * tile_height)

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setRenderHint(painter.Antialiasing)
        path = QPainterPath()
        rect = QRect(0, 0, self.width(), self.height())
        pen = QPen(QColor('blue'), 1)
        painter.setPen(pen)
        painter.drawRect(rect)


class RoomsWidget(QScrollArea):
    def __init__(self):
        super(RoomsWidget, self).__init__()
        self.setFixedWidth(tile_width)
        self.set
        lay = QVBoxLayout()
        for i in range(50):
            lay.addWidget(QPushButton(str(i)))
        self.setLayout(lay)



class ReservationsWidget(QWidget):
    def __init__(self):
        super(ReservationsWidget, self).__init__()


    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setRenderHint(painter.Antialiasing)
        path = QPainterPath()
        rect = QRect(0, 0, self.width(), self.height())
        pen = QPen(QColor('red'), 1)
        painter.setPen(pen)
        painter.drawRect(rect)


class RoomRackWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.load_reservations()
        # ----- Test area
        # Widget declarations

        # Main layout
        lay = QHBoxLayout()
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(0)
        room_layout = QGridLayout()
        room_layout.setContentsMargins(0, 0, 0, 0)
        room_layout.setSpacing(0)
        room_layout.addWidget(QPushButton('Filter'))
        room_layout.addWidget(QPushButton('Zoom'))
        room_layout.addWidget(RoomsWidget())
        days_lay = QVBoxLayout()
        days_lay.addWidget(DaysWidget())
        days_lay.addWidget(ReservationsWidget())
        lay.addLayout(room_layout)
        lay.addLayout(days_lay)
        self.setLayout(lay)

    def load_reservations(self):
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
