# Assignment: 01
print("Topic 05: Dictonaries")
name = "Ali"
age = 20
grade = "A."
print(name, "is", age, "years old and got grade",grade)

# Assignment: 02
car = {"brand": "Toyota", "year": 2020}
car["color"] = "red"
car["year"] = 2022
print(car)

# Assignment: 03
country = {"Pakistan: ": "Islamabad", "Turkey: ": "Ankara", "Japan: ": "Tokyo"}
for countries, capital in country.items():
    print(countries, capital)

# Assignment: 04
prices = {"apple": 1.5, "banana": 0.75, "orange": 1.2}
product = input("Enter product name: ").lower()
print("Price: ", prices[product])

# Assignment: 05
students = {"Ali":{"age": 18, "grade":"A"},
            "Sara": {"age": 19, "grade": "B"}}
for name, info in students.items():
    print("Name: ", name) 
    print("Age: ", info["age"])
    print("Grade:", info["grade"])
    print("____________________")





