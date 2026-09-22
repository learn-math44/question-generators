import random

print("=== Polynomial Multiplication Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    a = random.randint(1, 10)
    b = random.randint(1, 10)

    print(f"{i + 1}. (x + {a})(x + {b}) = ?")

    if show_answers == "y":
        print(f"   Answer: x² + {a+b}x + {a*b}")

print("\nDone!")
