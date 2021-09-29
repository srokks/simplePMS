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
tile_height = 25
tile_width = 80
class DayTile(QWidget):
    def __init__(self,date:QDate):
        super(DayTile, self).__init__()
        self.setFixedSize(tile_width, tile_height)
        main_lay = QVBoxLayout()
        main_lay.setContentsMargins(0, 0, 0, 0)
        main_lay.setSpacing(0)
        label = QLabel()
        font = QFont('Arial',11)
        label.setFont(font)

        label.setText(date.toString('dd/MM (ddd)'))
        label.setToolTip(date.toString('dd/MM/yyyy'))
        label.font().setPointSize(2)
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
        label.setToolTip(f'{room.room_no}\nType:{room.room_type_id}\nFloor:{room.floor}\n'
                         f'Status ID:{room.rooms_status_id}\nDesc:{room.desc}')

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

class ResTile(QWidget):
    def __init__(self,parent=None,date:QDate=None):
        self.clicked = False
        super(ResTile, self).__init__()
        self.parent:QGridLayout = parent
        self.setFixedSize(int(tile_width/2), tile_height)
        main_lay = QVBoxLayout()
        main_lay.setContentsMargins(0, 0, 0, 0)
        main_lay.setSpacing(0)
        label = QLabel()
        label.setAlignment(Qt.AlignVCenter)
        label.setContentsMargins(5, 0, 0, 0)
        self.setProperty('date',date)
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
        if self.clicked:
            path = QPainterPath()
            rect = QRect(0, 0, self.width(), self.height())
            pen = QPen(QColor('blue'), 1)
            painter.setPen(pen)
            brush = QBrush()
            brush.setStyle(Qt.SolidPattern)
            painter.fillRect(rect,brush)
    def mousePressEvent(self, e):
        self.clicked = True
        index = self.parent.indexOf(self)
        pos = self.parent.getItemPosition(index)
        #way to insert res tiles in grid
        # self.parent.addWidget(ResWidget(),pos[0],pos[1],1,1)
        print(self.property('date'))
        self.repaint()

    def mouseReleaseEvent(self, e):
        self.clicked = False
        self.repaint()