import json 
import Usercordinadora as uc


###funciones de notas
def readJson(rutanotas):
    try:
        with open(rutanotas,"r",encoding="utf-8") as file: 
            return json.load(file)  
    except (FileNotFoundError, json.JSONDecodeError):
        return {}
def guardar_notas (rutanotas,datos ):   
    try:
        with open( rutanotas,"w",encoding="utf-8")as file:
            json.dump(datos,file,indent=4)
    except Exception as e:
        print(f"Error al guardar datos:{str(e)}")
def actualizar_notas(rutanotas):
    campers = readJson(rutanotas) 
    if campers is None:
        return

def actualizar_notas(rutanotas):
    campers = readJson(rutanotas)
    if campers is None:
        return
    try:
        ide = int(input("ingrese el id del camper: "))
    except ValueError:
        print("error ingresa un numero valido ")
        return
    encontrado= False
    for camper in campers:
        if camper["ide"] == ide:
            curso= input("Ingrese el nombre del curso: ")
            if curso in camper["curso"]:
              print(f"Notas actuales en {curso} : {camper['cursos'][curso]}")
            try:
                nueva_Notas=list(map(int,input("ingrese las nuevas notas")))
                camper["cursos"][curso]= nueva_Notas
                print("notas actualizadas correctamente.")
                encontrado= True
                break
            except ValueError:
                print("Error ingrese solo numero separados por comas")
        else:
            print("error curso no encontrado")
    if not encontrado:
        print("camper no encontrado")
    guardar_notas(campers, rutanotas)
 ### uso de la funcion
 # ruta_json = "campers.json"
 ##actualizar_notas(ruta_json)   




        
            
def mirar_rutas():
    rutas = {
        "Ruta Java": ["Intro", "Python", "HTML/CSS", "Scrum", "Git", "JavaScript", "Intro Back", "Intro BBDD", "MySQL", "Java", "PostgreSQL", "SpringBoot"],
        "Ruta NodeJS": ["Intro", "Python", "HTML/CSS", "Scrum", "Git", "JavaScript", "Intro Back", "Intro BBDD", "MongoDB", "JavaScript", "MySQL", "Express"],
        "Ruta .NET": ["Intro", "Python", "HTML/CSS", "Scrum", "Git", "JavaScript", "Intro Back", "Intro BBDD", "MySQL", "C#", "PostgreSQL", ".Net Core"]
    }
    print("--- Rutas de Entrenamiento ---")
    for ruta, modulos in rutas.items():
        print(f"{ruta}: {', '.join(modulos)}")
        
def listar_estudiantes():
    datos = abrirJSON()
    print("--- Lista de Estudiantes ---")
    for estudiante in datos["campers"]:
        print(f"ID: {estudiante['ide']}, Nombre: {estudiante['Nombre']} {estudiante['Apellidos']}, Estado: {estudiante['Estado']}, Riesgo: {estudiante['Riesgo']}")