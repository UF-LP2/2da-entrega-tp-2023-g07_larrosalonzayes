# Clase que contiene listados de medicos, consultorios, ambulancias y medicos
from src.Paciente import cPaciente
from src.Medico import cMedico
from src.Enfermero import cEnfermero
from src.Ambulancia import cAmbulancia
from src.Consultorio import cConsultorio
from src.SalaEspera import cSalaEspera

class cHospital:
	def __init__(self, nombre, direccion, salaEspera: cSalaEspera, listaEnfermeros, listaConsultorios, listaAmbulancias, listaMedicos):
		
		self.nombre = nombre
		self.direccion = direccion
		self.salaEspera = salaEspera

		self.enfermeros = listaEnfermeros
		self.consultorios = listaConsultorios
		self.ambulancias = listaAmbulancias
		self.medicos = listaMedicos

	# def triage(self):