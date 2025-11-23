#operator overloading code simple without class for polymorphism concept

def add(x, y):
    return x + y

def add_floats(x, y):
    return x + y

def add_strings(x, y):
    return x + y    
# same function name but different data types
print(add(5, 10))            # integer addition 
print(add_floats(5.5, 10.2)) # float addition
print(add_strings("Hello, ", "MR> SUNIL!")) # string concatenation  

#code for polymorphism using class

class Adder:
    def add(self, a, b):
        return a + b

adder = Adder()
print(adder.add(5, 10))            # integer addition
print(adder.add(5.5, 10.2))        # float addition
print(adder.add("Hello, ", "MR> SUNIL!")) # string concatenation