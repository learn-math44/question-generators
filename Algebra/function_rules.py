import random

print("=== Function Rules Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    m = random.randint(1, 10)
    b = random.randint(-10, 10)
    x = random.randint(1, 10)

    answer = m * x + b

    print(f"{i + 1}. f(x) = {m}x + {b}. Find f({x}).")

    if show_answers == "y":
        print(f"   Answer: {answer}")

print("\nDone!")
