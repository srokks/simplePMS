import sys

from PyQt5.QtWidgets import (
    QApplication,
    QFormLayout,
    QLabel,
    QLineEdit,
    QWidget,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout
)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Edit:")#TODO: show who's entry is edited / new guest empty
        self.resize(270, 110)
        # Create a QFormLayout instance
        self.mainlay = QHBoxLayout()
        form_lay = QFormLayout()
        # Add widgets to the layout
        form_lay.addRow("Name:", QLineEdit())
        form_lay.addRow("Surname:", QLineEdit())
        form_lay.addRow("Mail:", QLineEdit())
        form_lay.addRow("Phone no:", QLineEdit())
        form_lay.addRow("Address:", QLineEdit())
        form_lay.addRow("Phone no:", QLineEdit())
        form_lay.addRow("Zip code:", QLineEdit())
        form_lay.addRow("City:", QLineEdit())

        self.button_lay = QVBoxLayout()
        self.button_lay.addWidget(QPushButton("lalal"))

      # Set the layout on the application's window
        self.mainlay.addLayout(form_lay)
        self.mainlay.addLayout(self.button_lay)
        self.setLayout(self.mainlay)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
