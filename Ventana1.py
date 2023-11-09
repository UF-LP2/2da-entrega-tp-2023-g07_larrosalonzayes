from tkinter import *
from tkinter import PhotoImage
from tkinter import ttk 
#from PIL import Image, ImageTk
from library.Enfermero import cEnfermero
from library.Consultorio import cConsultorio
from library.Medico import cMedico
from library.Hospital import cHospital
from library.SalaEspera import cSalaEspera
from library.funcionesCSV import cargarMedicosCSV, cargarEnfermerosCSV, cargarPacientesCSV
import tkinter as tk
from tkinter import Label, Button
from tkinter import Canvas 

listaPacientes = cargarPacientesCSV("pacientes.csv")
listaMedicos = cargarMedicosCSV("medicos.csv")
listaEnfermeros = cargarEnfermerosCSV("enfermeros.csv") 

cons0 = cConsultorio(0, False)
cons1 = cConsultorio(1, False)
cons2 = cConsultorio(2, False)
cons3 = cConsultorio(3, False)
cons4 = cConsultorio(4, False)

listaConsultorios = []
listaConsultorios.append(cons0)
listaConsultorios.append(cons1)
listaConsultorios.append(cons2)
listaConsultorios.append(cons3)
listaConsultorios.append(cons4) 

salaEspera = cSalaEspera( [] )

hospital = cHospital("Favaloro", "ABC123", salaEspera, listaEnfermeros, listaConsultorios, listaMedicos)
hospital.cargarPacientesIniciales(listaPacientes)


ventana = Tk()
ventana.geometry('800x600') # tamanyo en pixeles de la ventana
ventana.config(bg='dark slate gray') #asigno fondo blanco a la ventana
ventana.title('tp lp2')
etiqueta= Label(ventana, text='Hospital Favaloro', fg='white', bg='dark slate grey', font='Verdana')
etiqueta.place(x=180, y= 10)

#imagen 

image_image_1 = PhotoImage('imginicio.gif')
Label(ventana, image= image_image_1).place(x=50, y=500)
#image_1 = Canvas.create_image(125.0, 450.0,) 
#image= image_image_1





boton= Button(ventana, text='Mostrar sala de espera', fg='black', font='Verdana',command=hospital.imprimirPacientes())
boton.pack()
boton2= Button(ventana, text='Riesgo vital',bg='bisque4', fg='black', font='Verdana')
boton3= Button(ventana, text='Urgencia alta', bg='bisque4', fg='black',font='Verdana')
boton4= Button(ventana, text='Urgencia Media', bg='bisque4', fg='black',font='Verdana')
boton5= Button(ventana, text='Normal', bg='bisque4',fg='black', font='Verdana')
boton6= Button(ventana, text='No urgente', bg='bisque4', fg='black',font='Verdana')
              
              
#ubicacion de los botones 
boton.place(x=50, y= 70)
boton2.place(x= 50, y= 120 )
boton3.place(x= 50, y= 170 )
boton4.place(x= 50, y= 220 )
boton5.place(x= 50, y= 270 )
boton6.place(x= 50, y= 320 )

ventana.mainloop() # método que mantiene 24/7 activa a la ventana"""