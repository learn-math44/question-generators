import random

print("=== Counting Forward Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    start = random.randint(1, 90)

    print(f"{i + 1}. What number comes after {start}?")

    if show_answers == "y":
        print(f"   Answer: {start + 1}")

print("\nDone!")
