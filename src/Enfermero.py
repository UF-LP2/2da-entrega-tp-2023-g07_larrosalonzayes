import Persona
from enum import Enum

class Horarios(Enum):
	# NOCTURNO = 23:00 a 06:00
	# MANIANA = 06:00 a 10:00
	# HORAPICO = 10:00 a 16:00
	# TARDENOCHE = 16:00 a 23:00
	NOCTURNO = 1
	MANIANA = 2
	HORAPICO = 3
	TARDENOCHE = 4

class cEnfermero(Persona.cPersona):

	# Usando super(), no es necesario usar el nombre del elemento padre, 
	# sino que automaticamente heredará los metodos y propiedades de la clase padre

	def __init__(self, dni, nombre, apellido, horario, estado):
		super().__init__(dni, nombre, apellido)

		self.horario = horario

		# estado es un bool; ocupado o no
		self.estado = estado