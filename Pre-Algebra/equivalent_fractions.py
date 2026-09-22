import random

print("=== Equivalent Fractions Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    numerator = random.randint(1, 9)
    denominator = random.randint(2, 10)
    multiplier = random.randint(2, 5)

    new_numerator = numerator * multiplier
    new_denominator = denominator * multiplier

    print(f"{i + 1}. Complete: {numerator}/{denominator} = ?/{new_denominator}")

    if show_answers == "y":
        print(f"   Answer: {new_numerator}")

print("\nDone!")
