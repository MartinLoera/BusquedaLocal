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
    problema = pro
    utilidad = uti
    mejor = inicial
    actual = inicial
    # -- Escoger la temperatura para el problema 
    temperatura = 25

    while temperatura > 0.25:
        vecindad = getVecindad(actual, problema)
        nuevo = siguiente(vecindad, utilidad)
        iteracion = 0
        print(actual, utilidad[actual], mejor, utilidad[mejor], iteracion)
        
        if utilidad[nuevo] >= utilidad[mejor]:
            mejor = nuevo
        else:
            r = np.random.uniform()
            peor = np.exp((utilidad[mejor]-utilidad[nuevo])/temperatura)
            
            if r < peor:
                mejor = nuevo
        actual = nuevo
        temperatura = temperatura*0.5
        print(actual, utilidad[actual], mejor, utilidad[mejor])
        
        iteracion = iteracion + 1
    return mejor




