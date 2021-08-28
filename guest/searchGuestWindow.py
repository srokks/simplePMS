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
)
from Guest import GuestCtrl,Guest

class searchGuest(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Search guest")
        self.resize(800, 600)
        self.move(10, 10)
        self.general_layout = QVBoxLayout()
        self.setLayout(self.general_layout)
        self.searchBar()
        self.GuestTable()

    def searchBar(self):

        main_layout = QHBoxLayout()

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

        main_layout.addWidget(searchTab)
        acion_layout = QVBoxLayout()

        close_btn = QPushButton("Close")
        close_btn.clicked.connect(self.close)

        search_btn = QPushButton("Search")
        search_btn.clicked.connect(self.search_btn_onclick)

        acion_layout.addWidget(search_btn)
        acion_layout.addWidget(close_btn)
        # acion_layout.addStretch()
        main_layout.addLayout(acion_layout)

        self.general_layout.addLayout(main_layout)

    def GuestTable(self):
        main_layout = QVBoxLayout()
        cols = 9
        rows = 16
        guest_tbl = QTableWidget()
        guest_tbl.setColumnCount(cols)
        guest_tbl.setRowCount(rows)
        guest_tbl.setObjectName('tw_guest_grid')
        guest_tbl.verticalHeader().hide()

        labels = ['FirstName', 'LastName', 'Address', 'Address2', 'City', 'ZipCode', 'Country', 'PhoneNumber',
                  'MailAddress']

        guest_tbl.setHorizontalHeaderLabels(labels)

        for i in range(rows):
            for j in range(cols):
                guest_tbl.setItem(i, j, QTableWidgetItem(""))


        main_layout.addWidget(guest_tbl)
        self.general_layout.addLayout(main_layout)
    def clearGuestGrid(self):
        guest_tbl = self.findChild(QTableWidget,'tw_guest_grid')
        for i in range(guest_tbl.rowCount()):
            for j in range(guest_tbl.columnCount()):
               guest_tbl.item(i,j).setText('')

    def search_btn_onclick(self):
        guest_tbl = self.findChild(QTableWidget,'tw_guest_grid')
        le_surname= self.findChild(QTabWidget).findChild(QLineEdit,'gLastName')
        print(le_surname.text())
        guest_list = GuestCtrl().getGuestBySurName(le_surname.text())
        a = [x for x in range(9)]
        self.clearGuestGrid()
        #labels = ['FirstName', 'LastName', 'Address', 'Address2', 'City', 'ZipCode', 'Country', 'PhoneNumber',
        #          'MailAddress']
        for pos,el in enumerate(guest_list):
            guest_tbl.item(pos,0).setText(el.gFirstName)
            guest_tbl.item(pos,1).setText(el.gLastName)
            guest_tbl.item(pos,2).setText(el.gAddress)
            guest_tbl.item(pos,3).setText(el.gAddress2)
            guest_tbl.item(pos,4).setText(el.gCity)
            guest_tbl.item(pos,5).setText(el.gZipCode)
            # guest_tbl.item(pos,6).setText(el.gCountry)
            guest_tbl.item(pos,7).setText(el.gPhoneNumber)
            guest_tbl.item(pos,8).setText(el.gMailAddress)
        # for i in range(guest_tbl.rowCount()):
        #     for j in range(guest_tbl.columnCount()):
        #        guest_tbl.item(i,j).setText('a')
if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    MainWindow = searchGuest()
    MainWindow.show()
    sys.exit(app.exec_())
