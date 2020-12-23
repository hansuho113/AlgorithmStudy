import numpy as np

a = np.array([1,2,3,4,5])

print(np.min(a), np.argmin(a))

print(np.where(a>2, a, 0))