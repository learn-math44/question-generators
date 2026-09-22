import random
from fractions import Fraction

print("=== Rational Numbers Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    a = random.randint(1, 10)
    b = random.randint(2, 10)
    c = random.randint(1, 10)
    d = random.randint(2, 10)

    answer = Fraction(a, b) + Fraction(c, d)

    print(f"{i + 1}. {a}/{b} + {c}/{d} = ?")

    if show_answers == "y":
        print(f"   Answer: {answer}")

print("\nDone!")
