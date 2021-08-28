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
from Guest import GuestCtrl, Guest

#TODO: validacja wprowadzonych danych użyciem QlineEdit


class editGuest(QWidget):
    def __init__(self, gGuest=None):
        super().__init__()
        # ----
        self.legGuestID = QLineEdit()
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
        self.legIdNumberLabel = QLabel("ID number:")
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

    def getGuestFromForm(self):
        updated_guest = Guest()
        updated_guest.gGuestID = int(self.legGuestID.text())
        updated_guest.gFirstName = self.leGFirstName.text()
        updated_guest.gLastName = self.leGLastName.text()
        updated_guest.gAddress = self.leGAddress.text()
        updated_guest.gAddress2 = self.leGAddress2.text()
        updated_guest.gCity = self.leGCity.text()
        updated_guest.gState = self.leGState.text()
        updated_guest.gZipCode = self.leGZipCode.text()
        updated_guest.gCountry = self.leGCountry.text()
        updated_guest.gPhoneNumber = self.leGPhoneNumber.text()
        updated_guest.gMailAddress = self.leGMailAddress.text()
        # FIXME: gender na integer
        updated_guest.gGender = '0'
        updated_guest.gGuestType = self.guest_type_combo.currentIndex()
        updated_guest.gIdNumber = self.leGIDNumber.text()
        return updated_guest

    def updatedMessageBox(self):
        msg = QMessageBox()
        msg.setText("Information updated")
        msg.setStandardButtons(QMessageBox.Ok)
        retval = msg.exec_()

    def update_btn_on_click(self):
        if GuestCtrl().updateGuestObj(self.getGuestFromForm()):
            self.updatedMessageBox()
            print("Updated")
    def new_btn_on_click(self):
        #TODO:new_btn logic
        new_guest = self.getGuestFromForm()
        new_guest.gGuestID = None
        new_guest_id = GuestCtrl().addGuest(new_guest)

    def close_btn_on_click(self):
        self.close()
    def addActionBtn(self):
        VLayout = QVBoxLayout()

        new_bnt = QPushButton()
        new_bnt.setText('New..')
        new_bnt.clicked.connect(self.new_btn_on_click)

        change_btn = QPushButton()
        change_btn.setText('Change')
        change_btn.clicked.connect(self.update_btn_on_click)

        close_btn = QPushButton()
        close_btn.setText('Close')
        close_btn.clicked.connect(self.close_btn_on_click)
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
            self.legGuestID.setText(str(gGuest.gGuestID))
            #TODO: guest combo logic
            #Guest type - 0 - Guest ; 1 - company;2 agent
            self.guest_type_combo.setCurrentIndex(gGuest.gGuestType)

            #TODO: gender combo logic
            #Gender 0 male 1 female
            self.cmbGGender.setCurrentIndex(int(gGuest.gGender))
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
    def on_change_guestcmb(self):
        if self.guest_type_combo.currentIndex() == 0 :
            self.legIdNumberLabel.setText('ID number')
        else:
            self.legIdNumberLabel.setText('Cmp. number')

    def createForm(self):
        main_layout = QFormLayout()
        # ----
        guest_type_strings = ['Guest', 'Company', 'Agent']
        self.guest_type_combo.addItems(guest_type_strings)
        self.guest_type_combo.currentTextChanged.connect(self.on_change_guestcmb)
        # Todo:jak company or agent ukryć combo z gender
        # ----
        gender_strings = ['Mr.', 'Mrs.']
        self.cmbGGender.addItems(gender_strings)
        # TODO:add separator

        # Todo:add separator
        # ----
        self.legGuestID.setEnabled(False)
        main_layout.addRow(self.legGuestID)
        main_layout.addRow('Guest type', self.guest_type_combo)
        main_layout.addRow('Gender:',self.cmbGGender)
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
        # Todo:add separator


        main_layout.addRow(self.legIdNumberLabel, self.leGIDNumber)

        self.general_layout.addLayout(main_layout)



# if __name__ == "__main__":
#     import sys
#
#     a = GuestCtrl().getGuestByID(101)
#
#     app = QApplication(sys.argv)
#     MainWindow = editGuest(a)
#     MainWindow.show()
#     sys.exit(app.exec_())
