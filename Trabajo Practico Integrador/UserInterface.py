# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uiTPParquesEolicos.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from Generacion import *
from Poblacion import *
from Cromosoma import *
from OperadoresGeneticos import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1348, 731)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(360, 10, 461, 271))
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 40, 361, 181))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(5, 5, 5, 5)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.tamPoblacion = QtWidgets.QLineEdit(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tamPoblacion.sizePolicy().hasHeightForWidth())
        self.tamPoblacion.setSizePolicy(sizePolicy)
        self.tamPoblacion.setObjectName("tamPoblacion")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.tamPoblacion)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_12 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.selectSeleccion = QtWidgets.QComboBox(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectSeleccion.sizePolicy().hasHeightForWidth())
        self.selectSeleccion.setSizePolicy(sizePolicy)
        self.selectSeleccion.setObjectName("selectSeleccion")
        self.selectSeleccion.addItem("")
        self.selectSeleccion.addItem("")
        self.selectSeleccion.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.selectSeleccion)
        self.selectCrossover = QtWidgets.QComboBox(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectCrossover.sizePolicy().hasHeightForWidth())
        self.selectCrossover.setSizePolicy(sizePolicy)
        self.selectCrossover.setObjectName("selectCrossover")
        self.selectCrossover.addItem("")
        self.selectCrossover.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.selectCrossover)
        self.selectMutacion = QtWidgets.QComboBox(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectMutacion.sizePolicy().hasHeightForWidth())
        self.selectMutacion.setSizePolicy(sizePolicy)
        self.selectMutacion.setObjectName("selectMutacion")
        self.selectMutacion.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.selectMutacion)
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 10, 341, 271))
        self.groupBox_3.setObjectName("groupBox_3")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_3)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(30, 40, 291, 214))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(5, 5, 5, 5)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.tamCromosoma = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.tamCromosoma.setObjectName("tamCromosoma")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.tamCromosoma)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.cantAerogeneradores = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.cantAerogeneradores.setObjectName("cantAerogeneradores")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cantAerogeneradores)
        self.tamCelda = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tamCelda.sizePolicy().hasHeightForWidth())
        self.tamCelda.setSizePolicy(sizePolicy)
        self.tamCelda.setObjectName("tamCelda")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.tamCelda)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.velocidadViento = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.velocidadViento.setObjectName("velocidadViento")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.velocidadViento)
        self.label_14 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_14.setObjectName("label_14")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.coefRugosidad = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.coefRugosidad.setObjectName("coefRugosidad")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.coefRugosidad)
        self.groupBox_4 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_4.setGeometry(QtCore.QRect(840, 10, 391, 261))
        self.groupBox_4.setObjectName("groupBox_4")
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_4)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(20, 40, 351, 181))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setContentsMargins(5, 5, 5, 5)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_9.setObjectName("label_9")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.cantPoblaciones = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.cantPoblaciones.setObjectName("cantPoblaciones")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cantPoblaciones)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_10.setObjectName("label_10")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.probCrossover = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.probCrossover.setObjectName("probCrossover")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.probCrossover)
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_11.setObjectName("label_11")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.probMutacion = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.probMutacion.setObjectName("probMutacion")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.probMutacion)
        self.label_13 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_13.setObjectName("label_13")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioSIElitismo = QtWidgets.QRadioButton(self.formLayoutWidget_3)
        self.radioSIElitismo.setObjectName("radioSIElitismo")
        self.horizontalLayout.addWidget(self.radioSIElitismo)
        self.radioNOElitismo = QtWidgets.QRadioButton(self.formLayoutWidget_3)
        self.radioNOElitismo.setChecked(True)
        self.radioNOElitismo.setObjectName("radioNOElitismo")
        self.horizontalLayout.addWidget(self.radioNOElitismo)
        self.formLayout_3.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.btnEjecutar = QtWidgets.QPushButton(Dialog)
        self.btnEjecutar.setGeometry(QtCore.QRect(860, 650, 211, 61))
        self.btnEjecutar.setObjectName("btnEjecutar")
        self.btnResetear = QtWidgets.QPushButton(Dialog)
        self.btnResetear.setGeometry(QtCore.QRect(1090, 650, 101, 61))
        self.btnResetear.setObjectName("btnResetear")

        self.imagen1 = QtWidgets.QLabel(Dialog)
        self.imagen1.setGeometry(QtCore.QRect(50, 310, 591, 321))
        self.imagen1.setObjectName("imagen1")
        self.imagen1.setScaledContents(True)
        # self.imagen1.sizePolicy(QtWidgets.QSizePolicy.Fixed)

        self.imagen2 = QtWidgets.QLabel(Dialog)
        self.imagen2.setGeometry(QtCore.QRect(700, 310, 591, 321))
        self.imagen2.setObjectName("imagen2")
        self.imagen1.setScaledContents(True)



        # self.tamPoblacion = QtWidgets.QLineEdit(self.formLayoutWidget)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.tamPoblacion.sizePolicy().hasHeightForWidth())
        # self.tamPoblacion.setSizePolicy(sizePolicy)
        # self.tamPoblacion.setObjectName("tamPoblacion")
        
        # ACA AGREGUE
        self.btnEjecutar.clicked.connect(self.ejecutarAlgoritmo)

        self.retranslateUi(Dialog)
        self.selectCrossover.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox_2.setTitle(_translate("Dialog", "Parametros de la Población"))
        self.label.setText(_translate("Dialog", "    Tamaño de población"))
        self.tamPoblacion.setText(_translate("Dialog", "50"))
        self.label_3.setText(_translate("Dialog", "Tipo de selección"))
        self.label_4.setText(_translate("Dialog", "Tipo de crossover"))
        self.label_12.setText(_translate("Dialog", "Tipo de mutación"))
        self.selectSeleccion.setItemText(0, _translate("Dialog", "Ruleta"))
        self.selectSeleccion.setItemText(1, _translate("Dialog", "Torneo"))
        self.selectCrossover.setItemText(0, _translate("Dialog", "Crossover de 1 Punto por fila"))
        #self.selectCrossover.setItemText(1, _translate("Dialog", "Crossover Nico"))
        self.selectMutacion.setItemText(0, _translate("Dialog", "Invertida"))
        self.groupBox_3.setTitle(_translate("Dialog", "Parámetros del Cromosoma"))
        self.label_5.setText(_translate("Dialog", "Tamaño del cromosoma"))
        self.tamCromosoma.setText(_translate("Dialog", "10"))
        self.label_6.setText(_translate("Dialog", "Cantidad Generadores"))
        self.label_7.setText(_translate("Dialog", "Tamaño de celda"))
        self.cantAerogeneradores.setText(_translate("Dialog", "25"))
        self.tamCelda.setText(_translate("Dialog", "180"))
        self.label_8.setText(_translate("Dialog", "Velocidad del viento"))
        self.velocidadViento.setText(_translate("Dialog", "25"))
        self.label_14.setText(_translate("Dialog", "Coeficiente de rugosidad"))
        self.coefRugosidad.setText(_translate("Dialog", "0.05"))
        self.groupBox_4.setTitle(_translate("Dialog", "Parametros del Algoritmo"))
        self.label_9.setText(_translate("Dialog", "Cantidad de Poblaciones"))
        self.cantPoblaciones.setText(_translate("Dialog", "200"))
        self.label_10.setText(_translate("Dialog", "Probabilidad de crossover"))
        self.probCrossover.setText(_translate("Dialog", "0.9"))
        self.label_11.setText(_translate("Dialog", "Probabilidad de mutación"))
        self.probMutacion.setText(_translate("Dialog", "0.05"))
        self.label_13.setText(_translate("Dialog", "Elitismo"))
        self.radioSIElitismo.setText(_translate("Dialog", "SI"))
        self.radioNOElitismo.setText(_translate("Dialog", "NO"))
        self.btnEjecutar.setText(_translate("Dialog", "Correr Algoritmo Genético"))
        self.btnResetear.setText(_translate("Dialog", "Resetear"))
        
    def ejecutarAlgoritmo(self):
        print('Presiono ejecutar algoritmo')
        generaciones=[]

        CantPoblaciones = [int(self.cantPoblaciones.text())]
        #Parametros del Parque 
        Cromosoma.tCromo = int(self.tamCromosoma.text())
        Cromosoma.CantAerogeneradores=int(self.cantAerogeneradores.text())
        Cromosoma.VelocidadViento= int(self.velocidadViento.text()) #Velocidad del viento
        Cromosoma.TamañoCelda = int(self.tamCromosoma.text()) #Distancia Minima de 4*R, donde R es 45 m
        Cromosoma.CoeficienteRugosidad = float(self.coefRugosidad.text())
        #Parametros de la Poblacion
        Poblacion.tPobla = int(self.tamPoblacion.text()) #Cantidad de cromosomas x Poblacion
        Poblacion.tipoSeleccion=Ruleta()

        # Poblacion.tipoCrossover=CrossOverUnPunto(0.9)
        # Poblacion.tipoMutacion=MutacionInvertida(0.05)

        probCrossover = float(self.probCrossover.text())
        probMutacion = float(self.probMutacion.text())       

        if self.selectSeleccion.currentIndex() == 0:
            Poblacion.tipoSeleccion=Ruleta()
        elif self.selectSeleccion.currentIndex() == 1:
            Poblacion.tipoSeleccion=Torneo()

        if self.selectCrossover.currentIndex() == 0:
            Poblacion.tipoCrossover=CrossOverUnPunto(probCrossover)
        #elif self.selectSeleccion.currentIndex() == 1:
        #    Poblacion.tipoCrossover=CrossOverUnPuntoNico(probCrossover)

        if self.selectMutacion.currentIndex() == 0:
            Poblacion.tipoMutacion=MutacionInvertida(probMutacion)

        if self.radioSIElitismo.isChecked():
            Poblacion.elitismo=True
        else:
            Poblacion.elitismo=False

        for x in CantPoblaciones:
            generacion=Generacion()
            for _ in range(x):        
                generacion.creoPoblacion()
            Poblacion.reseteoIDPoblacion() #Metodo de clase que vuelve el ID a 1
            generaciones.append(generacion)


        #Se crea una archivo XLSX y se elimina la primer pagina
        wb = opyxl.Workbook() 
        wb.remove(wb.active) 
        print("\n")
        for generacion in generaciones:
            rutaImagen1, rutaImagen2 = generacion.datosGeneracion(wb)
            print(f'Ruta 1 : {rutaImagen1} y ruta 2 : {rutaImagen2}')
            pixmapImage1 = QtGui.QPixmap(rutaImagen1).scaled(591, 321, QtCore.Qt.KeepAspectRatio,QtCore.Qt.SmoothTransformation)
            self.imagen1.setPixmap(pixmapImage1) 
            pixmapImage2 = QtGui.QPixmap(rutaImagen2).scaled(591, 321, QtCore.Qt.KeepAspectRatio,QtCore.Qt.SmoothTransformation)
            self.imagen2.setPixmap(pixmapImage2) 
            print("\n")