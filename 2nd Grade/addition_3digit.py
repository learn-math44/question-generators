import random

print("=== 3-Digit Addition Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    a = random.randint(100, 999)
    b = random.randint(100, 999)

    print(f"{i + 1}. {a} + {b} = ?")

    if show_answers == "y":
        print(f"   Answer: {a + b}")

print("\nDone!")
