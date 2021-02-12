"""
By DHNNAM

Se supone que se hace a mano, pero que hueva.
"""
import numpy as np

"""Ejercicios 1"""
# Criterios
a = lambda x: 2*x-1

# Conjuntos globales
U = set(np.arange(1, 50, 1))
A = set(2*np.arange(1, 18, 1)-1)
B = set(2*np.arange(1, 39, 1))
C = set(5*np.arange(1, 100, 1))
D = set(10*np.arange(1, 100, 1))

# Define por enumeracion
res_a = B.intersection(A.union(C))
res_b = B.intersection(A).intersection(D)
res_c = A.intersection(U.difference(B))-C
res_d = A-(B.intersection(U.difference(C)))

print(res_a, res_b, res_c, res_d)

# Proposiciones verdad o falso
res_e = False
res_f = True
res_g = False
res_h = False # len(B.intersection(A.union(C))) == 3
res_i = False
res_j = True
res_k = "???"


    