from enum import Enum

class Colores(Enum):
	ROJO = 5
	NARANJA = 4
	AMARILLO = 3
	VERDE = 2
	AZUL = 1

class cColor:

	# ROJO = Politraumatismo grave = INMEDIATO

	# NARANJA = Coma, Convulsiones, Hemorragia digestiva, Isquemia = 10 minutos

	# AMARILLO = Cefalea brusca, Paresia, Hipertensión arterial,
	# Vértigo con afectación vegetativa, Síncope, rgencias psiquiátricas = 60 minutos

	# VERDE = Otalgias, Odontalgias, Dolores inespecíficos leves, Traumatismos y Esguinces = 120 minutos

	# AZUL = pacientes que no precisan atención de urgencia = 240 minutos

	def __init__(self, coloracion):
		# coloracion es del enum "Colores"
		self.coloracion = coloracion
		
		# Se asigna un tiempo de espera en base a la coloracion asignada
		# Como no hay switch() case: en python, usamos varios eli()f
		if (coloracion == Colores.ROJO):
			self.tiempo = 0
		elif (coloracion == Colores.NARANJA):
			self.tiempo = 10
		elif (coloracion == Colores.AMARILLO):
			self.tiempo = 60
		elif (coloracion == Colores.VERDE):
			self.tiempo = 120
		elif (coloracion == Colores.AZUL):
			self.tiempo = 240
		else:
			# En caso de no ser un color valido, se le asigna un tiempo imposible
			# Esto es para FUTURAS EXCEPCIONES
			self.tiempo = -1
