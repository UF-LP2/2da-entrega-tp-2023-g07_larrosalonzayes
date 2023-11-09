import pytest

from SalaEspera import cSalaEspera
from Paciente import cPaciente
from Enfermero import cEnfermero

#///////////////////////////////////////////////// TESTEOS PARA MERGE SORT //////////////////////////////////////////////////////

def test_mergeSort():
       # Prueba para una lista desordenada de pacientes
       
        Paciente1= cPaciente(1234, "Paciente", "1", "politraumatismo grave", 21, True)
        Paciente2= cPaciente (1934, "Paciente", "2", "cefalea brusca", 66, True)
        Paciente3= cPaciente(1834, "Paciente", "3", "hemorragia digestiva", 23, True) 

        Paciente1_mod= cEnfermero.catalogarPaciente(Paciente1)
        Paciente2_mod= cEnfermero.catalogarPaciente(Paciente2)
        Paciente3_mod= cEnfermero.catalogarPaciente(Paciente3) 

        Lista_pacientes= [Paciente1_mod,Paciente2_mod,Paciente3_mod] ## le paso pacientes con colores asignados 
       
        lista_ordenada = cSalaEspera.mergeSort(Lista_pacientes)
        
        # Verifica que la lista esté ordenada correctamente
        assert(lista_ordenada[0].dni, "DNI1")
        assert(lista_ordenada[1].dni, "DNI2")
        assert(lista_ordenada[2].dni, "DNI3")

def test2_mergeSort():
       # Prueba para una lista desordenada de otro set de pacientes
      
        Paciente1= cPaciente(1234, "Paciente", "1", "dolores inespecíficos leves", 56, True)
        Paciente2= cPaciente (1934, "Paciente", "2", "cefalea brusca", 42, True)
        Paciente3= cPaciente(1834, "Paciente", "3", "isquemia", 16, True) 

        Paciente1_mod= cEnfermero.catalogarPaciente(Paciente1)
        Paciente2_mod= cEnfermero.catalogarPaciente(Paciente2)
        Paciente3_mod= cEnfermero.catalogarPaciente(Paciente3) 

        Lista_pacientes= [Paciente1_mod,Paciente2_mod,Paciente3_mod] ## le paso pacientes con colores asignados 
       
        lista_ordenada = cSalaEspera.mergeSort(Lista_pacientes)
        
        # Verifica que la lista esté ordenada correctamente
        assert(lista_ordenada[0].dni, "DNI1")
        assert(lista_ordenada[1].dni, "DNI2")
        assert(lista_ordenada[2].dni, "DNI3")

#//////////////////////////////////////////////// TESTEOS PARA INSERTION SORT ////////////////////////////////////////////////////

def test_insertar_al_principio():
        

        Paciente1= cPaciente(1234, "Paciente", "1", "hemorragia digestiva"  , 21, True)
        Paciente2= cPaciente(1934, "Paciente", "2", "hipertension arterial" , 66, True)
        Paciente3= cPaciente(1834, "Paciente", "3", "esguinces"             , 23, True) 
        Paciente4= cPaciente(1854, "Paciente", "4", "politraumatismo grave" , 23, True)

        Paciente1_mod= cEnfermero.catalogarPaciente(Paciente1)
        Paciente2_mod= cEnfermero.catalogarPaciente(Paciente2)
        Paciente3_mod= cEnfermero.catalogarPaciente(Paciente3) 


        lista = [Paciente1_mod, Paciente2_mod, Paciente3_mod]
        new_paciente = cEnfermero.catalogarPaciente(Paciente4) 

        expected_result = [new_paciente, Paciente1_mod, Paciente2_mod, Paciente3_mod]
        assert(cSalaEspera.insertSorted(lista, new_paciente), expected_result) 

def test_insertar_al_medio():
        

        Paciente1= cPaciente(1234, "Paciente", "1", "hemorragia digestiva"  , 21, True)
        Paciente2= cPaciente(1934, "Paciente", "2", "hipertension arterial" , 66, True)
        Paciente3= cPaciente(1834, "Paciente", "3", "esguinces"             , 23, True) 
        Paciente4= cPaciente(1854, "Paciente", "4", "politraumatismo grave" , 23, True) 
        Paciente5= cPaciente( 3456, "Paciente", "5", "dolor de panza"       , 41, True)

        Paciente1_mod= cEnfermero.catalogarPaciente(Paciente1)
        Paciente2_mod= cEnfermero.catalogarPaciente(Paciente2)
        Paciente3_mod= cEnfermero.catalogarPaciente(Paciente3) 
        Paciente4_mod= cEnfermero.catalogarPaciente(Paciente4)
        Paciente5_mod=cEnfermero.catalogarPaciente(Paciente5)



        lista = [Paciente4_mod, Paciente1_mod, Paciente3_mod, Paciente5_mod]


        expected_result = [Paciente4_mod, Paciente1_mod, Paciente2_mod, Paciente3_mod, Paciente5_mod]
        assert(cSalaEspera.insertSorted(lista, Paciente2_mod), expected_result)
        