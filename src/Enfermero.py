import src.Persona
import src.Color
from src.Paciente import cPaciente
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

class cEnfermero(src.Persona.cPersona):

	# Usando super(), no es necesario usar el nombre del elemento padre, 
	# sino que automaticamente heredará los metodos y propiedades de la clase padre

	def __init__(self, dni, nombre, apellido, horario, estado):
		super().__init__(dni, nombre, apellido)

		self.horario = horario

		# estado es un bool, si esta ocupado o no
		self.estado = estado
	
	# ROJO = Politraumatismo grave = INMEDIATO
	# NARANJA = Coma, Convulsiones, Hemorragia digestiva, Isquemia = 10 minutos
	# AMARILLO = Cefalea brusca, Paresia, Hipertensión arterial,
	# Vértigo con afectación vegetativa, Síncope, urgencias psiquiátricas = 60 minutos
	# VERDE = otalgias, odontalgias, dolores inespecíficos leves, traumatismos y esguinces = 120 minutos
	# AZUL = pacientes que no precisan atención de urgencia = 240 minutos

	def catalogarPaciente(newPaciente: cPaciente):
		coloracion = 0
		if newPaciente.patologia == "politraumatismo grave":
			coloracion = src.Color.Colores.ROJO

		elif (newPaciente.patologia == "coma" or newPaciente.patologia == "convulsiones" or 
		newPaciente.patologia == "hemmoragia digestiva" or newPaciente.patologia == "isquemia"):
			coloracion = src.Color.Colores.NARANJA

		elif (newPaciente.patologia == "cefalea brusca" or newPaciente.patologia == "paresia" or 
		newPaciente.patologia == "hipertension arterial" or newPaciente.patologia == "vertigo con afectacion vegetativa" or
		newPaciente.patologia == "sincope" or newPaciente.patologia == "urgencias psiquiatricas"):
			coloracion = src.Color.Colores.AMARILLO

		elif (newPaciente.patologia == "otalgias" or newPaciente.patologia == "odontalgias" or 
		newPaciente.patologia == "dolores inespecíficos leves" or newPaciente.patologia == "traumatismos" or
		newPaciente.patologia == "esguinces"):
			coloracion = src.Color.Colores.VERDE

		else:
			coloracion = src.Color.Colores.AZUL
		

		newColor = src.Color.cColor(coloracion)
		newPaciente.setColor(newColor)
