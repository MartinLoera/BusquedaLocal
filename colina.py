import numpy as np

## Esta  funcion  forma  la  vecindad  del  estado  actual
def  getVecindad(actual ,proble):
    resp=proble[actual]
    resp.append(actual)
    return  resp

## Esta  funcion  extrae  al  siguiente  estado a expandir
def  siguiente(Vecindad ,fs):
    fmejor =0
    mejor=None
    for edo in  Vecindad:
        if fs[edo]>fmejor:
            mejor=edo
            fmejor=fs[edo]
    return  mejor
            
## Esta  funcion  implementa  la  busqueda  por  descenso  de  colina
def  asender_colina(ini ,proble ,fs):
    mejor=None
    nuevo=None
    actual=ini
    fmejor =100
    listo=False
    itera=0
    maxItera =50
    while  not  listo:
        if itera >maxItera:
            listo=True
            mejor=actual
        else:
            vecindad=getVecindad(actual ,proble)
            nuevo=siguiente(vecindad ,fs)
            if nuevo == actual:
                listo=True
                mejor=actual
            else:
                itera=itera +1
                actual=nuevo
    return  mejor
                            


