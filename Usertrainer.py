import json 

def menu_trainer():
    while True:
        print("\n--- Menú del Trainer ---")
        print("1. Registrar Notas")
        print("2. Consultar Campers en Riesgo")
        print("3. Agregar Quiz/Trabajo")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_notas()
        elif opcion == "2":
            consultar_campers_riesgo()
        elif opcion == "3":
            agregar_quiz_trabajo()
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")

def registrar_notas():
    id_camper = int(input("ID del Camper: "))
    id_ruta = int(input("ID de la Ruta: "))
    nota_teorica = float(input("Nota Teórica (0-100): "))
    nota_practica = float(input("Nota Práctica (0-100): "))
    nota_quices = float(input("Nota de Quices/Trabajos (0-100): "))

