import random

print("=== Rate of Change Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    x1 = random.randint(0, 10)
    x2 = x1 + random.randint(1, 5)
    y1 = random.randint(0, 20)
    y2 = y1 + random.randint(1, 20)

    answer = (y2 - y1) / (x2 - x1)

    print(f"{i + 1}. Find the rate of change from ({x1}, {y1}) to ({x2}, {y2}).")

    if show_answers == "y":
        print(f"   Answer: {answer}")

print("\nDone!")
