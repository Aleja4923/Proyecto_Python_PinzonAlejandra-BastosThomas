import json
import tabulate

RUTA_campers = "data/campers.json"  
RUTA_notas = "data/notas.json"  
RUTA_rutas = "data/rutas.json"
# Función para cargar el inventario desde un archivo JSON
def abrirJSON():
    try:
        with open("./campers.json", 'r') as openFile:
            estudiantes = json.load(openFile)
    except FileNotFoundError:
        estudiantes = {"campers": []} 
    return estudiantes
# Función para guardar el inventario en un archivo JSON
def guardarJSON(estudiantes):
    with open("./campers.json", 'w') as outFile:
        json.dump(estudiantes, outFile, indent=4)  # indent=4 para formato legible




estudiantes = abrirJSON()   

def agregarEstudiantes():
    ide = input("Ingresa el ide : ")
    nombre = input("Ingresa el nombre: ")
    apellido = input("Ingrese el apellido: ")
    acudiente = input("Ingrese el acudiente: ")
    direccion = input("Ingresa la dirección: ")
    telefono_cel = input("Ingrese el número de teléfono celular: ")
    telefono_fijo = input("Ingrese el número de teléfono fijo: ")
    correo_electronico = input("Ingrese el correo electrónico: ")
    estado = input("Ingrese el estado del estudiante: ")
    riesgo = input("Ingrese el nivel de riesgo: ")
    
    estudiante = {
        "ide": ide,
        "Nombre": nombre,
        "Apellido": apellido,
        "Acudiente": acudiente,
        "Dirección": direccion,
        "Telefono Celular": telefono_cel,
        "Telefono Fijo": telefono_fijo,
        "Correo Electrónico": correo_electronico,
        "Estado": estado,
        "Riesgo": riesgo
    }
    
    campers[ide] = estudiante
    print("Estudiante agregado con éxito.")


def verestudiantes(estudiantes):
    for i in range (len(estudiantes["campers"])):
        print("Estudiante "),i+1
        print("  ID: " + (estudiantes["campers"][i]["ide"])) 
        print("  Nombre: " + (estudiantes["campers"] [i]["Nombre"]))
        print("  Apellido: " + (estudiantes["campers"] [i]["Apellido"]))
        print("  Acudiente" + (estudiantes["Acudiente"][i]["Acudiente"]))
        print("  Dirección: " + (estudiantes["campers"][i]["Dirrecion"]))
        print("  Teléfono Celular: " + (estudiantes["campers"][i]["Telefono Celular"]))
        print("  Teléfono Fijo: " + (estudiantes["campers"][i]["Telefono Fijo"]))
        print("  Correo Electrónico: " + (estudiantes["campers"][i]["Correo electronico"]))
        print("  Estado: " + (estudiantes["campers"][i]["Estado"]))
        print("  Riesgo: " + (estudiantes["campers"][i]["Riesgo"]))

def editar_estudi(estudiantes):
    ide= int(input("Ingrese el id del estudiante a editar"))
    estudiencon= None
    for estudiante in estudiantes["campers"]:
        if estudiante ["ide"] == ide:
            estudiencon = estudiante
            break

    print ("Que desea editar")
    print("1. Nombre")
    print("2. Apellido")
    print("3. Acudiente")
    print("4. Direccion")
    print("5. Telefono Celular")
    print("6. Telefono Fijo")        
    print("7. Correo electrónico")
    print("8. Estado")
    print("9. Riesgo")
    print("10. Volver a menu")
    
    op=input("Selecione una opcion digitando el numero")

    if op == "1":
        estudiencon["campers"]["Nombre"] = str(input("Ingrese el nuevo nombre"))
    elif op == "2":
        estudiencon["campers"]["Apellido"] = input("Ingrese el nuevo apellido")
    elif op == "3":
        estudiencon["campers"]["Acudiente"] = input("Ingrese el nuevo acudiente")
    elif op == "4":
        estudiencon["campers"]["Direccion"] = input("Ingrese la nueva direccion")        
    elif op == "5":
        estudiencon["campers"]["Telefono Celular"] = int(input("Ingrese el nuevo telefono celular"))
    elif op == "6":
        estudiencon["campers"]["Telefono Fijo"] = int(input("Ingrese el nuevo telefono fijo"))
    elif op == "7":
        estudiencon["campers"]["Correo electronico"] = input("Ingrese el nuevo correo electronico")
    elif op == "8":
        estudiencon["campers"]["Estado"] = input("Opciones: (En proceso de ingreso, Inscrito, Aprobado,Cursando, Graduado, Expulsado, Retirado) ")
    elif op == "9":
        estudiencon["campers"]["Riesgo"] = input("Ingrese el nuevo nivel de riesgo")
    elif op == "10":
        return

    else:
        print("Opcion no valida")
        return 
    
    guardarJSON(estudiantes)


campers = {}  # Diccionario para almacenar los datos de los campers

def registrarNotas():
    ide = input("Ingrese el ID del camper: ")
    if ide in campers:
        notas = input("Agrega la nota de 10 a 100: ")
        campers[ide]["nota"] = notas
        print("Nota actualizada correctamente")
    else:
        print("Camper no encontrado. Registrándolo...")
        campers[ide] = {"nota": notas}
        print("Camper registrado y nota guardada.")

def horarios():
    print("\n--- Gestión de Horarios ---")
    ide = input("Ingrese el ID del camper: ")
    if ide in campers:
        print("1. Asignar horario")
        print("2. Consultar horario")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            horario = input("Ingrese el horario (Ej: jornada de la mañana 6 am a 2 pm o tarde 2 pm a 10 pm): ")
            campers[ide]["horario"] = horario
            print("Horario asignado correctamente.")
        elif opcion == "2":
            if "horario" in campers[ide]:
                print(f"Horario actual: {campers[ide]['horario']}")
            else:
                print("El camper no tiene un horario asignado.")
    else:
        print("no joda")
def reportes ():
    campers= guardarJSON()
    print("--- Generacion de reportes --- ")
    print("1. Reporte de campers matriculados")
    print("2. Reporte de campers en riesgo ")
    opcion = input("Seleccione una opcion: ")
    if opcion=="1":
        print("----Campers Matriculados ---")
        for ide, datos in campers.items():
            if "cursos" in datos and datos["cursos"]:
                print(f'Id:{ide}- nombre: {datos["Nombre"]} - cursos: {", ".join(datos["cursos"])}')
            print("-" * 30)

        if opcion == "2":
            print("--- campers en riesgo -----")
            for ide, datos in campers.items():
                if datos.get("riesgo", "bajo") in ["medio", "alto"]:
                    print(f'Id:{ide}- nombre: {datos["Nombre"]} - cursos: {", ".join(datos["cursos"])}')
                    print("-" * 30)
        else:
            print("Opción inválida.")
    
def modulo_matriculas():
    datos = abrirJSON()
    ide = int(input("Ingrese el ID del camper: "))
    for estudiante in datos["campers"]:
        if estudiante["ide"] == ide:
            print("1. Matricular camper en una ruta")
            print("2. Ver ruta actual del camper")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                ruta = input("Ingrese la ruta de entrenamiento (Java, NodeJS, .NET): ")
                estudiante["Ruta"] = ruta
                guardarJSON(datos)
                print(f"Camper matriculado en la ruta {ruta}.")
            elif opcion == "2":
                if "Ruta" in estudiante:
                    print(f"Ruta actual: {estudiante['Ruta']}")
                else:
                    print("El camper no está matriculado en ninguna ruta.")
            return
    print("Camper no encontrado.")

