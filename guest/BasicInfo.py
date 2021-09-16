from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QFormLayout,
    QLineEdit,
    QComboBox,
    QLabel,
)

from LineEdit import LineEdit


class BasicInfo(QWidget):
    obligatories_checked = pyqtSignal(bool)

    def __init__(self):
        super(BasicInfo, self).__init__()

        basic_info_lay = QFormLayout()
        basic_info_lay.setContentsMargins(10, 10, 10, 10)

        self.guest_id = QLineEdit()
        self.guest_id.setMaximumWidth(50)
        self.guest_id.setDisabled(True)

        self.type_cmb = QComboBox()

        self.type_cmb.setMaximumWidth(100)
        self.type_cmb.addItems(['Guest', 'Company', 'Agent'])

        self.gender_cmb = QComboBox()
        self.gender_cmb.addItems(['Mr.', 'Mrs.'])

        id_type_lay = QHBoxLayout()
        id_type_lay.setContentsMargins(0, 0, 0, 0)
        id_type_lay.addWidget(self.guest_id)
        id_type_lay.addStretch()
        id_type_lay.addWidget(self.type_cmb)

        self.first_name_le = LineEdit()
        self.last_name_le = LineEdit()
        self.phone_number_le = LineEdit()
        self.mail_address_le = LineEdit()
        'group of obligatory line edits, last two checked as or'
        self.obligatories_list = [self.first_name_le, self.last_name_le, self.phone_number_le, self.mail_address_le]

        self.id_number_le = LineEdit()

        self.address_le = QLineEdit()
        self.address2_le = QLineEdit()
        self.city_le = QLineEdit()
        self.state_le = QLineEdit()
        self.zip_code_le = QLineEdit()
        self.country_le = QLineEdit()

        self.id_number_lbl = QLabel("ID number:")
        basic_info_lay.addRow(id_type_lay)
        basic_info_lay.addRow("Gender:", self.gender_cmb)
        basic_info_lay.addRow("First Name:", self.first_name_le)
        basic_info_lay.addRow("Last Name:", self.last_name_le)
        basic_info_lay.addRow("Phone number:", self.phone_number_le)
        basic_info_lay.addRow("Mail address:", self.mail_address_le)
        basic_info_lay.addRow("Address:", self.address_le)
        basic_info_lay.addRow("Address 2:", self.address2_le)
        basic_info_lay.addRow("City:", self.city_le)
        basic_info_lay.addRow("State:", self.state_le)
        basic_info_lay.addRow("Zip code:", self.zip_code_le)
        basic_info_lay.addRow("Country:", self.country_le)
        basic_info_lay.addRow(self.id_number_lbl, self.id_number_le)
        self.setLayout(basic_info_lay)
        self.set_obligatories(self.obligatories_list)
        self.type_cmb.currentIndexChanged.connect(self.type_cmb_on_change)

    def set_obligatories(self, list):
        for el in list:
            el.setObligatory(True)
            el.textChanged.connect(self.check_obligatories)

    def type_cmb_on_change(self, index):
        """Change label on id_number_lbl according to type of guest"""
        if index == 0:
            '''sets labels for guest '''
            self.id_number_lbl.setText('ID number')
            self.obligatories_list.pop(0)
            self.id_number_le.setObligatory(False)
        elif index in [1, 2]:
            '''sets labels for company '''
            # TODO: add address to obligatories
            self.id_number_lbl.setText('Company ID')
            self.obligatories_list.insert(0, self.id_number_le)
            self.set_obligatories(self.obligatories_list)

    def check_obligatories(self, e):
        """Checks if all items (LineEdits) witch are in obligatory_list are with text
        Except two last (phone no and mail) them are checked """
        flag = False
        for el in self.obligatories_list[:-2]:
            if el.text() != '':
                flag = True
            else:
                flag = False
                break
        if flag:
            if self.obligatories_list[-1].text() == '' and self.obligatories_list[-2].text() == '':
                flag = False
        if flag:
            self.obligatories_checked.emit(True)
        else:
            self.obligatories_checked.emit(False)
