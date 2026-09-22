import random

print("=== Monomial Division Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    coefficient = random.randint(2, 20)
    divisor = random.randint(2, 10)

    while coefficient % divisor != 0:
        coefficient = random.randint(2, 20)

    exponent1 = random.randint(2, 6)
    exponent2 = random.randint(1, exponent1)

    print(f"{i + 1}. ({coefficient}x^{exponent1}) / ({divisor}x^{exponent2})")

    if show_answers == "y":
        print(f"   Answer: {coefficient // divisor}x^{exponent1 - exponent2}")

print("\nDone!")
