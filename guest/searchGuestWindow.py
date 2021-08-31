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
from Guest import GuestCtrl, Guest

class searchLineEdit(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setMaximumWidth(125)
        self.returnPressed.connect(searchGuest.search_btn_onclick)

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

    def basic_search_tab2(self):
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
        le_surname = searchLineEdit()
        le_surname.setObjectName('gLastName')
        le_surname.setPlaceholderText('Last name')

        le_surname.returnPressed.connect(self.search_btn_onclick)
        # ---
        le_name = searchLineEdit()
        le_name.setPlaceholderText("Name")
        le_name.setObjectName("gFirstName")
        le_name.returnPressed.connect(self.search_btn_onclick)
        # ---
        le_city = searchLineEdit()
        le_city.setPlaceholderText('City')
        le_city.setObjectName('gCity')
        # ---
        #TODO: number validator
        le_phone_number = searchLineEdit()
        le_phone_number.setPlaceholderText('Phone number')
        le_phone_number.setObjectName("gPhoneNumber")
        le_phone_number.setMaxLength(10)
        le_phone_number.setInputMask("999-999-999")
        le_phone_number.setCursorPosition(0)
        # ---
        le_mail_address = searchLineEdit()
        le_mail_address.setPlaceholderText('Mail address')
        le_mail_address.setObjectName('gMailAddress')
        le_mail_address.setInputMask(">AAAAA")
        le_mail_address.setCursorPosition(0)
        # ---
        hor_lay = QVBoxLayout()
        # ---
        ver_lay1 = QHBoxLayout()
        ver_lay1.addWidget(cb_guest_type)
        ver_lay1.addWidget(le_guest_id_name)
        ver_lay1.addStretch()
        # ---
        ver_lay2 = QHBoxLayout()
        ver_lay2.addWidget(le_surname)
        ver_lay2.setSpacing(5)
        ver_lay2.addWidget(le_name)
        ver_lay2.addWidget(le_city)
        ver_lay2.addStretch()
        # ---
        ver_lay3 = QHBoxLayout()
        ver_lay3.addStretch()
        ver_lay3.setSpacing(5)
        ver_lay3.addWidget(le_phone_number)
        ver_lay3.addWidget(le_mail_address)
        ver_lay3.addStretch()
        # ---
        ver_lay4 = QVBoxLayout()
        # ---
        hor_lay.addLayout(ver_lay1)
        hor_lay.addLayout(ver_lay2)
        hor_lay.addLayout(ver_lay3)
        hor_lay.addLayout(ver_lay4)
        searchWidget.setLayout(hor_lay)
        return searchWidget

    def basic_search_tab(self):
        searchTab = QTabWidget()
        searchTab.setMaximumHeight(75)

        le_surname = QLineEdit()
        le_surname.setObjectName('gLastName')
        le_surname.setPlaceholderText("Surname")

        le_name = QLineEdit()
        le_name.setPlaceholderText("Name")
        le_name.setObjectName("gFirstName")

        le_city = QLineEdit()
        le_city.setPlaceholderText('City')
        le_city.setObjectName('gCity')

        basic_wi = QWidget()
        basic_layout = QHBoxLayout()
        basic_layout.addWidget(le_surname)
        basic_layout.addWidget(le_name)
        basic_layout.addWidget(le_city)
        basic_wi.setLayout(basic_layout)

        searchTab.addTab(basic_wi, "Basic")
        return searchTab

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
        main_layout.addWidget(self.basic_search_tab2())

        main_layout.addLayout(self.search_action_layout())

        self.general_layout.addLayout(main_layout)

    def guest_grid_on_click(self):
        print(self.findChild(QTableWidget).currentRow())

    def guest_table(self):
        main_layout = QVBoxLayout()
        cols = 5
        rows = 16
        guest_tbl = QTableWidget()
        guest_tbl.setColumnCount(cols)
        guest_tbl.setRowCount(rows)
        guest_tbl.setEditTriggers(guest_tbl.NoEditTriggers)
        guest_tbl.setSelectionBehavior(guest_tbl.SelectRows)
        guest_tbl.setSelectionMode(guest_tbl.SingleSelection)
        guest_tbl.doubleClicked.connect(self.guest_grid_on_click)
        guest_tbl.setObjectName('tw_guest_grid')
        guest_tbl.verticalHeader().hide()
        labels = ['FirstName', 'LastName', 'City', 'PhoneNumber','MailAddress']

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

    def search_btn_onclick(self):
        # guest_tbl = self.findChild(QTableWidget, 'tw_guest_grid')
        # le_surname = self.findChild(QTabWidget).findChild(QLineEdit, 'gLastName')
        # print(le_surname.text())
        # guest_list = GuestCtrl().getGuestBySurName(le_surname.text())
        # self.clear_guest_grid()
        # # labels = ['FirstName', 'LastName', 'Address', 'Address2', 'City', 'ZipCode', 'Country', 'PhoneNumber',
        # #          'MailAddress']
        # for pos, el in enumerate(guest_list):
        #     guest_tbl.item(pos, 0).setText(el.gFirstName)
        #     guest_tbl.item(pos, 1).setText(el.gLastName)
        #     guest_tbl.item(pos, 2).setText(el.gAddress)
        #     guest_tbl.item(pos, 3).setText(el.gAddress2)
        #     guest_tbl.item(pos, 4).setText(el.gCity)
        #     guest_tbl.item(pos, 5).setText(el.gZipCode)
        #     # guest_tbl.item(pos,6).setText(el.gCountry)
        #     guest_tbl.item(pos, 7).setText(el.gPhoneNumber)
        #     guest_tbl.item(pos, 8).setText(el.gMailAddress)
        print(str(self.height()),str(self.width()),sep='x')
if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    MainWindow = searchGuest()
    MainWindow.show()
    sys.exit(app.exec_())
