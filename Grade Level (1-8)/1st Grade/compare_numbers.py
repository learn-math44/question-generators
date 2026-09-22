import random

print("=== Compare Numbers Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    a = random.randint(1, 20)
    b = random.randint(1, 20)

    symbol = ">" if a > b else "<" if a < b else "="

    print(f"{i + 1}. {a} ___ {b}")

    if show_answers == "y":
        print(f"   Answer: {symbol}")

print("\nDone!")
