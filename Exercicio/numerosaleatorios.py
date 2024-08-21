import numpy as np
import matplotlib.pyplot as plt

print('------RANDOM------')
rng = np.random.default_rng(seed=101)
# Gera dados logísticos

print(rng.random())
print('------------')
print(rng.random(size=5))
print('------------')
print(rng.random(size=(3, 4)))
print('------------')

print('------INTEGERS------')
print(rng.integers(10, size=8))
print('------------')
print(rng.integers(low=3, high=20, size=7))
print('------------')
print(rng.integers(size=3, low=[2, 7, 14], high=[10, 15, 25]))
print('------------')

print('------CHOICE------')
array = np.arange(5, 20)
print(rng.choice(a=array, size=7, replace=False))  # replace impede de repetir os valores
print('------------')
array2 = np.array([1, 2, 3])
probability = np.array([0.2, 0.7, 0.1])  # a soma deve dar 1
print(rng.choice(a=array2, size=10, p=probability))
print('------------')

print('------SHUFFLE, PERMUTATION e PERMUTED------')
rng.shuffle(array)
print(array)
print('------------')
rng.permutation(array)
print(array)
print('------------')
array3 = np.arange(20).reshape(4, 5)
print(array3)
print('     ******')
print(rng.permuted(array3, axis=1))
print('------------')

print('------DISTRIBUIÇÕES------')
print('------BETA------')
plt.hist(rng.beta(a=7, b=50, size=100_000), bins=100)
plt.show()

