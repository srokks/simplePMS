from operator import attrgetter
from PyQt5.QtCore import pyqtSignal
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


from BasicInfo import BasicInfo
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
        self.close_btn.clicked.connect(self.on_close_click)
        self.addWidget(self.close_btn)
        self.addStretch()
    def on_close_click(self):
        self.close()


class editGuest(QWidget):
    def __init__(self, gGuest=None):
        super(editGuest, self).__init__()
        main_layout = QHBoxLayout()

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
        self.set_fake_data()
    def new_btn_on_click(self):
        # gather info -> prepare querry - > execute querry -> init window with guest

        self.gather_data()
        self.prepare_querry()
        pass
    def prepare_querry(self):
        if self.address != '' or self.address2 != '' or self.city != '' or self.state != '' or self.zip_code != '' or self.country != '':
            pass

    def set_fake_data(self):
        self.basic_info.first_name_le.setText("Jarosław")
        self.basic_info.last_name_le.setText("Sroka")
        self.basic_info.phone_number_le.setText("123-432-123")
        self.basic_info.mail_address_le.setText("sroka@sroka.pl")
        self.basic_info.id_number_le.setText("AWG123432")

        # self.basic_info.address_le.setText("Bitwy Warszawskiej")
        # self.basic_info.address2_le.setText("12/12")
        # self.basic_info.city_le.setText("Warszawa")
        # self.basic_info.state_le.setText("mazowieckie")
        # self.basic_info.zip_code_le.setText("02-366")
        # self.basic_info.country_le.setText("Polska")

    def gather_data(self):
        self.type = self.basic_info.type_cmb.currentIndex()
        self.gender = self.basic_info.gender_cmb.currentIndex()
        self.first_name = self.basic_info.first_name_le.text()
        self.last_name = self.basic_info.last_name_le.text()
        self.phone_number = self.basic_info.phone_number_le.text()
        self.mail_address = self.basic_info.mail_address_le.text()

        self.address = self.basic_info.address_le.text()
        self.address2 = self.basic_info.address2_le.text()
        self.city = self.basic_info.city_le.text()
        self.state = self.basic_info.state_le.text()
        self.zip_code = self.basic_info.zip_code_le.text()
        self.country = self.basic_info.country_le.text()
        self.id_number = self.basic_info.id_number_le.text()

    def on_obligatories_checked(self,e):
        if e:
            self.action_btn_layout.new_btn.setDisabled(False)
        else:
            self.action_btn_layout.new_btn.setDisabled(True)
if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    MainWindow = editGuest()
    MainWindow.move(0, 0)
    MainWindow.resize(200, 400)
    MainWindow.show()
    sys.exit(app.exec_())
