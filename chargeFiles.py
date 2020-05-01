import os, sys
from valueFileGrammar import valueFileGrammar

def chargeFiles():
    
    while True:
        print("Menú De Archivos")
        print("1. Cargar un archivo Gramática")
        print("2. Salir")
        opc = int(input("Escoje una opcion: "))

        if opc == 1:
            # route = './files/test.grm'
            route = input('Coloque una ruta:')
            routeArray = route.split('/')
            name = routeArray[-1].split(".")[0]
            files = open(route, 'r')
            print('Archivo cargado correctamente\n')
            valueFileGrammar(name, files)
            files.close()
        
        if opc == 2:
            os.system('clear')
            break