import datetime

class cColor:

	def __init__(self, coloracion):
		# coloracion es del enum "Colores"
		self.coloracion = coloracion
		
		# Se asigna un tiempo de espera en base a la coloracion asignada
		# Como no hay switch() case: en python, usamos varios elif

		# El self de color sera una variable de referencia
		# que se va a usar en comparacion al tiempo que el paciente este esperando

		if (coloracion == 5):
			espera = datetime.timedelta(minutes=0)
			self.tiempo = espera
		elif (coloracion == 4):
			espera = datetime.timedelta(minutes=10)
			self.tiempo = espera
		elif (coloracion == 3):
			espera = datetime.timedelta(minutes=60)
			self.tiempo = espera
		elif (coloracion == 2):
			espera = datetime.timedelta(minutes=120)
			self.tiempo = espera
		elif (coloracion == 1):
			espera = datetime.timedelta(minutes=240)
			self.tiempo = espera
		else:
			# En caso de ser un color invalido, se le asigna un tiempo imposible
			# Esto es para FUTURAS EXCEPCIONES
			self.tiempo = -1
	
	def setTiempo(self, newTiempo):
		self.tiempo = newTiempo

	def getTiempo(self):
		return self.tiempo
	
	def getColoracion(self):
		return self.coloracion