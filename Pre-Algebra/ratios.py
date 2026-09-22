import random

print("=== Ratios Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    red = random.randint(1, 12)
    blue = random.randint(1, 12)

    print(f"{i + 1}. A bag has {red} red marbles and {blue} blue marbles. What is the ratio of red to blue?")

    if show_answers == "y":
        print(f"   Answer: {red}:{blue}")

print("\nDone!")
