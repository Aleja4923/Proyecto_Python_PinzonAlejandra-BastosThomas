import json
import Usercordinadora as admin
import Usertrainer as trainer
from tabulate import tabulate

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
            pass
        case "3":
            pass
        case "4":
            pass
        case "5":
            pass
        case _:
            pass

def campersRiesgo():

    highRisk = []

    data = admin.abrirJSON()
    for camper in data:
        if camper["Riesgo"] == "Alto":
            highRisk.append(camper)
    
    print(tabulate(highRisk))