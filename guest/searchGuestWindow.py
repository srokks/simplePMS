from PyQt5.QtSql import QSqlDatabase,QSqlTableModel,QSqlRelationalTableModel,QSqlQueryModel,QSqlQuery
from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import (
    QDialog,
    QWidget,
    QMainWindow,
    QApplication,
QTableView,
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
    QFormLayout,
    QLabel,
    QFrame, QDataWidgetMapper,
)



from guest.editGuestWindow import editGuest
from db.Connection import Connection
class QHBoxLayout(QHBoxLayout):
    def __init__(self):
        super(QHBoxLayout, self).__init__()
        self.setSpacing(1)

class SearchGuest(QWidget):

    def __init__(self):
        super(SearchGuest, self).__init__()
        self.db = Connection().db
        main_layout = QVBoxLayout()
        search_lines_layout  = QHBoxLayout()
        self.last_name_search = QLineEdit()
        self.last_name_search.textChanged.connect(self.update_querry)
        self.first_name_search = QLineEdit()
        self.first_name_search.textChanged.connect(self.update_querry)
        self.city_search = QLineEdit()
        self.city_search.textChanged.connect(self.update_querry)
        search_lines_layout.addWidget(self.last_name_search)
        search_lines_layout.addWidget(self.first_name_search)
        search_lines_layout.addWidget(self.city_search)

        search_action_layout = QHBoxLayout()

        self.search_btn = QPushButton("Search")
        self.search_btn.clicked.connect(self.search_on_click)
        self.choose_btn = QPushButton("Choose")
        self.close_btn = QPushButton("Close")

        search_action_layout.addWidget(self.search_btn)
        search_action_layout.addWidget(self.choose_btn)
        search_action_layout.addWidget(self.close_btn)
        search_layout = QHBoxLayout()
        search_layout.addLayout(search_lines_layout)
        # search_layout.addLayout(search_action_layout)

        self.guest_table = QTableView()
        self.guest_table.setEditTriggers(self.guest_table.NoEditTriggers)
        self.guest_table.setSelectionBehavior(self.guest_table.SelectRows)
        self.guest_table.doubleClicked.connect(self.table_on_dclick)
        self.guest_table.verticalHeader().hide()
        self.model = QSqlQueryModel()
        self.guest_table.setModel(self.model)

        self.query = QSqlQuery(db=self.db)
        self.query.prepare(
            "SELECT gGuestID,gFirstName,gLastName ,aCity,gPhoneNumber,gMailAddress FROM tblGuest "
            "INNER JOIN tblAddresses ON tblGuest.gAddressID = tblAddresses.aAddressID "
            "WHERE "
            "gLastName LIKE '%' || :last_name || '%' AND "
            "gFirstName LIKE '%' || :first_name || '%' AND "
            "aCity LIKE '%' || :city || '%'"


        )
        self.update_querry()
        main_layout.addLayout(search_layout)
        main_layout.addWidget(self.guest_table)
        self.setLayout(main_layout)

    def table_on_dclick(self,e):
        dialog = editGuest(self)

        dialog.show()
        print(self.model.index(e.row(),0).data())


    def update_querry(self):
        last_name = self.last_name_search.text()
        first_name = self.first_name_search.text()
        city = self.city_search.text()
        self.query.bindValue(':last_name',last_name)
        self.query.bindValue(':first_name',first_name)
        self.query.bindValue(':city',city)

        self.query.exec_()
        self.model.setQuery(self.query)
    def search_on_click(self,e):
        # print(self.query.)
        self.update_querry()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    win = SearchGuest()
    win.move(0,0)
    win.resize(600,400)
    win.show()
    sys.exit(app.exec_())
