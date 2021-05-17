import numpy as np

problema = {'A': ['B', 'C', 'D'],
            'B': ['A', 'C', 'E', 'F'],
            'C': ['A', 'B', 'F', 'G', 'D'],
            'D': ['A', 'C', 'G', 'K'],
            'E': ['H', 'I', 'F', 'B'],
            'F': ['G', 'I', 'E', 'B', 'C'],
            'G': ['C', 'F', 'D', 'I', 'J', 'K'],
            'H': ['E', 'I', 'L'],
            'I': ['H', 'E', 'L', 'F', 'G', 'J'],
            'J': ['I', 'G', 'K', 'M', 'N'],
            'K': ['D', 'G', 'J', 'N'],
            'L': ['H', 'I', 'M'],
            'M': ['L', 'J', 'N'],
            'N': ['M', 'J', 'K']}

utilidad = {'A': 25,
            'B': 20,
            'C': 23,
            'D': 18,
            'E': 12,
            'F': 23,
            'G': 15,
            'H': 15,
            'I': 16,
            'J': 5,
            'K': 25,
            'L': 25,
            'M': 3,
            'N': 12}


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
    mejor = inicial
    actual = inicial
    # -- Escoger la temperatura para el problema 
    temperatura = 25

    while temperatura > 0.25:
        vecindad = getVecindad(actual, problema)
        nuevo = siguiente(vecindad, utilidad)
        
        if utilidad[nuevo] <= utilidad[mejor]:
            mejor = nuevo
        else:
            r = np.random.uniform()
            peor = np.exp((utilidad[mejor]-utilidad[nuevo])/temperatura)
            
            if r < peor:
                mejor = nuevo