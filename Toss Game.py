import random

print("🪙 Welcome to the Coin Toss Game!")
choice = input("Choose Heads or Tails: ").lower()
result = random.choice(["heads", "tails"])

if choice == result:
    print("🎉 You win! It was", result)
else:
    print("😢 You lose! It was", result)