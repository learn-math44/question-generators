import random

print("=== Prime Number Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    number = random.randint(10, 100)

    is_prime = number > 1

    for n in range(2, int(number ** 0.5) + 1):
        if number % n == 0:
            is_prime = False
            break

    print(f"{i + 1}. Is {number} prime?")

    if show_answers == "y":
        print(f"   Answer: {'Yes' if is_prime else 'No'}")

print("\nDone!")
