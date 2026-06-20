import numpy as np
arr1 = np.array([1,2,3,4,5,6,7])

arr2= np.zeros((3,3))

arr3= np.arange(10)

arr4= np.linspace(0,100,11)

elements = (np.where(arr1>5))[0]
print(elements)