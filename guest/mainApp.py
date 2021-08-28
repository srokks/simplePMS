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
from Guest import GuestCtrl, Guest

from editGuestWindow import editGuest
from searchGuestWindow import searchGuest
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        search_btn = QPushButton('searchGuestWindow.py')
        search_btn.clicked.connect(self.showSearchGuest)

        new_btn = QPushButton('editGuestWindow.py')
        new_btn.clicked.connect(self.showEditGuest)
        but_layout = QVBoxLayout()
        but_layout.addWidget(search_btn)
        but_layout.addWidget(new_btn)
        self.searchGuest = searchGuest()
        self.editGuest = editGuest()
        wi = QWidget()
        wi.setLayout(but_layout)
        self.setCentralWidget(wi)
    def showSearchGuest(self):
        self.searchGuest.show()
    def showEditGuest(self):
        self.editGuest.show()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())