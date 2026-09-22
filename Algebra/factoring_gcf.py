import random

print("=== Factoring GCF Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    gcf = random.randint(2, 10)
    a = random.randint(2, 10)
    b = random.randint(2, 10)

    print(f"{i + 1}. Factor: {gcf*a}x + {gcf*b}")

    if show_answers == "y":
        print(f"   Answer: {gcf}({a}x + {b})")

print("\nDone!")
