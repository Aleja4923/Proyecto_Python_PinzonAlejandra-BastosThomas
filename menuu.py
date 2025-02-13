from desing.userCordinadora import *
from desing.ModuloRe import *
from desing.userTrainer import *

def opcion_cordinadora():
    print ("Bienvenido seleccione que desea hacer")
    print ("1. Agregar estudiante")
    print ("2. Modificar datos estudiante")
    print ("3. Ver estudiantes")
    print ("4. Registrar notas")
    print ("5. Crear rutas de entrenamiento")
    print ("6. Modulo matriculas")
    print ("7. Modulo reportes")
    opc = input("--> ")

    
    match opc:
        case "1":
            agregarEstudiantes()
        case "2":
            editar_estudi()
        case "3":
            verestudiantes()
        case "4":
            EditarNotas()
        case "5":
            mostrarMenuR ()
        case "6":
            modulo_matriculas()
        case "7":
            pass
        case _:
            print("ERROR VALIDO")

                
            

def opcion_trainer():
    print ("Bienvenido seleccione que desea hacer")
    print ("1. Agregar notas")
    print ("2. mirar rutas")
    print ("3. listas de estudiantes")
    print ("4. Horarios de trabajo")
    print ("5. Ver estudiantes en riesgo")
    print ("6. Modulo reportes")
    print ("7. Salida")
    op = input("= ")
    match op:
        case "1":
            pass
        case "2":
            pass
        case "3":
            pass
        case "4":
            pass
        case "5":
            pass
        case "6":
            pass
        case "7":
            pass
        case _:
            print("ERROR")

        
def menu():
    MAIN_MENU= """
    ########################################
    ########## CAMPUSLANDS OS###############
    ########################################
            1 USUARIO: CORDINADORA
            2 USUARIO: TRAINER
            3 USUARIO: CAMPER
            4 Salir
    """
    print(MAIN_MENU)  

    
    opc = input("--> ")

    
    match opc:
        case "1":
            opcion_cordinadora()
        case "2":
            opcion_trainer()
        case "3":
            vernotas()
        case "4":
            print("Saliendo..")





