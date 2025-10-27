# Inheritance

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):  # Dog inherits from Animal
    def bark(self):
        print("Dog barks")

# Object of Dog
d = Dog()
d.speak()  # from Animal (Parent)
d.bark()   # from Dog (Child)   


# Encapsulation

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

# Object
account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # Correct way

# print(account.__balance)   Error: can't access directly




# 3. Polymorphism

class Bird:
    def make_sound(self):
        print("Chirp Chirp")

class Dog:
    def make_sound(self):
        print("Bark Bark")

# Using one function for different objects
for animal in (Bird(), Dog()):
    animal.make_sound()

