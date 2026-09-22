import random

print("=== Number After Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    number = random.randint(1, 50)

    print(f"{i + 1}. What number comes after {number}?")

    if show_answers == "y":
        print(f"   Answer: {number + 1}")

print("\nDone!")
