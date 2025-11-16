# Assignment: 01
print("Topic 04: Sets")
numbers = {1, 2, 2, 3, 4, 4, 5}
print("After removing same numbers: ", numbers)

# Assignment: 02
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print("All unique elements from both sets: ", A.union(B))
print("Elements common to both sets: ", A.intersection(B))
print("Elements in A but not in B: ", A.difference(B))

# Assignment: 03
C = {2, 4, 6}
C.add(8)
C.remove(4)
print("Print the updated set: ", C)

# Assignment: 04
num = {1, 2, 3, 4, 5}
print(5 in num)
print(10 in num)

# Assignment: 05
list_numbers = [1, 2, 2, 3, 4, 4, 5]
set_numbers = set(list_numbers)
print("Original List: ", list_numbers)
print("set to automatically remove duplicates: ", set_numbers)
