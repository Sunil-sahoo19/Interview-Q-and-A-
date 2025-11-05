import array

# Create an integer array of marks
marks = array.array('i', [80, 75, 90, 85, 70])

# Print all marks
print("Marks:", marks)

# Calculate total and average
total = sum(marks)
average = total / len(marks)

print("Total Marks:", total)
print("Average Marks:", average)

