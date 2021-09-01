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
from Guest import GuestCtrl, Guest
from PyQt5.QtCore import Qt, QRegExp


# TODO: validacja wprowadzonych danych użyciem QlineEdit
class searchLineEdit(QLineEdit):
    def __init__(self):
        super().__init__()
        # self.setMinimumWidth(100)
        # self.setMinimumWidth(20)
        self.mandatory = False

    def setMandatory(self):
        self.mandatory = True
        self.setStyleSheet("background-color: rgb(255,230,100)")
        self.textChanged.connect(self.on_text_change)

    def on_text_change(self):
        print(self.width())


class actionButton(QPushButton):
    def __init__(self):
        super().__init__()
        self.setMaximumWidth(100)


class editGuest(QWidget):
    def __init__(self, gGuest=None):
        super().__init__()
        # ----
        self.legGuestID = QLineEdit()
        self.legGuestID.setFixedWidth(50)
        self.guest_type_combo = QComboBox()
        self.cmbGGender = QComboBox()
        # ----
        self.leGFirstName = searchLineEdit()
        self.leGFirstName.setMandatory()
        # ---
        self.leGLastName = searchLineEdit()
        self.leGLastName.setMandatory()
        # ---
        self.leGPhoneNumber = searchLineEdit()
        self.leGPhoneNumber.setInputMask('+ 99 999-999-999')
        self.leGPhoneNumber.setCursorPosition(0)
        # ---
        self.leGMailAddress = searchLineEdit()
        # ----
        self.leGAddress = searchLineEdit()
        self.leGAddress2 = searchLineEdit()
        self.leGZipCode = searchLineEdit()
        self.leGCity = searchLineEdit()
        self.leGState = searchLineEdit()
        self.leGCountry = searchLineEdit()
        # ----
        self.legIdNumberLabel = QLabel("ID number:")
        self.leGIDNumber = QLineEdit()
        # ---- Main window properties
        self.setWindowTitle("Edit guest")
        self.resize(200, 200)
        # self.setMaximumWidth(500)
        self.move(50, 100)
        # self.setMaximumWidth(300)
        # ----
        self.general_layout = QHBoxLayout()
        self.setLayout(self.general_layout)
        self.createForm()
        self.initGuest(gGuest)
        self.addActionBtn()
        # ---- WIP ---
        self.mandatory_fields_list = []
        for el in self.findChildren(searchLineEdit):
            if el.mandatory:
                self.mandatory_fields_list.append(el)
        for el in self.mandatory_fields_list:
            if el.text() != '':
                print(el.text())

    def getGuestFromForm(self):
        updated_guest = Guest()
        updated_guest.gGuestID = int(self.legGuestID.text()) if self.legGuestID.text() != '' else None
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

    def on_text_change(self):
        print("check flags activateds")

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
        new_guest = self.getGuestFromForm()
        new_guest.gGuestID = None
        new_guest.gGuestID = GuestCtrl().addGuest(new_guest)
        self.initGuest(new_guest)

    def close_btn_on_click(self):
        self.close()

    def addActionBtn(self):
        VLayout = QVBoxLayout()
        # ----
        new_bnt = actionButton()
        new_bnt.setText('New')
        new_bnt.clicked.connect(self.new_btn_on_click)
        # ----
        change_btn = actionButton()
        change_btn.setText('Modify')
        change_btn.clicked.connect(self.update_btn_on_click)
        # ----
        # TODO: delete guest event
        delete_btn = actionButton()
        delete_btn.setText('Delete')
        # ----
        close_btn = actionButton()
        close_btn.setText('Exit')
        close_btn.clicked.connect(self.close_btn_on_click)
        # ----
        VLayout.addWidget(new_bnt)
        VLayout.addWidget(change_btn)
        VLayout.addWidget(delete_btn)
        VLayout.addWidget(close_btn)
        VLayout.addStretch()
        self.general_layout.addLayout(VLayout)

    def initGuest(self, gGuest):
        if gGuest == None:
            pass
        else:
            # ----
            self.legGuestID.setText(str(gGuest.gGuestID))
            # Guest type - 0 - Guest ; 1 - company;2 agent
            self.guest_type_combo.setCurrentIndex(gGuest.gGuestType)
            # Todo:jak company or agent ukryć combo z gender
            # TODO: gender combo logic
            # Gender 0 male 1 female
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

    def guest_cmb_on_change(self):
        if self.guest_type_combo.currentIndex() == 0:
            self.legIdNumberLabel.setText('ID number')
            self.cmbGGender.show()
        else:
            self.legIdNumberLabel.setText('Cmp. number')
            self.cmbGGender.setVisible(0)

    def createForm(self):
        form_layout = QFormLayout()
        tab_widget = QTabWidget()
        tab_widget.setMaximumWidth(350)
        form_layout.setContentsMargins(5, 5, -5, 5)
        # ----
        guest_type_strings = ['Guest', 'Company', 'Agent']
        self.guest_type_combo.addItems(guest_type_strings)
        self.guest_type_combo.currentTextChanged.connect(self.guest_cmb_on_change)

        # ----
        gender_strings = ['Mr.', 'Mrs.']
        self.cmbGGender.addItems(gender_strings)

        # Todo:add separator
        # ----
        #TODO: wyciąnąć guest_type koło leGuestID, zmienić logikę
        self.legGuestID.setEnabled(False)
        form_layout.setLabelAlignment(Qt.AlignLeft)
        form_layout.setFormAlignment(Qt.AlignRight)
        hv = QHBoxLayout()
        hv.addWidget(self.legGuestID)
        hv.addWidget(QLabel('Guest type:'))
        hv.addWidget(self.guest_type_combo)
        form_layout.addRow(hv)

        form_layout.addRow('Guest type', self.cmbGGender)
        form_layout.addRow('First name:', self.leGFirstName)
        form_layout.addRow('Last name:', self.leGLastName)
        form_layout.addRow('Phone no.:', self.leGPhoneNumber)
        form_layout.addRow('Mail address:', self.leGMailAddress)
        # TODO:add separator

        form_layout.addRow('Address:', self.leGAddress)
        form_layout.addRow('Address ...:', self.leGAddress2)
        form_layout.addRow('Zip code:', self.leGZipCode)
        form_layout.addRow('City:', self.leGCity)
        form_layout.addRow('State:', self.leGState)
        form_layout.addRow('Country:', self.leGCountry)
        # Todo:add separator

        form_layout.addRow(self.legIdNumberLabel, self.leGIDNumber)
        masted_data_widget = QWidget()
        masted_data_widget.setLayout(form_layout)
        family_members = QWidget()
        family_members2 = QWidget()
        tab_widget.addTab(masted_data_widget, 'Master data')
        tab_widget.addTab(family_members, 'Family Members')
        self.general_layout.addWidget(tab_widget)

    def check_obligatories(self):
        a = self.findChildren(searchLineEdit)
        print(a)


if __name__ == "__main__":
    import sys

    # a = GuestCtrl().getGuestByID(101)

    app = QApplication(sys.argv)
    MainWindow = editGuest()
    MainWindow.show()
    sys.exit(app.exec_())
