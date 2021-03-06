import shutil

import numpy as np
from scipy.spatial import Delaunay, Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt
import matplotlib.colors
from math import dist
from practica1.Complejo import Complejo
import os
import imageio

directorio = "alphaComplejo"

"""
Para la triangulacion nos devuelve los triangulos a partir de los puntos que forman los vertices aqui:
    (simplicesDelaunay)
[[0 1 2], [0 1 3], ...]
Vamos a usar esos valores para luego obtener las coordenadas de esos puntos y obtener su 
circuncentro de forma numerica
    (points): -> nuestra variable con las coords de los puntos (se corresponden los indices con los de la lista anterior)

Nombre  -> Coords
punto 0 -> points[0]  
"""


def alphaComplejo(points):
    """
    Dado una serie de puntos calcula el complejo asociado con los pesos, siendo estos las distancias
    Se sigue el algoritmo de alpha complejos de la clase 4
    :return:
    """

    vor = Voronoi(points)
    # hago plot de voronoy y puntos (como no hago show se vera con el siguiente)
    voronoi_plot_2d(vor, show_vertices=False, line_width=2, line_colors='red')
    plt.plot(points[:, 0], points[:, 1], 'ko')

    Del = Delaunay(points)
    simplicesDelaunay = Del.simplices
    # ordenar lista de listas -> No realmente necesario, pero asi el print siempre es mas facil de ver
    simplicesDelaunay = ordenar(simplicesDelaunay)

    print("SIMPLCES: ", simplicesDelaunay)

    # Printeo triangulacion de Delaunay
    c = np.ones(len(points))
    cmap = matplotlib.colors.ListedColormap("limegreen")
    plt.tripcolor(points[:, 0], points[:, 1], simplicesDelaunay, c, edgecolor="k", lw=2, cmap=cmap)
    plt.plot(points[:, 0], points[:, 1], 'ko')
    plt.show()

    # los vertices se añaden al alphaComplejo con peso 0
    alphaComplejoRes = Complejo([])
    for index, point in enumerate(points):
        alphaComplejoRes.anadirSimplice([(index,)], 0)

    for simplice in simplicesDelaunay:

        # extraer los tres puntos del triangulo -> extraigo por coords y por indices
        trianglePointsCoords = []
        puntos = []
        for indexPoint in simplice:
            trianglePointsCoords.append(list(points[indexPoint]))  # me guardo sus coordenadas
            puntos.append(indexPoint)  # me guardo su indice
        trianglePointsTuplesIndice = tuple(puntos)

        # calcular circuncentro y circunradio
        circuncentro = circumcenter(trianglePointsCoords)
        circunradio = dist(trianglePointsCoords[0],
                           circuncentro)  # distancia desde un pto cualquiera del triang a circuncentro

        # añadir simplice (triang) al alphaComplejo
        alphaComplejoRes.anadirSimplice([trianglePointsTuplesIndice], circunradio)

        # definir las aristas --> defino por coords y por indices
        arista01 = [trianglePointsCoords[0], trianglePointsCoords[1]]
        arista12 = [trianglePointsCoords[1], trianglePointsCoords[2]]
        arista02 = [trianglePointsCoords[0], trianglePointsCoords[2]]
        arista01Tuples = (trianglePointsTuplesIndice[0], trianglePointsTuplesIndice[1])
        arista12Tuples = (trianglePointsTuplesIndice[1], trianglePointsTuplesIndice[2])
        arista02Tuples = (trianglePointsTuplesIndice[0], trianglePointsTuplesIndice[2])

        # calculamos el punto medio para cada una de las aristas
        for (arista, aristaTupla) in [(arista01, arista01Tuples), (arista12, arista12Tuples),
                                      (arista02, arista02Tuples)]:
            medio = puntoMedio(arista)
            radio = dist(medio, arista[0])
            hayPuntoDentro = False

            for point in points:
                # si hay un punto dentro entonces su peso es el circunradio, a no ser que tuviera uno anterior mas peque
                if dist(medio, point) < radio:
                    # caso arista ya añadida -> actualizamos el peso
                    if aristaTupla in alphaComplejoRes.simplices:
                        if alphaComplejoRes.pesos[alphaComplejoRes.simplices.index(aristaTupla)] > circunradio:
                            alphaComplejoRes.pesos[alphaComplejoRes.simplices.index(aristaTupla)] = circunradio
                    else:
                        alphaComplejoRes.anadirSimplice([aristaTupla], circunradio)
                    hayPuntoDentro = True
                    break  # para asi no seguir mirando con el resto de puntos ya que no necesario
            if not hayPuntoDentro:
                # añadir arista -> quedarse con el menor peso si ya estaba o añadirla nueva
                if aristaTupla in alphaComplejoRes.simplices:
                    if alphaComplejoRes.pesos[alphaComplejoRes.simplices.index(aristaTupla)] > radio:
                        alphaComplejoRes.pesos[alphaComplejoRes.simplices.index(aristaTupla)] = radio
                else:
                    alphaComplejoRes.anadirSimplice([aristaTupla], radio)

    return alphaComplejoRes


def puntoMedio(arista: list):
    return [0.5 * (arista[0][0] + arista[1][0]), 0.5 * (arista[0][1] + arista[1][1])]


def circumcenter(trianglePoints: list):
    """
    Partiendo de una lista con tres puntos de la forma (x,y), obtenemos el centro de
    la circunferencia que pasa por los tres

    :param trianglePoints: [ [ax, ay], [bx, by], [cx, cy] ]
    :return: [circuncentro.x, circuncentro.y]
    """
    [ax, ay] = trianglePoints[0]
    [bx, by] = trianglePoints[1]
    [cx, cy] = trianglePoints[2]

    d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
    ux = ((ax * ax + ay * ay) * (by - cy) + (bx * bx + by * by) * (cy - ay) + (cx * cx + cy * cy) * (ay - by)) / d
    uy = ((ax * ax + ay * ay) * (cx - bx) + (bx * bx + by * by) * (ax - cx) + (cx * cx + cy * cy) * (bx - ax)) / d
    return [ux, uy]


def ordenar(listaDeListas):
    for eachLista in listaDeListas:
        eachLista.sort()
    listaDeListas.sort()
    return listaDeListas


def printearAlphaComplejoGIF(complejo: Complejo, puntos):
    """
    Dado un alphaComplejo y sus puntos dibujamos la formacion del alphaComplejo completo

    :param complejo:
    :param puntos:
    :return:
    """
    # ordeno los pesos para printear las graficas en orden
    pesos = complejo.pesos.copy()
    pesos = list(set(pesos))  # borro repetidos en caso de que haya
    pesos.sort()
    # limpio las imagenes anteriores si existen
    cleanDir()

    # calculo todas las filtraciones posibles --> el nombre de cada grafica
    # es el num de iteracion para luego hacer el gif en orden
    for i in range(len(pesos)):
        peso = pesos[i]
        filtracionAlphaComplejoPlot(complejo, peso, i, puntos)

    # creo el gif
    make_gif()


def filtracionAlphaComplejoPlot(alphaComplejoTotal, peso, nombreFich, puntosCoord):
    """
    Dado un alphaComplejo genera la filtracion asociada al conjunto de puntos en el plano
    :param alphaComplejoTotal:
    :param nombreFich:
    :param peso:
    :param puntosCoord:
    :return:
    """
    if not os.path.exists(directorio):
        os.makedirs(directorio)
    filtracion = alphaComplejoTotal.filtration(peso)
    filtracionCoords = []
    for simplice in filtracion:
        simpliceCoords = []
        for each_point in simplice:
            simpliceCoords.append(puntosCoord[each_point])  # cojo las coords de los puntos para pintarlos
        filtracionCoords.append(simpliceCoords)  # una vez tengo el simplice con las coords entero lo guardo
    # printeo segun si es punto, arista o triangulo
    for simplice in filtracionCoords:
        if len(simplice) == 1:
            plt.plot(simplice[0][0], simplice[0][1], 'ko')
        elif len(simplice) == 2:
            X = [item[0] for item in simplice]
            Y = [item[1] for item in simplice]
            plt.plot(X, Y, "k")
        elif len(simplice) == 3:
            t1 = plt.Polygon(simplice, color="green")
            plt.gca().add_patch(t1)
    # Codigo para guardar las graficas
    plt.savefig(directorio + "/" + str(nombreFich) + '.png')
    plt.close()


def cleanDir():
    # borrar directorio de guardar imagenes si existe y volverlo a crear
    if os.path.exists(directorio):
        shutil.rmtree(directorio)
    if not os.path.exists(directorio):
        os.makedirs(directorio)


def make_gif():
    files = os.listdir(directorio)
    files.sort(key=lambda x: int(x.split(".")[0]))
    images = []
    for filename in files:
        images.append(imageio.imread(directorio + '/' + filename))
    imageio.mimsave(directorio + '/' + 'awesome.gif', images, fps=3)


def VietorisRips(points):
    """
    Dado una serie de puntos calcula el complejo de Vietoris-Rips asociado con los pesos, siendo estos las distancias
    Se sigue el algoritmo de Vietoris-Rips de la clase 4
    :return:
    """
    # para cada simplice calcular la arista mas larga y ese sera el diam del simplice --> maximos son de dimension 2
    # primero aristas les asigno su distancia
    # para cada triang le asigno el de la mayor arista

    # pasar primero puntos a array de nºs --> [0,1,2...]
    # crear un complejo con ello para usar getCarasDim de dim 0,1,2
    # meto los puntos con peso 0
    # meto las aristas con peso su diam * 0.5
    # meto los triangs con con peso el de la arista de mayor diam -->
    # diam*0.5 ==> bucle para dim hasta n-1 (n=nº de puntos)

    lst = list(range(0, len(points)))  # range hace [a,b)

    complejoAux = Complejo([tuple(lst)])  # creo un complejo con simplice maximal todos los vertices
    complejoVietoris = Complejo([])

    # obtenemos las logitudes de las aristas
    longitudes = {}  # CLAVE: 'punto1punto2', VALOR: dist(punto1, punto2)

    for i in lst:
        carasDimi = complejoAux.getCarasDim(i)

        # metemos los puntos con peso 0
        if i == 0:
            for elem in carasDimi:
                complejoVietoris.anadirSimplice([elem], 0.0)
        # calculamos la longitud de la arista y lo metemos con peso 0.5 porq simpl € si diam(simpl) <= 2r
        elif i == 1:
            for elem in carasDimi:
                valor = 0.5 * dist(points[elem[0]], points[elem[1]])
                # lo añado con valor r arist pertenece a VR(r) si diam <= 2r --> radio <= r
                complejoVietoris.anadirSimplice([elem], valor)
                longitudes.update({str(elem[0]) + '-' + str(elem[1]): valor}) # lo guardo en un dic para luego triangs
        # caso de dim mayor su peso sera el peso de la arista de mayor diam
        else:
            for elem in carasDimi:
                # creo un complejo con el triangulo para conseguir las aristas asociadas -->
                # el diam de un triangulo es el diam maximo de las aristas
                complejoAux2 = Complejo([elem])
                aristas = complejoAux2.getCarasDim(1)
                peso_complejo = None
                # obtengo la longitud maxima de las aristas que forman un simplice
                for each_arista in aristas:
                    if peso_complejo is None:
                        peso_complejo = longitudes.get(str(each_arista[0]) + '-' + str(each_arista[1]))
                    # si ya tiene un valor previo me quedo con el maximo
                    else:
                        peso_complejo = max(peso_complejo,
                                            longitudes.get(str(each_arista[0]) + '-' + str(each_arista[1])))
                # una vez tengo calculado su peso añado el triangulo
                complejoVietoris.anadirSimplice([elem], peso_complejo)

    return complejoVietoris
