import random

print("=== Multi-Step Equations Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    x = random.randint(1, 15)
    a = random.randint(2, 8)
    b = random.randint(1, 15)
    c = random.randint(1, 10)

    result = a * x + b - c

    print(f"{i + 1}. {a}x + {b} - {c} = {result}")

    if show_answers == "y":
        print(f"   Answer: x = {x}")

print("\nDone!")
