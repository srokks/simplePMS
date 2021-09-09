import datetime
import sys
from PyQt5.QtGui import QPainter, QColor, QBrush, QPen, QFont, QPainterPath,QPixmap
from PyQt5.QtSql import QSqlDatabase,QSqlTableModel
from PyQt5.QtCore import QAbstractTableModel,QEvent,Qt,QRect
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

ROOMS = [str(x) for x in range (101,121)]
today = datetime.date.today()
DAYS = [(today+datetime.timedelta(days=x)).strftime('%d.%m') for x in range(-3,31)]
tile_height = 25
tile_width = 100
days = 31
rooms = len(ROOMS)


class res_tile(QWidget):
    def __init__(self):
        super(res_tile, self).__init__()
        main_lay = QHBoxLayout()
        main_lay.setContentsMargins(0,0,0,0)
        main_lay.setSpacing(0)
        self.setLayout(main_lay)



        sample_res = {'id': '123', 'name': 'Jarek Sroka', 'color': 'yellow'}
        self.res_id = sample_res['id']
        self.name = sample_res['name']
        if sample_res['color']=='':
            self.color = 'green'
        else:
            self.color = sample_res['color']
    def mouseMoveEvent(self, event):
        print(event.pos())
    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setRenderHint(painter.Antialiasing)
        path = QPainterPath()
        rect = QRect (1,1,self.width(),self.height())

        path.addRoundedRect(1,1,self.width()-1,self.height()-1,5,5)

        pen = QPen(QColor('green'),1)
        painter.setPen(pen)
        painter.fillPath(path,QColor('red'))
        painter.drawPath(path)
        painter.end()
    def mousePressEvent(self, event):
        print(self.size())
class day_tile(QWidget):
    def __init__(self):
        super(day_tile, self).__init__()
        pixmap = QPixmap(self.width(),self.height())
        main_lay = QHBoxLayout()
        main_lay.setContentsMargins(0,0,0,0)
        main_lay.setSpacing(0)
        self.selected = None
        self.setLayout(main_lay)

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setRenderHint(painter.Antialiasing)
        path = QPainterPath()
        rect = QRect (0,0,self.width(),self.height())
        painter.drawRect(rect)
        print(e.type())
        if self.selected=='L' or self.selected=='R':
            if self.selected=='L':
                rect = QRect(0,0,int(self.width()/2),self.height())
            elif self.selected=='R':
                rect = QRect(int(self.width()/2), 0, self.width(), self.height())
            brush = QBrush()
            brush.setColor(QColor(195,195,195))
            brush.setStyle(Qt.SolidPattern)
            painter.fillRect(rect,brush)

        painter.end()

    def draw_something(self):
        painter = QPainter(self.pixmap())
        pen = QPen()
        pen.setWidth(40)
        pen.setColor(QColor('red'))
        painter.setPen(pen)
        painter.drawPoint(200, 150)
        painter.end()

    def mousePressEvent(self, event):
        clicked_pos = event.pos().x()
        if clicked_pos<tile_width/2:
            print('L')
            self.selected='L'
            self.update()
        elif clicked_pos>tile_width/2:
            print('R')
            self.selected='R'
            self.update()
    def mouseReleaseEvent(self, event):
        self.selected=None
        self.update()
class day_label(QLabel):
    def __init__(self,date=''):
        super(day_label, self).__init__()
        self.setFixedSize(70,tile_height)
        self.setText("Day")
        self.setAlignment(Qt.AlignCenter)
        self.setFrameShape(QFrame.Panel)
        self.setFrameShadow(QFrame.Sunken)
class room_label(QLabel):
    def __init__(self,date=''):
        super(room_label, self).__init__()
        self.setFixedSize(70,tile_height)
        self.setText("Room")
        self.setFrameShape(QFrame.Panel)
        self.setFrameShadow(QFrame.Sunken)
        self.setAlignment(Qt.AlignCenter)
class room_rack(QWidget):
    def __init__(self):
        super().__init__()# self.setMaximumSize(400,300)
        self.grid_layout = QGridLayout()
        self.grid_layout.setSpacing(1)
        gripper = QSizeGrip(self)
        today = datetime.date.today()
        # ----

        for i in range(1,days*2,2):
            lab = day_label()
            lab.setText((today-datetime.timedelta(days=i-2)).strftime('%d.%m'))
            self.grid_layout.addWidget(lab,0,i,1,2)
        for i in range(1,rooms):
            lab = room_label()
            lab.setText(ROOMS[i-1])
            self.grid_layout.addWidget(lab, i, 0)
        for i in range(1,self.grid_layout.columnCount(),2):
            for j in range(1,self.grid_layout.rowCount()):
                self.grid_layout.addWidget(day_tile(), j, i, 1, 2)
        # self.grid_layout.addWidget(day_tile(),1,1,1,2)
        but = QPushButton()
        but.setText("FILTER")
        self.i = 1
        self.grid_layout.addWidget(but,0,0)
        # self.grid_layout.addWidget(day_tile(), 1, 1, 1, 2)
        # self.grid_layout.addWidget(res_tile(),self.i, 2, 1, 2)
        # self.grid_layout.addWidget(res_tile(), 3, 4, 1, 2)
        # self.grid_layout.addWidget(res_tile(), 1, 2, 1, 2)
        wi = QWidget()
        wi.setLayout(self.grid_layout)
        scroll = QScrollArea()
        scroll.setWidget(wi)
        main_layout = QHBoxLayout()

        main_layout.addWidget(scroll)
        self.setLayout(main_layout)
    def test(self,e):
        self.i += 1
        self.grid_layout.addWidget(day_tile(), self.i, 2, 1, 2)

app = QApplication(sys.argv)
win = room_rack()
win.move(0,0)
win.resize(800,600)
win.show()
app.exec_()