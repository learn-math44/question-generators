import random

print("=== Scientific Notation Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    coefficient = random.randint(1, 9)
    exponent = random.randint(1, 6)

    number = coefficient * (10 ** exponent)

    print(f"{i + 1}. Write {number} in scientific notation.")

    if show_answers == "y":
        print(f"   Answer: {coefficient} × 10^{exponent}")

print("\nDone!")
