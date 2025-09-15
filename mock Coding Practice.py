 
   #Q1 What are Python’s key features? Why is it called an interpreted language?
Simple and readable syntax
Interpreted and dynamically typed
Supports OOP and procedural programming
Rich standard library
Cross-platform compatibility

🔹 Why Interpreted?
Python runs code line-by-line using an interpreter, making it easier to debug and test without compiling.
 

# 2. Difference between **Python 2 and Python 3**?

Python 2 vs Python 3
print: Python 2 → print "Hi", Python 3 → print("Hi")
Division: Python 2 → integer by default, Python 3 → float
Strings: Python 2 → ASCII, Python 3 → Unicode
xrange: Only in Python 2
Support: Python 2 is outdated, Python 3 is current

# 3. Explain **indentation** in Python. What happens if indentation is incorrect?

 Indentation in Python
Python uses indentation to define code blocks (like loops, functions).
Incorrect indentation causes an IndentationError and stops the code from running.
Always use consistent spacing—typically 4 spaces per level.

#4. What are Python **keywords**? Can you use them as variable names?

 Python Keywords
Reserved words with special meaning (e.g., if, for, class, def)

Cannot be used as variable names — causes a SyntaxError


#5. Difference between **list, tuple, set, and dictionary**. Give examples.?

List vs Tuple vs Set vs Dictionary

List: Ordered, mutable, allows duplicates → fruits = ['apple', 'banana']
Tuple: Ordered, immutable, allows duplicates → person = ('John', 25)
Set: Unordered, mutable, no duplicates → nums = {1, 2, 3}
Dictionary: Key-value pairs, mutable, keys must be unique → student = {'name': 'Alice'}

#6. What is the difference between **mutable and immutable** data types?

Mutable vs Immutable

Mutable: Can be changed after creation (e.g., list, dict, set)

Immutable: Cannot be changed once created (e.g., int, str, tuple)


#7. Explain **== vs is** operator in Python with examples.
== vs is in Python

== checks if values are equal

is checks if objects are the same in memory

a = [1, 2]; b = [1, 2]; c = a  
a == b  # True  
a is b  # False  
a is c  # True  

#8.  What is the difference between **append() vs extend()** in lists?

append() vs extend() in Lists

* append() adds a single item to the list → list.append([4, 5]) → adds as one element

* extend() adds each element of an iterable → list.extend([4, 5]) → adds 4 and 5 separately

#9.Explain **shallow copy vs deep copy** in Python.?

Shallow Copy vs Deep Copy

* Shallow Copy: Copies references to nested objects → changes affect both → copy.copy(obj)

* Deep Copy: Copies entire structure recursively → changes don’t affect original → copy.deepcopy(obj)

# 10. How does Python handle **memory management** (Garbage collection)?

Python Memory Management

* Python uses automatic memory management.

* It relies on reference counting and a garbage collector to clean up unused objects.

* The gc module handles cyclic references and allows manual control if needed.