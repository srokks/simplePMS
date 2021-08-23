import sys

from PyQt5.QtWidgets import (
    QApplication,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QLineEdit,
    QVBoxLayout,
    QPushButton,
    QHBoxLayout,
    QTabWidget,
    QWidget
)

from guest import Guest


class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Edit:")#TODO: show who's entry is edited / new guest empty
        self.resize(300, 400)
        main_lay = QHBoxLayout()

        form = self.guest_info_form()
        main_lay.addLayout(form)
        main_lay.addLayout(self.func_btn_lay())
        self.data_init(117)
        self.setLayout(main_lay)

    def data_init(self,guest_id):
        #guest_id,guest_first_name,guest_last_name,guest_email,guest_phone,address_id
        self.guest_id = guest_id
        if self.guest_id == "":
            self.change_btn.setDisabled(True)
        else:
            self.guest_data = Guest().getGuestbyID(self.guest_id)
            self.id_row.setText(str(self.guest_data[0]))
            self.name.setText(self.guest_data[2])
            self.last_name.setText(self.guest_data[1])
            self.mail.setText(self.guest_data[3])
            self.phone.setText(self.guest_data[4])
            self.change_btn.setEnabled(True)

    def data_change(self):

        new_guest =[
                str(self.id_row.text()),
                self.last_name.text(),
                self.name.text(),
                self.mail.text(),
                self.phone.text(),
        ]
        print(new_guest)
        Guest().updateByID(new_guest)

    def func_btn_lay(self):
        lay = QVBoxLayout()

        new_btn = QPushButton()
        new_btn.setText("New...")
        new_btn.clicked.connect(self.newBtnEvent)


        self.change_btn = QPushButton()
        self.change_btn.setDisabled(True)
        self.change_btn.setText("Change")
        self.change_btn.clicked.connect(self.updateBtnEvent)

        close_btn = QPushButton()
        close_btn.setText("Close")

        lay.addWidget(new_btn)
        lay.addWidget(self.change_btn)
        lay.addWidget(close_btn)
        lay.addStretch()
        return lay

    def guest_info_form(self):
        lay = QFormLayout()
        self.id_row = QLineEdit()
        self.id_row.setReadOnly(True)

        lay.addRow('id:',self.id_row)
        self.name = QLineEdit()
        self.last_name = QLineEdit()
        self.mail = QLineEdit()
        self.phone = QLineEdit()



        lay.addRow("Name:", self.name)
        lay.addRow("Last name:", self.last_name)
        lay.addRow("Mail:", self.mail)
        lay.addRow("Phon NO:", self.phone)

        return lay

    def newBtnEvent(self):
        pass
    def updateBtnEvent(self):
        self.data_change()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
