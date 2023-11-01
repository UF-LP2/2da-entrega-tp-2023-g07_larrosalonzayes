class cConsultorio:
	def __init__(self, N, estado):
		# N es el numero de consultorio, del 1 al 5
		self.N = N
		# estado es un bool; siendo usado o no
		self.estado = estado
	
	def habilitar(horaActual):
		# El metodo habiliar recibe la hora del dia, y en base a eso y el numero de consultorio, se hablita o deshabilita
		print()