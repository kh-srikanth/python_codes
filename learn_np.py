import numpy as np
# a = np.array([[1, 2, 3]
#              ,[4, 5, 6]
#              ,[7, 8, 9]])
# print(a)
# print(np.sqrt(a))
# print(a.sum(axis=1))
# print(a.reshape(1,9))
# print(a.size)
# print(a.shape)
#
# b = np.array([[11,22,33]
#              ,[44,55,66]
#              ,[77,88,99]])
# print('sum of a and b is:')
# print(a + b)
# print(b.dot(a))
# print(a.dot(b))

c = np.arange(0,6).reshape(3,2)
d = np.arange(6,12).reshape(3,2)
print(c)
print(d)
##union two tables
print(np.vstack((c,d)))
##fulljoin two tables
print(np.hstack((c,d)))
aa = np.arange(30).reshape(2,15)
print(aa)
print(np.hsplit(aa,3))
print(np.vsplit(aa,2))