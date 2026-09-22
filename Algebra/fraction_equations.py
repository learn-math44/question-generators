import random

print("=== Fraction Equations Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    denominator = random.randint(2, 10)
    answer = random.randint(1, 10)
    result = denominator * answer

    print(f"{i + 1}. x/{denominator} = {result}")

    if show_answers == "y":
        print(f"   Answer: x = {result * denominator}")

print("\nDone!")
