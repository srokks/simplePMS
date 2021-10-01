from PyQt5.QtCore import QRect,Qt,QDate,QModelIndex
from PyQt5.QtGui import QPainter, QPainterPath, QPen, QColor,QStandardItemModel,QKeyEvent
from PyQt5.QtWidgets import QWidget, QHBoxLayout,QTableWidget,QHeaderView,QVBoxLayout,QPushButton,QTableWidgetItem

class table(QTableWidget):
    def __init__(self,no_of_guests:int=0):

        super(table, self).__init__()
        if no_of_guests == 0:
            #TODO: show to fill guest no in res details
            pass
        else:
            self.no_of_guest=no_of_guests
        # ---
        #---
        self.setEditTriggers(self.DoubleClicked)

        #Inits
        #TODO: gets atributes from res_widget
        self.no_of_guest = 4 # no of guest from res details
        self.arrival_date = QDate(2021,10,1)
        self.departure_date = QDate(2021,10,5)
        # ----
        self.verticalHeader().hide()
        self.setColumnCount(4)
        self.setHorizontalHeaderLabels(['Name', 'Room no', 'Arrival date', 'Departure date'])
        self.setRowCount(self.no_of_guest)
        for i in range(self.rowCount()):
            self.setItem(i,2,QTableWidgetItem(self.arrival_date.toString(Qt.SystemLocaleShortDate)))
            self.setItem(i,3,QTableWidgetItem(self.arrival_date.toString(Qt.SystemLocaleShortDate)))

    def keyPressEvent(self, e:QKeyEvent):
        if e.key()==16777219:
            if self.item(self.currentIndex().row(),self.currentIndex().column()) is None:
                pass
            else:
                self.item(self.currentIndex().row(),self.currentIndex().column()).setText('')


class RoomingListWidget(QWidget):
    def __init__(self):
        super(RoomingListWidget, self).__init__()
        self.setMinimumHeight(200)
        self.setMinimumWidth(200)
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        tab = table()
        # ---
        buttons_lay = QVBoxLayout() # action  button layout
        buttons_lay.setContentsMargins(0,0,0,0)
        buttons_lay.setAlignment(Qt.AlignTop)
        add_guest_btn = QPushButton()
        add_guest_btn.setFixedSize(30,30)
        add_guest_btn.setText('+')
        buttons_lay.addWidget(add_guest_btn)

        # ---
        main_layout.addWidget(tab)
        main_layout.addLayout(buttons_lay)
        self.setLayout(main_layout)
    def new_room(self,e):
        pass
    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setRenderHint(painter.Antialiasing)
        path = QPainterPath()
        rect = QRect(0, 0, self.width(), self.height())
        pen = QPen(QColor('purple'), 1)
        painter.setPen(pen)
        painter.drawRect(rect)
