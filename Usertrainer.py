import json 

def menu_trainer():
    while True:
        print(" Menu del Trainer ")
        print("1. Registrar Notas")
        print("2. Consultar Campers en Riesgo")
        print("3. Salir")
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            registrar_notas()
        elif opcion == "2":
            campersriesgo()
        elif opcion == "3":
            break
        else:
            print("Opción no válida.")

def registrar_notas():
    id_camper = int(input("ID del Camper: "))
    id_ruta = int(input("ID de la Ruta: "))
    nota_teorica = float(input("Nota Teórica (0-100): "))
    nota_practica = float(input("Nota Práctica (0-100): "))
    nota_quices = float(input("Nota de Quices/Trabajos (0-100): "))

def campersriesgo():
    id_camper = int(input("ID del Camper: "))

