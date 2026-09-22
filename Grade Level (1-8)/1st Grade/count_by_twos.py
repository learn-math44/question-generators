import random

print("=== Count by 2s Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    start = random.randint(0, 20) * 2
    answer = start + 2

    print(f"{i + 1}. What comes next? {start}, {start + 2}, {start + 4}, ___")

    if show_answers == "y":
        print(f"   Answer: {answer}")

print("\nDone!")
