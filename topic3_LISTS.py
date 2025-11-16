
# Assignment: 01
print("Topic 03: Lists")
students = ["Moiz", "Shayan", "Faiq", "Mekail", "Ali"]
students.append("Zeeshan")
students.remove("Faiq")
print("The list of Students", students)

# Assignment: 02
grocery = ["milk", "bread", "eggs", "rice", "sugar"]
grocery[0] = ("butter")
print("The list of grocery: ", grocery)
print("Total number of items: ", len(grocery))

# Assignment: 03
random_numbers = [45, 12, 78, 23, 56, 89, 34]
print("Before Sorting: ", random_numbers)
random_numbers.sort()
print("After Sorting: ", random_numbers)

# Assignment: 04
movie = ("Mirzapur", "Sholay", "3idots", "Dangal", "Pathaan")
print("The first two movies", movie[:2])
print("The last movie", movie[-1:])
print("The total number of movies", len(movie))

# Assignment: 05
sum_numbers = [5, 10, 15, 20]
total = sum(sum_numbers)
print("The total sum of the numbers: ", total)

avg = total/4
print("The average of the numbers: ", avg)
