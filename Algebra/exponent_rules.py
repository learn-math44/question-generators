import random

print("=== Exponent Rules Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    a = random.randint(1, 10)
    m = random.randint(1, 5)
    n = random.randint(1, 5)

    print(f"{i + 1}. x^{m} × x^{n} = ?")

    if show_answers == "y":
        print(f"   Answer: x^{m+n}")

print("\nDone!")
