class cConsultorio:
	def __init__(self, N, habilitado):
		# N es el numero de consultorio, del 1 al 5
		self.N = N

		# Habilitado es si el consultorio SE PUEDE USAR o no, depende del horario
		self.habilitado = habilitado

		# Estado es un bool; siendo usado o no
		# Por default, estaria cerrado, incluso si se habilita
		self.estado = False

	def habilitar(self, accion):
		if accion == True:
			self.habilitado = accion
		elif accion == False:
			self.habilitado = accion