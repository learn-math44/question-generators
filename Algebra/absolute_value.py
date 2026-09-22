import random

print("=== Absolute Value Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    number = random.randint(-50, 50)

    print(f"{i + 1}. |{number}| = ?")

    if show_answers == "y":
        print(f"   Answer: {abs(number)}")

print("\nDone!")
