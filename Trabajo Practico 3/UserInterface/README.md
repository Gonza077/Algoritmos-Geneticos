# Libreria PyQT5

Pasos básicos para crear una UI con PyQT

Diseñar la UI desde QtDesigner agregando componentes y previsualizando
Pasar a arachivo .py
? Como manejo los eventos y los datos

Clases base PyQT

QtCore
QtGui
QtWidgets

Componentes QT Designer
QWidget
QFrame
QTabWidget
QStackedWidget
QToolBox

Entorno de inicio
- apt-get install
- Ver como se haría desde WIndows

Crear la UI con QT y pasarla a archivo python

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Libreria PyQT5](#libreria-pyqt5)

<!-- /code_chunk_output -->

- userinterface.ui (Creado con QT Desiger)
- userinterface.py (Archivo con clases y objetos Python)

Crear otro archivo que va a manejar la UI creada antes
- main.py

Por ultimo, asocio mi codigo con este archivo main
- función leer datos desde excel, buscarRuta, buscarRutaMinima, buscarAGenetico