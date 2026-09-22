import random

print("=== Distributive Property Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    a = random.randint(2, 10)
    b = random.randint(1, 20)

    print(f"{i + 1}. {a}(x + {b}) = ?")

    if show_answers == "y":
        print(f"   Answer: {a}x + {a * b}")

print("\nDone!")
