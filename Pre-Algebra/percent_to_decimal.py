import random

print("=== Percent to Decimal Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    percent = random.randint(1, 99)
    answer = percent / 100

    print(f"{i + 1}. Convert {percent}% to a decimal.")

    if show_answers == "y":
        print(f"   Answer: {answer}")

print("\nDone!")
