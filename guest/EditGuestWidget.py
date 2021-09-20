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
        self.setMinimumSize(300,600)
        tab = QTabWidget()
        tab.setMinimumWidth(200)
        main_layout.addWidget(tab)
        self.basic_info = BasicInfo()

        tab.addTab(self.basic_info, 'Basic')

        tab.addTab(QWidget(), 'Family Members')

        self.basic_info.obligatories_checked.connect(self.on_obligatories_checked)

        self.action_btn_layout = ActionButtonsLayout()

        self.action_btn_layout.new_btn.clicked.connect(self.new_btn_on_click)
        self.action_btn_layout.update_btn.clicked.connect(self.update_btn_on_click)
        main_layout.addLayout(self.action_btn_layout)
        self.setLayout(main_layout)
        self.init_guest(guest)
        # self.resize(200,400)


    def init_guest(self,guest):
        'in case of passed guest from parent widget fuction sets text in line edits'
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
            if guest.guest_id!=None:
                self.action_btn_layout.update_btn.setDisabled(False)

    def update_btn_on_click(self):
        # TODO: connection from main app
        db = Connection().db
        guest = self.gather_data()
        if guest.update_guest(db):
            self.showdialog('updated')

    def new_btn_on_click(self):
        # gather info -> prepare querry - > execute querry -> init window with guest
        #TODO: connection from main app
        db = Connection().db
        new_guest = self.gather_data()
        if new_guest.insert_guest(db):
            self.showdialog('added')
        self.init_guest(new_guest)


    def showdialog(self,str):
        #Todo: - prettyfy dialog :D
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        msg.setText(f"Guest {str}")
        msg.setWindowTitle("MessageBox demo")

        msg.setStandardButtons(QMessageBox.Ok)


        retval = msg.exec_()


    def gather_data(self):
        new_guest = Guest()
        new_guest.guest_id = None if self.basic_info.guest_id_le.text() == '' else self.basic_info.guest_id_le.text()
        new_guest.type = self.basic_info.type_cmb.currentIndex()
        new_guest.gender = self.basic_info.gender_cmb.currentIndex()
        new_guest.first_name = self.basic_info.first_name_le.text()
        new_guest.last_name = self.basic_info.last_name_le.text()
        new_guest.phone_number = self.basic_info.phone_number_le.text()
        new_guest.mail_address = self.basic_info.mail_address_le.text()

        # new_guest.address_id = None
        new_guest.address = self.basic_info.address_le.text()
        new_guest.address2 = self.basic_info.address2_le.text()
        new_guest.city = self.basic_info.city_le.text()
        new_guest.state = self.basic_info.state_le.text()
        new_guest.zip_code = self.basic_info.zip_code_le.text()
        new_guest.country = self.basic_info.country_le.text()
        new_guest.id_number = self.basic_info.id_number_le.text()
        return new_guest
    def on_obligatories_checked(self,e):
        if e:
            self.action_btn_layout.new_btn.setDisabled(False)
        else:
            self.action_btn_layout.new_btn.setDisabled(True)
if __name__ == "__main__":
    import sys
    a = Guest()
    db = Connection().db
    a.fetch_by_id(db,501)
    app = QApplication(sys.argv)
    MainWindow = editGuest(a)
    MainWindow.show()
    sys.exit(app.exec_())
