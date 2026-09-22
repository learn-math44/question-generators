import random

print("=== Mixed Numbers Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    whole = random.randint(1, 9)
    numerator = random.randint(1, 7)
    denominator = random.randint(numerator + 1, 10)

    improper_numerator = whole * denominator + numerator

    print(f"{i + 1}. Convert {whole} {numerator}/{denominator} to an improper fraction.")

    if show_answers == "y":
        print(f"   Answer: {improper_numerator}/{denominator}")

print("\nDone!")
