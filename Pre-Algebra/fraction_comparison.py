import random
from fractions import Fraction

print("=== Fraction Comparison Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    a = random.randint(1, 9)
    b = random.randint(2, 10)
    c = random.randint(1, 9)
    d = random.randint(2, 10)

    first = Fraction(a, b)
    second = Fraction(c, d)

    symbol = ">" if first > second else "<" if first < second else "="

    print(f"{i + 1}. {a}/{b} ___ {c}/{d}")

    if show_answers == "y":
        print(f"   Answer: {symbol}")

print("\nDone!")
