from src.Paciente import cPaciente
from src.Enfermero import cEnfermero

class cSalaEspera:
	def __init__(self, listaPacientes, listaEnfermeros):
		self.pacientes = listaPacientes
		# Los enfermeros y pacientes que esten aqui no pueden estar en ninguno de los consultorios
		# Se asume que el enfermero que esta en la sala de espera es porque esta libre
		self.enfermeros = listaEnfermeros
	
	# Agrega un nuevo paciente al final de la lista
	# Solo la utilizamos para cargar los datos de los pacientes al comienzo del programa
	# ya que no tiene un orden de prioridades establecido
	def ingresaPacienteAlFinal(self, newPaciente: cPaciente):
		cSalaEspera.chequeoSeguro(newPaciente)
		self.pacientes.append(newPaciente)

	# Agrega un nuevo paciente a una lista que ya esta ordenada, respetando el orden ya establecido
	def ingresarPacienteOrdenado(self, newPaciente: cPaciente):
		cSalaEspera.chequeoSeguro(newPaciente)
		self.pacientes = self.insertSorted(self.pacientes, newPaciente)

	def getPacientes(self):
		return self.pacientes
	
	def setPacientes(self, newPacientes):
		self.pacientes = newPacientes


	# Tanto mergeSort() como merge() son metodos DE CLASE
	# y no de objeto, para poder usarse de forma recursiva sin problemas
	# (lo probamos aparte y de no ser asi se rompia siempre)
	def mergeSort(listaPacientes):
		medio = len(listaPacientes) // 2

		if medio < 1:
			return listaPacientes
		
		mitadIzq = listaPacientes[:medio]
		mitadDer = listaPacientes[medio:]
		# Llama recursivamente a merge_sort en ambas mitades.
		mitadIzq = cSalaEspera.mergeSort(mitadIzq)
		mitadDer = cSalaEspera.mergeSort(mitadDer)

		# Combina las dos mitades ordenadas en un solo array ordenado.
		return cSalaEspera.merge(mitadIzq, mitadDer)
	
	def merge(izquierda, derecha):
		resultado = []
		posIzq, posDer = 0, 0

		while posIzq < len(izquierda) and posDer < len(derecha):
			if izquierda[posIzq].getColoracion() > derecha[posDer].getColoracion():
				resultado.append(izquierda[posIzq])
				posIzq += 1
			else:
				resultado.append(derecha[posDer])
				posDer += 1

		resultado.extend(izquierda[posIzq:])
		resultado.extend(derecha[posDer:])

		return resultado
	
	# Ingresa un paciente a una lista ya ordenada segun valores
	def insertSorted(listaPacientes, newPaciente):
		# Usamos búsqueda binaria para encontrar la posición adecuada para insertar el newPaciente
		bajo = 0
		alto = len(listaPacientes) - 1
	
		while bajo <= alto:
			medio = (bajo + alto) // 2
	
			if listaPacientes[medio].getValor() == newPaciente.getValor():
				# Si el newPaciente ya está en la lista, lo insertamos en su posición actual
				listaPacientes.insert(medio, newPaciente)
				return listaPacientes
				
			elif listaPacientes[medio].getValor() > newPaciente.getValor():
				bajo = medio + 1
			else:
				alto = medio - 1

		# Insertamos el newPaciente en la posición adecuada, en caso de que no haya coincidido con lo propuesto en el while
		listaPacientes.insert(bajo, newPaciente)

		return listaPacientes
	

	# Ordena los pacientes ya cargados utilizando mergeSort
	def ordenarPacientes(self):
		self.pacientes = cSalaEspera.mergeSort( self.getPacientes() )


	# Chequea si el paciente tiene seguro medico o es votante de Massa
	# En caso de ser pobre, levanta una exception
	def chequeoSeguro(newPaciente: cPaciente):
		if (newPaciente.getSeguro() != True):
			raise AttributeError("Paciente sin seguro, se lo hecha")