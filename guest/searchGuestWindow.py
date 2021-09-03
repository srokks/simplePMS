from PyQt5.QtWidgets import (
    QDialog,
    QWidget,
    QMainWindow,
    QApplication,
    QHBoxLayout,
    QVBoxLayout,
    QTabWidget,
    QLineEdit,
    QPushButton,
    QBoxLayout,
    QTableWidget,
    QTableWidgetItem,
    QComboBox,
    QAbstractItemView,
)
from Guest import Guest, Controller
from editGuestWindow import editGuest

class searchLineEdit(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setMaximumWidth(125)

class searchGuest(QWidget):



    def __init__(self):
        super().__init__()
        self.setWindowTitle("Search guest")
        self.resize(560, 450)
        self.move(10, 10)
        self.general_layout = QVBoxLayout()
        self.setLayout(self.general_layout)
        self.search_bar()
        self.guest_table()

    def basic_search_tab(self):
        searchWidget = QWidget()
        # ---
        cb_guest_type = QComboBox()
        guest_type_strings = ['Guest', 'Company', 'Agent','']
        cb_guest_type.addItems(guest_type_strings)
        cb_guest_type.setCurrentIndex(3)
        cb_guest_type.setMaximumWidth(100)
        # ---
        le_guest_id_name = searchLineEdit()
        le_guest_id_name.setObjectName('gGuestIdName')
        le_guest_id_name.setPlaceholderText('ID')

        # ---
        self.le_surname = searchLineEdit()
        self.le_surname.setObjectName('gLastName')
        self.le_surname.setPlaceholderText('Last name')
        self.le_surname.returnPressed.connect(self.search_btn_onclick)
        # ---
        self.le_name = searchLineEdit()
        self.le_name.setPlaceholderText("Name")
        self.le_name.setObjectName("gFirstName")
        self.le_name.returnPressed.connect(self.search_btn_onclick)
        # ---
        self.le_city = searchLineEdit()
        self.le_city.setPlaceholderText('City')
        self. le_city.setObjectName('gCity')
        self.le_city.returnPressed.connect(self.search_btn_onclick)
        # ---
        #TODO: number validator
        self.le_phone_number = searchLineEdit()
        self.le_phone_number.setPlaceholderText('Phone number')
        self.le_phone_number.setObjectName("gPhoneNumber")
        self.le_phone_number.setMaxLength(10)
        self.le_phone_number.setInputMask("999-999-999")
        self.le_phone_number.setCursorPosition(0)
        self.le_phone_number.returnPressed.connect(self.search_btn_onclick)
        # ---
        self.le_mail_address = searchLineEdit()
        self.le_mail_address.setPlaceholderText('Mail address')
        self.le_mail_address.setObjectName('gMailAddress')
        # self.le_mail_address.setInputMask(">AAAAA")
        self.le_mail_address.setCursorPosition(0)
        self.le_mail_address.returnPressed.connect(self.search_btn_onclick)
        # ---
        hor_lay = QVBoxLayout()
        # ---
        # ver_lay1 = QHBoxLayout()
        # ver_lay1.addWidget(cb_guest_type)
        # ver_lay1.addWidget(le_guest_id_name)
        # ver_lay1.addStretch()
        # ---
        ver_lay2 = QHBoxLayout()
        ver_lay2.addWidget(self.le_surname)
        ver_lay2.setSpacing(5)
        ver_lay2.addWidget(self.le_name)
        ver_lay2.addWidget(self.le_city)
        ver_lay2.addStretch()
        # ---
        ver_lay3 = QHBoxLayout()
        ver_lay3.addStretch()
        ver_lay3.setSpacing(5)
        ver_lay3.addWidget(self.le_phone_number)
        ver_lay3.addWidget(self.le_mail_address)
        ver_lay3.addStretch(2)
        # ---
        ver_lay4 = QVBoxLayout()
        # ---
        # hor_lay.addLayout(ver_lay1)
        hor_lay.addLayout(ver_lay2)
        hor_lay.addLayout(ver_lay3)
        hor_lay.addLayout(ver_lay4)
        searchWidget.setLayout(hor_lay)
        return searchWidget

    def search_action_layout(self):
        action_layout = QVBoxLayout()

        close_btn = QPushButton("Close")
        close_btn.clicked.connect(self.close)

        search_btn = QPushButton("Search")
        search_btn.clicked.connect(self.search_btn_onclick)

        action_layout.addWidget(search_btn)
        action_layout.addWidget(close_btn)

        return action_layout

    def search_bar(self):

        main_layout = QHBoxLayout()
        main_layout.addWidget(self.basic_search_tab())

        main_layout.addLayout(self.search_action_layout())

        self.general_layout.addLayout(main_layout)

    def grid_on_dclick(self):
        table = self.findChild(QTableWidget)
        # guest  = Controller().get_by_id(table.item(table.currentRow(),0).text())
        if table.item(table.currentRow(),0).text()=='':
            self.editWindow = editGuest()
            self.editWindow.show()
        else:
            self.editWindow = editGuest(Controller().get_by_id(table.item(table.currentRow(),0).text()))
            self.editWindow.show()
    def guest_table(self):
        main_layout = QVBoxLayout()
        cols = 6
        rows = 16
        guest_tbl = QTableWidget()
        guest_tbl.setColumnCount(cols)
        guest_tbl.setRowCount(rows)
        # guest_tbl.setColumnHidden(0,True)
        guest_tbl.setEditTriggers(guest_tbl.NoEditTriggers)
        guest_tbl.setSelectionBehavior(guest_tbl.SelectRows)
        guest_tbl.setSelectionMode(guest_tbl.SingleSelection)
        guest_tbl.doubleClicked.connect(self.grid_on_dclick)
        guest_tbl.setObjectName('tw_guest_grid')
        guest_tbl.verticalHeader().hide()
        labels = ['ID','FirstName', 'LastName', 'City', 'PhoneNumber','MailAddress']

        guest_tbl.setHorizontalHeaderLabels(labels)

        for i in range(rows):
            for j in range(cols):
                guest_tbl.setItem(i, j, QTableWidgetItem(""))

        main_layout.addWidget(guest_tbl)
        self.general_layout.addLayout(main_layout)

    def clear_guest_grid(self):
        guest_tbl = self.findChild(QTableWidget, 'tw_guest_grid')
        for i in range(guest_tbl.rowCount()):
            for j in range(guest_tbl.columnCount()):
                guest_tbl.item(i, j).setText('')
    def get_search_keyword(self):
        lista = []
        lista.append(self.le_surname.text())
        lista.append(self.le_name.text())
        lista.append(self.le_phone_number.text().replace('-',''))
        lista.append(self.le_mail_address.text())
        lista.append(self.le_city.text())

        return lista

    def search_btn_onclick(self):
        guest_tbl = self.findChild(QTableWidget, 'tw_guest_grid')
        keyword = self.get_search_keyword()
        self.guest_list = Controller().get_guest_by_names(keyword)
        self.clear_guest_grid()
        if  self.guest_list:
            for pos, el in enumerate(self.guest_list):
                guest_tbl.item(pos, 0).setText(str(el.GuestID))
                guest_tbl.item(pos, 1).setText(el.FirstName)
                guest_tbl.item(pos, 2).setText(el.LastName)
                guest_tbl.item(pos, 3).setText(el.City)
                guest_tbl.item(pos, 4).setText(el.PhoneNumber)
                guest_tbl.item(pos, 5).setText(el.MailAddress)

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    MainWindow = searchGuest()
    MainWindow.show()
    sys.exit(app.exec_())
