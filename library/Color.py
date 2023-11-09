class cColor:

	def __init__(self, coloracion):
		# coloracion es del enum "Colores"
		self.coloracion = coloracion
		
		# Se asigna un tiempo de espera en base a la coloracion asignada
		# Como no hay switch() case: en python, usamos varios eli()f
		if (coloracion == 5):
			self.tiempo = 0
		elif (coloracion == 4):
			self.tiempo = 10
		elif (coloracion == 3):
			self.tiempo = 60
		elif (coloracion == 2):
			self.tiempo = 120
		elif (coloracion == 1):
			self.tiempo = 240
		else:
			# En caso de no ser un color valido, se le asigna un tiempo imposible
			# Esto es para FUTURAS EXCEPCIONES
			self.tiempo = -1
	
	def setTiempo(self, newTiempo):
		self.tiempo = newTiempo

	def getTiempo(self):
		return self.tiempo
	
	def getColoracion(self):
		return self.coloracion