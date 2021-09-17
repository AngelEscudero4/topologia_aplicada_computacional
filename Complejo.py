from itertools import combinations


class Complejo:
    # recibe lista de los simplices maximales
    def __init__(self, maximal_simplice_list):
        self.simplices = maximal_simplice_list

    def __print__(self):
        print(self.simplices)

    def dim(self):
        # la dimension del complejo es su simplice (lista) mas larga - 1
        return len(max(self.simplices, key=len)) - 1

    def getCaras(self):
        aux = []
        # recorremos los simplices maximales para construir las caras
        for cada_simplice in self.simplices:
            # para cada simplice construimos todas las caras (dimension menor que la del simplice)
            for i in range(1, len(cada_simplice)):
                aux = aux + list(combinations(cada_simplice, i))
        # como combinations nos devuelve tuplas -> casteamos a listas
        # tambien tenemos que eliminar los repetidos ya que [0,1] y [0,2] generan dos veces el 0
        aux = list(set(aux))
        caras = [list(x) for x in aux]
        caras.sort(key=len)  # ordenar por tamaño de simplices
        return caras

    """
    Falta por probar.
    """

    def getCarasDim(self, dim):
        aux = []
        listaSimplices = []
        # consigo los simplices que tengan una dimension superior o igual a la que quiero sacar las caras
        for x in self.simplices:
            if len(x) >= dim + 1:
                listaSimplices.append(x)

        # recorremos los simplices maximales para construir las caras
        for cada_simplice in listaSimplices:
            lista=list(combinations(cada_simplice, dim))
            # para cada simplice construimos todas las caras (dimension menor que la del simplice)
            aux = aux + lista
        # como combinations nos devuelve tuplas -> casteamos a listas
        caras = [list(x) for x in aux]
        return caras

    # recomendable hacer funcion auxiliar que nos diga si un elem es cara de otro elem
