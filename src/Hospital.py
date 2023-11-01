# Clase que contiene listados de medicos, consultorios, ambulancias y medicos
import src.Paciente
import src.Medico
import src.Enfermero
import src.Ambulancia
import src.Consultorio
import src.SalaEspera

class cHospital:
	def __init__(self, nombre, direccion, salaEspera: src.SalaEspera.cSalaEspera, listaEnfermeros, listaConsultorios, listaAmbulancias, listaMedicos):
		
		self.nombre = nombre
		self.direccion = direccion
		self.salaEspera = salaEspera

		self.enfermeros = listaEnfermeros
		self.consultorios = listaConsultorios
		self.ambulancias = listaAmbulancias
		self.medicos = listaMedicos
