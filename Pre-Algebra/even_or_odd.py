import random

print("=== Even or Odd Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    number = random.randint(1, 100)

    answer = "Even" if number % 2 == 0 else "Odd"

    print(f"{i + 1}. Is {number} even or odd?")

    if show_answers == "y":
        print(f"   Answer: {answer}")

print("\nDone!")
