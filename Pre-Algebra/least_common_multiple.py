import random
import math

print("=== Least Common Multiple Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    a = random.randint(2, 15)
    b = random.randint(2, 15)

    answer = abs(a * b) // math.gcd(a, b)

    print(f"{i + 1}. Find the LCM of {a} and {b}.")

    if show_answers == "y":
        print(f"   Answer: {answer}")

print("\nDone!")
