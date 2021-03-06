from practica1.Complejo import Complejo
import numpy as np

def imprimir_matriz(matriz):
    print(np.array(matriz))
    print("---------------------------------------------------------------------")


# EJEMPLO 1 (Tetraedro)
print("EJEMPLO 1 (Tetraedro)")
sc = Complejo([(0, 1, 2, 3)])

print("Matriz borde 1:")
imprimir_matriz(sc.matriz_borde(1))

print("Matriz borde 2:")
imprimir_matriz(sc.matriz_borde(2))

print("Matriz borde 3:")
imprimir_matriz(sc.matriz_borde(3))


print("Nºs de Betti del tetraedro: ", sc.betti_number(0), sc.betti_number(1), sc.betti_number(2), sc.betti_number(3))
print("---------------------------------------------------------------------")

# EJEMPLO 2 (2-Esfera - Borde tetraedro)
print("EJEMPLO 2 (2-Esfera - Borde tetraedro)")
sc1 = Complejo(list(sc.getCarasDim(2)))


print("Nºs de Betti de la 2-esfera: ", sc1.betti_number(0), sc1.betti_number(1), sc1.betti_number(2))
print("---------------------------------------------------------------------")

# EJEMPLO 3 (Complejo simplicial diap 4)
print("EJEMPLO 3 (Complejo simplicial diap 4)")
sc = Complejo([(0, 1), (1, 2, 3, 4), (4, 5), (5, 6), (4, 6), (6, 7, 8), (8, 9)])

print("Matriz borde 1:")
imprimir_matriz(sc.matriz_borde(1))

print("Matriz borde 2:")
imprimir_matriz(sc.matriz_borde(2))

print("Matriz borde 3:")
imprimir_matriz(sc.matriz_borde(3))


print("Nºs de Betti: ", sc.betti_number(0), sc.betti_number(1), sc.betti_number(2), sc.betti_number(3))
print("---------------------------------------------------------------------")

# EJEMPLO 4 (1-esqueleto del comp simplicial)
print("EJEMPLO 4 (1-esqueleto del comp simplicial)")
sc1 = Complejo(list(sc.getCarasDim(1)))

print("Nºs de Betti: ", sc1.betti_number(0), sc1.betti_number(1))
print("---------------------------------------------------------------------")

# EJEMPLO 5 (Complejo simplicial)
print("EJEMPLO 5 (Complejo simplicial)")
sc = Complejo([(0, 1, 2), (2, 3), (3, 4)])

print("Matriz borde 1:")
imprimir_matriz(sc.matriz_borde(1))

print("Matriz borde 2:")
imprimir_matriz(sc.matriz_borde(2))


print("Números de Betti: ", sc.betti_number(0), sc.betti_number(1), sc.betti_number(2))
print("---------------------------------------------------------------------")

# EJEMPLO 6 (Anillo)
print("EJEMPLO 6 (Anillo)")
sc = Complejo([(1, 2, 4), (1, 3, 6), (1, 4, 6), (2, 3, 5), (2, 4, 5), (3, 5, 6)])

print("Matriz borde 1:")
imprimir_matriz(sc.matriz_borde(1))

print("Matriz borde 2:")
imprimir_matriz(sc.matriz_borde(2))


print("Números de Betti: ", sc.betti_number(0), sc.betti_number(1), sc.betti_number(2))
print("---------------------------------------------------------------------")

# EJEMPLO 7 (1-esqueleto del anillo)
print("EJEMPLO 7 (1-esqueleto del anillo)")
sc1 = Complejo(list(sc.getCarasDim(1)))

print("Nºs de Betti: ", sc1.betti_number(0), sc1.betti_number(1))
print("---------------------------------------------------------------------")

# EJEMPLO 8 (Toro)
print("EJEMPLO 8 (Toro)")
sc = Complejo([(1, 2, 4), (2, 4, 5), (2, 3, 5), (3, 5, 6), (1, 3, 6), (1, 4, 6),
               (4, 5, 7), (5, 7, 8), (5, 6, 8), (6, 8, 9), (4, 6, 9), (4, 7, 9), (1, 7, 8), (1, 2, 8),
               (2, 8, 9), (2, 3, 9), (3, 7, 9), (1, 3, 7)])

print("Matriz borde 1:")
imprimir_matriz(sc.matriz_borde(1))

print("Matriz borde 2:")
imprimir_matriz(sc.matriz_borde(2))

print("Nºs de Betti del borde del toro: ", sc.betti_number(0), sc.betti_number(1), sc.betti_number(2))
print("---------------------------------------------------------------------")

# EJEMPLO 8 (1-esqueleto del toro)
print("EJEMPLO 8 (1-esqueleto del toro)")
sc1 = Complejo(list(sc.getCarasDim(1)))

print("Nºs de Betti: ", sc1.betti_number(0), sc1.betti_number(1))
print("---------------------------------------------------------------------")

# EJEMPLO 9 (Plano proyectivo)
print("EJEMPLO 9 (Plano proyectivo)")
sc = Complejo(
    [(1, 2, 6), (2, 3, 4), (1, 3, 4), (1, 2, 5), (2, 3, 5), (1, 3, 6), (2, 4, 6), (1, 4, 5), (3, 5, 6), (4, 5, 6)])

print("Matriz borde 1:")
imprimir_matriz(sc.matriz_borde(1))

print("Matriz borde 2:")
imprimir_matriz(sc.matriz_borde(2))

print("Nºs de Betti: ", sc.betti_number(0), sc.betti_number(1), sc.betti_number(2))
print("---------------------------------------------------------------------")

# EJEMPLO 10 (Comp simplicial)
print("EJEMPLO 10 (Comp simplicial)")
sc = Complejo([(0,), (1,), (2, 3), (4, 5), (5, 6), (4, 6), (6, 7, 8, 9)])

print("Matriz borde 1:")
imprimir_matriz(sc.matriz_borde(1))

print("Matriz borde 2:")
imprimir_matriz(sc.matriz_borde(2))


print("Nºs de Betti: ", sc.betti_number(0), sc.betti_number(1), sc.betti_number(2), sc.betti_number(3))
print("---------------------------------------------------------------------")

# EJEMPLO (Otra triangulacion del toro)
print("EJEMPLO (Otra triang del toro)")
sc = Complejo([(1, 3, 7), (3, 4, 6), (4, 6, 7), (1, 6, 7), (1, 5, 6), (2, 3, 6),
               (1, 2, 3), (3, 4, 5),
               (2, 5, 6), (2, 5, 7), (3, 5, 7), (1, 4, 5), (1, 2, 4), (2, 4, 7)])

print("Matriz borde 1:")
imprimir_matriz(sc.matriz_borde(1))

print("Matriz borde 2:")
imprimir_matriz(sc.matriz_borde(2))

print("Nºs de Betti: ", sc.betti_number(0), sc.betti_number(1), sc.betti_number(2), sc.betti_number(3))
print("---------------------------------------------------------------------")

# EJEMPLO (Botella de Klein)
print("EJEMPLO (Botella de Klein)")
sc = Complejo(
    [(0, 1, 5), (0, 3, 5), (1, 2, 5), (2, 5, 6), (0, 2, 6), (0, 4, 6), (3, 4, 5), (4, 5, 7), (5, 6, 7), (6, 7, 8),
     (4, 6, 8), (3, 4, 8), (0, 4, 7), (0, 1, 7), (1, 7, 8), (1, 2, 8), (0, 2, 8), (0, 3, 8)])

print("Matriz borde 1:")
imprimir_matriz(sc.matriz_borde(1))

print("Matriz borde 2:")
imprimir_matriz(sc.matriz_borde(2))

print("Nºs de Betti: ", sc.betti_number(0), sc.betti_number(1), sc.betti_number(2))
print("---------------------------------------------------------------------")

# EJEMPLO (Sombrero del Asno)
print("EJEMPLO (Sombrero del Asno)")
sc = Complejo([(1, 3, 6), (3, 6, 7), (1, 5, 6), (1, 3, 5), (2, 3, 5), (2, 4, 5),
               (4, 5, 6),
               (4, 6, 8), (6, 7, 8), (1, 2, 7), (2, 3, 7), (1, 7, 8), (1, 2, 8),
               (2, 3, 8), (3, 4, 8), (1, 3, 4), (1, 2, 4)])

print("Matriz borde 1:")
imprimir_matriz(sc.matriz_borde(1))

print("Matriz borde 2:")
imprimir_matriz(sc.matriz_borde(2))



print("Nºs de Betti: ", sc.betti_number(0), sc.betti_number(1), sc.betti_number(2), sc.betti_number(3))
print("---------------------------------------------------------------------")

# EJEMPLO (Doble toro)
print("EJEMPLO (Doble toro)")
sc = Complejo([(1, 2, 3), (1, 3, 7), (3, 7, 11), (3, 9, 11), (9, 10, 11), (2, 3, 4),
               (2, 4, 8), (0, 4, 8), (0, 6, 8), (6, 7, 8), (5, 7, 11), (5, 6, 7),
               (4, 5, 6), (4, 6, 10), (2, 6, 10), (2, 8, 10), (8, 9, 10), (0, 1, 2),
               (0, 2, 6), (0, 1, 11), (0, 10, 11), (0, 4, 10), (1, 5, 11),
               (1, 5, 9), (1, 7, 9), (7, 8, 9), (3, 5, 9), (3, 4, 5)])

print("Matriz borde 1:")
imprimir_matriz(sc.matriz_borde(1))

print("Matriz borde 2:")
imprimir_matriz(sc.matriz_borde(2))

print("Nºs de Betti: ", sc.betti_number(0), sc.betti_number(1), sc.betti_number(2))
print("---------------------------------------------------------------------")
