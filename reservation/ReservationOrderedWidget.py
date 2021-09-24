from PyQt5.QtCore import Qt, QRect, QSize
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


class ReservationOrderedWidget(QWidget):
    is_completer = False

    def __init__(self, parent=None, db=None):
        if db == None:
            self.db = Connection().db
        else:
            self.db = db
        super(ReservationOrderedWidget, self).__init__()
        self.setParent(parent)
        main_layout = QHBoxLayout()

        form_lay = QFormLayout()
        form_lay.setLabelAlignment(Qt.AlignLeft)

        self.gender_cmb = QComboBox()
        self.gender_cmb.addItems(['', 'Mr.', 'Mrs.'])
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
        count_pstcd_cty.addWidget(QLineEdit())
        count_pstcd_cty.addWidget(QLineEdit())
        count_pstcd_cty.addWidget(QLineEdit())

        self.last_name_le = QLineEdit()
        self.last_name_le.textEdited.connect(self.on_edited)

        self.completer = QCompleter([])
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.completer.activated.connect(self.on_activated)
        self.last_name_le.setCompleter(self.completer)
        # self.first_name_le.setMinimumWidth(self.width())
        form_lay.setLabelAlignment(Qt.AlignLeft)
        form_lay.addRow('Title/guest type:', gender_type_lay)
        form_lay.addRow('Last name:', self.last_name_le)
        form_lay.addRow('First name:', QLineEdit())
        form_lay.addRow('Street:', QLineEdit())
        form_lay.addRow('Country/Post code/City:', count_pstcd_cty)
        form_lay.addRow('Phone:', QLineEdit())
        form_lay.addRow('Email:', QLineEdit())
        form_lay.addRow('Last stay:', QLineEdit())
        main_layout.addLayout(form_lay)
        form_lay.setFieldGrowthPolicy(form_lay.ExpandingFieldsGrow)
        self.set_model()
        self.setLayout(main_layout)

    def set_model(self):
        self.model = QSqlRelationalTableModel()

        self.query = QSqlQuery(db=self.db)
        self.query.prepare(
            "SELECT gGuestID,gFirstName,gLastName ,aCity,gPhoneNumber,gMailAddress FROM tblGuest "
            "INNER JOIN tblAddresses ON tblGuest.gAddressID = tblAddresses.aAddressID "
            "WHERE "
            "gLastName LIKE '%' || :last_name || '%' AND "
            "gFirstName LIKE '%' || :first_name || '%' AND "
            "aCity LIKE '%' || :city || '%' "
            "ORDER BY gLastName ASC"
        )

    def update_querry(self):
        last_name = self.last_name_le.text()
        first_name = ''
        city = ''
        self.query.bindValue(':last_name', last_name)
        self.query.bindValue(':first_name', first_name)
        self.query.bindValue(':city', city)
        self.query.exec_()

        self.model.setQuery(self.query)

    def on_activated(self, e):
        print("activated", e)

    def update_completer(self):
        pass

    def on_edited(self, str):
        pass

    def on_text_change(self, str):
        # if len(str)>2 and not(self.is_completer):
        #     self.set_completer()
        #     print('might set it')
        pass

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setRenderHint(painter.Antialiasing)
        path = QPainterPath()
        rect = QRect(0, 0, self.width(), self.height())
        pen = QPen(QColor('red'), 1)
        painter.setPen(pen)
        painter.drawRect(rect)

    def sizeHint(self):
        return QSize(250, 600)
