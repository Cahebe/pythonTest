import numpy as np

rng = np.random.default_rng(seed=2)
vector_1 = rng.integers(low=-10, high=10, size=4)
vector_2 = rng.integers(low=-10, high=10, size=4)
matrix_1 = rng.integers(low=-10, high=10, size=12).reshape(4, 3)
matrix_2 = rng.integers(low=-10, high=10, size=12).reshape(3, 4)
matrix_3 = rng.integers(low=-10, high=10, size=12).reshape(4, 3)
matrix_4 = rng.integers(low=-10, high=10, size=9).reshape(3, 3)
print('-------------------------------------------------')
print(vector_1)
print('-------------------------------------------------')
print(vector_2)
print('-------------------------------------------------')
print(matrix_1)
print('-------------------------------------------------')
print(matrix_4)
print('-------------------------------------------------')

print('------NP.DOT------')
print(np.dot(a=vector_1, b=vector_2))  # calcula o produto entre 2 vetores
print('-------------------------------------------------')
print(np.dot(a=matrix_1, b=matrix_2))  # tb retorna a multiplicação matricial
print('-------------------------------------------------')
print(np.dot(a=matrix_2, b=vector_1))  # soma do produto do ultimo eixo
# do vetor + o tensor
print('-------------------------------------------------')

print('------NP.VDOT------')  # aceita somente vetores
print(np.vdot(vector_1, vector_2))  # calcula o produto entre 2 vetores
print('-------------------------------------------------')
print('------NP.INNER------')  # calcula o produto interno de vetores
# e matrizes
print(np.inner(vector_1, vector_2))
print('-------------------------------------------------')
print(np.inner(matrix_1, matrix_3))
print('-------------------------------------------------')
print('------NP.OUTER------')  # produto externo
print(np.outer(a=vector_1, b=vector_2))
print('-------------------------------------------------')
print('------NP.MATMUL------')  # produto matricial entre 2 arrays
print(np.matmul(vector_1, vector_2))  # resultado = produto interno
print('-------------------------------------------------')
print(np.matmul(matrix_1, matrix_2))  # resultado = produto matricial
print('-------------------------------------------------')
print('------NP.LINALG.DET------')  # retorna o determinante para
# arrays quadrados
print(np.linalg.det(matrix_4))
print('-------------------------------------------------')
print('------NP.LINALG.INV------')  # matriz inversa
print(np.linalg.inv(matrix_4))


