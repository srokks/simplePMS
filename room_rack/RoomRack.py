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

ROOMS = [str(x) for x in range(101,150)]
today = datetime.date.today()
DAYS = [(today + datetime.timedelta(days=x)).strftime('%d.%m') for x in range(-3, 31)]
tile_height = 25
tile_width = 75
days_limit =25
rooms = len(ROOMS)
from room_rack.dayTile import DayTile

class res_tile(QWidget):
    def __init__(self):
        '''
        res_tile properties:
        self.id
        self.
        '''
        super(res_tile, self).__init__()
        main_lay = QHBoxLayout()
        main_lay.setContentsMargins(0, 0, 0, 0)
        main_lay.setSpacing(0)
        self.setLayout(main_lay)
        self._pressed = False

        sample_res = {'id': '123', 'name': 'Jarek Sroka', 'color': 'yellow'}
        self.res_id = sample_res['id']
        self.name = sample_res['name']
        if sample_res['color'] == '':
            self.color = 'red'
        else:
            self.color = sample_res['color']

    def mousePressEvent(self, event):
        self._pressed = True
        self.update()

    def mouseReleaseEvent(self, event):
        self._pressed = False
        self.update()

    def mouseMoveEvent(self, event):
        pass

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setRenderHint(painter.Antialiasing)

        if self._pressed == True:
            path = QPainterPath()
            path.addRoundedRect(2, 2, self.width() - 2, self.height() - 2, 3, 3)
            pen = QPen(QColor('red'), 1)
            painter.setPen(pen)
            painter.fillPath(path, QColor('green'))
            painter.drawPath(path)
        else:
            path = QPainterPath()
            path.addRoundedRect(1, 1, self.width() - 1, self.height() - 1, 5, 5)
            pen = QPen(QColor('red'), 1)
            painter.setPen(pen)
            painter.fillPath(path, QColor('red'))
            painter.drawPath(path)
        painter.end()


class day_label(QLabel):
    def __init__(self, date=''):
        super(day_label, self).__init__()
        self.setFixedHeight(tile_height)
        self.setFixedWidth(tile_width)
        self.setText("Day")
        self.setAlignment(Qt.AlignCenter)
        self.setFrameShape(QFrame.Panel)
        self.setFrameShadow(QFrame.Sunken)
        self.date = datetime.date(2000,1,1)
    def setDate(self,date):
        self.date=date
        self.setText(self.date.strftime('%d.%m'))
        self.setToolTip(self.date.strftime('%d.%m.%Y'))
    def mousePressEvent(self,e):
        print(self.date,self.size())
class room_label(QLabel):
    def __init__(self, date=''):
        super(room_label, self).__init__()
        self.setFixedSize(tile_width, tile_height)
        self.setText("Room")
        self.setFrameShape(QFrame.Panel)
        self.setFrameShadow(QFrame.Sunken)
        self.setAlignment(Qt.AlignCenter)
        self.room_id = None
        self.setWordWrap(True)
    def setID(self,room_id):
        self.room_id = room_id
        self.setText(self.room_id)
class room_rack(QWidget):
    def __init__(self):
        super().__init__()
        self.main_layout = QVBoxLayout()
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        # ----
        day_scroll = QScrollArea()
        day_scroll.setWidgetResizable(True)
        day_scroll.setContentsMargins(0, 0, 0, 0)
        day_scroll.setFrameShape(day_scroll.NoFrame)
        day_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        day_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        day_scroll.setFixedHeight(tile_height)
        day_wi = QWidget()
        self.day_lay = QHBoxLayout()
        self.day_lay.setSpacing(0)
        self.day_lay.setContentsMargins(0, 0, 0, 0)
        for i in range(days_limit):
            lab = day_label()
            lab.setDate(today+datetime.timedelta(days=i))
            lab.setWordWrap(True)
            self.day_lay.addWidget(lab)


        day_wi.setLayout(self.day_lay)
        day_scroll.setWidget(day_wi)
        # ---
        top_layout = QHBoxLayout()
        top_layout.setSpacing(0)
        top_layout.setContentsMargins(0, 0, 0, 0)
        self.filtr_btn = day_label()

        self.filtr_btn.setText("FILTER")

        # --
        top_layout.addWidget(self.filtr_btn)
        top_layout.addWidget(day_scroll)
        top_layout.setSpacing(0)
        top_layout.setContentsMargins(0, 0, 0, 0)
        # --
        room_scroll = QScrollArea()
        room_scroll.setWidgetResizable(True)
        room_scroll.setFrameShape(room_scroll.NoFrame)
        room_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        room_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        room_scroll.setMaximumWidth(tile_width)
        room_wi = QWidget()
        self.room_lay = QVBoxLayout()
        self.room_lay.setSpacing(0)
        self.room_lay.setContentsMargins(0, 0, 0, 0)
        for el in ROOMS:
            lab = room_label()
            lab.setID(el)
            self.room_lay.addWidget(lab)
        room_wi.setLayout(self.room_lay)
        room_scroll.setWidget(room_wi)
        # ------
        grid_scroll = QScrollArea()
        grid_scroll.setWidgetResizable(True)
        grid_scroll.setFrameShape(grid_scroll.NoFrame)
        grid_wi = QWidget()
        self.grid_lay = QHBoxLayout()
        self.grid_lay.setSpacing(0)
        self.grid_lay.setContentsMargins(0, 0, 0, 0)
        grid_scroll.verticalScrollBar().valueChanged.connect(
            lambda value: room_scroll.verticalScrollBar().setValue(value))
        grid_scroll.horizontalScrollBar().valueChanged.connect(
            lambda value: day_scroll.horizontalScrollBar().setValue(value))
        for i in range(len(self.day_lay)):
            lay = QVBoxLayout()
            lay.setSpacing(0)
            lay.setContentsMargins(0,0,0,0)
            date = self.day_lay.itemAt(i).widget().date
            lay.setObjectName(date.strftime('%d.%m.%Y'))
            for j in range(len(self.room_lay)):
                tile = DayTile()
                room_id = self.room_lay.itemAt(j).widget().room_id
                tile.setObjectName(lay.objectName()+'|'+room_id)
                lay.addWidget(tile)
            self.grid_lay.addLayout(lay)
        grid_wi.setLayout(self.grid_lay)
        grid_scroll.setWidget(grid_wi)
        # ----
        control_layout = QHBoxLayout()
        self.prev_day_btn = QPushButton()
        self.prev_day_btn.setText('<-')
        self.prev_day_btn.clicked.connect(self.prev_day_btn_on_click)
        control_layout.addWidget(self.prev_day_btn)
        self.today_btn = QPushButton()
        self.today_btn.setText("today")
        self.today_btn.clicked.connect(self.today_btn_on_click)
        control_layout.addWidget(self.today_btn)
        control_layout.addWidget(QPushButton("->"))
        # ----
        bottom_layout = QHBoxLayout()
        bottom_layout.setSpacing(0)
        bottom_layout.setContentsMargins(0, 0, 0, 0)
        bottom_layout.addWidget(room_scroll)
        bottom_layout.addWidget(grid_scroll)
        self.main_layout.addLayout(top_layout)
        self.main_layout.addLayout(bottom_layout)
        self.main_layout.addLayout(control_layout)
        self.setLayout(self.main_layout)
        #self.grid_lay.addWidget(res_tile(), 0, 1, 1, 4)

    def today_btn_on_click(self):
        print(self.day_lay.sizeHint())
        print(self.grid_lay.sizeHint())

    def prev_day_btn_on_click(self):

        #adds day label in up grid
        lab = day_label()
        lab.setDate((self.day_lay.itemAt(0).widget().date)-datetime.timedelta(days=1))
        self.day_lay.insertWidget(0,lab)
        lay = QVBoxLayout()
        lay.setSpacing(0)
        lay.setContentsMargins(0, 0, 0, 0)


        date = self.day_lay.itemAt(0).widget().date
        lay.setObjectName(date.strftime('%d.%m.%Y'))
        for j in range(len(self.room_lay)):
            tile = DayTile()
            room_id = self.room_lay.itemAt(j).widget().room_id
            tile.setObjectName(lay.objectName() + '|' + room_id)
            lay.addWidget(tile)
        self.grid_lay.insertLayout(0,lay)
        pass
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = room_rack()
    win.move(0, 0)
    win.resize(800, 600)
    win.show()
    app.exec_()
