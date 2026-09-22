import random

print("=== Polynomial Addition Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    d = random.randint(1, 10)

    print(f"{i + 1}. ({a}x + {b}) + ({c}x + {d})")

    if show_answers == "y":
        print(f"   Answer: {a+c}x + {b+d}")

print("\nDone!")
