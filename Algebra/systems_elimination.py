import random

print("=== Systems by Elimination Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    x = random.randint(1, 10)
    y = random.randint(1, 10)

    print(f"{i + 1}.")
    print(f"   x + y = {x + y}")
    print(f"   x - y = {x - y}")

    if show_answers == "y":
        print(f"   Answer: x = {x}, y = {y}")

print("\nDone!")
