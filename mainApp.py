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
from room_rack.RoomRack import room_rack
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        search_btn = QPushButton('guest/searchGuestWindow.py')
        search_btn.clicked.connect(self.showSearchGuest)

        new_btn = QPushButton('guest/editGuestWindow.py')
        new_btn.clicked.connect(self.showEditGuest)

        room_rack_btn = QPushButton('room_rack')
        room_rack_btn.clicked.connect(self.show_room_rack_on_click)

        but_layout = QVBoxLayout()
        but_layout.addWidget(search_btn)
        but_layout.addWidget(new_btn)
        but_layout.addWidget(room_rack_btn)
        # self.searchGuest = searchGuestWindow.searchGuest()
        # self.editGuest = editGuestWindow.editGuest()
        self.room_rack_window = room_rack()
        wi = QWidget()
        wi.setLayout(but_layout)
        self.setCentralWidget(wi)
    def showSearchGuest(self):
        # self.searchGuest.show()
        pass
    def showEditGuest(self):
        # self.editGuest.show()
        pass
    def show_room_rack_on_click(self):
        self.room_rack_window.show()
        pass
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())