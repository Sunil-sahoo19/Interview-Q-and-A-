text = "I love Python programming"
count = 0
for ch in text.lower():
    if ch in "aeiou":
        count += 1
print("Number of vowels:", count)
