from UserInterface import uiPyQT
from CiudadesDAO import CiudadesDAO
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
    
class ExampleApp(QtWidgets.QMainWindow, uiPyQT.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)

def main():
    app = QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    # Carga de los datos del excel
    CiudadesDAO.cargarCiudades()
    main()
    #menuConsola()


