# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UITP3Viajante.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from Busquedas import *
import numpy as np

class Example(QtWidgets.QMainWindow):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        
    def mousePressEvent(self, QMouseEvent):
        print(QMouseEvent.pos())

    def mouseReleaseEvent(self, QMouseEvent):
        cursor = QtGui.QCursor()
        print(cursor.pos())

    def initUI(self):
        qbtn = QtWidgets.QPushButton('Quit', self)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)
        self.setGeometry(0, 0, 1024, 768)
        self.setWindowTitle('Quit button')
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint)
        self.show()

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainBox = QtWidgets.QGroupBox(self.centralwidget)
        self.mainBox.setGeometry(QtCore.QRect(0, 20, 681, 600))
        self.mainBox.setObjectName("mainBox")
        self.labelRuta = QtWidgets.QLabel(self.mainBox)
        self.labelRuta.setGeometry(QtCore.QRect(20, 70, 221, 71))
        self.labelRuta.setObjectName("labelRuta")
        self.labelRespuesta = QtWidgets.QLabel(self.mainBox)
        self.labelRespuesta.setGeometry(QtCore.QRect(350, 70, 300, 40))
        self.labelRespuesta.setObjectName('labelRespuesta')
        self.labelAGenetico = QtWidgets.QLabel(self.mainBox)
        self.labelAGenetico.setGeometry(QtCore.QRect(20, 320, 211, 41))
        self.labelAGenetico.setObjectName("labelAGenetico")
        self.labelRutaTotal = QtWidgets.QLabel(self.mainBox)
        self.labelRutaTotal.setGeometry(QtCore.QRect(20, 190, 241, 61))
        self.labelRutaTotal.setObjectName("labelRutaTotal")
        self.label_5 = QtWidgets.QLabel(self.mainBox)
        self.label_5.setGeometry(QtCore.QRect(100, 40, 501, 31))
        self.label_5.setObjectName("label_5")
        self.selectCiudad = QtWidgets.QComboBox(self.mainBox)
        self.selectCiudad.setGeometry(QtCore.QRect(30, 130, 171, 51))
        self.selectCiudad.setObjectName("selectCiudad")
        self.selectCiudad.setItemText(0,"None")
        self.setItemsCombo()
        self.btnRutaMinima = QtWidgets.QPushButton(self.mainBox)
        self.btnRutaMinima.setGeometry(QtCore.QRect(30, 240, 161, 51))
        self.btnRutaMinima.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btnRutaMinima.setAutoDefault(False)
        self.btnRutaMinima.setObjectName("btnRutaMinima")
        self.btnRutaAGenetico = QtWidgets.QPushButton(self.mainBox)
        self.btnRutaAGenetico.setGeometry(QtCore.QRect(30, 370, 161, 51))
        self.btnRutaAGenetico.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btnRutaAGenetico.setAutoDefault(False)
        self.btnRutaAGenetico.setObjectName("btnRutaAGenetico")
        # self.mostrarTabla = QtWidgets.QTableView(self.mainBox)
        # self.mostrarTabla.setGeometry(QtCore.QRect(275, 110, 291, 281))
        # self.mostrarTabla.setGridStyle(QtCore.Qt.DotLine)
        # self.mostrarTabla.setObjectName("mostrarTabla")
        #self.mostrarTabla.setColumnsCount(4)
        #self.mostrarTabla.setTitle('TItulo de la table')
        #self.mostrarTabla.setItemText(1,1,1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 754, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def setItemsCombo(self):
        for ciu in CiudadesDAO.retornarCiudades():
            self.selectCiudad.addItem("")
            #EL -1 ES POR QUE EL ID DE LA CIUDAD ARRANCA EN 1 Y EL DEL COMBO EN 0 
            self.selectCiudad.setItemText(ciu.getID()-1, ciu.getNombre())
            #print(f'Id: {i + 1} Ciudad: {nombre}')

    def selectCiudad_onChanged(self, text):
        # print(f'La ciudad selecionada es: {text}')
        ruta = buscarRuta(text)
        #print("La ruta minima encontrada es:")
        #print(f'{list(map(lambda x:x.getNombre(), ruta))}')
        arreglo_distancias = list(map(lambda x:x.getDistancia(), ruta))
        # print(f"Lista de ciudades mapeadas: {arreglo_distancias}")
        #print(f"Total de ciudades: {len(arreglo_distancias)}")
        #print(f"La distancia total es: {np.sum(arreglo_distancias)}")
        # self.qlabel = QLabel(self)
        # self.qlabel.move(30,70)
        rutaString = "\n".join(ciu.getNombre() for ciu in ruta)
        self.labelRespuesta.setText(rutaString)
        self.labelRespuesta.adjustSize()
        # self.mainBox.setParent(self.labelRespuesta)
        # self.qlabel.setText(text)
        # self.qlabel.adjustSize()

    def btnRutaMinimia_clicked(self):
        ruta = buscarRutaMinima()
        rutaString = "\n".join(ciu.getNombre() for ciu in ruta)
        self.labelRespuesta.setText(rutaString)
        self.labelRespuesta.adjustSize()

    def moussePressEvent(self, event):
        if event.buttons() and Qt.LeftButton:
            print(f'Posicion x: {event.pos().x()}')
            print(f'Posicion y  : {event.pos().y()}')
        self.update()

    def dibujarPunto(self, x, y, numero):
        # creating a label widget
        # by default label will display at top left corner
        self.criculo1 = QLabel(' ' + numero, self)
        # moving position
        self.criculo1.move(x, y)
        # making label square in size
        self.criculo1.resize(30, 30)
        # setting up border and radius
        self.criculo1.setStyleSheet("border: 2px solid green; border-radius: 15px; color: red; background-color: white")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.mainBox.setTitle(_translate("MainWindow", "Problema del Viajante"))
        self.labelRuta.setText(_translate("MainWindow", "Buscar ruta mínima desde:"))
        self.labelAGenetico.setText(_translate("MainWindow", "Buscar ruta mínima utilizando \n"
"un Algoritmo Genético:"))
        self.labelRutaTotal.setText(_translate("MainWindow", "Buscar ruta mínima total:"))
        self.label_5.setText(_translate("MainWindow", "Aplicado a las distancias entre las provincias de la República Argentina.\n"
""))
        self.btnRutaMinima.setText(_translate("MainWindow", "Buscar ruta mínima"))
        self.btnRutaMinima.clicked.connect(self.btnRutaMinimia_clicked)
        self.btnRutaAGenetico.setText(_translate("MainWindow", "Buscar ruta con AG"))
        self.selectCiudad.setItemText(0, _translate("MainWindow", "Seleccione ciudad ..."))
        self.selectCiudad.activated[str].connect(self.selectCiudad_onChanged)

        # ==================== WIDGET QLABEL =======================
        
        self.labelImagen = QLabel(self)
        self.labelImagen.setGeometry(750, 25, 365, 634)
        self.labelImagen.setToolTip("Imagen")
        self.labelImagen.setCursor(Qt.PointingHandCursor)

        self.labelImagen.setStyleSheet("QLabel {background-color: white; border: 1px solid "
                                       "#01DFD7; border-radius: 5px;}")
        
        self.labelImagen.setAlignment(Qt.AlignCenter)
        # TODO Clase QPixMap para poder escribir un punto sobre la imagen
        pixmapImagen = QPixmap('./UserInterface/provincias.png').scaled(365, 634, Qt.KeepAspectRatio,
                                                  Qt.SmoothTransformation)

        # Mostrar imagen
        cero_x = 932.5
        cero_y = 310
        self.labelImagen.setPixmap(pixmapImagen)  
        self.dibujarPunto(cero_x, cero_y, '1')
        self.dibujarPunto(cero_x - 80, cero_y + 5, '2')
        self.dibujarPunto(cero_x - 140, cero_y + 20, '3')
        self.dibujarPunto(cero_x - 120, cero_y -30, '4')
        self.dibujarPunto(cero_x - 90, cero_y - 60, '5')
        self.dibujarPunto(cero_x - 50, cero_y - 90, '6')
        self.dibujarPunto(cero_x - 20, cero_y - 120, '7')
        self.dibujarPunto(cero_x + 10, cero_y - 85, '8')
        self.dibujarPunto(cero_x - 90, cero_y + 60, '9')
        self.dibujarPunto(cero_x - 120, cero_y + 140, '10')
        self.dibujarPunto(cero_x - 120, cero_y + 230, '11')
        self.dibujarPunto(cero_x - 160, cero_y - 120, '12')
        self.dibujarPunto(cero_x - 140, cero_y - 165, '13')
        self.dibujarPunto(cero_x - 130, cero_y - 210, '14')
        self.dibujarPunto(cero_x - 120, cero_y - 245, '15')
        self.dibujarPunto(cero_x - 75, cero_y - 258, '16')
        self.dibujarPunto(cero_x - 50, cero_y - 155, '17')
        self.dibujarPunto(cero_x - 5, cero_y - 220, '18')
        self.dibujarPunto(cero_x - 5, cero_y - 265, '19')
        self.dibujarPunto(cero_x + 30, cero_y - 150, '20')
        self.dibujarPunto(cero_x + 80, cero_y - 170, '21')
        self.dibujarPunto(cero_x + 30, cero_y - 50, '22')
        self.dibujarPunto(cero_x - 60, cero_y + 280, '23')
        self.dibujarPunto(cero_x - 80, cero_y - 188, '24')


