# Clase Madre de Pacientes y Enfermeros
class cPersona:
	# Inicializacion generica
	def __init__(self, dni, nombre, apellido, mail):
		self.dni = dni
		self.nombre = nombre
		self.apellido = apellido

		# mail esta de mas porque no lo usamos, pero queda bien
		self.mail = mail
		