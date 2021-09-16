from operator import attrgetter

from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import (
    QDialog,
    QWidget,
    QMainWindow,
    QApplication,
    QHBoxLayout,
    QVBoxLayout,
    QFormLayout,
    QTabWidget,
    QLineEdit,
    QPushButton,
    QBoxLayout,
    QTableWidget,
    QTableWidgetItem,
    QComboBox,
    QLabel,
    QMessageBox,

)

from PyQt5.QtCore import Qt, QRegExp


class LineEdit(QLineEdit):
    def __init__(self,obligatory=False):
        super(LineEdit, self).__init__()
        self.obligatory = obligatory
        self.setObligatory()
        self.textChanged.connect(self.setObligatory)
    def setObligatory(self):
        if self.obligatory == True:
            self.setStyleSheet('background-color:rgba(255, 238, 0,90)')
        else:
            self.setStyleSheet('background-color:rgb(255, 255, 255)')

class BasicInfo(QWidget):
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

        self.first_name_le = LineEdit(True)
        self.first_name_le.setMinimumWidth(100)
        self.last_name_le = QLineEdit()
        self.phone_number_le = QLineEdit()
        self.mail_address_le = QLineEdit()
        self.id_number_le = QLineEdit()

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

        self.type_cmb.currentIndexChanged.connect(self.type_cmb_on_change)

    def type_cmb_on_change(self, index):
        if index == 0:
            self.id_number_lbl.setText('ID number')
        elif index in [1, 2]:
            self.id_number_lbl.setText('Company ID')


class editGuest(QWidget):
    def __init__(self, gGuest=None):
        super(editGuest, self).__init__()
        main_layout = QHBoxLayout()

        tab = QTabWidget()

        main_layout.addWidget(tab)
        basic_info = BasicInfo()
        basic_info.first_name_le.text()
        tab.addTab(basic_info, 'Basic')
        tab.addTab(QWidget(), 'Family Members')

        action_btn_layout = QVBoxLayout()
        action_btn_layout.addWidget(QPushButton("New"))
        action_btn_layout.addWidget(QPushButton("Update"))
        action_btn_layout.addWidget(QPushButton("Close"))
        action_btn_layout.addStretch()

        main_layout.addLayout(action_btn_layout)
        self.setLayout(main_layout)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    MainWindow = editGuest()
    MainWindow.move(0, 0)
    MainWindow.resize(200, 400)
    MainWindow.show()
    sys.exit(app.exec_())
