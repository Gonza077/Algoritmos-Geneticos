from Generacion import *
from Poblacion import *
from Cromosoma import *
from OperadoresGeneticos import *
import openpyxl as opyxl
from UserInterface import Ui_Dialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
    
class App(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self, parent=None):
        super(App, self).__init__(parent)
        self.setupUi(self)

def main():
    app = QApplication(sys.argv)
    form = App()
    form.show()
    app.exec_() 

if __name__ == '__main__':
    main()
