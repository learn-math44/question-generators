import random

print("=== Fraction to Decimal Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    denominator = random.choice([2, 4, 5, 10, 20, 25, 50, 100])
    numerator = random.randint(1, denominator - 1)

    answer = numerator / denominator

    print(f"{i + 1}. Convert {numerator}/{denominator} to a decimal.")

    if show_answers == "y":
        print(f"   Answer: {answer}")

print("\nDone!")
