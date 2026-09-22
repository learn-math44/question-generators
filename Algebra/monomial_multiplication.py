import random

print("=== Monomial Multiplication Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    a = random.randint(2, 10)
    b = random.randint(2, 10)
    exponent1 = random.randint(1, 4)
    exponent2 = random.randint(1, 4)

    print(f"{i + 1}. ({a}x^{exponent1})({b}x^{exponent2})")

    if show_answers == "y":
        print(f"   Answer: {a*b}x^{exponent1 + exponent2}")

print("\nDone!")
