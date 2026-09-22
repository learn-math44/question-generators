import random

print("=== Positive or Negative Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    number = random.choice([
        random.randint(-100, -1),
        random.randint(1, 100)
    ])

    answer = "Positive" if number > 0 else "Negative"

    print(f"{i + 1}. Is {number} positive or negative?")

    if show_answers == "y":
        print(f"   Answer: {answer}")

print("\nDone!")
