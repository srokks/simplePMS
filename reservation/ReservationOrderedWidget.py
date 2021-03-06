from PyQt5.QtCore import Qt, QRect, QSize,pyqtSignal
from PyQt5.QtGui import QPainter, QColor, QPen, QPainterPath
from PyQt5.QtSql import QSqlRelationalTableModel, QSqlQuery
from PyQt5.QtWidgets import (
    QCompleter,
    QWidget,
    QHBoxLayout,
    QLineEdit,
    QComboBox,
    QFormLayout,
)

from db.Connection import Connection
from guest.Guest import Guest
class LineEdit(QLineEdit):
    def __init__(self):
        super(LineEdit, self).__init__()


class ReservationOrderedWidget(QWidget):
    guest_inited = pyqtSignal(bool)
    guest_valid = False
    def __init__(self, parent=None, db=None,guest = None):
        if db is None:  # if parent widget don't pass database
            self.db = Connection().db  # init new connection
        else:
            self.db = db
        self.guest=guest
        super(ReservationOrderedWidget, self).__init__()


        self.setParent(parent)
        self.setMinimumHeight(300)
        self.setMinimumWidth(300)
        self.setMaximumHeight(400)
        self.setMaximumWidth(400)

        main_layout = QHBoxLayout()

        form_lay = QFormLayout()
        form_lay.setLabelAlignment(Qt.AlignLeft)
        #TODO: gender cmb vals from lang file
        self.gender_cmb = QComboBox()
        self.gender_cmb.addItems(['', 'Mr.', 'Mrs.'])
        #TODO: guest_type_cmb - types from lang file
        self.guest_type_cmb = QComboBox()
        self.guest_type_cmb.addItems(['', 'Guest', 'Agent', 'Company'])
        self.guest_type_cmb.setDisabled(True)

        gender_type_lay = QHBoxLayout()
        gender_type_lay.setContentsMargins(0, 0, 0, 0)
        gender_type_lay.setSpacing(0)
        gender_type_lay.addWidget(self.gender_cmb)
        gender_type_lay.addWidget(self.guest_type_cmb)

        count_pstcd_cty = QHBoxLayout()
        count_pstcd_cty.setSpacing(1)

        self.country_le = QLineEdit()
        self.post_code = QLineEdit()
        self.city_le=QLineEdit()


        count_pstcd_cty.addWidget(self.post_code)
        count_pstcd_cty.addWidget(self.city_le)


        self.first_name_le = LineEdit()
        self.last_name_le = QLineEdit()
        self.street_le = QLineEdit()
        self.phone_le = QLineEdit()
        self.mail_address_le = QLineEdit()

        self.last_stay_le = QLineEdit()
        self.last_stay_le.setDisabled(True)
        form_lay.setLabelAlignment(Qt.AlignLeft)
        form_lay.addRow('Title/guest type:', gender_type_lay)
        form_lay.addRow('Last name:', self.last_name_le)
        form_lay.addRow('First name:', self.first_name_le)
        form_lay.addRow('Street:', self.street_le)
        form_lay.addRow('Post code/City:', count_pstcd_cty)
        form_lay.addRow('Country',self.country_le)
        form_lay.addRow('Phone:', self.phone_le)
        form_lay.addRow('Email:', self.mail_address_le)
        form_lay.addRow('Last stay:', self.last_stay_le)
        main_layout.addLayout(form_lay)
        form_lay.setFieldGrowthPolicy(form_lay.ExpandingFieldsGrow)
        self.setLayout(main_layout)
        self.init_guest(self.guest)
        for obj in form_lay.findChildren(QLineEdit):
            obj.textchanged.connect(self.on_text_change)

    def on_text_change(self):
        print('change')
    def init_guest(self, guest):
        'in case of passed guest_id_signal from parent widget fuction sets text in line edits'
        if guest is None:
            pass
        else:
            self.guest = guest
            self.gender_cmb.setCurrentIndex(guest.gender+1)
            self.guest_type_cmb.setCurrentIndex(guest.type+1)
            self.first_name_le.setText(guest.first_name)
            self.last_name_le.setText(guest.last_name)
            self.phone_le.setText(guest.phone_number)
            self.mail_address_le.setText(guest.mail_address)
            self.street_le.setText(guest.address+','+guest.address2)
            self.city_le.setText(guest.city)
            self.country_le.setText(guest.country)
            self.post_code.setText(guest.zip_code)
            self.guest_valid=True
            self.guest_inited.emit(True)




    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setRenderHint(painter.Antialiasing)
        path = QPainterPath()
        rect = QRect(0, 0, self.width(), self.height())
        pen = QPen(QColor('red'), 1)
        painter.setPen(pen)
        painter.drawRect(rect)


