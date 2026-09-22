import random

print("=== Discriminant Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    a = random.randint(1, 5)
    b = random.randint(-10, 10)
    c = random.randint(-10, 10)

    discriminant = b ** 2 - 4 * a * c

    print(f"{i + 1}. Find the discriminant of {a}x² + {b}x + {c} = 0.")

    if show_answers == "y":
        print(f"   Answer: {discriminant}")

print("\nDone!")
