# Program to print multiplication table using range()

# Taking user input
num = int(input("Enter a number to print its multiplication table: "))

print(f"\nMultiplication Table of {num}\n")

# Using range() to print 1 to 10 multiples
for i in range(1, 11):
    result = num * i
    print(f"{num} x {i} = {result}")
