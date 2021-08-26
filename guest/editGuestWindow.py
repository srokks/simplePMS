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
from Guest import GuestCtrl,Guest

class editGuest(QWidget,):
    def __init__(self,gGuest):
        super().__init__()
        self.setWindowTitle("Search guest")
        self.resize(200, 200)
        self.move(10, 10)
        self.general_layout = QVBoxLayout()
        self.setLayout(self.general_layout)
        self.createForm()

    def createForm(self):
        main_layout = QFormLayout()

        guest_type_combo = QComboBox()
        guest_type_strings = ['Guest','Company','Agent']
        guest_type_combo.addItems(guest_type_strings)
        #Todo: oddzielic sekcje jakims separatorem
        leGFirstName = QLineEdit()

        leGLastName = QLineEdit()

        leGPhoneNumber = QLineEdit()

        leGMailAddress = QLineEdit()



        main_layout.addRow('Guest type', guest_type_combo)
        main_layout.addRow('First name:', leGFirstName)
        main_layout.addRow('Last name:', leGLastName)
        main_layout.addRow('Phone no.:',leGPhoneNumber)
        main_layout.addRow('Mail address:',leGMailAddress)
        #Todo: oddzielic sekcje jakims separatorem
        leGAddress = QLineEdit()
        leGAddress2 = QLineEdit()
        leGZipCode = QLineEdit()
        leGCity = QLineEdit()
        leGState = QLineEdit()
        leGCountry = QLineEdit()
        legPhoneNumber = QLineEdit()



        main_layout.addRow('Address:', leGAddress)
        main_layout.addRow('Address ...:', leGAddress2)
        main_layout.addRow('Zip code:', leGZipCode)
        main_layout.addRow('City:', leGCity)
        main_layout.addRow('State:', leGState)
        main_layout.addRow('Country:', leGCountry)




        self.general_layout.addLayout(main_layout)
'''
        leGFirstName
        leGLastName
        leGPhoneNumber
        leGMailAddress
        
        #Adress section
        leGAddress
        leGAddress2
        leGZipCode
        leGCity
        leGState
        leGCountry
        legPhoneNumber
        
'''






if __name__ == "__main__":
    import sys
    a = GuestCtrl().getGuestByID(12)

    app = QApplication(sys.argv)
    MainWindow = editGuest(a)
    MainWindow.show()
    sys.exit(app.exec_())