import os, sys
from valueFileGrammar import valueFileGrammar

def chargeFiles():

    route = input('Coloque una ruta:')
    routeArray = route.split('/')
    name = routeArray[-1].split(".")[0]
    files = open(route, 'r')
    print('Archivo cargado correctamente\n')
    return valueFileGrammar(name, files)
    files.close()