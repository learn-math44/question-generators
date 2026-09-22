import random

print("=== Systems by Substitution Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    x = random.randint(1, 10)
    y = random.randint(1, 10)

    b = random.randint(1, 5)
    c = x + b * y

    print(f"{i + 1}.")
    print(f"   x + {b}y = {c}")
    print(f"   y = {y}")

    if show_answers == "y":
        print(f"   Answer: x = {x}, y = {y}")

print("\nDone!")
