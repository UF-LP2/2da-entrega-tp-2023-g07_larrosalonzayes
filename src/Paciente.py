import Persona


class cPaciente(Persona.cPersona):
	def __init__(self, dni, nombre, apellido, patologia, edad, seguro, color):
		super().__init__(dni, nombre, apellido)
		# La edad esta como dato extra para acomodar por prioridad
		# El seguro es booleano, en caso de no tener se lo deriva al Hospital Mordor (publico, obviamente)

		self.patologia = patologia
		self.edad = edad
		self.seguro = seguro

		# color es de clase cColor
		self.color = color