import numpy as np

rng = np.random.default_rng(seed=2)
array_1 = rng.integers(low=-10, high=10, size=20).reshape(4, 5)
array_2 = rng.integers(low=-10, high=10, size=20).reshape(4, 5)
print(array_1)
print('------------')
print(array_2)
print('------------')

print('------ADD------')  # operação com Phyton Puro
print(np.add(array_1, array_2))  # array_1 + array_2

print('------SUBTRACT------')
print(np.subtract(array_1, array_2))  # array_1 - array_2

print('------MULTIPLY------')
print(np.multiply(array_1, array_2))  # array_1 * array_2

print('------DIVIDE------')
print(np.divide(array_1, array_2))  # array_1 / array_2

print('------MOD------')
print(np.mod(array_1, 2))  # array_1 % 2

print('------DIVMOD------')
print(np.divmod(array_1, 2))  # primeiro divide, depois resto da divisão

print('------ABSOLUTE------')
print(np.absolute(array_1))

print('------DIFF------')
print(np.diff(a=array_1))  # diferença entre um valor e o proximo
print('------------')
print(np.diff(a=array_1, axis=0))
print('------------')
print(np.diff(a=array_1, n=2))  # diferença da diferença
print('------------')

print('------POWER------')
print(np.power(array_1, 2))  # elevação = array_1 ** 2
print('------------')
print(np.power(array_1, [[2], [2], [3], [3]]))  # 1° e 2° linhas ao quadrado
# 3° e 4° ao cubo
print('------------')
print(np.power(array_1, [[2, 2, 3, 3, 3]]))  # colunas 1 e 2 ao quadrado
# 3, 4 e 5 ao cubo

print('------EXP------')
print(np.exp(array_1))  # elevação ao número de Euler
print('------------')

print('------LOG------')
print(np.log(array_1))  # calcula o logaritmo
print('------------')

print('------RECIPROCAL------')
print(np.reciprocal(array_1.astype(float)))  # retorna os valores reciprocos
# 1 / array_1
print('------------')

print('------SQRT------')
print(np.sqrt(array_1))  # raiz quadrada
print('------------')

print('------CBRT------')
print(np.cbrt(array_1))  # raiz cubica
print('------------')

print('------GCD------')
print(np.gcd(array_1, array_2))  # greatest common divisor
print('------------')

print('------LCM------')
print(np.lcm(array_1, array_2))  # lowest commom multiple
print('------------')

print('------PI------')
pi = np.radians(180)
print(pi)
print('------------')

print('------SENO/SIN------')
print(np.sin(pi))
print('------------')

print('------COSENO/COS------')
print(np.cos(pi))
print('------------')

print('------TANGENTE/TANH------')
print(np.tanh(pi))
print('------------')

print('------ARCO TANGENTE/ARCTAN------')
print(np.arctan(1))
print('------------')

print('------MAXIMUM/MINIMUM------')
print(np.maximum(array_1, array_2))  # exibe o valor maximo, na mesma posição
# entre os 2 arrays
print('------------')
print(np.minimum(array_1, array_2))  # minimo
print('------------')

print('------GREATER/GREATER_EQUAL------')
print(np.greater(array_1, array_2))  # o valor do array_1 é maior?!
print('------------')
print(np.greater_equal(array_1, array_2))  # maior ou igual?!
print('------------')

print('------LESS/LESS_EQUAL------')
print(np.less(array_1, array_2))  # o valor do array_1 é menor?!
print('------------')
print(np.less_equal(array_1, array_2))  # menor ou igual?!
print('------------')

print('------NOT_EQUAL/EQUAL------')
print(np.not_equal(array_1, array_2))  # os valores não são iguais?
print('------------')
print(np.equal(array_1, array_2))  # são iguais?
print('------------')

print('------LOGICAL_AND/LOGICAL_OR/LOGICAL_XOR/LOGICAL_NOT------')
comparison_1 = array_1 > 0  # numeros positivos
comparison_2 = np.mod(array_1, 2) == 0  # numeros pares
print(np.logical_and(comparison_1, comparison_2))  # positivos E pares
# PYTHON PURO = comparison_1 & comparision_2
print('------------')
print(np.logical_or(comparison_1, comparison_2))  # positivos OU pares
# PYTHON PURO = comparison_1 | comparision_2
print('------------')
print(np.logical_xor(comparison_1, comparison_2))  # NEM positivos NEM pares
print('------------')
print(np.logical_not(comparison_1, comparison_2))  # positivos POREM NÃO pares
# PYTHON PURO = comparison_1 != comparision_2
print('------------')

print('------ISCLOSE/ALLCLOSE------')
array_close_1 = np.array([1.554, 0.999, -1.001])
array_close_2 = np.array([1.555, 0.998, -1.000])
print(np.isclose(a=array_close_1, b=array_close_2, atol=0.001))
# analisa elmento por elemento
# a=array 1, b=array 2, atol=tolerancia
print('------------')
print(np.allclose(a=array_close_1, b=array_close_2, atol=0.001))
# analisa o array completo
print('------------')

print('------ARRAY_EQUAL------')
print(np.array_equal(array_1, array_2))  # verifica se são identicos
# mesma forma e mesmos elementos
print('------------')

print('------ISFINITE/ISINF/ISNEGINF/ISNAN------')
print(np.isfinite(np.divide(1, 0)))  # 1 / 0 = infinito
print('------------')
print(np.isinf(np.divide(1, 0)))  # 1 / 0 = infinito
print('------------')
print(np.isneginf(np.divide(-1, 0)))  # -1 / 0 = infinito e negativo
print('------------')
print(np.isnan(np.log(-1)))  # logaritmo de -1 não existe, então 'NotANumber'
print('------------')

print('------FLOOR/CEIL/TRUNC------')
print(np.floor([-3.6, 2.7, 0.4, 7.0]))  # arredonda para baixo
print('------------')
print(np.ceil([-3.6, 2.7, 0.4, 7.0]))  # arredonda para cima
print('------------')
print(np.trunc([-3.6, 2.7, 0.4, 7.0]))  # arredonda para o valor
# mais proximo de zero
print('------------')