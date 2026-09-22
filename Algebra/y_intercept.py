import random

print("=== Y-Intercept Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    m = random.randint(1, 10)
    b = random.randint(-20, 20)

    print(f"{i + 1}. Find the y-intercept: y = {m}x + {b}")

    if show_answers == "y":
        print(f"   Answer: {b}")

print("\nDone!")
