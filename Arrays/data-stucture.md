# Arrays Data Structure

Introduction to Arrays Data Structure in Python.



## What is an Array ?

- An arrays is defined as a `Storage` or `Container` or similar items placed in `Contiguous` memory locations.

Example -> Storing `Books` in a `Bookshelf` where each book is placed next to each other (`Contiguous`).

## Implementing Arrays in Python.

- Two ways to implement Arrays in Python.

  1. Using `List` data structure.
  
   - `Can store heterogeneous data types.`
   
     Example ->
     
     ```python
     # Creating an array using list
     my_array = [1, 2, 3, 4, 5]
     print(my_array)
     ```
  
  2. Using `array` module.
  
  - `Can only store homogeneous data types.`

     Example ->
     
     ```python
     import array as arr
     
     # Creating an array using array module
     my_array = arr.array('i', [1, 2, 3, 4, 5])
     print(my_array)
     ```
   3. Using `Numpy` Arrays.
  
      Example ->
      
      ```python
      import numpy as np
      
      # Creating an array using numpy
      my_array = np.array([1, 2, 3, 4, 5])
      print(my_array)
      ```

## Homogeneous and Hererogeneous Arrays ?

- `Homogeneous` Arrays -> Arrays that store elements of the same data type.

```python
Example -> An array of integers: [1, 2, 3, 4, 5]
```

- `Heterogeneous` Arrays -> Arrays that store elements of different data types.

```python
Example -> An array with mixed data types: [1, "Hello", 3.14, True]
```

## Indexing in Arrays

- `Indexing` is a way to access individual elements in an array using their position.

- `Zero-based Indexing` -> The first element of the array is at index `0`, the second element is at index `1`, and so on.

Example ->

```python
my_array = [10, 20, 30, 40, 50]
print(my_array[0])  # Output: 10
print(my_array[2])  # Output: 30
```
- `Negative Indexing` -> The last element of the array is at index `-1`, the second last element is at index `-2`, and so on.

Example ->

```python
my_array = [10, 20, 30, 40, 50] 
print(my_array[-1])  # Output: 50
print(my_array[-3])  # Output: 30
```

## Slicing in Arrays

- `Slicing` is a way to access a subset of elements in an array by specifying a range of indices.

Example ->

```python
my_array = [10, 20, 30, 40, 50]
print(my_array[1:4])  # Output: [20, 30, 40]
print(my_array[:3])   # Output: [10, 20, 30]  
print(my_array[2:])   # Output: [30, 40, 50]
``` 


## Sorting Arrays

- `Sorting` is the process of arranging the elements of an array in a specific order, either ascending or descending.

Example ->

```python
my_array = [50, 20, 40, 10, 30]
my_array.sort()  # Sort in ascending order
print(my_array)  # Output: [10, 20, 30, 40, 50]
my_array.sort(reverse=True)  # Sort in descending order
print(my_array)  # Output: [50, 40, 30, 20, 10]
``` 

# Hands on

- Python Array module: CRUD operations
- Searching and Sorting in Arrays
- Numpy Arrays: CRUD operations and Manipulations
- Searching and Sorting in Numpy Arrays
