import PyQt5
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore, QtWidgets

class DibujarLineaMouseDialog(object):
    
    def setupUi(self, DibujarLineaMouseDialog):
        DibujarLineaMouseDialog.setObjectName('DibujarLineaMouseDialog')
        DibujarLineaMouseDialog.resize(512, 240)
        self.lbl_mensaje = QtWidgets.QLabel(DibujarLineaMouseDialog)
        self.lbl_mensaje.setGeometry(QtCore.QRect(22, 16, 451, 16))
        self.lbl_mensaje.setObjectName('lbl_mensaje')

        self.retranslateUi(DibujarLineaMouseDialog)
        QtCore.QMetaObject.connectSlotsByName(DibujarLineaMouseDialog)

    def retranslateUi(self, DibujarLineaMouseDialog):
        _translate = QtCore.QCoreApplication.translate
        DibujarLineaMouseDialog.setWindowTitle(_translate('DibujarLineaMouseDialog', 'Gráficos: Dibujar una Línea'))
        self.lbl_mensaje.setText(_translate('DibujarLineaMouseDialog', 'Click en un punto específico y arrrastre el mouse hasta dende desea hacer la linea'))


