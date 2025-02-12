from desing.Usercordinadora import *

def menu():
        print('''
        ########################################
        ########## CAMPUSLANDS OS###############
        ########################################
                1 USUARIO: CORDINADORA
                2 USUARIO: TRAINER
                3 USUARIO: CAMPER
                4 Salir
        ''')  

        
        opc = input("--> ")

        
        match opc:
            case "1":
                opcion_cordinadora()
            case "2":
                opcion_trainer()
            case "3":
                opcion_camper()
            case "4":
                print("Saliendo")



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
                pass
            case "5":
                pass
            case "6":
                pass
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
        
def opcion_camper():
        print (" 1 Ver notas")
        print("2 ver horarios")
        print("3 ver estado  ")
        print("4 salir")
