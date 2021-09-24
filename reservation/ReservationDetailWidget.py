from PyQt5.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QLineEdit,
    QComboBox,
    QFormLayout,
)

from reservation.RoomingListWidget import RoomingListWidget

class ReservationDetailWidget(QWidget):
    def __init__(self):
        super(ReservationDetailWidget, self).__init__()
        main_layout = QHBoxLayout()
        form1 = QFormLayout()
        self.room_type_cmb = QComboBox()
        # TODO: database implementation
        self.room_type_cmb.addItems(['SGL', 'DBL'])

        form1.addRow("Room category:", self.room_type_cmb)
        form1.addRow("Arrival:", QLineEdit())
        form1.addRow("Nights:", QLineEdit())
        form1.addRow("No. of rooms:", QLineEdit())
        form1.addRow("No. of guest:", QLineEdit())

        form2 = QFormLayout()

        form2.addRow("Room:", QLineEdit())
        form2.addRow("Departure:", QLineEdit())
        form2.addRow("Reservation no.:", QLineEdit())
        form2.addRow("Reservation type:", QComboBox())
        form2.addRow("Channel:", QComboBox())

        lay3 = RoomingListWidget()

        main_layout.addLayout(form1)
        main_layout.addLayout(form2)
        main_layout.addWidget(lay3)
        self.setLayout(main_layout)
