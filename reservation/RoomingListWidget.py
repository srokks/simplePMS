from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPainter, QPainterPath, QPen, QColor
from PyQt5.QtWidgets import QWidget, QHBoxLayout


class RoomingListWidget(QWidget):
    def __init__(self):
        super(RoomingListWidget, self).__init__()
        self.setMinimumHeight(200)
        self.setMinimumWidth(200)
        main_layout = QHBoxLayout()

        self.setLayout(main_layout)

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setRenderHint(painter.Antialiasing)
        path = QPainterPath()
        rect = QRect(0, 0, self.width(), self.height())
        pen = QPen(QColor('purple'), 1)
        painter.setPen(pen)
        painter.drawRect(rect)
