import numpy as np


def getVecindad(estado, diagrama):
    return diagrama[estado]


def siguiente(vecindad, utilidad):
    fmejor = 100
    mejor = None
    for edo in vecindad:
        if utilidad[edo] < fmejor:
            mejor = edo
            fmejor = utilidad[edo]
    return mejor

def templado(inicial, pro, uti):
    iteracion = 1
    problema = pro
    utilidad = uti
    mejor = inicial
    actual = inicial
    # -- Escoger la temperatura para el problema 
    temperatura = 25

    while temperatura > 0.25:
        print("Iteracion numero ", iteracion)
        vecindad = getVecindad(actual, problema)
        nuevo = siguiente(vecindad, utilidad)
        
        if utilidad[nuevo] >= utilidad[mejor]:
            mejor = nuevo
        else:
            r = np.random.uniform()
            peor = np.exp((utilidad[mejor]-utilidad[nuevo])/temperatura)
            
            if r < peor:
                mejor = nuevo
        actual = nuevo
        temperatura = temperatura*0.5
        print('El mejor es: ',mejor, 'con un valor util de ', utilidad[mejor])
        iteracion= iteracion + 1

    return mejor


