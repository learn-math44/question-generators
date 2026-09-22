import random

print("=== Scientific Notation Operations Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    exponent = random.randint(1, 5)

    answer = a * b

    print(f"{i + 1}. ({a} × 10^{exponent}) × {b} = ?")

    if show_answers == "y":
        print(f"   Answer: {answer} × 10^{exponent}")

print("\nDone!")
