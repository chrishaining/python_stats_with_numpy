#this file is practice for numpy
import numpy as np

#create a two_dimensional array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr)

arr_two = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

#find the first column of the array
column_one = arr[:, 0]
print("The first column is {}".format(column_one))

#find the first row of the array
row_one = arr[0,:]
print("the first row is {}".format(row_one))
#find the second column of the array
column_two=arr[:,1]
print("The second column is {}".format(column_two))

#find the second row of the array
row_two = arr[1,:]
print("The second row is {}".format(row_two))

#print a diagonal, from top left to bottom right
#this requires creating a for loop, and some kind of positional counter
def left_right_diagonal(array):
    index = -1
    left_right_diagonal_array = []
    for row in array:
        index += 1
        left_right_diagonal_array.append(row[index])
    return left_right_diagonal_array

print(left_right_diagonal(arr))

#print a diagonal, from top right to bottom left
def right_left_diagonal(array):
    index = len(array)
    right_left_diagonal_array = []
    for row in array:
        index -= 1
        right_left_diagonal_array.append(row[index])
    return right_left_diagonal_array
print(right_left_diagonal(arr))

#find the sums of the two diagonal lists, and calculate the difference between the sums
def calculate_difference_between_summed_diagonals(array):
    l_r_sum = sum(left_right_diagonal(array))
    r_l_sum = sum(right_left_diagonal(array))
    diff = l_r_sum - r_l_sum
    return diff

print(calculate_difference_between_summed_diagonals(arr))

#note that this does not work if the array is not a square:
# print(calculate_difference_between_summed_diagonals(arr_two))
# print(arr_two)
