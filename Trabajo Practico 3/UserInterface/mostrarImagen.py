# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Nombre:       mostrarImagen.py
# Autor:        Miguel Andres Garcia Niño
# Creado:       23 de Abril 2018
# Modificado:   23 de Abril 2018
# Copyright:    (c) 2018 by Miguel Andres Garcia Niño, 2018
# License:      Apache License 2.0
# ----------------------------------------------------------------------------

__versión__ = "1.0"

"""
El módulo *mostrarImagen* permite seleccionar una imagen, mostrarla en un QLabel y eliminarla
"""

from os import getcwd

from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QPushButton, QFileDialog


# ===================== CLASE QLabelClickable ======================

class QLabelClickable(QLabel):
    clicked = pyqtSignal()
    
    def __init__(self, parent=None):
        super(QLabelClickable, self).__init__(parent)

    def mousePressEvent(self, event):
        self.clicked.emit()


# ====================== CLASE mostrarImagen =======================

class mostrarImagen(QDialog):
    def __init__(self, parent=None):
        super(mostrarImagen, self).__init__(parent)
        
        self.setWindowTitle("Mostrar imagen por: ANDRES NIÑO")
        self.setWindowIcon(QIcon("icono.png"))
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)
        self.setFixedSize(1200, 900)

        self.initUI()

    def initUI(self):

      # ==================== WIDGET QLABEL =======================
        
        self.labelImagen = QLabelClickable(self)
        self.labelImagen.setGeometry(500, 8, 365, 634)
        self.labelImagen.setToolTip("Imagen")
        self.labelImagen.setCursor(Qt.PointingHandCursor)

        self.labelImagen.setStyleSheet("QLabel {background-color: white; border: 1px solid "
                                       "#01DFD7; border-radius: 5px;}")
        
        self.labelImagen.setAlignment(Qt.AlignCenter)
        # TODO Clase QPixMap para poder escribir un punto sobre la imagen
        pixmapImagen = QPixmap('./provincias.png').scaled(365, 634, Qt.KeepAspectRatio,
                                                  Qt.SmoothTransformation)

        # Mostrar imagen
        self.labelImagen.setPixmap(pixmapImagen)

      # ================= WIDGETS QPUSHBUTTON ====================

        buttonSeleccionar = QPushButton("Seleccionar", self)
        buttonSeleccionar.setToolTip("Seleccionar imagen")
        buttonSeleccionar.setCursor(Qt.PointingHandCursor)
        buttonSeleccionar.setGeometry(143, 15, 120, 25)

        buttonEliminar = QPushButton("Eliminar", self)
        buttonEliminar.setToolTip("Eliminar imagen")
        buttonEliminar.setCursor(Qt.PointingHandCursor)
        buttonEliminar.setGeometry(143, 45, 120, 25)

      # ===================== EVENTO QLABEL ======================

      # Llamar función al hacer clic sobre el label
        self.labelImagen.clicked.connect(self.seleccionarImagen)

      # ================== EVENTOS QPUSHBUTTON ===================

        buttonSeleccionar.clicked.connect(self.seleccionarImagen)
        buttonEliminar.clicked.connect(lambda: self.labelImagen.clear())
        
        # creating a label widget
        # by default label will display at top left corner
        self.criculo1 = QLabel('  1  ', self)
        # moving position
        self.criculo1.move(600, 250)
        # making label square in size
        self.criculo1.resize(40, 40)
        # setting up border and radius
        self.criculo1.setStyleSheet("border: 2px solid green; border-radius: 20px; color: red; background-color: white")
     

  # ======================= FUNCIONES ============================

    def seleccionarImagen(self):
        imagen, extension = QFileDialog.getOpenFileName(self, "Seleccionar imagen", getcwd(),
                                                        "Archivos de imagen (*.png *.jpg)",
                                                        options=QFileDialog.Options())
          
        if imagen:
            # Adaptar imagen
            pixmapImagen = QPixmap('img2.jpg').scaled(365, 634, Qt.KeepAspectRatio,
                                                  Qt.SmoothTransformation)

            # Mostrar imagen
            self.labelImagen.setPixmap(pixmapImagen)


# ================================================================

if __name__ == '__main__':
    
    import sys
    
    aplicacion = QApplication(sys.argv)
    
    ventana = mostrarImagen()
    ventana.show()
    
    sys.exit(aplicacion.exec_())
