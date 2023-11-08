from library.Paciente import cPaciente
from library.Persona import cPersona
from library.Color import cColor

class cEnfermero(cPersona):

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
			coloracion = 5

		elif (newPaciente.patologia == "coma" or newPaciente.patologia == "convulsiones" or 
		newPaciente.patologia == "hemmoragia digestiva" or newPaciente.patologia == "isquemia"):
			coloracion = 4

		elif (newPaciente.patologia == "cefalea brusca" or newPaciente.patologia == "paresia" or 
		newPaciente.patologia == "hipertension arterial" or newPaciente.patologia == "vertigo con afectacion vegetativa" or
		newPaciente.patologia == "sincope" or newPaciente.patologia == "urgencias psiquiatricas"):
			coloracion = 3

		elif (newPaciente.patologia == "otalgias" or newPaciente.patologia == "odontalgias" or 
		newPaciente.patologia == "dolores inespecíficos leves" or newPaciente.patologia == "traumatismos" or
		newPaciente.patologia == "esguinces"):
			coloracion = 2

		else:
			coloracion = 1
		

		newColor = cColor(coloracion)
		newPaciente.setColor(newColor)
		return newPaciente

	# Si el paciente del listado que se le pasa no esta catalogado, se lo analiza
	def catalogarPacientes(listaPacientes):
		for i in listaPacientes:
			if i.getColor() == None:
				i = cEnfermero.catalogarPaciente(i)
		
		return listaPacientes
	