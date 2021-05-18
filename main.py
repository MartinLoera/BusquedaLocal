import numpy as np
from templado import *
from colina import *
from genetico import *
import time

letras = ['A', 'B', 'C', 'D', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
    
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

def estado_inicial():
    num = np.random.randint(13)
    return letras[num]

def main():

    est_init = estado_inicial()

    print('El estado inicial es: ', est_init)
    time.sleep(2)
    print('-----------------------------------------------------------------------------')
    mejor_templado = templado(est_init, problema, utilidad)
    print ('\nTemplado da como resultado '+ mejor_templado + ' como la mejor solucion, con un valor util de ', utilidad[mejor_templado])
    time.sleep(5)
    print('-----------------------------------------------------------------------------')
    solucion_colina = asender_colina(est_init ,problema , utilidad)
    print ('\nColina da como resultado '+ solucion_colina + ' como la mejor solucion, con un valor util de ', utilidad[solucion_colina])
    pass
    print('\n')
    time.sleep(5)
    print('-----------------------------------------------------------------------------')
    solucion_AG = main_genetico(est_init)
    
    print ('\nAG da como resultado '+ solucion_AG + ' como la mejor solucion, con un valor util de ', utilidad[solucion_AG])
    pass
    
main()