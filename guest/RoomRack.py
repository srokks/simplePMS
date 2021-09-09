import datetime
import sys
from PyQt5.QtGui import QPainter,QColor,QBrush,QPen,QFont
from PyQt5.QtSql import QSqlDatabase,QSqlTableModel
from PyQt5.QtCore import QAbstractTableModel,QEvent,Qt,QRect
from PyQt5.QtWidgets import (
    QDialog,
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
        main_lay = QVBoxLayout()

        sample_res = {'id': '123', 'name': 'Jarek Sroka', 'color': 'yellow'}
        self.res_id = sample_res['id']
        self.name = sample_res['name']
        if sample_res['color']=='':
            self.color = 'green'
        else:
            self.color = sample_res['color']
    def paintEvent(self, e):
        painter = QPainter(self)
        brush = QBrush()
        brush.setColor(QColor('green'))
        brush.setStyle(Qt.SolidPattern)
        rect = QRect(1,1,self.width()-1,self.height()-1,)
        # painter.fillRect(rect,brush)
        painter.drawRoundedRect(rect,2,2)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(self.height()-10)
        font.setBold(True)
        painter.setFont(font)
        pen = QPen()
        pen.setColor(QColor('black'))
        pen.setWidth(1)
        painter.setPen(pen)
        painter.drawText(5,self.height()-7,self.res_id+':'+self.name)
        painter.end()

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
        grid_layout = QGridLayout()
        grid_layout.setSpacing(1)

        today = datetime.date.today()
        # ----
        for i in range(1,days):
            lab = day_label()
            lab.setText((today-datetime.timedelta(days=i-2)).strftime('%d.%m'))
            grid_layout.addWidget(lab,0,i)
        for i in range(1,rooms):
            lab = room_label()
            lab.setText(ROOMS[i-1])
            grid_layout.addWidget(lab, i, 0)
        but = QPushButton()
        but.setText("FILTER")
        grid_layout.addWidget(but,0,0)
        grid_layout.addWidget(res_tile(), 2, 1, 1, 2)
        grid_layout.addWidget(res_tile(), 3, 5, 1, 2)
        wi = QWidget()
        wi.setLayout(grid_layout)
        scroll = QScrollArea()
        scroll.setWidget(wi)
        main_layout = QHBoxLayout()

        main_layout.addWidget(scroll)
        self.setLayout(main_layout)
    def test(self,e):
        print(e.pos())


app = QApplication(sys.argv)
win = room_rack()
win.resize(800,600)
win.show()
app.exec_()