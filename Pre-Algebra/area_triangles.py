import random

print("=== Triangle Area Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    base = random.randint(2, 20)
    height = random.randint(2, 20)

    answer = base * height / 2

    print(f"{i + 1}. Find the area of a triangle with base {base} and height {height}.")

    if show_answers == "y":
        print(f"   Answer: {answer} square units")

print("\nDone!")
