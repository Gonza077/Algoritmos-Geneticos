from main import *
from tkinter import ttk
from tkinter import *

def creoVentanAuxiliar():
    ventanaAuxiliar=Toplevel()
    ventanaAuxiliar.geometry("500x250")
    return ventanaAuxiliar

#------------- Opciones -------------
def Opcion1():
    ventanaAuxiliar=creoVentanAuxiliar()
    ventanaAuxiliar.title("Busqueda desde una provincia")
    #ComboBox
    comboBox=ttk.Combobox(ventanaAuxiliar, values=nombreCiudades(), state="readonly")
    comboBox.grid(padx = 10, pady = 10, row = 0 , column=1 )
    #Boton

def Opcion2():
    ventanaAuxiliar=creoVentanAuxiliar()
    ventanaAuxiliar.title("Recorrido mas corto")
    #Label

def Opcion3():
    ventanaAuxiliar=creoVentanAuxiliar()
    ventanaAuxiliar.title("Busqueda por medio de un AG")

#------------- Opciones -------------

#------------- Ventana principal -------------
ventana = Tk()
ventana.resizable(False, False)
ventana.geometry("500x250")
ventana.eval('tk::PlaceWindow . center')
ventana.title("Trabajo Practico N°3")
label=Label(ventana,text="Menu principal")
label.pack(anchor=CENTER, pady = 10)

#Boton 1
botonOpc1=Button(ventana, text="Busqueda desde una provincia", width=25,command=Opcion1)
botonOpc1.pack(anchor=CENTER, pady = 10)
#Boton 2
botonOpc2=Button(ventana, text="Recorrido mas corto", width=25,command=Opcion2)
botonOpc2.pack(anchor=CENTER, pady = 10)
#Boton 3
botonOpc3=Button(ventana, text="Busqueda por medio de un AG", width=25,command=Opcion3)
botonOpc3.pack(anchor=CENTER, pady = 10)

ventana.mainloop()

#------------- Ventana principal -------------