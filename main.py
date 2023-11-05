import csv

# COSAS PARA HACER #

# - Agregar caso particular de pacientes ingresados por ambulancia

# - Como organizar el tema de los cambios de turnos, medicos y enfermeros y como usar tiempo en python

# - Agregar funciones para la lectura de archivos .csv

# - Desarrollar una interfaz (y consultar si es necesario)

from src.Ambulancia import cAmbulancia
from src.Color import cColor
from src.Color import Colores
from src.Consultorio import cConsultorio
from src.Enfermero import cEnfermero
from src.Hospital import cHospital
from src.Medico import cMedico
from src.Paciente import cPaciente
from src.SalaEspera import cSalaEspera

def cargarPacientesCSV():
	listaPacientes = []
	return listaPacientes

def cargarMedicosCSV():
	listaMedicos = []
	return listaMedicos

def cargarEnfermerosCSV():
	listaEnfermeros = []
	return listaEnfermeros


def main() -> None:
	# Inicio del main
	listaPacientes = cargarPacientesCSV()
	listaMedicos = cargarMedicosCSV()
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