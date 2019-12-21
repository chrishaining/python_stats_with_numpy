import numpy as np

#create an array
array = np.array([1, 2, 3, 4, 5, 6])
print(array)

#find the items that meet a boolean criterion (expect 4, 5, 6)
over_fives = array[array > 3]
print(over_fives)

#for each item in the array, checks whether that item meets a boolean criterion (expect an array of True/False, in this case [False, False, False, True, True, True]) 
print(array > 3)
