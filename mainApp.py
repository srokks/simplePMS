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
QDockWidget,
QMdiArea,QMdiSubWindow
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QBrush, QPen, QFont, QPainterPath, QPixmap, QDrag
from PyQt5.QtCore import QAbstractTableModel, QEvent, Qt, QRect, QMimeData, pyqtSignal


from guest.EditGuestWidget import editGuest
from room_rack.RoomRack import room_rack
from guest.SearchGuestWidget import SearchGuest


class ActionBtnLayout(QWidget):
    def __init__(self):
        super(ActionBtnLayout, self).__init__()
        self.setMaximumHeight(50)
        lay = QHBoxLayout()
        self.search_guest_btn = QPushButton('/guest/SearchGuestWidget')
        lay.addWidget(self.search_guest_btn)
        self.edit_guest_btn = QPushButton('/guest/EditGuestWidget')
        lay.addWidget(self.edit_guest_btn)
        self.room_rack_btn = QPushButton('/room_rack/RoomRack.py')
        lay.addWidget(self.room_rack_btn)
        self.setLayout(lay)
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        main_wi = QWidget()
        main_lay = QVBoxLayout()
        main_wi.setLayout(main_lay)

        action_btn = ActionBtnLayout()
        main_lay.addWidget(action_btn)

        self.mdi_area = QMdiArea()

        main_lay.addWidget(self.mdi_area)

        action_btn.edit_guest_btn.clicked.connect(self.edit_guest_show)
        action_btn.search_guest_btn.clicked.connect(self.show_guest_show)
        action_btn.room_rack_btn.clicked.connect(self.room_rack_show)





        self.setCentralWidget(main_wi)

    def room_rack_show(self):
        sub = QMdiSubWindow()
        sub.setWidget(room_rack())
        self.mdi_area.addSubWindow(sub)
        sub.show()

    def edit_guest_show(self):
        sub = QMdiSubWindow()
        sub.setWidget(editGuest())
        sub.setWindowTitle("Edit")
        self.mdi_area.addSubWindow(sub)
        sub.show()

    def show_guest_show(self):
        sub = QMdiSubWindow()
        sub.setWidget(SearchGuest())
        sub.setWindowTitle("Search")
        self.mdi_area.addSubWindow(sub)
        sub.show()

if __name__ == "__main__":
    import sys
    import qdarkstyle

    app = QApplication(sys.argv)

    # app.setStyleSheet(qdarkstyle.load_stylesheet())
    MainWindow = MainWindow()
    MainWindow.resize(1024,768)
    MainWindow.show()
    sys.exit(app.exec_())