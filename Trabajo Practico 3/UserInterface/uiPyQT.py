 
# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'UITP3Viajante.ui'
# Created by: PyQt5 UI code generator 5.14.1
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from CiudadDAO import CiudadesDAO
import numpy as np

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
            self.selectCiudad.setItemText(ciu.getID(), ciu.getNombre())
            
    def setPuntosMapa(self, ruta = []):
        posiciones_x = [ 30, -50, 30, -5, 0, -140, -120, -140, 10, 80, -120, -5, -120, -130, -80, -75, -120, -160, -90, -20, -80, -50, -60, -90 ]
        posiciones_y = [ -50, -90, -150, -265, 0, -165, -30, 20, -85, -170, 140, -220, 230, -210, -188, -258, -240, -120, -60, -120, 5, -155, 280, 60 ]
        nombres=[]
        for ciudad in CiudadesDAO.retornarCiudades():
            nombres.append(ciudad._nombre)
        for i, nombre in enumerate(nombres):
            if not(ruta):
                punto = Punto(i + 1, nombre, posiciones_x[i], posiciones_y[i], str(i))
                punto.dibujarPunto(self)
            else:
                nombres_ruta = list(map(lambda i:i.getNombre(), ruta))
                text = str(int(nombres_ruta.index(nombres[i])) + 1)
                punto = Punto(i + 1, nombre, posiciones_x[i], posiciones_y[i], text)
                punto.dibujarPunto(self)

    def selectCiudad_onChanged(self, text):
        if (text!="Seleccione ciudad ..."):
            ruta = CiudadesDAO.buscarRuta(text)
            arreglo_distancias = list(map(lambda x:x.getDistancia(), ruta))
            distancia = np.sum(arreglo_distancias)
            rutaString = "\n".join(ciu.getNombre() for ciu in ruta)
            respuesta = f"La distancia entre {ruta[23].getNombre()} y {ruta[0].getNombre()} \n es de {distancia} KMs"
            self.labelRespuesta.setText("Recorrido partiendo de la ciudad de "+ruta[23].getNombre()+"\n"*2+rutaString + "\n"*2 + respuesta)
            self.labelRespuesta.adjustSize()
            self.setPuntosMapa(ruta)

    def btnRutaMinimia_clicked(self):
        ruta = CiudadesDAO.buscarRutaMinima()
        # Strign con la lista de ciudades de la ruta encontrada.
        rutaString = "\n".join(ciu.getNombre() for ciu in ruta)
        arreglo_distancias = list(map(lambda x:x.getDistancia(), ruta))
        distancia = np.sum(arreglo_distancias)
        respuesta = f"La distancia entre {ruta[23].getNombre()} y {ruta[0].getNombre()} \n es de {distancia} KMs"
        self.labelRespuesta.setText("Recorrido partiendo de la ciudad de "+ruta[23].getNombre()+"\n"*2+rutaString + "\n"*2 + respuesta)
        self.labelRespuesta.adjustSize()
        self.selectCiudad.setCurrentText(ruta[23].getNombre())
        self.setPuntosMapa(ruta)

    def btnGeneticos_showDialog(self):
        dialog = QtWidgets.QDialog()
        self.buttonBox = QtWidgets.QDialogButtonBox(dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 280, 400, 80))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 191, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 191, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 191, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 170, 191, 41))
        self.label_4.setObjectName("label_4")
        self.numCromosomas = QtWidgets.QLineEdit(dialog)
        self.numCromosomas.setGeometry(QtCore.QRect(250, 20, 113, 36))
        self.numCromosomas.setObjectName("numCromosomas")
        self.numCromosomas.setText('50')
        self.cantCiclos = QtWidgets.QLineEdit(dialog)
        self.cantCiclos.setGeometry(QtCore.QRect(250, 70, 113, 36))
        self.cantCiclos.setObjectName("cantCiclos")
        self.cantCiclos.setText('200')
        self.probCrossover = QtWidgets.QLineEdit(dialog)
        self.probCrossover.setGeometry(QtCore.QRect(250, 120, 113, 36))
        self.probCrossover.setObjectName("probCrossover")
        self.probCrossover.setText('0.70')
        self.probMutacion = QtWidgets.QLineEdit(dialog)
        self.probMutacion.setGeometry(QtCore.QRect(250, 170, 113, 36))
        self.probMutacion.setObjectName("probMutacion")
        self.probMutacion.setText('0.05')
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle("Parametros del Algoritmo Genético")
        self.label.setText(_translate("Dialog", "Número de cromosomas:"))
        self.label_2.setText(_translate("Dialog", "Cantidad de ciclos:"))
        self.label_3.setText(_translate("Dialog", "Probabilidad de crossover:"))
        self.label_4.setText(_translate("Dialog", "Probabilidad de mutación:"))
        dialog.setWindowModality(Qt.ApplicationModal)
        self.buttonBox.accepted.connect(dialog.accept)
        self.buttonBox.rejected.connect(dialog.reject)

        respuesta = dialog.exec_()
        print("Valor del boton presionado 1-Aceptar 0-Cancelar:", respuesta)

        if(respuesta):
            """
                Aca iria la función que retorna la mejor solución encontrada
                por el algoritmo genetico.

                numCromosomas = int(self.numCromosomas.text())
                cantCiclos = int(self.cantCiclos.text())
                probMutacion = float(self.probMutacion.text())
                probCrossover = float(self.probCrossover.text())

                ruta = buscarRutaAlgoritmoGenetico(numCromosomas, cantCiclos, probMutacion, probCrossover)
                arreglo_distancias = list(map(lambda x:x.getDistancia(), ruta))
                distancia = np.sum(arreglo_distancias)
                rutaString = "\n".join(ciu.getNombre() for ciu in ruta)

                respuesta = (f"La distancia mínima encontrada por el Algoritmo Genetico es \n"
                 f"desde {ruta[23].getNombre()} a {ruta[0].getNombre()} \n con una distancia de {distancia} KMs")
                
                self.labelRespuesta.setText(respuesta)
                self.labelRespuesta.adjustSize()
                self.setPuntosMapa(ruta)

            """
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Valores ingresados")
            msg.setInformativeText("Ver valores ingresados")
            msg.setWindowTitle("Ver valores")
            # String multilinea definido entre parentesis. Ej: string = (f"\n" f"\n" f"\n" )
            stringDetailedText = (f"Número de cromosomas: {self.numCromosomas.text()} \n" 
                f"Cantidad de ciclos: {self.cantCiclos.text()}\n"
                f"Probabilidad de mutación: {self.probMutacion.text()}\n"
                f"Probabilidad de crossover: {self.probCrossover.text()} \n"
                f"Suma Mutacion y Crossover: {float(self.probCrossover.text()) + float(self.probMutacion.text())}")
            msg.setDetailedText(stringDetailedText)
            msg.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.mainBox.setTitle(_translate("MainWindow", "Problema del Viajante"))
        self.labelRuta.setText(_translate("MainWindow", "Buscar ruta mínima desde:"))
        self.labelAGenetico.setText(_translate("MainWindow", "Buscar ruta mínima utilizando \n un Algoritmo Genético:"))
        self.labelRutaTotal.setText(_translate("MainWindow", "Buscar ruta mínima total:"))
        self.label_5.setText(_translate("MainWindow", "Aplicado a las distancias entre las provincias de la República Argentina.\n"))
        self.btnRutaMinima.setText(_translate("MainWindow", "Buscar ruta mínima"))
        self.btnRutaMinima.clicked.connect(self.btnRutaMinimia_clicked)
        self.btnRutaAGenetico.setText(_translate("MainWindow", "Buscar ruta con AG"))
        self.btnRutaAGenetico.clicked.connect(self.btnGeneticos_showDialog)
        self.selectCiudad.addItem("")
        self.selectCiudad.setItemText(0, _translate("MainWindow", "Seleccione ciudad ..."))
        self.setItemsCombo()
        self.selectCiudad.activated[str].connect(self.selectCiudad_onChanged)
        self.labelImagen = QLabel(self)
        self.labelImagen.setGeometry(750, 25, 365, 634)
        self.labelImagen.setToolTip("Imagen")
        self.labelImagen.setCursor(Qt.PointingHandCursor)
        self.labelImagen.setStyleSheet("QLabel {background-color: white; border: 1px solid #01DFD7; border-radius: 5px;}")     
        self.labelImagen.setAlignment(Qt.AlignCenter)
        pixmapImagen = QPixmap('./UserInterface/provincias.png').scaled(365, 634, Qt.KeepAspectRatio,Qt.SmoothTransformation)
        self.labelImagen.setPixmap(pixmapImagen)  
        self.setPuntosMapa()
