# find intersection of 3 arrays

arr1 = [1, 2, 3, 4, 5, 6]
arr2 = [2, 4, 6, 8, 10]
arr3 = [1, 4, 6, 7, 10]

# using set intersection
result = set(arr1).intersection(arr2, arr3)
print(result)
