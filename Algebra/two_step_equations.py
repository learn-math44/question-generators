import random

print("=== Two-Step Equations Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    x = random.randint(1, 20)
    a = random.randint(2, 10)
    b = random.randint(1, 20)
    result = a * x + b

    print(f"{i + 1}. {a}x + {b} = {result}")

    if show_answers == "y":
        print(f"   Answer: x = {x}")

print("\nDone!")
