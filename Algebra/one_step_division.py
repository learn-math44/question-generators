import random

print("=== One-Step Division Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    x = random.randint(1, 20)
    divisor = random.randint(2, 12)
    dividend = x * divisor

    print(f"{i + 1}. x / {divisor} = {x}")

    if show_answers == "y":
        print(f"   Answer: x = {x * divisor}")

print("\nDone!")
