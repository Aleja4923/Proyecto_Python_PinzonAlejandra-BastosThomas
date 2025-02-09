import json

# Función para cargar el inventario desde un archivo JSON
def abrirJSON():
    try:
        with open("./estudiantes.json", 'r') as openFile:
            estudiantes = json.load(openFile)
    except FileNotFoundError:
        estudiantes = {"campers": []}  # Si el archivo no existe, se crea un diccionario con una lista vacía
    return estudiantes

# Función para guardar el inventario en un archivo JSON
def guardarJSON(estudiantes):
    with open("./estudiantes.json", 'w') as outFile:
        json.dump(estudiantes, outFile, indent=4)  # indent=4 para formato legible

# Función para agregar un nuevo estudiante
def agregarEstudiantes(estudiantes):
    print("Agregar un nuevo Estudiante:")
    ide = int(input("Ingresa el ID: "))
    for estudiante in estudiantes["campers"]:
        if estudiante["ide"] == ide:
            print("El ID ya existe")
            return

    Nombre = input("Ingresa el nombre: ")
    Direccion = input("Ingresa la dirección: ")
    TelefonoCel = int(input("Ingrese el número de teléfono celular: "))
    TelefonoFijo = int(input("Ingrese el número de teléfono fijo: "))
    correoElectronico = input("Ingrese el correo electrónico: ")
    estado = input("Ingrese el estado del estudiante: ")
    riesgo = input("Ingrese el nivel de riesgo: ")

    estudiante23 = {
        "ide": ide,
        "Nombre": Nombre,
        "Dirección": Direccion,
        "Telefono Celular": TelefonoCel,
        "Telefono Fijo": TelefonoFijo,
        "Correo electrónico": correoElectronico,
        "Estado": estado,
        "Riesgo": riesgo,
    }

    estudiantes["campers"].append(estudiante23)
    guardarJSON(estudiantes)
    print("Estudiante agregado con éxito")

# Función para ver todos los estudiantes
def verEstudiantes(estudiantes):
    for i, estudiante in enumerate(estudiantes["campers"], 1):
        print(f"Estudiante {i}:")
        print("  ID: " + str(estudiante['ide']))
        print("  Nombre: " + estudiante['Nombre'])
        print("  Dirección: " + estudiante['Dirección'])
        print("  Teléfono Celular: " + str(estudiante['Telefono Celular']))
        print("  Teléfono Fijo: " + str(estudiante['Telefono Fijo']))
        print("  Correo Electrónico: " + estudiante['Correo electrónico'])
        print("  Estado: " + estudiante['Estado'])
        print("  Riesgo: " + estudiante['Riesgo'])

# Función para editar un estudiante
def editarEstudiante(estudiantes):
    ide = int(input("Ingrese el ID del estudiante a editar: "))
    estudianteEncontrado = None
    for estudiante in estudiantes["campers"]:
        if estudiante["ide"] == ide:
            estudianteEncontrado = estudiante
            break

    if not estudianteEncontrado:
        print("Estudiante no encontrado")
        return

    print("¿Qué desea editar?")
    print("1. Nombre")
    print("2. Dirección")
    print("3. Teléfono Celular")
    print("4. Teléfono Fijo")
    print("5. Correo electrónico")
    print("6. Estado")
    print("7. Riesgo")
    print("8. Volver al menú")

    op = input("Seleccione una opción digitando el número: ")

    if op == "1":
        estudianteEncontrado["Nombre"] = input("Ingrese el nuevo nombre: ")
    elif op == "2":
        estudianteEncontrado["Dirección"] = input("Ingrese la nueva dirección: ")
    elif op == "3":
        estudianteEncontrado["Telefono Celular"] = int(input("Ingrese el nuevo teléfono celular: "))
    elif op == "4":
        estudianteEncontrado["Telefono Fijo"] = int(input("Ingrese el nuevo teléfono fijo: "))
    elif op == "5":
        estudianteEncontrado["Correo electrónico"] = input("Ingrese el nuevo correo electrónico: ")
    elif op == "6":
        estudianteEncontrado["Estado"] = input("Ingrese el nuevo estado: ")
    elif op == "7":
        estudianteEncontrado["Riesgo"] = input("Ingrese el nuevo nivel de riesgo: ")
    elif op == "8":
        return
    else:
        print("Opción no válida")
        return

    guardarJSON(estudiantes)
    print("Estudiante editado con éxito")

def registrarNotas():
    campers = json
    ide = input("ingrese el ID del camper : ")
    if ide in campers:
     notas = input("agrega la nota de 10 a 100 :")
     campers[ide]["nota"]=notas
     print ("nota actualizada correctamente")
    else:
        print("camper no encontrado.")
def cambiar_Estado_campers():
 campers= campers
 ide = input("ingrese el id del camper : ")
  
 if ide in campers:
  nuevo_estado = input("nuevo estado (Activo/Inactivo): ")
  campers[ide]["estado"]=nuevo_estado
  print("Estado actualizado correctamente")
  guardarJSON(campers)
 else:
  print("campers no encontrado")
 
 
def campers_en_Riesgo():
     campers =json
     ide= input ("ingrese el id del camper en riesgo")
     if ide in campers:
       riesgo= input("nivel de riesgo(bajo/medio/alto): " )
       campers[ide]["riesgo"] = riesgo
       guardarJSON(campers)
       print("riesgo actualizado correctamente.")
     else:
       print("campers no encontrado")
def horarios():
    campers= guardarJSON()
    print("\n--- Gestión de Horarios ---")
    ide= input("ingrese el id del camper: " )
    if ide in campers:
        print("1. Asignar horario")
        print("2. cosultar horario")
        opcion = input("seleccione una opcion: ")
        if opcion == "1":
         horario= input("ingrese el horario (Ej: joranda de la mañana 6 am a 2 pm o tarde 2pm a 10pm)")
        campers[ide]["horario"] = horario
        print("horario asignado correctamente. ")
    elif opcion == "2 ":
           if " horario" in campers[ide]:
            print(f"horario actual: {campers[ide]["horario"]}")
           else:
            print("El camper no tiene un horario asignado .")
def reportes ():
   campers= guardarJSON()
   print("--- Generacion de reportes --- ")
   print("1. reporte de campers matirculados")
   print("2. reporte de campers en riesgo ")
   opcion = input("selecione una opcion: ")
   if opcion=="1":
      print("----Campers Matriculados ---")
      for ide, datos in campers.items():
         if "cursos"in datos and datos ["cursos"]:
            print(f"Id:{ide}- nombre: {datos["Nombre"]} - cursos: {", ".join(datos["cursos"])}")
      print("-"*30)  
   elif opcion == "2":
      print ("--- campers en riesgo -----")
      for ide, datos in campers.items():
         if datos.get("riesgo", "bajo") in ["meido","alto"]:
             print(f"Id:{ide}- nombre: {datos["Nombre"]} - cursos: {", ".join(datos["cursos"])}")
             print("-" * 30)
         else:
           print("Opción inválida.")