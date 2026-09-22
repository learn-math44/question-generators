import random

print("=== One-Step Subtraction Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    x = random.randint(1, 50)
    b = random.randint(1, 50)
    answer = x

    print(f"{i + 1}. x - {b} = {x - b}")

    if show_answers == "y":
        print(f"   Answer: x = {answer}")

print("\nDone!")
