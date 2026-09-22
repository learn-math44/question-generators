import random

print("=== Perfect Square Trinomial Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    a = random.randint(2, 10)

    print(f"{i + 1}. Factor: x² + {2*a}x + {a*a}")

    if show_answers == "y":
        print(f"   Answer: (x + {a})²")

print("\nDone!")
