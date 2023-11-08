class cConsultorio:
	def __init__(self, N, habilitado):
		# N es el numero de consultorio, del 1 al 5
		self.N = N

		# estado es un bool; siendo usado o no
		# Por default, estaria cerrado, incluso si se habilita
		self.estado = False

		# habilitado es si el consultorio SE PUEDE USAR o no, depende del horario
		self.habilitado = habilitado

	def abrirCerrar(self, accion):
		if accion == True:
			self.estado = accion
		elif accion == False:
			self.estado = accion

	def habilitar(self, accion):
		if accion == True:
			self.habilitado = accion
		elif accion == False:
			self.habilitado = accion