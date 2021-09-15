import datetime
import sys
from PyQt5.QtGui import QPainter, QColor, QBrush, QPen, QFont, QPainterPath, QPixmap, QDrag
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtCore import QAbstractTableModel, QEvent, Qt, QRect, QMimeData, pyqtSignal
from PyQt5.QtWidgets import (
    QDialog,
    QSizeGrip,
    QScrollArea,
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

ROOMS = [str(x) for x in range(101, 150)]
today = datetime.date.today()
DAYS = [(today + datetime.timedelta(days=x)).strftime('%d.%m') for x in range(-3, 31)]
tile_height = 25
tile_width = 75
days_limit = 31
rooms = len(ROOMS)

class DayTile(QWidget):
    clicked = pyqtSignal()

    def __init__(self):
        super(DayTile, self).__init__()
        self.setFixedSize(tile_width, tile_height)
        pixmap = QPixmap(self.width(), self.height())
        main_lay = QHBoxLayout()
        main_lay.setContentsMargins(0, 0, 0, 0)
        main_lay.setSpacing(0)
        self.room_id = None
        self.date = datetime.date(2000, 1, 1)
        self.installEventFilter(self)
        self.selected = None
        self.hover = False
        self.over = False
        self.setLayout(main_lay)
        self.pressed_point = None

    def set_name(self, date, room_id):
        self.date = date
        self.room_id = room_id

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setRenderHint(painter.Antialiasing)
        path = QPainterPath()
        rect = QRect(0, 0, self.width(), self.height())
        pen = QPen(QColor('red'), 1)
        painter.setPen(pen)
        painter.drawRect(rect)
        if self.selected == 'L' or self.selected == 'R':
            if self.selected == 'L':
                rect = QRect(0, 0, int(self.width() / 2), self.height())
            elif self.selected == 'R':
                rect = QRect(int(self.width() / 2), 0, self.width(), self.height())
            brush = QBrush()
            brush.setColor(QColor(195, 195, 195))
            brush.setStyle(Qt.SolidPattern)
            painter.fillRect(rect, brush)
        elif self.hover == True:
            brush = QBrush()
            rect = QRect(0, 0, self.width(), self.height())
            brush.setColor(QColor(195, 195, 12))
            brush.setStyle(Qt.SolidPattern)
            painter.fillRect(rect, brush)

    # def mouseMoveEvent(self,event):
    #     '''when tile pressed restrict mouse movement to y dimension'''
    #
    #     self.cursor().setPos(self.cursor().pos().x(),self.pressed_point)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Leave:
            self.offHovered()
        elif event.type() == QEvent.Enter:
            self.onHovered()
        elif event.type() == QEvent.MouseButtonPress:
            self.on_pressed(event)
        elif event.type() == QEvent.MouseButtonRelease:
            self.on_release()
        return super(DayTile, self).eventFilter(obj, event)

    def on_release(self):
        self.selected = None
        self.update()

    def on_pressed(self, event):
        if event.pos().x() < tile_width / 2:
            self.selected = 'L'
            self.update()
        if event.pos().x() > tile_width / 2:
            self.selected = 'R'
            self.update()
            # Fixme: get rid of it
        print(self.date, self.room_id, sep="|")

    def onHovered(self):
        # self.hover = True
        # print('hovered')
        # self.update()

        pass

    def offHovered(self):
        # self.hover = False
        # print('hovered')

        pass
        # self.update()

    # def mousePressEvent(self, event):
    #     if event.buttons() & Qt.LeftButton:
    #         self.dragstart = event.pos()
    #         self.clicked.emit()
    #     clicked_pos = event.pos().x()
    #     self.pressed_point = self.cursor().pos().y()
    #
    #     if clicked_pos<tile_width/2:
    #         #triggered when clicked left side of widget
    #         print('l')
    #         self.selected='L'
    #         self.update()
    #     elif clicked_pos>tile_width/2:
    #         #triggered when clicked right side of widget
    #         self.selected='R'
    #         self.update()
    # def mouseReleaseEvent(self, event):
    #     self.selected=None
    #     self.dragstart = None
    #     self.update()
