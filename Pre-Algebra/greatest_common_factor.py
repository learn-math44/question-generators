import random
import math

print("=== Greatest Common Factor Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    a = random.randint(10, 100)
    b = random.randint(10, 100)

    answer = math.gcd(a, b)

    print(f"{i + 1}. Find the GCF of {a} and {b}.")

    if show_answers == "y":
        print(f"   Answer: {answer}")

print("\nDone!")
