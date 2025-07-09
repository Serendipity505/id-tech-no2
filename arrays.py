#the following program uses the NumPy Library
import numpy as np
numbers_array = np.array([])
print(numbers_array)

import numpy as np
numbers_array = np.array([1,2,3,4])
print(numbers_array)

import numpy as np
numbers_array = np.array([1,2,3,4])
print(numbers_array.shape)

import numpy as np

numbers_array=np.array([1,2,3,4,5,6,7,8,9,3,4,5,4,5,3,45,4,3,45,4,3,45,43,4,53,4])
print(numbers_array.shape)
#shape indicates the size of the array(the amount in an array)
#or the number of elements in each dimension

import numpy as np
numbers_array = np.array([[1,2,3,4],[5,6,7,8,]])
print(numbers_array.shape)

# create an array that has the shape (3,2,4) shape
numbers_array = np.array([[1,2,3,4],[1,2,3,4],[1,2,3,4]],[[1,2,3,4],[1,2,3,4],[1,2,3,4]])
print(numbers_array)