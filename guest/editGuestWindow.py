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

)
from Guest import GuestCtrl, Guest


class editGuest(QWidget, ):
    def __init__(self, gGuest=None):
        super().__init__()
        # ----
        self.guest_type_combo = QComboBox()
        self.cmbGGender = QComboBox()
        # ----
        self.leGFirstName = QLineEdit()
        self.leGLastName = QLineEdit()
        self.leGPhoneNumber = QLineEdit()
        self.leGMailAddress = QLineEdit()
        # ----
        self.leGAddress = QLineEdit()
        self.leGAddress2 = QLineEdit()
        self.leGZipCode = QLineEdit()
        self.leGCity = QLineEdit()
        self.leGState = QLineEdit()
        self.leGCountry = QLineEdit()
        # ----
        self.leGIDNumber = QLineEdit()
        # ---- Main window properties
        self.setWindowTitle("Edit guest")
        self.resize(200, 200)
        self.move(10, 10)
        # ----
        self.general_layout = QHBoxLayout()
        self.setLayout(self.general_layout)
        self.createForm()
        self.initGuest(gGuest)
        self.addActionBtn()

    def addActionBtn(self):
        VLayout = QVBoxLayout()

        new_bnt = QPushButton()
        new_bnt.setText('New..')

        change_btn = QPushButton()
        change_btn.setText('Change')

        close_btn = QPushButton()
        close_btn.setText('Close')

        VLayout.addWidget(new_bnt)
        VLayout.addWidget(change_btn)
        VLayout.addWidget(close_btn)
        VLayout.addStretch()
        self.general_layout.addLayout(VLayout)

    def initGuest(self, gGuest):
        if gGuest == None:
            pass
        else:
            # ----
            self.guest_type_combo = QComboBox()
            self.cmbGGender = QComboBox()
            # ----
            self.leGFirstName.setText(gGuest.gFirstName)
            self.leGLastName.setText(gGuest.gLastName)
            self.leGPhoneNumber.setText(gGuest.gPhoneNumber)
            self.leGMailAddress.setText(gGuest.gMailAddress)
            # ----
            self.leGAddress.setText(gGuest.gAddress)
            self.leGAddress2.setText(gGuest.gAddress2)
            self.leGZipCode.setText(gGuest.gZipCode)
            self.leGCity.setText(gGuest.gCity)
            self.leGState.setText(gGuest.gState)
            self.leGCountry.setText(gGuest.gCountry)
            # ----
            self.leGIDNumber.setText(gGuest.gIdNumber)

    def createForm(self):
        main_layout = QFormLayout()

        guest_type_strings = ['Guest', 'Company', 'Agent']
        self.guest_type_combo.addItems(guest_type_strings)
        # Todo:jak company or agent ukryć combo z gender

        gender_strings = ['male', 'female']
        self.cmbGGender.addItems(gender_strings)
        # TODO:add separator

        # Todo:add separator

        main_layout.addRow('Guest type', self.guest_type_combo)
        main_layout.addRow('First name:', self.leGFirstName)
        main_layout.addRow('Last name:', self.leGLastName)
        main_layout.addRow('Phone no.:', self.leGPhoneNumber)
        main_layout.addRow('Mail address:', self.leGMailAddress)
        # TODO:add separator

        main_layout.addRow('Address:', self.leGAddress)
        main_layout.addRow('Address ...:', self.leGAddress2)
        main_layout.addRow('Zip code:', self.leGZipCode)
        main_layout.addRow('City:', self.leGCity)
        main_layout.addRow('State:', self.leGState)
        main_layout.addRow('Country:', self.leGCountry)
        # Todo: oddzielic sekcje jakims separatorem
        # Todo:jak company albo agent zmienic opis dokumentu na nip

        main_layout.addRow('ID number', self.leGIDNumber)

        self.general_layout.addLayout(main_layout)


if __name__ == "__main__":
    import sys

    a = GuestCtrl().getGuestByID(12)

    app = QApplication(sys.argv)
    MainWindow = editGuest(a)
    MainWindow.show()
    sys.exit(app.exec_())
