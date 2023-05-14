import numpy as np
a = np.array([[1, 2, 3]
             ,[4, 5, 6]
             ,[7, 8, 9]])
print(a)
print(np.sqrt(a))
print(a.sum(axis=1))
print(a.reshape(1,9))
print(a.size)
print(a.shape)

b = np.array([[11,22,33]
             ,[44,55,66]
             ,[77,88,99]])
print('sum of a and b is:')
print(a + b)
print (b.dot(a))
print (a.dot(b))