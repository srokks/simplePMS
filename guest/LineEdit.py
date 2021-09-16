from PyQt5.QtWidgets import QLineEdit
class LineEdit(QLineEdit):

    def __init__(self):
        super(LineEdit, self).__init__()
        self.setMinimumWidth(125)
        self.setMaximumWidth(300)
        self.obligatory = False
        self.setObligatory()
    def setObligatory(self,obligatory=False):
        self.obligatory = obligatory
        if self.obligatory == True:
            self.setStyleSheet('background-color:rgba(255, 238, 0,90)')
        else:
            self.setStyleSheet('background-color:rgb(255, 255, 255)')