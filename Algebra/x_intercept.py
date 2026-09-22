import random

print("=== X-Intercept Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    a = random.randint(1, 10)
    b = random.randint(1, 20)

    x = -b / a

    print(f"{i + 1}. Find the x-intercept: {a}x + {b} = 0")

    if show_answers == "y":
        print(f"   Answer: x = {x}")

print("\nDone!")
