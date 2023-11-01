class cSalaEspera:
	def __init__(self, listaPacientes, listaEnfermeros):
		self.pacientes = listaPacientes
		# Los enfermeros y pacientes que esten aqui no pueden estar en ninguno de los consultorios
		# Se asume que el enfermero que esta en la sala de espera es porque esta libre
		self.enfermeros = listaEnfermeros