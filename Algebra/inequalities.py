import random

print("=== Inequalities Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    x = random.randint(1, 20)
    b = random.randint(1, 20)
    result = x + b

    print(f"{i + 1}. x + {b} > {result - random.randint(1, 5)}")

    if show_answers == "y":
        print(f"   Answer: x > {result - random.randint(1, 5) - b}")

print("\nDone!")
