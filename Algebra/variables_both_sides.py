import random

print("=== Variables on Both Sides Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    x = random.randint(1, 15)
    a = random.randint(2, 8)
    b = random.randint(1, 8)
    c = random.randint(1, 15)

    result = a * x + c
    left = b * x + (result - b * x)

    print(f"{i + 1}. {a}x + {c} = {b}x + {result - b * x}")

    if show_answers == "y":
        print(f"   Answer: x = {x}")

print("\nDone!")
