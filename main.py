import csv
import string

# COSAS PARA HACER #

# - Agregar caso particular de pacientes ingresados por ambulancia

# - Como organizar el tema de los cambios de turnos, medicos y enfermeros y como usar tiempo en python

# - Agregar funciones para la lectura de archivos .csv

# - Desarrollar una interfaz (y consultar si es necesario)

from library.Ambulancia import cAmbulancia
from library.Color import cColor
from library.Consultorio import cConsultorio
from library.Enfermero import cEnfermero
from library.Hospital import cHospital
from library.Medico import cMedico
from library.Paciente import cPaciente
from library.SalaEspera import cSalaEspera

# 1 NOCTURNO = 23:00 a 06:00
# 2 MANIANA = 06:00 a 10:00
# 3 HORAPICO = 10:00 a 16:00
# 4 TARDENOCHE = 16:00 a 23:00

# 5 ROJO
# 4 NARANJA
# 3 AMARILLO
# 2 VERDE 

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


def main() -> None:
	# Inicio del main
	listaPacientes = cargarPacientesCSV("pacientes.csv")
	listaMedicos = cargarMedicosCSV("medicos.csv")
	listaEnfermeros = cargarEnfermerosCSV("enfermeros.csv")

	# Por la poca cantidad de datos, los inicializamos sin la necesidad de un .csv
	cons0 = cConsultorio(0, False)
	cons1 = cConsultorio(1, False)
	cons2 = cConsultorio(2, False)
	cons3 = cConsultorio(3, False)
	cons4 = cConsultorio(4, False)

	listaConsultorios = []
	listaConsultorios.append(cons0)
	listaConsultorios.append(cons2)
	listaConsultorios.append(cons3)
	listaConsultorios.append(cons4)

	# Lista de ambulancias por ahora vacia, ya que no desarrollamos esa parte
	listaAmbulancias = []
	
	# La sala de espera se inicializa con una lista vacia
	salaEspera = cSalaEspera( [] )
	hospital = cHospital("Favaloro", "ABC123", salaEspera, listaEnfermeros, listaConsultorios, listaAmbulancias, listaMedicos)

	# En este metodo
	hospital.cargarPacientesIniciales(listaPacientes)


if __name__ == "__main__":
	main()