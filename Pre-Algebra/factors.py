import random

print("=== Factors Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    number = random.randint(10, 50)

    factors = []

    for n in range(1, number + 1):
        if number % n == 0:
            factors.append(n)

    print(f"{i + 1}. Find all the factors of {number}.")

    if show_answers == "y":
        print(f"   Answer: {factors}")

print("\nDone!")
