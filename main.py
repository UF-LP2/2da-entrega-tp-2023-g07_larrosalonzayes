import csv
import string

# COSAS PARA HACER #

# - Agregar caso particular de pacientes ingresados por ambulancia

# - Como organizar el tema de los cambios de turnos, medicos y enfermeros y como usar tiempo en python

# - Agregar funciones para la lectura de archivos .csv

# - Desarrollar una interfaz (y consultar si es necesario)

from library.Ambulancia import cAmbulancia
from library.Color import cColor
from library.Color import Colores
from library.Consultorio import cConsultorio
from library.Enfermero import cEnfermero
from library.Enfermero import Horarios
from library.Hospital import cHospital
from library.Medico import cMedico
from library.Paciente import cPaciente
from library.SalaEspera import cSalaEspera

# dni, nombre, apellido, patologia, edad, seguro

def cargarPacientesCSV():
	listaPacientes = []
	return listaPacientes

# def cargarAuxCSV(listaPacientes, archivo: string):
# 	with open(archivo, mode="r") as file:
# 		# DictReader() se usa para archivos con encabezado
# 		fp = csv.DictReader(file)
# 		for i in fp:
# 			aux = cAux( int( i["id"] ) )
# 			listaPacientes.append(aux)
# 		return listaPacientes
	
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
				auxTurno = Horarios.NOCTURNO

			elif i["turno"] == 2:
				auxTurno = Horarios.MANIANA

			elif i["turno"] == 3:
				auxTurno= Horarios.HORAPICO

			else:
				auxTurno = Horarios.TARDENOCHE

			auxBool = False
			if i["estado"] == "True":
				auxBool = True
			# dni,nombre,apellido,matricula,estado,turno

			auxMed = cMedico(i["dni"], i["nombre"], i["apellido"], i["matricula"], auxBool, auxTurno)

			listaMedicos.append(auxMed)

	return listaMedicos

def cargarEnfermerosCSV():
	listaEnfermeros = []
	return listaEnfermeros


def main() -> None:
	# Inicio del main
	listaPacientes = cargarPacientesCSV()
	listaMedicos = cargarMedicosCSV("medicos.csv")
	listaEnfermeros = cargarEnfermerosCSV()

	# Por la poca cantidad de datos, los inicializamos sin la necesidad de un .csv
	cons0 = cConsultorio(0, False)
	cons1 = cConsultorio(1, False)
	cons2 = cConsultorio(2, False)
	cons3 = cConsultorio(3, False)
	cons4 = cConsultorio(4, False)

	listaConsultorios = []
	listaConsultorios.append(cons0)
	listaConsultorios.append(cons1)
	listaConsultorios.append(cons2)
	listaConsultorios.append(cons3)
	listaConsultorios.append(cons4)

	# Lista de ambulancias por ahora vacia, ya que no desarrollamos esa parte
	listaAmbulancias = []

	salaEspera = cSalaEspera(listaPacientes)
	hospital = cHospital("Favaloro", "ABC123", salaEspera, listaEnfermeros, listaConsultorios, listaAmbulancias, listaMedicos)


if __name__ == "__main__":
	main()