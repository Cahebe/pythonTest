import numpy as np

rng = np.random.default_rng(seed=5)

vector_1 = rng.integers(low=-10, high=10, size=4)
matrix_1 = rng.integers(low=-10, high=10, size=12).reshape(4, 3)

print('-------------------------------------------------')
print('------NP.PERCENTILE------')  # retorna o percentil solicitado
# o valor (q) tem que estar entre 0 e 100
print(np.percentile(a=vector_1, q=10))  # retornará o percentil de 10% dos dados
print('-------------------------------------------------')
print(np.percentile(a=vector_1, q=50))  # retorna a mediana (50%)
print('-------------------------------------------------')
print(np.percentile(a=matrix_1, q=50))  # tb pode-se utilizar a função para
# calcular o percentil de matrizes, que são convertidas para vetor para
# fazer o calculo
print('-------------------------------------------------')
print('------NP.QUANTILE------')  # mesmo comportamento de 'np.percentile'
# porem o valor (q) deve ser entre 0 e 1
print(np.quantile(a=vector_1, q=0.1))
print('-------------------------------------------------')
print(np.quantile(a=matrix_1, q=0.5, axis=1))
print('-------------------------------------------------')
print('------NP.MEDIAN/MEAN/AVERAGE------')  # Mediana/Média/Média ponderada
print(np.median(a=vector_1))
print('-------------------------------------------------')
print(np.median(a=matrix_1, axis=1))
print('-------------------------------------------------')
print(np.mean(a=vector_1))
print('-------------------------------------------------')
print(np.average(a=vector_1, weights=[0.15, 0.25, 0.4, 0.2]))  # o somatório
# weights deve ser igual a 1
print('-------------------------------------------------')
print('------NP.STD/VAR------')  # desvio padrão/variancia
print(np.std(a=vector_1))
print('-------------------------------------------------')
print(np.std(a=matrix_1, axis=1))  # desvio padrão de cada uma das linhas
print('-------------------------------------------------')
print(np.var(a=matrix_1, axis=1))
print('-------------------------------------------------')
print('------NP.COV------')  # covariancia
print(np.cov(m=vector_1))  # covariancia do vetor 1 com ele mesmo
print('-------------------------------------------------')
vector_2 = vector_1 * 3
print(np.cov(m=vector_1, y=vector_2))  # covariancia do vetor 1 com o vetor 2
print('-------------------------------------------------')
print('------NP.CORRCOEF------')  # coeficiente de correlação
# de Peason entre 2 arrays -- util para obter a similaridade entre 2 vetores
print(np.corrcoef(vector_1, vector_1))  # resultado é uma escala de 0 a 1
# quanto menor o valor, menos associados os valores estão..
print('-------------------------------------------------')
print(np.corrcoef(vector_1, vector_2))  # neste exemplo o resultado é 1
# pois o vector_2 é multiplo do vector_1
print('-------------------------------------------------')
print('------NP.HISTOGRAM------')
vector_3 = rng.integers(low=-10, high=10, size=100)
hist, bin_edges = np.histogram(a=vector_3, bins=4)  # bins são os intervalos
print(hist, bin_edges)
print('1° intervalo = -10 a -5.25 / existem 28 valores nesse intervalo')
print('2° intervalo = -5.25 a -0.5 / existem 24 valores nesse intervalo..assim em diante')
print('-------------------------------------------------')
hist, bin_edges = np.histogram(a=vector_3, bins=4, density=True)  # densidade
print(hist, bin_edges)
print('-------------------------------------------------')
print('------NP.BINCOUNT------')
vector_4 = np.arange(6)
vector_5 = rng.integers(low=0, high=10, size=6)
print(vector_4, 'vetor 4')
print('-------------------------------------------------')
print(vector_5, 'vetor 5')
print('-------------------------------------------------')
print(np.bincount(vector_4), 'vetor 4 = 1 valor em cada posição')
print('-------------------------------------------------')
print(np.bincount(vector_5), 'vetor 5 = (0) 0, (1) 1, (0) 2..assim sucessivamente')
print('-------------------------------------------------')
print('------CONSTANTES------')
print('------NP.E------')
print(np.e)
print('------NP.PI------')
print(np.pi)
print('------NP.INFO------')  # valores infinitos
print(np.info())
print('------NP.NAN------')  # not a number
print(np.log(-1))  # não é possivel fazer o logaritmo de números negativos
print('------NP.NEWAXIS------')  # novos eixos
array_para_teste = np.array([1, 2, 3])
array_para_teste_2 = array_para_teste[np.newaxis]
print(array_para_teste_2)
