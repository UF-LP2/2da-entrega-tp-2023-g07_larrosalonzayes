# Clase que contiene listados de medicos, consultorios y ambulancias
class cHospital:
	def __init__(self, nombre, direccion, salaEspera, listaEnfermeros, listaConsultorios, listaAmbulancias, listaMedicos):
		self.nombre = nombre
		self.direccion = direccion
		self.salaEspera = salaEspera

		self.enfermeros = listaEnfermeros
		self.consultorios = listaConsultorios
		self.ambulancias = listaAmbulancias
		self.medicos = listaMedicos