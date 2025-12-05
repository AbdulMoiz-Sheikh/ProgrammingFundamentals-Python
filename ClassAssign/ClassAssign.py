from abc import ABC, abstractmethod

# -----------------------
# Abstract Class (Animal)
# -----------------------
class Animal(ABC):
    def __init__(self, name, age, health):
        self.name = name
        self.__age = age       # Encapsulation
        self.__health = health # Encapsulation

    # Getters (encapsulation)
    def get_age(self):
        return self.__age
    
    def get_health(self):
        return self.__health

    # Setters (encapsulation)
    def set_age(self, age):
        self.__age = age

    def set_health(self, health):
        self.__health = health

    @abstractmethod
    def sound(self):
        pass


# -----------------------
# Dog Class
# -----------------------
class Dog(Animal):
    def sound(self):
        return "Woof! Woof!"


# -----------------------
# Cat Class
# -----------------------
class Cat(Animal):
    def sound(self):
        return "Meow! Meow!"


# -----------------------
# Lion Class
# -----------------------
class Lion(Animal):
    def sound(self):
        return "Roarrrrr!"


# -----------------------
# Zoo Management System
# -----------------------
class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal: Animal):
        self.animals.append(animal)

    def show_animals(self):
        for animal in self.animals:
            print(f"Name: {animal.name}, Age: {animal.get_age()}, Health: {animal.get_health()}")

    def play_sounds(self):
        for animal in self.animals:
            print(f"{animal.name} → {animal.sound()}")


# --------------------------------------
# Example Usage
# --------------------------------------
z = Zoo()

dog1 = Dog("Buddy", 3, "Good")
cat1 = Cat("Kitty", 2, "Excellent")
lion1 = Lion("Simba", 5, "Strong")

z.add_animal(dog1)
z.add_animal(cat1)
z.add_animal(lion1)

print("=== Zoo Animals ===")
z.show_animals()

print("\n=== Animal Sounds ===")
z.play_sounds()

