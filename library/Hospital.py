# Clase que contiene listados de medicos, consultorios, ambulancias y medicos

from datetime import time

from library.SalaEspera import cSalaEspera
from library.Enfermero import cEnfermero

class cHospital:
	def __init__(self, nombre, direccion, salaEspera: cSalaEspera, listaEnfermeros, listaConsultorios, listaMedicos):
		
		self.nombre = nombre
		self.direccion = direccion
		self.salaEspera = salaEspera


		self.enfermeros = listaEnfermeros
		self.consultorios = listaConsultorios
		self.medicos = listaMedicos

	# Hora es un numero entero entre 0 y 2359
	# (por temas de simulacion tratamos la hora del dia asi)
	# Sabemos que se harian horas imposibles como las 14:70, pero no es nada del otro mundo
	# Iriamos sumando de a 5 minutos por simplicidad

	# NOCTURNO = 23:00 a 06:00 - 1
	# MANIANA = 06:00 a 10:00 - 2
	# HORAPICO = 10:00 a 16:00 - 5
	# TARDENOCHE = 16:00 a 23:00 - 3

	# hora es la hora a la cual se invoca este metodo
	# (en relacion al tiempo del programa, es decir, 5 minutos cada ciclo)
	def habilitarConsultorios(self, hora):
		ahora = hora.time()
		if (time(23,0) <= ahora and ahora <= time(23,59)) or (time(0,0) <= ahora and ahora < time(6,00)):
			self.consultorios[0].habilitar(True)
			self.consultorios[1].habilitar(False)
			self.consultorios[2].habilitar(False)
			self.consultorios[3].habilitar(False)
			self.consultorios[4].habilitar(False)

		elif (time(6,0) <= ahora and ahora < time(10,0)):
			self.consultorios[0].habilitar(True)
			self.consultorios[1].habilitar(True)
			self.consultorios[2].habilitar(False)
			self.consultorios[3].habilitar(False)
			self.consultorios[4].habilitar(False)
			
		elif (time(10,0) <= ahora and ahora < time(16,0)):
			self.consultorios[0].habilitar(True)
			self.consultorios[1].habilitar(True)
			self.consultorios[2].habilitar(True)
			self.consultorios[3].habilitar(True)
			self.consultorios[4].habilitar(True)

		elif (time(16,0) <= ahora and ahora < time(23,0)):
			self.consultorios[0].habilitar(True)
			self.consultorios[1].habilitar(True)
			self.consultorios[2].habilitar(True)
			self.consultorios[3].habilitar(False)
			self.consultorios[4].habilitar(False)



	# Elige un enfermero dependiendo de la hora para que catalogue a todos los pacientes
	# que no hayan sido previamente diagnosticados (que su color sea NONE)

	# Son 11 enfermeros
	# NOCTURNO = 23:00 a 06:00 - Enf0
	# MANIANA = 06:00 a 10:00 - Enf1 y Enf2
	# HORAPICO = 10:00 a 16:00 - Enf3, Enf4, Enf5, Enf6 y Enf7
	# TARDENOCHE = 16:00 a 23:00 - Enf8, Enf9 y Enf10
	def catalogarPacientes(self, hora):
		if (2300 <= hora and hora < 2359) or (0000 <= hora and hora < 600):
			self.enfermeros[0].catalogarPacientes( self.salaEspera.getPacientes() )

		elif (600 <= hora and hora < 1000):
			self.enfermeros[1].catalogarPacientes( self.salaEspera.getPacientes() )
			
		elif (1000 <= hora and hora < 1600):
			self.enfermeros[3].catalogarPacientes( self.salaEspera.getPacientes() )

		elif (1600 <= hora and hora < 2300):
			self.enfermeros[8].catalogarPacientes( self.salaEspera.getPacientes() )

	
	# Se cargan todos los pacientes del inicio del programa al hospital
	def cargarPacientesIniciales(self, listaEnfermos):
		self.salaEspera.setPacientes( cEnfermero.catalogarPacientes(listaEnfermos) )
		self.salaEspera.ordenarPacientes()


	# Imprime la lista de pacientes de la sala de espera
	def imprimirPacientes(self):
		self.salaEspera.imprimir() 
		


	def imprimirConsultorios(self):
		for i in self.consultorios:
			print("N%d" % i.N , i.habilitado)
		print("\n")


	# Por motivos de simulacion, habra un boton que invoque 
	# este metodo adelantara los tiempos esperados de todos
	# los pacientes QUE NO ESTEN ATENDIDOS unos 5 minutos
	def adelantar5Min(self):
		for i in self.salaEspera.getPacientes():
			i.setEsperado5Min()


	def atenderRojos(self):
		for i in self.consultorios:
			print(i.estado)

		print("\n")
		
		for i in self.salaEspera.getPacientes():
			if i.getColoracion() == 5:
				for j in self.consultorios:
					if j.estado == False and j.habilitado:
						j.estado = True

		for i in self.consultorios:
			print(i.estado)

	def getListaPacientes(self):
		return self.salaEspera
	
	def getMedicosString(self):
		lista = []
		aux = ""
		for i in self.medicos:
			aux = i.dni + " " + i.nombre + " " + i.apellido + " " + i.matricula
			lista.append(aux)
		return lista