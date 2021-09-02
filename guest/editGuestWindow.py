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
# from Guest import Guest,Cont
from PyQt5.QtCore import Qt, QRegExp
from Guest import Guest,Controller

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
        pass


class actionButton(QPushButton):
    def __init__(self):
        super().__init__()
        self.setMaximumWidth(200)


class editGuest(QWidget):
    def __init__(self, gGuest=None):
        super().__init__()
        # ----
        self.con = Controller()
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
        # self.leGPhoneNumber.setInputMask('+ 99 999-999-999')
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
        self.create_form()
        self.initGuest(gGuest)
        self.add_action_button()
        # ---- WIP ---
        self.mandatory_fields_list = []
        for el in self.findChildren(searchLineEdit):
            if el.mandatory:
                self.mandatory_fields_list.append(el)
        for el in self.mandatory_fields_list:
            if el.text() != '':
                pass

    def get_guest_from_form(self):
        updated_guest = Guest()
        # ---
        updated_guest.GuestType = self.guest_type_combo.currentIndex()
        updated_guest.Gender = self.cmbGGender.currentIndex()
        updated_guest.GuestID = int(self.legGuestID.text()) if self.legGuestID.text() != '' else None
        updated_guest.FirstName = self.leGFirstName.text()
        updated_guest.LastName = self.leGLastName.text()
        updated_guest.PhoneNumber = self.leGPhoneNumber.text()
        updated_guest.MailAddress = self.leGMailAddress.text()
        # --- Addres get
        updated_guest.Address = self.leGAddress.text()
        updated_guest.Address2 = self.leGAddress2.text()
        updated_guest.City = self.leGCity.text()
        updated_guest.State = self.leGState.text()
        updated_guest.ZipCode = self.leGZipCode.text()
        updated_guest.Country = self.leGCountry.text()
        updated_guest.gGender = self.guest_type_combo.currentIndex()
        updated_guest.IdNumber = self.leGIDNumber.text()
        return updated_guest

    def on_text_change(self):
        print("check flags activateds")

    def updatedMessageBox(self):
        msg = QMessageBox()
        msg.setText("Information updated")
        msg.setStandardButtons(QMessageBox.Ok)
        retval = msg.exec_()
    def created_msg_box(self,guest):
        msg = QMessageBox()
        msg.setText(f"Created entry for {guest.FirstName},{guest.LastName}")
        msg.setStandardButtons(QMessageBox.Ok)
        retval = msg.exec_()
    def on_click_update_btn(self):
        #TODO: implement for new db
        new_guest = self.get_guest_from_form()
        if self.con.update_guest(new_guest):
            self.updatedMessageBox()
        else:
            print('problem')
    def on_click_new_btn(self):
        new_guest = self.get_guest_from_form()
        self.con.add(new_guest)
        self.initGuest(new_guest)
        self.created_msg_box(new_guest)
    def close_btn_on_click(self):
        self.close()

    def add_action_button(self):
        VLayout = QVBoxLayout()
        # ----
        new_bnt = actionButton()
        new_bnt.setText('New')
        new_bnt.clicked.connect(self.on_click_new_btn)
        # ----
        change_btn = actionButton()
        change_btn.setText('Modify')
        change_btn.clicked.connect(self.on_click_update_btn)
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
            self.legGuestID.setText(str(gGuest.GuestID))
            # Guest type - 0 - Guest ; 1 - company;2 agent
            self.guest_type_combo.setCurrentIndex(gGuest.GuestType)
            # Todo:jak company or agent ukryć combo z gender
            # TODO: gender combo logic
            # Gender 0 male 1 female
            self.cmbGGender.setCurrentIndex(int(gGuest.Gender))
            # ----
            self.leGFirstName.setText(gGuest.FirstName)
            self.leGLastName.setText(gGuest.LastName)
            self.leGPhoneNumber.setText(gGuest.PhoneNumber)
            self.leGMailAddress.setText(gGuest.MailAddress)
            # ----
            self.leGAddress.setText(gGuest.Address)
            self.leGAddress2.setText(gGuest.Address2)
            self.leGZipCode.setText(gGuest.ZipCode)
            self.leGCity.setText(gGuest.City)
            self.leGState.setText(gGuest.State)
            self.leGCountry.setText(gGuest.Country)
            # ----
            self.leGIDNumber.setText(gGuest.IdNumber)

    def guest_cmb_on_change(self):
        if self.guest_type_combo.currentIndex() == 0:
            self.legIdNumberLabel.setText('ID number')
            self.cmbGGender.show()
        else:
            self.legIdNumberLabel.setText('Cmp. number')
            self.cmbGGender.setVisible(0)

    def create_form(self):
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

    con = Controller()
    a = con.get_by_id(227)
    app = QApplication(sys.argv)
    MainWindow = editGuest(a)
    MainWindow.show()
    sys.exit(app.exec_())
