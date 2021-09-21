from PyQt5.QtGui import QPainter, QColor, QBrush, QPen, QFont, QPainterPath, QPixmap, QDrag
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlRelationalTableModel, QSqlQueryModel
from PyQt5.QtCore import QAbstractTableModel, QEvent, Qt, QRect, QMimeData, pyqtSignal, QDir
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
    QGroupBox,
    QFrame,
QFormLayout,
)



class ReservationDetailWidget(QWidget):
    def __init__(self):
        super(ReservationDetailWidget, self).__init__()
        main_layout = QHBoxLayout()
        form1 = QFormLayout()
        self.room_type_cmb = QComboBox()
        #TODO: database implementation
        self.room_type_cmb.addItems(['SGL','DBL'])

        form1.addRow("Room category:",self.room_type_cmb)
        form1.addRow("Arrival:",QLineEdit())
        form1.addRow("Nigts:",QLineEdit())
        form1.addRow("No. of rooms:",QLineEdit())
        form1.addRow("No. of guest:",QLineEdit())

        form2 = QFormLayout()

        form2.addRow("Room:",QLineEdit())
        form2.addRow("Departure:",QLineEdit())
        form2.addRow("Reservation no.:",QLineEdit())
        form2.addRow("Reservation type:",QComboBox())
        form2.addRow("Channel:",QComboBox())


        lay3= RoomingListWidget()

        main_layout.addLayout(form1)
        main_layout.addLayout(form2)
        main_layout.addWidget(lay3)
        self.setLayout(main_layout)
class RoomingListWidget(QWidget):
    def __init__(self):
        super(RoomingListWidget, self).__init__()
        self.setMinimumHeight(200)
        self.setMinimumWidth(200)
        main_layout = QHBoxLayout()

        self.setLayout(main_layout)
    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setRenderHint(painter.Antialiasing)
        path = QPainterPath()
        rect = QRect(0, 0, self.width(), self.height())
        pen = QPen(QColor('purple'), 1)
        painter.setPen(pen)
        painter.drawRect(rect)

class ReservationOrderedWidget(QWidget):
    def __init__(self):
        super(ReservationOrderedWidget, self).__init__()
        self.setMinimumSize(250,250)
        main_layout = QHBoxLayout()

        form_lay = QFormLayout()

        gender_type_lay = QHBoxLayout()
        gender_type_lay.addWidget(QComboBox())
        gender_type_lay.addWidget(QComboBox())

        count_pstcd_cty = QHBoxLayout()
        count_pstcd_cty.addWidget(QLineEdit())
        count_pstcd_cty.addWidget(QLineEdit())
        count_pstcd_cty.addWidget(QLineEdit())

        form_lay.addRow('Title/guest type:',gender_type_lay)
        form_lay.addRow('First name:',QLineEdit())
        form_lay.addRow('Last name:',QLineEdit())
        form_lay.addRow('Street:',QLineEdit())
        form_lay.addRow('Country/Post code/City:',count_pstcd_cty)
        form_lay.addRow('Phone:',QLineEdit())
        form_lay.addRow('Email:',QLineEdit())
        form_lay.addRow('Last stay:',QLineEdit())

        main_layout.addLayout(form_lay)
        self.setLayout(main_layout)
    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setRenderHint(painter.Antialiasing)
        path = QPainterPath()
        rect = QRect(0, 0, self.width(), self.height())
        pen = QPen(QColor('red'), 1)
        painter.setPen(pen)
        painter.drawRect(rect)
class ReservationAvelRooms(QWidget):
    def __init__(self):
        super(ReservationAvelRooms, self).__init__()
        self.setMinimumSize(200,200)
        main_layout = QHBoxLayout()
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0,0,0,0)
        self.tab_widget = QTabWidget()
        self.tab_widget.addTab(QWidget(),'Criteria')
        self.tab_widget.addTab(QWidget(),'Avel rooms')
        self.tab_widget.setCurrentIndex(1)
        main_layout.addWidget(self.tab_widget)
        self.setLayout(main_layout)
    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setRenderHint(painter.Antialiasing)
        path = QPainterPath()
        rect = QRect(0, 0, self.width(), self.height())
        pen = QPen(QColor('green'), 1)
        painter.setPen(pen)
        painter.drawRect(rect)
class ReservationEdit(QWidget):
    def __init__(self):
        super(ReservationEdit, self).__init__()
        main_layout = QGridLayout()
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(5,5,5,5)

        res_details = ReservationDetailWidget()
        res_ordered = ReservationOrderedWidget()
        rooms_avel = ReservationAvelRooms()
        main_layout.addWidget(res_ordered,0,0)
        main_layout.addWidget(rooms_avel,0,1)
        main_layout.addWidget(res_details,1,0,1,2)
        self.setLayout(main_layout)

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    win = ReservationEdit()
    win.move(0, 0)
    win.resize(400, 400)
    win.show()
    app.exec_()
