import json
from desing.userCordinadora import *
from desing.userTrainer import *


MENU_REPORTES = """
*-----------------------------*
---------Menu Reportes---------
*-----------------------------*
¿Que deseas hacer?

    1. Ver campers inscritos
    2. Ver campers aprobados
    3. Ver trainers
    4. Ver campers en alto riesgo
    5. Regresar menu anterior
"""

DB_FILE = "../data/campers.json"
def mostrarMenuR ():
    print (MENU_REPORTES)
    option = input("= ")
    match option:
        case "1":
            pass
        case "2":
            actualizar_notas()
        case "3":
            pass
        case "4":
            campersRiesgo()
        case "5":
            pass
        case _:
            pass

def campersRiesgo():

    altoriesgo = []

    data = abrirJSON()
    for camper in data:
        if camper["Riesgo"] == "Alto":
            altoriesgo.append(camper)
    if altoriesgo:
        for camper in altoriesgo:
            print (camper)

def campersInscritos():

    data = abrirJSON()  

    for camper in data:
        if camper("Estado") == "Inscrito":  
            print(camper)

def campersAprobados():
    data = abrirJSON()  
    for camper in data:
        if camper.get("Estado") == "Aprobado":  
            print(camper)
