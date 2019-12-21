import numpy as np

#create a two_dimensional array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

#calculate the average of the two_dimensional array - expect 5
two_d_mean = np.mean(arr)
print("The mean of the entire 2D array is {}".format(two_d_mean))

#find the averages of each internal array - expect 2, 5, 8
internal_array_mean = np.mean(arr, axis=1)
print("The means of the internal arrays are {}".format(internal_array_mean))

#the result is in a format I didn't expect - [2. 5. 8.]. I want to know if this is a normal array, so I will try some calculations on it (hope I get 15)
sum = sum(internal_array_mean)
print(sum)
#This gave the hoped for result, but with a full stop at the end. This suggests the full stops are a presentation issue, rather than changing the meaning of the results

#find the averages of each index position within the array (so, the averages of the columns). Expect [4. 5. 6.]
column_mean = np.mean(arr, axis=0)
print("The mean of the columns are {}.".format(column_mean))
#result is as expected
