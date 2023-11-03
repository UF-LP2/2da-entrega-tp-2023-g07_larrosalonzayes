from src.Paciente import cPaciente
from src.Enfermero import cEnfermero

class cSalaEspera:
	def __init__(self, listaPacientes, listaEnfermeros):
		self.pacientes = listaPacientes
		# Los enfermeros y pacientes que esten aqui no pueden estar en ninguno de los consultorios
		# Se asume que el enfermero que esta en la sala de espera es porque esta libre
		self.enfermeros = listaEnfermeros
	
	# Agrega un nuevo paciente al final de la lista
	def ingresaPacienteAlFinal(self, newPaciente: cPaciente):
		self.pacientes.append(newPaciente)
	
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
	
	# Ordena los pacientes ya cargados utilizando mergeSort
	def ordenarPacientes(self):
		self.pacientes = cSalaEspera.mergeSort( self.getPacientes() )