from enum import Enum

class Colores(Enum):
	ROJO = 5
	NARANJA = 4
	AMARILLO = 3
	VERDE = 2
	AZUL = 1

class cColor:

	# politraumatismo grave

	# coma, convulsiones, hemorragia digestiva, isquemia

	#Cefalea brusca, Paresia, Hipertensión arterial, vertigo con afectación vegetativa, Síncope, rgencias psiquiátricas

	#Otalgias, Odontalgias, Dolores inespecíficos leves, Traumatismos y Esguinces

	#pacientes que no precisan atención de urgencia

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
	
	def setTiempo(self, newTiempo):
		self.tiempo = newTiempo

	def getTiempo(self):
		return self.tiempo