from PyQt5.QtSql import QSqlDatabase,QSqlTableModel,QSqlRelationalTableModel,QSqlQueryModel,QSqlQuery
from PyQt5.QtCore import pyqtSignal
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


from guest.Guest import Guest
from guest.EditGuestWidget import editGuest
from db.Connection import Connection
class QHBoxLayout(QHBoxLayout):
    def __init__(self):
        super(QHBoxLayout, self).__init__()
        self.setSpacing(1)

class SearchLineLayout(QHBoxLayout):
    update_querry = pyqtSignal()
    def __init__(self):

        super(SearchLineLayout, self).__init__()

        self.last_name_search = QLineEdit()
        self.last_name_search.setPlaceholderText('Last name')
        self.last_name_search.textChanged.connect(self.update_querry.emit)

        self.first_name_search = QLineEdit()
        self.first_name_search.setPlaceholderText('First name')
        self.first_name_search.textChanged.connect(self.update_querry.emit)

        self.city_search = QLineEdit()
        self.city_search.setPlaceholderText('City')
        self.city_search.textChanged.connect(self.update_querry.emit)

        self.addWidget(self.last_name_search)
        self.addWidget(self.first_name_search)
        self.addWidget(self.city_search)


class SearchGuest(QWidget):
    clicked_widget = pyqtSignal(bool)
    def __init__(self):
        super(SearchGuest, self).__init__()
        self.setMinimumSize(500,500)

        self.db = Connection().db

        main_layout = QVBoxLayout()

        self.search_line_layout = SearchLineLayout()
        self.search_line_layout.update_querry.connect(self.update_querry)
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
            "LEFT OUTER JOIN tblAddresses ON tblGuest.gAddressID = tblAddresses.aAddressID "
            "WHERE "
            "gLastName LIKE '%' || :last_name || '%' AND "
            "gFirstName LIKE '%' || :first_name || '%' AND "
            "aCity LIKE '%' || :city || '%'"


        )
        self.update_querry()
        main_layout.addLayout(self.search_line_layout)
        main_layout.addWidget(self.guest_table)
        self.setLayout(main_layout)

    def table_on_dclick(self,e):

        temp_guest = Guest()
        temp_guest.fetch_by_id(self.db,self.model.index(e.row(),0).data())
        self.dialog = editGuest(db=self.db,guest=temp_guest)
        self.dialog.show()

    def mousePressEvent(self, e):
        self.clicked_widget.emit(True)

    def update_querry(self):
        last_name = self.search_line_layout.last_name_search.text()
        first_name = self.search_line_layout.first_name_search.text()
        city = self.search_line_layout.city_search.text()
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
