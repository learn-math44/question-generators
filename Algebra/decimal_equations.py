import random

print("=== Decimal Equations Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    x = random.randint(1, 20)
    number = round(random.uniform(1, 10), 1)
    result = round(x + number, 1)

    print(f"{i + 1}. x + {number} = {result}")

    if show_answers == "y":
        print(f"   Answer: x = {x}")

print("\nDone!")
