from datetime import datetime, time

from tkinter import *
from tkinter import PhotoImage

from library.Consultorio import cConsultorio
from library.Hospital import cHospital
from library.SalaEspera import cSalaEspera

from library.funcionesCSV import cargarMedicosCSV, cargarEnfermerosCSV, cargarPacientesCSV

# 1 NOCTURNO = 23:00 a 06:00
# 2 MANIANA = 06:00 a 10:00
# 3 HORAPICO = 10:00 a 16:00
# 4 TARDENOCHE = 16:00 a 23:00

# 5 ROJO
# 4 NARANJA
# 3 AMARILLO
# 2 VERDE 

# COSAS PARA HACER
# 
# - Intefaz (si o si)
# - Simulación (si o si)
# - Función para los tiempos de espera (si un naranja supera el tiempo de espera maximo, hay que setearle el color a rojo para q lo atiendan) 
# - Asignar a los pacientes de la lista (ya ordenados) el consulorio (si o si)

def main() -> None:
	# Inicio del main
	listaPacientes = cargarPacientesCSV("pacientes.csv")
	listaMedicos = cargarMedicosCSV("medicos.csv")
	listaEnfermeros = cargarEnfermerosCSV("enfermeros.csv")


	# Por la poca cantidad de datos, los inicializamos sin la necesidad de un .csv
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

	# La sala de espera se inicializa con una lista vacia
	salaEspera = cSalaEspera( [] )
	hospital = cHospital("Favaloro", "ABC123", salaEspera, listaEnfermeros, listaConsultorios, listaMedicos)

	# En este metodo se cargan los pacientes iniciales en la sala de espera, se categorizan
	# segun el metodo usado por los enfermeros, y luego se ordenan usando merge-sort
	hospital.cargarPacientesIniciales(listaPacientes)

	hospital.imprimirPacientes()

	hospital.imprimirConsultorios()
	hospital.habilitarConsultorios(datetime.now())
	hospital.imprimirConsultorios()

	hospital.adelantar5Min()

##INTERFAZ

"""ventana = Tk()
ventana.geometry('500x600') # tamanyo en pixeles de la ventana
ventana.config(bg='grey') #asigno fondo blanco a la ventana
ventana.title('tp lp2')
etiqueta= Label(ventana, text='Hospital Favaloro', fg='white', bg='grey', font='Verdana')
etiqueta.place(x=180, y= 10)
#img=PhotoImage(file='logo.png')
#Label=(ventana,Image=imagen)
#lbl=(ventana, image= img)

boton= Button(ventana, text='Mostrar sala de espera', fg='black', font='Verdana')
boton2= Button(ventana, text='Riesgo vital',bg='red', fg='white', font='Verdana')
boton3= Button(ventana, text='Urgencia alta', bg='orange', fg='black',font='Verdana')
boton4= Button(ventana, text='Urgencia Media', bg='yellow', fg='black',font='Verdana')
boton5= Button(ventana, text='Normal', bg='green',fg='white', font='Verdana')
boton6= Button(ventana, text='No urgente', bg='blue', fg='white',font='Verdana')
              
              
#ubicacion de los botones 
boton.place(x=50, y= 70)
boton2.place(x= 50, y= 120 )
boton3.place(x= 50, y= 170 )
boton4.place(x= 50, y= 220 )
boton5.place(x= 50, y= 270 )
boton6.place(x= 50, y= 320 )

ventana.mainloop() # método que mantiene 24/7 activa a la ventana"""


if __name__ == "__main__":
	main()