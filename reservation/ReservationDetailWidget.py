from PyQt5.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QLineEdit,
    QComboBox,
    QFormLayout,
    QPushButton,
    QCalendarWidget,
    QSizePolicy,
    QDateEdit,
)
from PyQt5.QtCore import QRegExp, pyqtSignal
from PyQt5.QtGui import QRegExpValidator, QIntValidator
from PyQt5.QtCore import Qt, QDate
from reservation.RoomingListWidget import RoomingListWidget
from guest.Guest import Guest
from reservation.Reservation import Reservation


class ReservationDetailWidget(QWidget):
    reservation_inited = pyqtSignal(bool)  # emits if all fields are valid
    reservation_valid = False # hold state of reservation
    def __init__(self):
        super(ReservationDetailWidget, self).__init__()
        main_layout = QHBoxLayout()
        form1 = QFormLayout()
        form1.setHorizontalSpacing(20)
        # -----
        self.room_type_cmb = QComboBox()
        # TODO: load room_types from DB
        self.room_type_cmb.addItems(['SGL', 'DBL'])
        # -----
        self.arrival_date = QDateEdit()
        self.arrival_date.setDate(QDate().currentDate())
        self.arrival_date.setCalendarPopup(True)
        self.arrival_date.dateChanged.connect(self.night_recalculate)  # recalculate night if date changed
        # -----
        self.nights = QLineEdit()
        val = QIntValidator(0,99)  # allow only ints
        self.nights.setValidator(val)
        self.nights.textChanged.connect(self.departure_date_recalculate)  # recalculate departure date if changed
        # -----
        self.room_no = QLineEdit()
        self.room_no.setValidator(val)
        # -----
        self.guests_no = QLineEdit()
        self.guests_no.setValidator(val)
        # -----
        form1.addRow("Room category:", self.room_type_cmb)
        form1.addRow("Arrival:", self.arrival_date)
        form1.addRow("Nights:", self.nights)
        form1.addRow("No. of rooms:", self.room_no)
        form1.addRow("No. of guest:", self.guests_no)
        # -----
        form2 = QFormLayout()
        form2.setLabelAlignment(Qt.AlignLeft)
        form2.setFieldGrowthPolicy(form2.ExpandingFieldsGrow)
        # -----
        self.departure_date = QDateEdit()
        self.departure_date.setDate(QDate().currentDate().addDays(1))
        self.departure_date.dateChanged.connect(self.night_recalculate) # recalculate departure date if changed
        self.departure_date.setCalendarPopup(True) # allows calendar pop up
        # -----
        self.room = QLineEdit()
        # -----
        self.res_number = QLineEdit()
        self.res_number.setDisabled(True)
        # -----
        self.res_type_cmb = QComboBox()
        self.res_type_cmb.addItems(["1.Guarantee", '2.Unguarantee', '3.Option'])
        # -----
        form2.addRow("Room:", self.room)
        form2.addRow("Departure:", self.departure_date)
        form2.addRow("Reservation no.:", self.res_number)
        form2.addRow("Reservation type:", self.res_type_cmb)
        # -----
        main_layout.addLayout(form1)
        main_layout.addLayout(form2)
        main_layout.addStretch()
        # -----
        self.setLayout(main_layout)
        # -----
        for el in self.findChildren(QLineEdit):
            el.textEdited.connect(self.check_obligatories)

        # -----
        self.night_recalculate()

    def departure_date_recalculate(self, e: str):
        """Trigered by changing night value. Recalculate departure date and update it"""
        if e != '':
            arival_date = self.arrival_date.date()
            departure_date = arival_date.addDays(int(e))
            self.departure_date.setDate(departure_date)

    def check_obligatories(self):
        """ Emit signal for if all entered data in form are valid"""
        if self.nights.hasAcceptableInput() and self.room_no.hasAcceptableInput() and self.guests_no.hasAcceptableInput():
            self.reservation_valid = True
            self.reservation_inited.emit(True)
        # Logic for turning unfilled field to red
        if self.sender().hasAcceptableInput(): # check if sender has acceptable input
            self.sender().setStyleSheet('background-color:white')
        elif self.sender().text() == '': # if sender text is empty
            self.sender().setStyleSheet('background-color:red') # turn bcg color to red

    def night_recalculate(self):
        """Trigered by changing arrival/departure value. Recalculate nigth value and update it
        Also check if arrival date < departure date """
        self.departure_date.setMinimumDate(self.arrival_date.date())
        self.nights.setText(str(self.arrival_date.date().daysTo(self.departure_date.date())))

    def init_res_details(self, res):
        """ Populate form line edits with res date """
        if res is None:
            pass
        else:
            self.reservation = res
            self.room_type_cmb.setCurrentIndex(self.reservation.room_type)
            self.guests_no.setText(str(self.reservation.guest_no))
            self.arrival_date.setDate(self.reservation.date_from)
            self.departure_date.setDate(self.reservation.date_to)
            self.res_number.setText(self.reservation.booking_no)
            self.room_no.setText(str(self.reservation.room_no))

    def gather_res_details(self):
        """Gathers all thing from form and returns as Reservation"""
        res = Reservation()
        # self.booking_no =
        # self.guest_id = 3
        res.date_from = self.arrival_date.date()
        res.date_to = self.departure_date.date()
        self.room_no = self.room_no.text()
        res.guest_no = self.guests_no.text()
        res.booking_status_id = self.res_type_cmb.currentIndex()
        res.room_type = self.room_type_cmb.currentIndex()
        return res
