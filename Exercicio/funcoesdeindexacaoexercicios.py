import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import pairwise_distances

rng = np.random.default_rng(seed=60)
array = rng.integers(low=0, high=7, size=50).reshape(2, 5, 5)
array_square1 = rng.integers(0, 50, size=(6, 2))
print(array_square1)
print(array)

print('------NONZERO------')
print(np.nonzero(array))
indices2 = np.nonzero(array)
print(array[indices2])
print()

print('------WHERE------')
print(np.where(array < 0.4))
print(np.where(array < 0.4, 0, 1))  # se a condição for verdadeira preenche com 0,
# se for falsa preenche com 1
print(np.where(array == 0, np.nan, array * 2))  # se a condição for verdadeira
# preenche com o array original,
# se falsa preenche com array + 10
array_par_impar = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # par/impar
print(np.where(array_par_impar % 2 == 0, 'par', 'impar'))

print('------ARGWHERE------')
print(np.argwhere(array != 0))  # retorna os indices em forma de tupla
# linha 0, coluna 0...assim sucessivamente

print('------SELECT------')  # igual WHERE mas pode passar mais condições
print(np.select(condlist=[array == 0, array != 0], choicelist=[np.nan, array * 2]))
#  condList = lista de condições -- choiceList = o que fazer --
#  default = valor padrão caso as condições não sejam atendidas

print('------UNRAVEL_INDEX------')
print(np.unravel_index(indices=35, shape=(2, 5, 5)))  # retorna a posição do 12°
# elemento em um array de shape 4, 5

print('------DIAG_INDICES------') # descomentar
#  plt.scatter(array_square1[:, 0], array_square1[:, 1])
print('------PLT_SHOW()------')  # descomentar
# plt.show()
distance = pairwise_distances(array_square1, array_square1)
print(distance)
array_2d = np.arange(0, 16).reshape(4, 4)
indices = np.diag_indices(n=6, ndim=2)  # retorna a diagonal principal
# n = inteiro que especifica a dimensão
# ndim = n° de dimensões
values_diag = distance[indices]
print(indices)
print(values_diag)
mask = values_diag == 0
print(mask)
print(mask.all())
print(distance)


print('------TRIL_INDICES------')  # triangulo inferior
array_triangle = np.arange(0, 9).reshape(3, 3)
indices_tril = np.tril_indices(n=6, m=5)  # n = linhas, m = colunas
print(indices_tril)
distance[indices_tril] = 0
print(distance)

print('------TRIU_INDICES------')  # triangulo superior
array_triangle2 = np.arange(0, 9).reshape(3, 3)
indices_triu = np.triu_indices(n=3, m=3)  # n = linhas, m = colunas
print(indices_triu)
print(array_triangle2[indices_triu])

print('------DIAG_INDICES_FROM, TRIL_INDICES_FROM e TRIU_INDICES_FROM------')
print(np.diag_indices_from(array_square))  # indices diagonal principal
print(np.tril_indices_from(array_square))  # triangulo inferior
print(np.triu_indices_from(array_square))  # triangulo superior
