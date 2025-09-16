#Q1. What are **functions** in Python? Difference between \*args and \*\*kwargs?

args	[Handles variable positional arguments	Tuple]
kwargs	[Handles variable keyword arguments	Dict]

def demo(*args, **kwargs):
    print(args)     # (5,14)
    print(kwargs)   # {'name': 'Mr.Sunil'}

demo(5, 14, name="Mr.Sunil")

#Q2. Explain decorators in Python with an example.

Decorators are functions that modify the behavior of another function without changing its code.
They’re used for logging, timing, access control, etc.
Syntax: Use @decorator_name above the function.


def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@my_decorator
def greet():
    print("Hello sir Good Morning")

greet()

#Q3. What are generators and yield?

* Generators are special functions that return an iterator and allow you to iterate over data one item at a time, saving memory.

* They use the yield keyword instead of return.

* Each time yield is called, the function pauses and resumes from that point on the next call.

* Ideal for large datasets or streaming data.
    
# Example:
def gen_even(n):
    for i in range(n):
        if i % 2 == 0:
            yield i
next()
for num in gen_even(10):
    print(num)  # Outputs even numbers from 0 to 8

# 4. Difference between **iterable, iterator, and generator
| Term      | Definition                                      | Example                     |
|-----------|-------------------------------------------------|-----------------------------|   
| Iterable  | An object that can return an iterator.          | List, Tuple, String         |
| Iterator  | An object that represents a stream of data.     | Object returned by iter
| Generator | A special type of iterator defined with yield.  | Function using yield        |


#Q5.Explain **list comprehension** with an example.
# List comprehension is a concise way to create lists in Python.
# It consists of brackets containing an expression followed by a for clause, and optionally if clauses.
# It is more readable and often faster than traditional loops.
# Example:
squares = [x**2 for x in range(10) if x % 2
print(squares)  # Outputs: [0, 4, 16, 36, 64] == 0]
== 0]

#Q6. What is the difference between **classmethod, staticmethod, and instance method**?

🔹 Python Method Types — Quick Differences
# Instance Method

*Uses self
*Accesses object data
*Called on an instance
*Example: obj.method()

# Class Method

*Uses cls
*Accesses class-level data
*Decorated with @classmethod
Example: Class.method()

# Static Method

*No self or cls
*Doesn’t access object or class data
*Decorated with @staticmethod
*Example: Class.method()

#Q7.Explain Python’s OOP concepts: inheritance, polymorphism, encapsulation.

Explain **Python’s OOP concepts**: inheritance, polymorphism, encapsulation.

#  1. inheritance

*Allows a class (child) to inherit attributes and methods from another class (parent).
*Promotes code reuse and logical hierarchy.
Example:
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

# 2.Polymorphism

*Means “many forms”: same method name behaves differently depending on the object.
*Achieved via method overriding or duck typing.
Example:
class Cat:
    def sound(self):
        print("Meow")

class Dog:
    def sound(self):
        print("Bark")

for animal in [Cat(), Dog()]:
    animal.sound()  # Calls respective method

# 3.Encapsulation

*Bundles data and methods within a class.
*Restricts direct access to internal variables using private/protected attributes.
Example:

class Person:
    def __init__(self):
        self.__age = 30  # private variable

    def get_age(self):
        return self.__age
    
#Q8. What are **magic/dunder methods** in Python? Give examples (`__str__`, `__init__`).

* Magic/Dunder Methods

*Special methods with double underscores (e.g., __init__, __str__)
*Python calls them automatically for built-in operations

* Examples
* __init__: Initializes object when created

* __str__: Defines how the object is printed

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"

# Creating an object
my_book = Book("Python Mastery", "Suraj")

# Printing the object
print(my_book)  # Output: 'Python Mastery' by Suraj

#9Q.Explain **Python’s Global Interpreter Lock (GIL)**. Why is it important?

What is Python’s GIL?

*The Global Interpreter Lock (GIL) is a mutex (lock) used in CPython (the most common Python implementation).
*It ensures that only one thread executes Python bytecode at a time, even on multi-core systems.

# Why Is It Important?
Pros:
*Prevents complex thread synchronization issues.
*Simplifies memory management in CPython.

Cons:
*Limits true multithreading for CPU-bound tasks.
*Can be a performance bottleneck in multi-threaded programs.

#Q10. Difference between **deepcopy vs copy.copy()** in Python.

# Shallow Copy vs Deep Copy in Python

*copy.copy() → Shallow copy: Copies only the outer object. Nested objects are shared.
*copy.deepcopy() → Deep copy: Recursively copies everything. Nested objects are duplicated.


    



 





    
    
 
 



