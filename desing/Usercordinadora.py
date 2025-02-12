import json
import tabulate 

RUTA_campers = "data/campers.json"  
RUTA_notas = "data/notas.json"  
RUTA_rutas = "data/rutas.json"
# Función para cargar el inventario desde un archivo JSON
def abrirJSON():
    try:
        with open("/data/campers.json", 'r') as openFile:
            estudiantes = json.load(openFile)
    except FileNotFoundError:
        estudiantes = {"campers": []} 
    return estudiantes
# Función para guardar el inventario en un archivo JSON
def guardarJSON(estudiantes):
    with open("./data/campers.json", 'w') as outFile:
        json.dump(estudiantes, outFile, indent=4)  # indent=4 para formato legible
    return ("Guardado exitosamente")



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

    guardarJSON(campers)
    print("Estudiante agregado con éxito.")


def verestudiantes():
    for i in range (len(estudiantes)):
        print("Estudiante "),i+1
        print("  ID: " + (estudiantes[i]["ide"])) 
        print("  Nombre: " + (estudiantes, [i]["Nombre"]))
        print("  Apellido: " + (estudiantes, [i]["Apellido"]))
        print("  Acudiente" + (estudiantes["Acudiente"][i]["Acudiente"]))
        print("  Dirección: " + (estudiantes,[i]["Dirrecion"]))
        print("  Teléfono Celular: " + (estudiantes,[i]["Telefono Celular"]))
        print("  Teléfono Fijo: " + (estudiantes,[i]["Telefono Fijo"]))
        print("  Correo Electrónico: " + (estudiantes,[i]["Correo electronico"]))
        print("  Estado: " + (estudiantes,[i]["Estado"]))
        print("  Riesgo: " + (estudiantes,[i]["Riesgo"]))

def editar_estudi():
    verestudiantes()
    ide= int(input("Ingrese el id del estudiante a editar"))
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
    opc=int(input(": "))
    for i in range(estudiantes):
        match opc:
            case 1:
                nm=input("Ingrese el nuevo nombre: ")
                estudiantes[ide-1]["Nombre"]=(nm)
            case 2: 
                ap=input("Ingrese el nuevo apellido: ")
                estudiantes[ide-1]["Apellido"]=(ap)
            case 3:
                ac=input("Ingrese el numero acudiente")
                estudiantes[ide-1]["Acudiente"]=(ac)
            case 4:
                di=input("Ingrese la nueva dirrecion")
                estudiantes[ide-1]["Dirrecion"]=(di)
            case 5:
                tc=input("Ingrese el nuevo telefono")
                estudiantes[ide-1]["Telefono Celular"]=(tc)
            case 6:
                tf=input("Ingrese el nuevo telefono fijo")
                estudiantes[ide-1]["Telefono Fijo"]=(tf)
            case 7:
                ce=input("Ingrese el correo electronico")
                estudiantes[ide-1]["Correo electronico"]=(ce)
            case 8:
                es=input("Ingrese el estado que se encuentra")
                estudiantes[ide-1]["Estado"]=(es)
            case 9:
                Ri=input("Ingrese el riesgo en el que esta")
                estudiantes[ide-1]["Riesgo"]=(Ri)         

    guardarJSON(estudiantes)


campers = {}  #Diccionario para almacenar los datos de los campers

def registrarNotas(): #Probarla y reestructurar
    ide= abrirJSON()
    ide = input("Ingrese el ID del camper: ")
    if ide in campers:
        notas = input("Agrega la nota de 10 a 100: ")
        campers[ide]["nota"] = notas
        print("Nota actualizada correctamente")
        ide= guardarJSON()   
    else:
        print("Camper no encontrado. Registrándolo...")
        campers[ide] = {"nota": notas}
        print("Camper registrado y nota guardada.")

def horarios(): #Estructurar 
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
    for estudiante in datos,:
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

