import numpy as np

rng = np.random.default_rng(seed=1)
array = rng.normal(loc=50, scale=3, size=60).reshape(3, 5, 4).round(3)

print('------MAX e ARGMAX------')
print(array.max(axis=0))
print('------------')
print(array.argmax(axis=0))
print('------------')
print(array.max())
print('------MIN e ARGMIN------')
print(array.min(axis=0))
print('------------')
print(array.argmin(axis=0))
print('------------')
print(array.min())

print('------PTP------')
print(array.ptp(axis=0))
print('------------')
print(array.ptp())

print('------CLIP------')
array_clip = array.copy()
print(array_clip.clip(min=43, max=55))

print('------ROUND------')
print(array.round(decimals=2))

print('------SUM------')
array_sum_axis_2 = array.copy()
array_sum_axis_0 = array_sum_axis_2.sum(axis=2)
print(array_sum_axis_2.sum(axis=2))
print('------------')
print(array_sum_axis_0.sum(axis=0))

print('------CUMSUM------')
print(array.cumsum(axis=2))

print('------MEAN------')
print(array.mean(axis=2))

print('------VAR------')
print(array.var(axis=2))

print('------STD------')
print(array.std(axis=2))

print('------PROD------')
print(array.var(axis=1))

print('------CUMPROD------')
print(array.cumprod(axis=1))

print('------ALL------')
array_mask = array > 50
print(array_mask)
print('------------')
print(array_mask.all(axis=2))

print('------ANY------')
print(array_mask.any(axis=2))

