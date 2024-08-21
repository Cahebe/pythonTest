import numpy as np

array_1 = np.array([0, 1, 2, 3, 4])
array_2 = np.array([5, 6, 7, 8, 9])

print('-------------------------------------------------')
print('------NP.SAVE/LOAD------')  # atenção às barras / \
np.save(file='array_1_file', arr=array_1)
array_1_loaded = np.load(file='/Users\Caheb\PycharmProjects\pythonTest\Exercicio/array_1_file.npy')
print(array_1_loaded)
print('-------------------------------------------------')
print('------NP.SAVEZ------')  # salva mais de um array
np.savez('array_savez', array_1, array_2)
arrays_loaded = np.load('array_savez.npz')
print(arrays_loaded, ' --> existem 2 arrays: arr_0 e arr_1')  #  print para
# verificar quais as chaves dos arrays
print(arrays_loaded['arr_0'])
print('-------------------------------------------------')
print('------NP.SAVEZ_COMPRESSED------')  # salva 1 ou mais arrays em
# 1 arquivo compactado
np.savez_compressed('array_compacted', array_1, array_2)
print('-------------------------------------------------')
print('------NP.SAVETXT/LOADTXT------')
array_2d = np.vstack([array_1, array_2])

np.savetxt(fname='array_csv.csv', X=array_2d, fmt='%s', delimiter=',')
# fmt='%s' = formato original -> delimiter=',' = delimitador é uma virgula
print('-------------------------------------------------')
print('------NP.SKIPROWS/USECOLS/MAXROWS------')
# skiprows: n° de linhas para pular do inicio do arquivo
# usecols: indices das colunas para carregar
# max_rows: n° máximo de linhas para carregar
