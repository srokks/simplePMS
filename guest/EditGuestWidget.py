from operator import attrgetter
from PyQt5.QtCore import pyqtSignal,QDir
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtSql import QSqlQuery,QSqlDatabase
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
from db.Connection import Connection

from guest.Guest import Guest


from guest.BasicInfo import BasicInfo
class ActionButtonsLayout(QVBoxLayout):
    close_btn_signal = pyqtSignal()
    def __init__(self):

        super(ActionButtonsLayout, self).__init__()

        self.new_btn = QPushButton("New")
        self.new_btn.setDisabled(True)

        self.addWidget(self.new_btn)
        self.update_btn = QPushButton("Update")
        self.update_btn.setDisabled(True)
        self.addWidget(self.update_btn)
        self.close_btn = QPushButton("Close")
        self.close_btn.clicked.connect(self.close_btn_on_click)
        self.addWidget(self.close_btn)
        self.addStretch()

    def close_btn_on_click(self):
        if self.parent().parent().parent():
            self.parent().parent().parent().close()
        else:
            self.parent().parent().close()

class editGuest(QWidget):
    def __init__(self, guest=None):
        super().__init__()
        main_layout = QHBoxLayout()
        self.setMinimumSize(350,600)
        tab = QTabWidget()

        main_layout.addWidget(tab)
        self.basic_info = BasicInfo()
        self.basic_info.first_name_le.text()
        tab.addTab(self.basic_info, 'Basic')
        tab.addTab(QWidget(), 'Family Members')
        self.basic_info.obligatories_checked.connect(self.on_obligatories_checked)
        self.action_btn_layout = ActionButtonsLayout()

        self.action_btn_layout.new_btn.clicked.connect(self.new_btn_on_click)
        main_layout.addLayout(self.action_btn_layout)
        self.setLayout(main_layout)
        self.init_guest(guest)
        # self.resize(200,400)


    def init_guest(self,guest):
        if guest==None:
            pass
        else:
            self.basic_info.guest_id_le.setText(str(guest.guest_id))
            self.basic_info.first_name_le.setText(guest.first_name)
            self.basic_info.last_name_le.setText(guest.last_name)
            self.basic_info.phone_number_le.setText(guest.phone_number)
            self.basic_info.mail_address_le.setText(guest.mail_address)
            self.basic_info.address_le.setText(guest.address)
            self.basic_info.address2_le.setText(guest.address2)
            self.basic_info.city_le.setText(guest.city)
            self.basic_info.state_le.setText(guest.state)
            self.basic_info.zip_code_le.setText(guest.zip_code)
            self.basic_info.country_le.setText(guest.country)
            self.basic_info.id_number_le.setText(guest.id_number)

    def new_btn_on_click(self):
        # gather info -> prepare querry - > execute querry -> init window with guest
        self.db = Connection().db
        self.gather_data()
        self.prepare_querry()
        pass
    def add_guest(self):
        querry = QSqlQuery(db=self.db)
        querry.prepare(
            "INSERT INTO "
            "tblGuest(gGuestType,gGender,gFirstName,gLastName,gPhoneNumber,gMailAddress,gIDNumber,gAddressID) "
            "VALUES (:guest_type,:gender,:first_name,:last_name,:phone_number,:mail_address,:id_number,:address_id)"

        )
        querry.bindValue(":guest_type", self.new_guest.type)
        querry.bindValue(':gender', self.new_guest.gender)
        querry.bindValue(':first_name', self.new_guest.first_name)
        querry.bindValue(':last_name', self.new_guest.last_name)
        querry.bindValue(':phone_number', self.new_guest.phone_number)
        querry.bindValue(':mail_address', self.new_guest.mail_address)
        querry.bindValue(':id_number', self.new_guest.id_number)
        querry.bindValue(':address_id', self.new_guest.address_id)

        if querry.exec_():
            print("addres added")
            self.new_guest.address_id = querry.lastInsertId()
            return True
        else:
            print('error ', querry.lastError().text())
            return False, querry.lastError().text()
    def add_address(self):
        querry = QSqlQuery(db=self.db)
        querry.prepare(
            "INSERT INTO tblAddresses(aAddress,aAddress2,aCity,aState,aZipCode,aCountry) "
            "VALUES (:address,:address2,:city,:state,:zip_code,:country)"

        )
        querry.bindValue(":address",self.new_guest.address)
        querry.bindValue(":address2",self.new_guest.address2)
        querry.bindValue(":city",self.new_guest.city)
        querry.bindValue(":state",self.new_guest.state)
        querry.bindValue(":zip_code",self.new_guest.zip_code)
        querry.bindValue(":country",self.new_guest.country)
        if querry.exec_():
            print("addres added")
            self.new_guest.address_id = querry.lastInsertId()
            return True
        else:
            print('error ',querry.lastError().text())
            return False,querry.lastError().text()


    def prepare_querry(self):
        if self.new_guest.address != '' or self.new_guest.address2 != '' or self.new_guest.city != '' or self.new_guest.state != '' or self.new_guest.zip_code != '' or self.new_guest.country != '':
            if self.add_address() or self.add_guest():
                print('guest + address added')
        else:
            if self.add_guest():
                print('guest added')

    def set_fake_data(self):
        self.basic_info.first_name_le.setText("Jarosław")
        self.basic_info.last_name_le.setText("Sroka")
        self.basic_info.phone_number_le.setText("123-432-123")
        self.basic_info.mail_address_le.setText("sroka@sroka.pl")
        self.basic_info.id_number_le.setText("AWG123432")

        self.basic_info.address_le.setText("Bitwy Warszawskiej")
        self.basic_info.address2_le.setText("12/12")
        self.basic_info.city_le.setText("Warszawa")
        self.basic_info.state_le.setText("mazowieckie")
        self.basic_info.zip_code_le.setText("02-366")
        self.basic_info.country_le.setText("Polska")

    def gather_data(self):
        self.new_guest = Guest()
        self.new_guest.type = self.basic_info.type_cmb.currentIndex()
        self.new_guest.gender = self.basic_info.gender_cmb.currentIndex()
        self.new_guest.first_name = self.basic_info.first_name_le.text()
        self.new_guest.last_name = self.basic_info.last_name_le.text()
        self.new_guest.phone_number = self.basic_info.phone_number_le.text()
        self.new_guest.mail_address = self.basic_info.mail_address_le.text()
        #TODO:address logic
        self.new_guest.address_id = None
        self.new_guest.address = self.basic_info.address_le.text()
        self.new_guest.address2 = self.basic_info.address2_le.text()
        self.new_guest.city = self.basic_info.city_le.text()
        self.new_guest.state = self.basic_info.state_le.text()
        self.new_guest.zip_code = self.basic_info.zip_code_le.text()
        self.new_guest.country = self.basic_info.country_le.text()
        self.new_guest.id_number = self.basic_info.id_number_le.text()

    def on_obligatories_checked(self,e):
        if e:
            self.action_btn_layout.new_btn.setDisabled(False)
        else:
            self.action_btn_layout.new_btn.setDisabled(True)
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = editGuest()
    MainWindow.show()
    sys.exit(app.exec_())
