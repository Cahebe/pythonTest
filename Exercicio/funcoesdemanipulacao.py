import numpy as np

array = np.arange(0, 1, 0.1).reshape(2, 5)
print(array)
array2 = np.arange(1, 2, 0.1).reshape(2, 5)
print(array2)
array_concatenated = np.concatenate([array, array2])
array_par = np.arange(0, 18).reshape(3, 6)

print('------CONCATENATE------')
print(np.concatenate([array, array2]))
print('------------')

print('------STACK------')
array_stacked = np.stack(arrays=[array, array2])
print(array_stacked)
print('------------')

print('------VSTACK------')
print(np.vstack(tup=[array, array2]))  # mesmo resultado do np.concatenate axis=0
print('------------')

print('------HSTACK------')
print(np.hstack(tup=[array, array2]))  # mesmo resultado do np.concatenate axis=1
print('------------')

print('------SPLIT------')
print(np.split(ary=array, indices_or_sections=2))
print('------------')
print('------VSPLIT------')
print(np.vsplit(ary=array_par, indices_or_sections=3))  # igual np.split
print('------------')
print('------HSPLIT------')
print(np.hsplit(ary=array_par, indices_or_sections=3))
print('------------')

print('------EXPAND_DIMS, NEWAXIS e RESHAPE------')  # obtem o mesmo resultado
new_array_3D = np.expand_dims(a=array_par, axis=1)  # contrario da np.squeeze()
print(new_array_3D)
print('------------')
new_array_3D_1 = array_par[:, np.newaxis, :]
print(new_array_3D_1)
print('------------')
print(array_par.reshape(3, 1, 6))

print('------FLIP------')
print(np.flip(array))
print('------------')

print('------RESIZE------')
print(np.resize(a=array, new_shape=8))
print('------------')
print(np.resize(a=array, new_shape=(3, 6)))
print('------------')

print('------INSERT------')
print(np.insert(arr=array, obj=2, values=9, axis=1))  # obj = posição
print('------------')
print(np.insert(arr=array, obj=2, values=[8, 9], axis=1))
print('------------')
print(np.insert(arr=array, obj=0, values=9, axis=0))
print('------------')

print('------DELETE------')
array_delete_axis1 = np.delete(arr=array, obj=2, axis=1)
print(array_delete_axis1)
print('------------')
array_delete_axis0 = np.delete(arr=array, obj=0, axis=0)
print(array_delete_axis0)
print('------------')

print('------APPEND------')
array_append = np.append(arr=array, values=array2, axis=0)  # mesmo resultado de np.concatenate axis=0
print(array_append)
print('------------')

print('------TILE------')
print(np.tile(A=array, reps=(2, 4)))  # reps = 2 vezes eixo 0 e 4 vezes eixo 1
print('------------')
print(np.tile(A=array, reps=(3, 1)))
print('------------')

print('------PAD------')
print(np.pad(array=array2, pad_width=(3, 4), mode="constant", constant_values=0))
# foram adicionadas 3 linhas/colunas antes e 4 linhas/colunas depois
print('------------')
print(np.pad(array=array2, pad_width=(3, 4), mode="edge"))
print('------------')
print(np.pad(array=array2, pad_width=(3, 4), mode="minimum"))  # preenchido com o valor minimo
print('------------')
print(np.pad(array=array2, pad_width=(3, 4), mode="maximum"))  # valor maximo
print('------------')
print(np.pad(array=array2, pad_width=(3, 4), mode="mean"))  # média
print('------------')

print('------TRIM_ZEROS------')  # só funciona com arrays 1D
array_zeros = np.array([0, 0, 0, 1, 2, 3, 0, 0, 0])
print(np.trim_zeros(filt=array_zeros))
print('------------')
print(np.trim_zeros(filt=array_zeros, trim="f"))  # f = front
print('------------')
print(np.trim_zeros(filt=array_zeros, trim="b"))  # b = back
print('------------')

print('------UNIQUE------')
rng = np.random.default_rng(seed=75)
array_unique = rng.integers(low=50, high=75, size=200)
print(array_unique)
print('------------')
unique_values, indices_first, indices_redo, counts = np.unique(array_unique, return_index=True, return_inverse=True,
                                                               return_counts=True)
print("Unique values", unique_values)  #  valores unicos
print('------------')
print("Indices first", indices_first)  #  indices onde cada valor aparece 1°
print('------------')
print("Indices redo", indices_redo)  # indices que podem ser utilizados para reconstruir o array original
print('------------')
print("Counts", counts)  # contagem dos valores unicos
print('------------')
print(unique_values[indices_redo])  # array original reconstruido