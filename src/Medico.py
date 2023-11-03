from src.Persona import cPersona

class cMedico(cPersona):
	# Estado es si se encuentra ocupado o no
	def __init__(self, dni, nombre, apellido, matricula, estado):
		self.dni = dni
		self.nombre = nombre
		self.apellido = apellido
		self.matricula = matricula
		self.estado = estado