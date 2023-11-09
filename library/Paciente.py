import datetime

from library.Persona import cPersona
from library.Color import cColor

class cPaciente(cPersona):
	def __init__(self, dni, nombre, apellido, patologia, edad, seguro):
		super().__init__(dni, nombre, apellido)
		# La edad esta como dato extra para acomodar por prioridad
		# El seguro es booleano, en caso de no tener se lo deriva al Hospital Mordor (publico, obviamente)

		self.patologia = patologia
		self.edad = edad
		self.seguro = seguro

		# color es de clase cColor, de entrada NULL, porque no tiene nada asignado por el hospital
		self.color = None

		# espera es el atributo que muestra el tiempo esperado por el paciente en la sala de espera
		self.espera = datetime.timedelta(minutes=0)
	
	def setColor(self, nuevoColor: cColor):
		self.color = nuevoColor
	
	# Retorna el puntero del color asignado al paciente
	def getColor(self):
		return self.color
	
	def getEsperaMax(self):
		return self.color.getTiempo()
	
	def setEsperado5Min(self):
		self.espera += datetime.timedelta(minutes=5)

	def getEsperado(self):
		return self.espera

	# Retorna directamente el numero que representa el color del paciente
	def getColoracion(self):
		return self.color.getColoracion()
	
	# retorna si el paciente tiene seguro o no
	def getSeguro(self):
		return self.seguro