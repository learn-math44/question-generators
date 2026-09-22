import random
import math

print("=== Quadratic Equation Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    r1 = random.randint(-10, 10)
    r2 = random.randint(-10, 10)

    b = -(r1 + r2)
    c = r1 * r2

    print(f"{i + 1}. x² + {b}x + {c} = 0")

    if show_answers == "y":
        print(f"   Answer: x = {r1}, {r2}")

print("\nDone!")
