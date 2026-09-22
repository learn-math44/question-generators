import random

print("=== Point-Slope Form Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    m = random.randint(-5, 5)
    x1 = random.randint(-10, 10)
    y1 = random.randint(-10, 10)

    print(f"{i + 1}. Write the equation with slope {m} through ({x1}, {y1}).")

    if show_answers == "y":
        print(f"   Answer: y - ({y1}) = {m}(x - ({x1}))")

print("\nDone!")
