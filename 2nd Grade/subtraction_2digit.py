import random

print("=== 2-Digit Subtraction Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    a = random.randint(10, 99)
    b = random.randint(10, a)

    print(f"{i + 1}. {a} - {b} = ?")

    if show_answers == "y":
        print(f"   Answer: {a - b}")

print("\nDone!")
