# import python array module
from array import array


# Creating of an array
int_arr = array("i", [1, 2, 3, 4, 5])
double_arr = array("d", [1.1, 2.2, 3.3, 4.4, 5.5])
unicode_arr = array("w", ["a", "b", "c", "d", "e"])


# typecodes
print(int_arr.typecode)
print(double_arr.typecode)
print(unicode_arr.typecode)

# first look at the array
print(int_arr)
print(double_arr)
print(unicode_arr)

# Lenght of an array
print(len(int_arr))
print(len(double_arr))
print(len(unicode_arr))

# Iterating over arrays
for i in range(0, len(int_arr)):
    print(int_arr[i], end=" ")
print("\n")
for i in range(0, len(double_arr)):
    print(double_arr[i], end=" ")
print("\n")
for i in range(0, len(unicode_arr)):
    print(unicode_arr[i], end=" ")
print("\n")

# Indexing in arrays

x = list(range(1, 100, 2))
new_arr = array("i", x)

for i in range(0, len(new_arr)):
    print(new_arr[i], end=" ")

print("\n")

print(new_arr[10])  # accessing 11th element
print(new_arr[-10])  # accessing 10th element from last (negative indexing)

# Adding elements to an array
new_arr.append(100)  # adding element at the end
new_arr.insert(0, 44)  # adding element at the beginning

for i in range(0, len(new_arr)):
    print(new_arr[i], end=" ")
print("\n")

# Updating elements in an array
new_arr[0] = 33  # updating first element
new_arr[10] = 55  # updating 11th element

for i in range(0, len(new_arr)):
    print(new_arr[i], end=" ")
print("\n")


# Deleting elements from an array
new_arr.pop(3)  # removing element at index 3
new_arr.remove(33)  # removing element with value 33
del new_arr[-1]  # deleting last element
for i in range(0, len(new_arr)):
    print(new_arr[i], end=" ")
print("\n")

# Slicing of an array

slice_arr = new_arr[0:10]  # slicing first 10 elements
for i in range(0, len(slice_arr)):
    print(slice_arr[i], end=" ")
print("\n")

slice_neg_arr = new_arr[10:-10]  # slicing with negative indexing
for i in range(0, len(slice_neg_arr)):
    print(slice_neg_arr[i], end=" ")
print("\n")

reversing_arr = new_arr[::-1]  # reversing the array using slicing
for i in range(0, len(reversing_arr)):
    print(reversing_arr[i], end=" ")
print("\n")

# Searchig operation in an array

for i in range(0, len(new_arr[0:10])):
    if new_arr[i] == 17:
        print("Element found at index:", i)
        break
    else:
         continue
print("\n")

index = new_arr.index(99)  # searching index of element with value 99
res = new_arr[index] # accessing element at found index
print("Element found at index:", index, "with value:", res, end=" ")
print("\n")

# Note: array module only supports single dimensional arrays

# Sorting of an array

unsorted_arr = array("i", [5, 3, 8, 6, 2, 7, 4, 1])
print(unsorted_arr, end="\n")
sorted_arr = unsorted_arr.tolist()
# ascending order sort
sorted_arr.sort()
print(sorted_arr, end="\n")
# descending order sort
sorted_arr.sort(reverse=True)
print(sorted_arr, end="\n")


# Numpy library is preferred for multi-dimensional arrays and advanced operations

import numpy as np

#creating a numpy array

arr = np.array([1, 2, 3, 4, 5])
print(arr)
print("\n")

# creating an array with all zeros
zeroes_arr = np.zeros((2, 2))  # 2 rows and 2 columns
print(zeroes_arr)
# creating an array with all ones
ones_arr = np.ones((3, 3))  # 3 rows and 3 columns
print(ones_arr)
# creating an identity matrix
identity_arr = np.eye(4)  # 4x4 identity matrix
print(identity_arr)
# creating an array with constant value
constant_arr = np.full((2, 3), 7)  # 2 rows and 3 columns with all values as 7
print(constant_arr)
# creating an array with random values
random_arr = np.random.rand(2, 2)  # 2 rows and 2 columns with random values
print(random_arr)
# creating an array with evenly spaced values
evenly_spaced_arr = np.arange(0, 10, 2)  # values from 0 to 10 with step of 2
print(evenly_spaced_arr)
# creating an array with linearly spaced values
linearly_spaced_arr = np.linspace(0, 1, 5)  # 5 values between 0 and 1
print(linearly_spaced_arr)
# reshaping an array
reshaped_arr = arr.reshape((5, 1))  # reshaping to 5 rows and 1 column
print(reshaped_arr)
# two dimensional array
two_d_arr = np.array([[1, 2, 3], [4, 5, 6]])
print(two_d_arr)
# three dimensional array
three_d_arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(three_d_arr)
#multi-dimensional array
multi_d_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape((3, 3))
print(multi_d_arr)
print("\n")


# CRUD operations in numpy arrays

# Reading elements in a numpy array
sample_arr = np.array([10, 20, 30, 40, 50])
for i in range(len(sample_arr)):
    print(sample_arr[i], end=" :")
print("\n")

# updating elements in a numpy array
sample_arr[0] = 15  # updating first element
print(sample_arr)
print("\n")

# deleting elements in a numpy array
sample_arr = np.delete(sample_arr, 2)  # deleting element at index 2
print(sample_arr)
print("\n")

# Searching elements in a numpy array
index = np.where(sample_arr == 40)  # searching for element with value 40
print("Element found at coordinate:", index[0][0])
print("Checking that we found correct element:", sample_arr[2])  # accessing element at found index
print("\n")

# Sorting numpy arrays
unsorted_np_arr = np.array([5, 3, 8, 6, 2, 7, 4, 1])
print("Unsorted array:", unsorted_np_arr)
sorted_np_arr = np.sort(unsorted_np_arr)  # ascending order sort
print("Sorted array in ascending order:", sorted_np_arr)
sorted_np_arr_desc = np.sort(unsorted_np_arr)[::-1]  # descending order sort
print("Sorted array in descending order:", sorted_np_arr_desc)
print("\n")



