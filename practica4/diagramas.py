from practica1 import Complejo
import numpy as np
from practica3 import homologia


def matriz_borde_generalizada(complejo: Complejo):
    """
    Dado un complejo simplicial calculamos su matriz borde generalizada
    *** MATRIZ [FILAS][COL] ***
    """
    # primero sacamos todos los simplices posibles
    simplices = complejo.getCaras()
    simplices = list(simplices)
    # ahora vamos a tener que ordenarlos por longitud (habria que mirar por peso tmbn)
    simplices.sort(key=len)
    print(simplices)
    # ahora tenemos que hacer la matriz de incidencia
    matriz = np.zeros((len(simplices), len(simplices)))
    matriz = matriz.tolist()
    # hay que poner un 1 en la casilla [i][j] si el simplice_dim_p1[i] es cara de simplice_dim_p[j]
    for i in range(homologia.num_filas(matriz)):
        for j in range(homologia.num_columnas(matriz)):
            if len(simplices[i]) == len(simplices[j]) - 1 and Complejo.esCara(simplices[i], simplices[j]):
                matriz[i][j] = 1.0
    return matriz


def algoritmo_emparejamiento_nacimiento_muerte(matriz):
    """
    Recibida una matriz vamos a calculas los emparejamientos nacimiento-muerte
    """
    # dada una columna sacamos su low()
    # miramos en las columnas de su izqda y si tienen el mismo low borramos ese low en la de la izqda
    for i in range(homologia.num_columnas(matriz)):
        index_low = get_low(get_columna(matriz, i))
        # si existe low en esa columna
        if index_low != -1:
            # borramos los low iguales de columnas anteriores
            for otro_i in range(i):
                # si tienen el mismo low
                if get_low(get_columna(matriz, otro_i)) == index_low:
                    # sumamos las dos columnas
                    homologia.sumar_dos_columnas(matriz, i, otro_i)

    return matriz


def get_low(col):
    """
    Recibimos una columna y calculamos su 1 mas abajo.
    Devolvemos su indice.
    """
    indice = -1
    for i in range(len(col)):
        if col[i] == 1:
            indice = i
    return indice


def get_columna(matriz, indice):
    return [x[indice] for x in matriz]


def get_emparejamientos(matriz):
    """
    Dada una matriz de borde generalizada calculamos el algoritmo para reducir la matriz.
    Despues calculamos los emparejamientos para cada columna

    Emparejamientos son [low(j),j]
    ##### OJO luego hay que sacar los simplices de la lista 'simplices' de matriz_borde_generalizada()

    Para pasarlo luego a puntos en el diagrama hay que coger los pesos de los simplices
    """
    emparejamientos = []
    algoritmo_emparejamiento_nacimiento_muerte_y_otras_cosas_que_todavia_no_hemos_demostrado_que_funcionan_pero_acabaremos_demostrando(
        matriz)

    # recorremos las columnas
    for j in homologia.num_columnas(matriz):
        # sacamos su low y creamos una parejita
        index_low = get_low(get_columna(matriz, j))
        # metemos la pareja
        emparejamientos.append((index_low, j))

    return emparejamientos
