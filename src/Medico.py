from src.Persona import cPersona
from src.Enfermero import Horarios

class cMedico(cPersona):
	# Estado es si se encuentra ocupado o no
	def __init__(self, dni, nombre, apellido, matricula, estado, turno):
		super().__init__(dni, nombre, apellido)
		self.matricula = matricula
		self.estado = estado

		self.turno = turno