
import json 
import desing.userCordinadora as uc


###funciones de notas


 ### uso de la funcion
 # ruta_json = "campers.json"
 ##actualizar_notas(ruta_json)   

## Colocar quien eres Pedro Maria o Aura dependiendo de su ruta y proyectar la ruta
## proyectarle los estudiantes

op= """Bienvenido que  trainer eres?
            1. Pedro
            2. Maria
            3. Aura
        Porfavor digite un numero
    """

        
            
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

def menutrainers ():
    op= input( """Bienvenido que  trainer eres?
            1. Pedro
            2. Maria
            3. Aura
        Porfavor digite un numero
    """)

    match op:
        case 1: 
            print ("sapo perro")


