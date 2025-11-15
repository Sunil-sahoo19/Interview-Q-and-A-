def find_hcf(x, y):
    # find the smaller number
    smaller = x if x < y else y
    for i in range(1, smaller + 1):
        if (x % i == 0) and (y % i == 0):
            hcf = i
    return hcf

def find_lcm(x, y):
    lcm = (x * y) // find_hcf(x, y)
    return lcm

# Input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("HCF of", num1, "and", num2, "is:", find_hcf(num1, num2))
print("LCM of", num1, "and", num2, "is:", find_lcm(num1, num2))