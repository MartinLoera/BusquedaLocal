import numpy as np



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


def formarDiccionario(poblacion, utilidad, nom2gen, gen2nom):
    resp = {}
    for estado in poblacion:
        resp[estado] = utilidad[estado]
    return resp


def getMejor(poblacion, utilidad):
    fmejor = 0
    for estado in poblacion:
        if utilidad[estado] > fmejor:
            fmejor = utilidad[estado]
            mejor = estado
    return mejor


def seleccionar(poblacion, nom2gen, gen2nombre):
    ordenada = sorted(poblacion.items(), key=lambda x: x[1])
    suma = 0
    for estado in ordenada:
        suma = suma + estado[1]
    probas = []
    for estado in ordenada:
        probas.append(estado[1]/suma)
    cotas = []
    antes = 0.0
    for p in probas:
        cotas.append([antes, antes+p])
        antes = antes+p
    r1 = np.random.uniform(0, 1)
    r2 = np.random.uniform(0, 1)
    indi = 0
    for par in cotas:
        if r1 >= par[0] and r1 <= par[1]:
            indi1 = indi
            break
        indi = indi + 1
    indi = 0
    for par in cotas:
        if r2 >= par[0] and r2 <= par[1]:
            indi2 = indi
            break
        indi2 = indi
    padre = list(poblacion)[indi1]
    madre = list(poblacion)[indi2]
    padreGen = nom2gen[padre]
    madreGen = nom2gen[madre]
    return padre, padreGen, madre, madreGen


def mutar(estado, nom2gen, gen2nom):
    gen = nom2gen[estado]
    gen2 = list(gen)
    total = len(gen2)
    indi = np.random.randint(0, total)
    if gen2[indi] == '0':
        gen2[indi] = '1'
    else:
        gen2[indi] = '0'
    gen = "".join(gen2)
    letra = gen2nom.get(gen)
    if not letra:
        letra = 'N'
        gen = '1101'
    return gen, letra


def cruzar(padre, madre, let2gen, gen2let):
    genP = let2gen[padre]
    genM = let2gen[madre]
    genP2 = list(genP)
    genM2 = list(genM)
    total = len(genP2)
    indi = np . random . randint(0, total)
    padre1 = genP2[: indi]
    padre2 = genP2[indi:]
    madre1 = genM2[: indi]
    madre2 = genM2[: indi]
    hijo1 = padre1 + madre2
    hijo2 = padre2 + madre1
    genHijo1 = "". join(hijo1)
    genHijo2 = "". join(hijo2)
    letraHijo1 = gen2let . get(genHijo1)
    letraHijo2 = gen2let . get(genHijo2)

    if not letraHijo1:
        letraHijo1 = 'N'
        genHijo1 = '1101'
    if not letraHijo2:
        letraHijo2 = 'N'
        genHijo2 = '1101'
    return letraHijo1, genHijo1, letraHijo2, genHijo2


def aGen(ini, proble, fs, let2gen, gen2let):
    mejor = None
    maxItera = 50
    itera = 0
    pobla = list(fs.keys())
    total = len(pobla)
    while itera <= maxItera:
        nPtotal = 0
        nPobla = []
        while nPtotal < total:
            dicPobla = formarDiccionario(pobla, fs, let2gen, gen2let)
            padre, genPadre, madre, genMadre = seleccionar(
                dicPobla, let2gen, gen2let)
            hijo1, genHijo1, hijo2, genHijo2 = cruzar(
                padre, madre, let2gen, gen2let)
            hijo1m, genHijo1m = mutar(hijo1, let2gen, gen2let)
            hijo2m, genHijo12 = mutar(hijo2, let2gen, gen2let)
            nPobla.append(hijo1m)
            nPobla.append(hijo2m)
            nPtotal = nPtotal+2
            print(hijo1, genHijo1, hijo2, genHijo2)
        itera = itera+1
    mejor = getMejor(pobla, fs)
    return mejor

def estado_inicial():
    letras = ['A', 'B', 'C', 'D', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
    num = np.random.randint(13)
    return letras[num]

def main_genetico(estado_inicial):
    
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

    nom2rom = {
        'A': '0000',
        'B': '0001',
        'C': '0010',
        'D': '0011',
        'E': '0100',
        'F': '0101',
        'G': '0110',
        'H': '0111',
        'I': '1000',
        'J': '1001',
        'K': '1010',
        'L': '1011',
        'M': '1100',
        'N': '1101'
    }

    crom2nom = {
        '0000': 'A',
        '0001': 'B',
        '0010': 'C',
        '0011': 'D',
        '0100': 'E',
        '0101': 'F',
        '0110': 'G',
        '0111': 'H',
        '1000': 'I',
        '1001': 'J',
        '1010': 'K',
        '1011': 'L',
        '1100': 'M',
        '1101': 'N'
    }
    
    est_init = estado_inicial
    
    
    mejor = aGen(est_init, problema, utilidad, nom2rom, crom2nom)
    return mejor
