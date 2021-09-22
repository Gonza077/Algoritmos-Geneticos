from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtGui import QPainter
from DibujarLineaMouseDialog import DibujarLineaMouseDialog
import sys  

class DibujarLineaMouseApplication(QDialog):

    def __init__(self):
        super().__init__()

        self.ui = DibujarLineaMouseDialog()
        self.ui.setupUi(self)

        self.posicion_1 = [0, 0]
        self.posicion_2 = [0, 0]

        self.show()

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.drawLine(self.posicion_1[0], self.posicion_1[1], self.posicion_2[0], self.posicion_2[1])
        painter.end()

    def mouseReleaseEvent(self, event):
        self.posicion_2[0] = event.pos().x()
        self.posicion_2[1] = event.pos().y()

        self.update()
    
    def mousePressEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            self.posicion_1[0] = event.pos().x()
            self.posicion_1[1] = event.pos().y()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = DibujarLineaMouseApplication()
    ventana.show()

    sys.exit(app.exec_())


