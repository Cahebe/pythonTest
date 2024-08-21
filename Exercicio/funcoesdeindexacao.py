import numpy as np

array = np.arange(0, 1, 0.1).reshape(2, 5)
print(array)
array2 = np.arange(1, 2, 0.1).reshape(2, 5)
print(array2)
array_square = np.arange(0, 9).reshape(3, 3)

print('------NONZERO------')
print(np.nonzero(array))

print('------WHERE------')
print(np.where(array < 0.4))
print(np.where(array < 0.4, 0, 1))  # se a condição for verdadeira preenche com 0,
# se for falsa preenche com 1
print(np.where(array < 0.4, array, array + 10))  # se a condição for verdadeira
# preenche com o array original,
# se falsa preenche com array + 10
print(np.where(array < 0.4, array, array2))  # se verdadeiro preenche com array
# se falso preenche com array2
array_par_impar = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # par/impar
print(np.where(array_par_impar % 2 == 0, 'par', 'impar'))

print('------ARGWHERE------')
print(np.argwhere(array < 0.4))  # retorna os indices em forma de tupla
# linha 0, coluna 0...assim sucessivamente

print('------SELECT------')  # igual WHERE mas pode passar mais condições
print(np.select(condlist=[array < 0.4, array > 0.6], choicelist=[array + 10, array + 20], default=-1))
#  condList = lista de condições -- choiceList = o que fazer --
#  default = valor padrão caso as condições não sejam atendidas

print('------UNRAVEL_INDEX------')
print(np.unravel_index(indices=12, shape=(4, 5)))  # retorna a posição do 12°
# elemento em um array de shape 4, 5

print('------DIAG_INDICES------')
array_2d = np.arange(0, 16).reshape(4, 4)
indices = np.diag_indices(n=4, ndim=2)  # retorna a diagonal principal
# n = inteiro que especifica a dimensão
# ndim = n° de dimensões
print(indices)
array_2d[indices] = -1
print(array_2d)

print('------TRIL_INDICES------')  # triangulo inferior
array_triangle = np.arange(0, 9).reshape(3, 3)
indices_tril = np.tril_indices(n=3, m=3)  # n = linhas, m = colunas
print(indices_tril)
print(array_triangle[indices_tril])

print('------TRIU_INDICES------')  # triangulo superior
array_triangle2 = np.arange(0, 9).reshape(3, 3)
indices_triu = np.triu_indices(n=3, m=3)  # n = linhas, m = colunas
print(indices_triu)
print(array_triangle2[indices_triu])

print('------DIAG_INDICES_FROM, TRIL_INDICES_FROM e TRIU_INDICES_FROM------')
print(np.diag_indices_from(array_square))  # indices diagonal principal
print(np.tril_indices_from(array_square))  # triangulo inferior
print(np.triu_indices_from(array_square))  # triangulo superior
