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
from PyQt5.QtCore import QRegExp,pyqtSignal
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import Qt,QDate
from reservation.RoomingListWidget import RoomingListWidget
from guest.Guest import Guest

class ReservationDetailWidget(QWidget):
    guest_id_signal = pyqtSignal(int)
    def __init__(self):
        super(ReservationDetailWidget, self).__init__()
        main_layout = QHBoxLayout()
        form1 = QFormLayout()
        form1.setHorizontalSpacing(20)

        self.room_type_cmb = QComboBox()
        # TODO: load room_types from DB
        self.room_type_cmb.addItems(['SGL', 'DBL'])


        self.arrival_date = QDateEdit()
        self.arrival_date.setDate(QDate().currentDate())
        self.arrival_date.setCalendarPopup(True)

        self.nights = QLineEdit()
        self.nights.textEdited.connect(self.departure_date_recalculate)
        self.room_no = QLineEdit()
        self.guests_no = QLineEdit()

        form1.addRow("Room category:", self.room_type_cmb)
        form1.addRow("Arrival:", self.arrival_date)
        form1.addRow("Nights:", self.nights)
        form1.addRow("No. of rooms:", self.room_no)
        form1.addRow("No. of guest:", self.guests_no)

        form2 = QFormLayout()
        form2.setLabelAlignment(Qt.AlignLeft)
        form2.setFieldGrowthPolicy(form2.ExpandingFieldsGrow)

        self.departure_date = QDateEdit()
        self.departure_date.setDate(QDate().currentDate().addDays(1))
        self.departure_date.dateChanged.connect(self.night_recalculate)
        self.departure_date.setCalendarPopup(True)
        self.room = QLineEdit()

        self.res_number = QLineEdit()

        self.res_type_cmb = QComboBox()
        # TODO: load res_types from DB
        self.res_type_cmb.addItems(["1.Guarantee",'2.Unguarantee','3.Option'])

        form2.addRow("Room:", self.room)
        form2.addRow("Departure:", self.departure_date)
        form2.addRow("Reservation no.:", self.res_number)
        form2.addRow("Reservation type:", self.res_type_cmb)


        main_layout.addLayout(form1)
        main_layout.addLayout(form2)
        main_layout.addStretch()
        self.setLayout(main_layout)

    def al(self,e:QDate):
        self.arrival_date.setText(e.toString(Qt.SystemLocaleShortDate))
        self.cal.close()
        pass

    def departure_date_recalculate(self, e):
        'Trigered by changing night value. Recalculate departure date and update it'
        if e!='':
            arival_date = self.arrival_date.date()
            departure_date = arival_date.addDays(int(e))
            self.departure_date.setDate(departure_date)
    def night_recalculate(self,date):
        'Trigered by changing departure value. Recalculate nigth value and update it'
        self.nights.setText(str(self.arrival_date.date().daysTo(date)))


    def gather_res_details(self):
        pass
