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
from Busquedas import buscarRuta, buscarRutaMinima, cargarCiudades, nombreCiudades
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

class Punto(object):
    # Variables iniciales de referencia para dibujar puntos en las provincias del mapa.
    CERO_X = 932.5
    CERO_Y = 310

    def __init__(self, idCiudad, nombre, pos_x, pos_y, numero):
        self.pos_x = self.CERO_X + pos_x
        self.pos_y = self.CERO_Y + pos_y
        self.idCiudad = idCiudad
        self.nombreCiudad = nombre
        self.text = numero

    def getNombre(self):
        return self.nombreCiudad

    def setText(self, text):
        self.text = text

    def dibujarPunto(self, mainWindow):
        # creating a label widget
        # by default label will display at top left corner
        self.circulo = QLabel(' ' + self.text, mainWindow)
        # moving position
        self.circulo.move(self.pos_x, self.pos_y)
        # making label square in size
        self.circulo.resize(30, 30)
        # setting up border and radius
        self.circulo.setStyleSheet("border: 2px solid green; border-radius: 15px; color: red; background-color: white")
        self.circulo.show()

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
        self.selectCiudad.addItem("")
        self.selectCiudad.addItem("")
        self.selectCiudad.addItem("")
        self.selectCiudad.addItem("")
        self.selectCiudad.addItem("")
        self.selectCiudad.addItem("")
        self.selectCiudad.addItem("")
        self.selectCiudad.addItem("")
        self.selectCiudad.addItem("")
        self.selectCiudad.addItem("")
        self.selectCiudad.addItem("")
        self.selectCiudad.addItem("")
        self.selectCiudad.addItem("")
        self.selectCiudad.addItem("")
        self.selectCiudad.addItem("")
        self.selectCiudad.addItem("")
        self.selectCiudad.addItem("")
        self.selectCiudad.addItem("")
        self.selectCiudad.addItem("")
        self.selectCiudad.addItem("")
        self.selectCiudad.addItem("")
        self.selectCiudad.addItem("")
        self.selectCiudad.addItem("")
        self.selectCiudad.addItem("")
        self.btnRutaMinima = QtWidgets.QPushButton(self.mainBox)
        self.btnRutaMinima.setGeometry(QtCore.QRect(30, 240, 171, 51))
        self.btnRutaMinima.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btnRutaMinima.setAutoDefault(False)
        self.btnRutaMinima.setObjectName("btnRutaMinima")
        self.btnRutaAGenetico = QtWidgets.QPushButton(self.mainBox)
        self.btnRutaAGenetico.setGeometry(QtCore.QRect(30, 370, 171, 51))
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
        nombres = nombreCiudades()
        for i, nombre in enumerate(nombres):
            self.selectCiudad.setItemText(i + 1, nombre)
            print(f'Id: {i + 1} Ciudad: {nombre}')

    def setPuntosMapa(self, ruta = []):
        posiciones_x = [ 30, -50, 30, -5, 0, -140, -120, -140, 10, 80, -120, -5, -120, -130, -80, -75, -120, -160, -90, -20, -80, -50, -60, -90 ]
        posiciones_y = [ -50, -90, -150, -265, 0, -165, -30, 20, -85, -170, 140, -220, 230, -210, -188, -258, -240, -120, -60, -120, 5, -155, 280, 60 ]
        nombres = nombreCiudades()
        for i, nombre in enumerate(nombres):
            if not(ruta):
                punto = Punto(i + 1, nombre, posiciones_x[i], posiciones_y[i], str(i))
                punto.dibujarPunto(self)
            else:
                # text = str(int(nombres.index(ruta[i].getNombre())) + 1)
                nombres_ruta = list(map(lambda i:i.getNombre(), ruta))
                text = str(int(nombres_ruta.index(nombres[i])) + 1)
                print(f'En ruta posicion {ruta[i].getNombre()} se encontro la posición: {text}')
                print(f'index nombres devolvio {nombres.index(ruta[i].getNombre())}')
                punto = Punto(i + 1, nombre, posiciones_x[i], posiciones_y[i], text)
                punto.dibujarPunto(self)


    def selectCiudad_onChanged(self, text):
        # print(f'La ciudad selecionada es: {text}')
        ruta = buscarRuta(cargarCiudades(), text)
        print("La ruta minima encontrada es:")
        print(f'{list(map(lambda x:x.getNombre(), ruta))}')
        arreglo_distancias = list(map(lambda x:x.getDistancia(), ruta))
        distancia = np.sum(arreglo_distancias)
        print(f"La distancia total es: {distancia}")
        # self.qlabel = QLabel(self)
        # self.qlabel.move(30,70)
        # Strign con la lista de ciudades de la ruta encontrada.
        rutaString = "\n".join(ciu.getNombre() for ciu in ruta)
        respuesta = f"La distancia entre {ruta[23].getNombre()} y {ruta[0].getNombre()} \n es de {distancia} KMs"
        self.labelRespuesta.setText(respuesta)
        self.labelRespuesta.adjustSize()
        self.setPuntosMapa(ruta)
        # self.mainBox.setParent(self.labelRespuesta)
        # self.qlabel.setText(text)
        # self.qlabel.adjustSize()

    def btnRutaMinimia_clicked(self):
        ruta = buscarRutaMinima(cargarCiudades())
        # Strign con la lista de ciudades de la ruta encontrada.
        rutaString = "\n".join(ciu.getNombre() for ciu in ruta)
        arreglo_distancias = list(map(lambda x:x.getDistancia(), ruta))
        distancia = np.sum(arreglo_distancias)
        respuesta = f"La distancia entre {ruta[23].getNombre()} y {ruta[0].getNombre()} \n es de {distancia} KMs"
        self.labelRespuesta.setText(respuesta)
        self.labelRespuesta.adjustSize()
        self.setPuntosMapa(ruta)

    def moussePressEvent(self, event):
        if event.buttons() and Qt.LeftButton:
            print(f'Posicion x: {event.pos().x()}')
            print(f'Posicion y  : {event.pos().y()}')
    
        self.update()

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
        self.setItemsCombo()
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
        pixmapImagen = QPixmap('provincias.png').scaled(365, 634, Qt.KeepAspectRatio,
                                                  Qt.SmoothTransformation)

        self.labelImagen.setPixmap(pixmapImagen)  
        self.setPuntosMapa()
        # Mostrar imagen
        # cero_x = 932.5
        # cero_y = 310
        # self.dibujarPunto(cero_x + 30, cero_y - 50, '1')
        # self.dibujarPunto(cero_x - 50, cero_y - 90, '2')
        # self.dibujarPunto(cero_x + 30, cero_y - 150, '3')
        # self.dibujarPunto(cero_x - 5, cero_y - 265, '4')
        # self.dibujarPunto(cero_x, cero_y, '5') # LaPlata
        # self.dibujarPunto(cero_x - 140, cero_y - 165, '6')
        # self.dibujarPunto(cero_x - 120, cero_y -30, '7')
        # self.dibujarPunto(cero_x - 140, cero_y + 20, '8')
        # self.dibujarPunto(cero_x + 10, cero_y - 85, '9')
        # self.dibujarPunto(cero_x + 80, cero_y - 170, '10')


        # self.dibujarPunto(cero_x - 80, cero_y + 5, '')
        # self.dibujarPunto(cero_x - 90, cero_y - 60, '5')
        # self.dibujarPunto(cero_x - 20, cero_y - 120, '7')
        # self.dibujarPunto(cero_x - 90, cero_y + 60, '9')
        # self.dibujarPunto(cero_x - 120, cero_y + 140, '10')
        # self.dibujarPunto(cero_x - 120, cero_y + 230, '11')
        # self.dibujarPunto(cero_x - 160, cero_y - 120, '12')
        # self.dibujarPunto(cero_x - 130, cero_y - 210, '14')
        # self.dibujarPunto(cero_x - 120, cero_y - 245, '15')
        # self.dibujarPunto(cero_x - 75, cero_y - 258, '16')
        # self.dibujarPunto(cero_x - 50, cero_y - 155, '17')
        # self.dibujarPunto(cero_x - 5, cero_y - 220, '18')
        # self.dibujarPunto(cero_x - 60, cero_y + 280, '23')
        # self.dibujarPunto(cero_x - 80, cero_y - 188, '24')


