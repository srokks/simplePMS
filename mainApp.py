from PyQt5.QtWidgets import (
    QWidget,
    QMainWindow,
    QApplication,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QMdiArea, QMdiSubWindow
)

from guest.EditGuestWidget import editGuest
from guest.SearchGuestWidget import SearchGuest
from room_rack.RoomRack import RoomRackWindow
from reservation.ResEdit import ReservationEdit

class ActionBtnLayout(QWidget):
    def __init__(self):
        super(ActionBtnLayout, self).__init__()
        self.setMaximumHeight(50)
        lay = QHBoxLayout()
        self.search_guest_btn = QPushButton('/guest_id_signal/SearchGuestWidget')
        lay.addWidget(self.search_guest_btn)
        self.edit_guest_btn = QPushButton('/guest_id_signal/EditGuestWidget')
        lay.addWidget(self.edit_guest_btn)
        self.room_rack_btn = QPushButton('/RoomRackWindow/RoomRack.py')
        lay.addWidget(self.room_rack_btn)
        self.res_edit_btn = QPushButton('/reservation/ResEdit.py')
        lay.addWidget(self.res_edit_btn)
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
        action_btn.res_edit_btn.clicked.connect(self.res_edit_show)





        self.setCentralWidget(main_wi)

    def res_edit_show(self):
        sub = QMdiSubWindow()
        sub.setWidget(ReservationEdit(self.mdi_area))
        self.mdi_area.addSubWindow(sub)
        sub.show()
    def room_rack_show(self):
        sub = QMdiSubWindow()
        sub.setWidget(RoomRackWindow())
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

    app = QApplication(sys.argv)

    # app.setStyleSheet(qdarkstyle.load_stylesheet())
    MainWindow = MainWindow()
    MainWindow.resize(1024,768)
    MainWindow.move(500,0)
    MainWindow.show()
    MainWindow.res_edit_show()
    sys.exit(app.exec_())