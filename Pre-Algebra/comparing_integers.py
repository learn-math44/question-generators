import random

print("=== Comparing Integers Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    a = random.randint(-50, 50)
    b = random.randint(-50, 50)

    symbol = ">" if a > b else "<" if a < b else "="

    print(f"{i + 1}. {a} ___ {b}")

    if show_answers == "y":
        print(f"   Answer: {symbol}")

print("\nDone!")
