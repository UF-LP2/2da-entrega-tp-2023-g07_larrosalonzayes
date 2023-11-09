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
			self.tiempo = datetime.timedelta(minutes=0)

		elif (coloracion == 4):
			self.tiempo = datetime.timedelta(minutes=10)

		elif (coloracion == 3):
			self.tiempo = datetime.timedelta(minutes=60)

		elif (coloracion == 2):
			self.tiempo = datetime.timedelta(minutes=120)

		elif (coloracion == 1):
			self.tiempo = datetime.timedelta(minutes=240)
			
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