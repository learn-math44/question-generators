import random

print("=== Counting Backward Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    start = random.randint(2, 100)

    print(f"{i + 1}. What number comes before {start}?")

    if show_answers == "y":
        print(f"   Answer: {start - 1}")

print("\nDone!")
