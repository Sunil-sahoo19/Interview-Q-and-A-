# Parent Class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some generic sound"

# Child Class 1
class Dog(Animal):
    def speak(self):
        return "Woof! Woof!"

# Child Class 2
class Cat(Animal):
    def speak(self):
        return "Meow! Meow!"

# Child Class 3
class Cow(Animal):
    def speak(self):
        return "Moo! Moo!"

# Create objects
dog = Dog("Tommy")
cat = Cat("Kitty")
cow = Cow("Ganga")

# Polymorphism in action
animals = [dog, cat, cow]

for animal in animals:
    print(f"{animal.name} says: {animal.speak()}")

