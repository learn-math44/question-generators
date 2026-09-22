import random

print("=== Difference of Squares Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    a = random.randint(2, 12)
    b = random.randint(1, a - 1)

    print(f"{i + 1}. Factor: x² - {b*b}")

    if show_answers == "y":
        print(f"   Answer: (x - {b})(x + {b})")

print("\nDone!")
