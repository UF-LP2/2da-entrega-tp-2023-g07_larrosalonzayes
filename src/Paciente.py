from src.Persona import cPersona
from src.Color import cColor

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
	
	def setColor(self, nuevoColor: cColor):
		self.color = nuevoColor
	
	def getColor(self):
		return self.color

	def getColoracion(self):
		return self.color.getColoracion()
	
	def getSeguro(self):
		return self.seguro