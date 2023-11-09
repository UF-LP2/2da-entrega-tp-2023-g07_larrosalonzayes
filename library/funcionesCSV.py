import csv
import string

from library.Paciente import cPaciente
from library.Medico import cMedico
from library.Enfermero import cEnfermero

def cargarPacientesCSV(archivo):
	listaPacientes = []

	with open(archivo, mode="r") as file:
		fp = csv.DictReader(file)
		for i in fp:
			auxBool = False
			if i["seguro"] == "true":
				auxBool = True
			# dni, nombre, apellido, patologia, edad, seguro
			auxPac = cPaciente(i["dni"], i["nombre"], i["apellido"], i["patologia"], int(i["edad"]), auxBool)

			listaPacientes.append(auxPac)

	return listaPacientes

	
def cargarMedicosCSV(archivo: string):
	listaMedicos = []
	
	with open(archivo, mode="r") as file:
		fp = csv.DictReader(file)
		# NOCTURNO = 1
		# MANIANA = 2
		# HORAPICO = 3
		# TARDENOCHE = 4
		for i in fp:
			auxTurno = 0
			if i["turno"] == 1:
				auxTurno = 1

			elif i["turno"] == 2:
				auxTurno = 2

			elif i["turno"] == 3:
				auxTurno= 3

			else:
				auxTurno = 4

			auxBool = False
			if i["estado"] == "True":
				auxBool = True

			# dni,nombre,apellido,matricula,estado,turno
			auxMed = cMedico(i["dni"], i["nombre"], i["apellido"], i["matricula"], auxBool, auxTurno)

			listaMedicos.append(auxMed)

	return listaMedicos


def cargarEnfermerosCSV(archivo):
	listaEnfermeros = []

	# dni, nombre, apellido, horario, estado
	with open(archivo, mode="r") as file:
		fp = csv.DictReader(file)
		for i in fp:

			auxTurno = 0
			if i["horario"] == 1:
				auxTurno = 1

			elif i["horario"] == 2:
				auxTurno = 2

			elif i["horario"] == 3:
				auxTurno= 3

			else:
				auxTurno = 4

			auxBool = False
			if i["estado"] == "true":
				auxBool = True

			auxEnf = cEnfermero(i["dni"], i["nombre"], i["apellido"], auxTurno, auxBool)
			listaEnfermeros.append(auxEnf)

	return listaEnfermeros