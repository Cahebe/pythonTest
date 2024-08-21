import numpy as np

rng = np.random.default_rng(seed=1)
array = rng.normal(loc=50, scale=3, size=60).reshape(3, 5, 4).round(3)

array.itemset((2, 1, 0), 49.705)

print(array)

print(array.item(2, 1, 0))

array_view = array.view()
array_view.itemset((2, 1, 0), 49.705)

print(array.item(2, 1, 0), array_view.item(2, 1, 0))

array_copy = array.copy()
array_copy.itemset((2, 1, 0), 49.709)

print(array.item(2, 1, 0), array_copy.item(2, 1, 0))

print("------RESHAPE------")
array_reshape = array.reshape(3, 20)
print(array_reshape)

print("------TRANSPOSE------")
array_transpose = array.transpose((1, 2, 0))

print(array_transpose)

print("------SWAPAXES------")
array_swapaxes = array_transpose.swapaxes(1, 2)

print(array_swapaxes)

print("------FLATTEN(cópia) e RAVEL(view)------")
array_flatten = array.flatten()
array_ravel = array.ravel()

print(array_flatten)
print(array_ravel)

print("------SQUEEZE------")
array_first_day = array[0:1]
print(array_first_day.squeeze())

print("------TAKE------")
print(array.take(indices=[12, 25, 31, 40]))
print(array.take(indices=[[12, 31],
                          [25, 40]]))
print("------PUT------")
array_put = array.copy()
array_put.put(indices=[12, 25, 31, 40], values=[np.nan, np.nan, np.nan, np.nan])
print(array_put)

print("------REPEAT------")
array_repeat = array.repeat(repeats=2, axis=0)
print(array_repeat.shape)

print("------SORT------")
array_sort = array.copy()
array_sort.sort(axis=0)
print(array_sort)

print("------ARGSORT------")
print(array.argsort(axis=1))

print("------SEARCHSORTED------")
array_filtered = array_flatten.copy()
array_filtered.sort(axis=0)
print(array_filtered[0:16])
print(array_filtered.searchsorted([40.50, 42.357, 47.025, 48.952]))

print("------DIAGONAL------")
print(array[0].diagonal())
