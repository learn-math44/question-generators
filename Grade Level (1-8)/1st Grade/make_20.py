import random

print("=== Make 20 Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    a = random.randint(0, 20)
    answer = 20 - a

    print(f"{i + 1}. What number makes 20? {a} + ___ = 20")

    if show_answers == "y":
        print(f"   Answer: {answer}")

print("\nDone!")
