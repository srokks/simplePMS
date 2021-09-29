class BlankWidget(QWidget):
    '''Widgets witch only show how big is area in '''
    def __init__(self, color):
        super(BlankWidget, self).__init__()
        self.color = color

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setRenderHint(painter.Antialiasing)
        path = QPainterPath()
        rect = QRect(0, 0, self.width(), self.height())
        pen = QPen(QColor(self.color), 1)
        painter.setPen(pen)
        painter.drawRect(rect)