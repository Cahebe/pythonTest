import numpy as np

rng = np.random.default_rng(seed=5)

scores = np.clip( # limita as notas para o intervalo [0, 10]
    a=np.round( # arredondamento das notas para 1 casa decimal
        a=rng.normal(loc=7, scale=2, size=20), # amostra de números com distribuição normal
        decimals=1
        ),
    a_min=0,
    a_max=10
).reshape(5, 4) # altera para o shape desejado
print(scores)
print('-------------------------------------------------')
weights = np.array([[0.2],
                    [0.3],
                    [0.4],
                    [0.1]])
print(weights)
print('-------------------------------------------------')
print('------NP.DOT------')  # calcula o produto entre 2 vetores
print(np.dot(a=scores, b=weights))
print('-------------------------------------------------')
print('------NP.VDOT------')  # aceita somente vetores
scores_2 = scores[2, :]  # notas apenas do aluno de indice 2
print(scores_2)
print(np.vdot(scores_2, weights.ravel()))
print('-------------------------------------------------')
print('------NP.INNER------')  # calcula o produto interno de vetores
# e matrizes
print(np.inner(scores_2, weights.ravel()))
print('-------------------------------------------------')
print('------NP.MATMUL------')  # produto matricial entre 2 arrays
print(np.matmul(scores_2, weights.ravel()))
print('-------------------------------------------------')
print('------NP.OUTER------')  # produto externo
array_0 = np.array([2, 3, 7])
array_1 = np.array([0.7, 0.2, 0.3, 0.4])
print(np.outer(a=array_0, b=array_1))
print('-------------------------------------------------')
print('------NP.LINALG.DET------')  # retorna o determinante para
# arrays quadrados
array_2 = rng.normal(loc=5, scale=2, size=16).reshape(4, 4)
print(array_2)
print('-------------------------------------------------')
print(np.linalg.det(array_2))
print('-------------------------------------------------')
print('------NP.LINALG.INV------')
array_2_inv = np.linalg.inv(array_2)
print(array_2_inv)
print('-------------------------------------------------')
array_mul = np.matmul(array_2, array_2_inv)
print(array_mul)
print('-------------------------------------------------')
array_identity = np.identity(n=4)
print(array_identity)
print('-------------------------------------------------')
print(np.allclose(a=array_mul, b=array_identity))  # verifica se os 2 arrays são iguais
