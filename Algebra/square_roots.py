import random

print("=== Square Roots Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    number = random.randint(2, 15)
    value = number ** 2

    print(f"{i + 1}. √{value} = ?")

    if show_answers == "y":
        print(f"   Answer: {number}")

print("\nDone!")
