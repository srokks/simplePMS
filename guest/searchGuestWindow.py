import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QHeaderView
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton


from guest import Guest


class SearchGuestUi(QMainWindow):
    def __init__(self):
        """View initializer."""
        super().__init__()
        # Set some main window's properties
        self.setWindowTitle('Search guests')
        # self.setSize(800, 600)
        self.generalLayout = QVBoxLayout()
        # Set the central widget
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        self.createSearchBar()
        self.genGuestGridInfo()

    def createSearchBar(self):
        self.searchBarLayout = QHBoxLayout()

        self.name_field = QLineEdit()
        self.name_field.setFixedHeight(35)
        self.name_field.setAlignment(Qt.AlignRight)

        self.surname_field = QLineEdit()
        self.surname_field.setFixedHeight(35)
        self.surname_field.setAlignment(Qt.AlignRight)

        #Backbut
        self.backButton = QPushButton()
        self.backButton.setText('<-Back')
        self.backButton.clicked.connect(self.clearButton_on_click)

        #Search button
        self.searchButton = QPushButton()
        self.searchButton.setText('Search->')
        self.searchButton.clicked.connect(self.searchButton_on_click)


        self.searchBarLayout.addWidget(self.name_field)
        self.searchBarLayout.addWidget(self.surname_field)
        self.searchBarLayout.addWidget(self.backButton)
        self.searchBarLayout.addWidget(self.searchButton)


        self.generalLayout.addLayout(self.searchBarLayout)
    def genGuestGridInfo(self):
        #FIXME: chage cols and rows, should be as big as window
        cols =5
        rows = 15
        self.table = QTableWidget()
        self.table.setObjectName("guestview")


        self.table.setColumnCount(cols)
        self.table.setRowCount(rows)
        self.table.verticalHeader().hide()
        self.table.setHorizontalHeaderLabels(['Name', 'Surname', 'Email', 'Phone','Address'])
        keyword = self.name_field.text()
        for i in range(rows):
            for j in range(cols):
                self.table.setItem(i,j,QTableWidgetItem(""))
        self.generalLayout.addWidget(self.table)

    def clearButton_on_click(self):
        print(self.width(),self.table.width(),self.generalLayout.sizeHint())
        
    def searchButton_on_click(self):
        result = Guest().getGuestsbyName(self.name_field.text())
        self.clearGridInfo()
        for pos,el in enumerate(result):
            for j in range(5):
                self.table.item(pos,j).setText(el[j+1])


    def clearGridInfo(self):
        print("clear")
        for i in range(15):
            for j in range(5):
                self.table.item(i,j).setText("")
    # Client code
def main():
    """Main function."""
    # Create an instance of QApplication
    pycalc = QApplication(sys.argv)
    # Show the calculator's GUI
    view = SearchGuestUi()
    view.show()
    # Execute the calculator's main loop
    sys.exit(pycalc.exec_())

if __name__ == '__main__':
    main()
