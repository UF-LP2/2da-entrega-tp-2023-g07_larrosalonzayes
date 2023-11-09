# Clase que contiene listados de medicos, consultorios, ambulancias y medicos

import datetime
from library.funcionesTiempo import tiempoActual, tiempoTranscurrido

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
	def verHabilitacion(self, hora):
		if (2300 <= hora and hora < 2359) or (0000 <= hora and hora < 600):
			self.consultorios[0].habilitar(True)
			self.consultorios[1].habilitar(False)
			self.consultorios[2].habilitar(False)
			self.consultorios[3].habilitar(False)
			self.consultorios[4].habilitar(False)

		elif (600 <= hora and hora < 1000):
			self.consultorios[0].habilitar(True)
			self.consultorios[1].habilitar(True)
			self.consultorios[2].habilitar(False)
			self.consultorios[3].habilitar(False)
			self.consultorios[4].habilitar(False)
			
		elif (1000 <= hora and hora < 1600):
			self.consultorios[0].habilitar(True)
			self.consultorios[1].habilitar(True)
			self.consultorios[2].habilitar(True)
			self.consultorios[3].habilitar(True)
			self.consultorios[4].habilitar(True)

		elif (1600 <= hora and hora < 2300):
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
	def imprimir(self):
		self.salaEspera.imprimir()

	def simular(self):
		# Tiempo inicial
		tiempoAhora = tiempoActual()
		# Tiempo Pasado
		tiempoPasado = 0
		while tiempoPasado(tiempoPasado <= 1435):
			for i in self.salaEspera.getPacientes():

			if tiempo == 1435:
				tiempo = 0
				


		# Simula estar en la sala de espera durante 30 segundos (puedes ajustar según lo que necesites)
		tiempoMaxEspera = datetime.timedelta(seconds=30)

		while datetime.now() - tiempo_actual < tiempo_total_espera:
			# Simula esperar 1 segundo antes de sumar 5 minutos
			datetime.time.sleep(1)
	
			# Suma 5 minutos al tiempo actual
			tiempo_actual += datetime.timedelta(minutes=5)