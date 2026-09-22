import random

print("=== Function Evaluation Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    x = random.randint(1, 10)
    a = random.randint(2, 10)
    b = random.randint(1, 20)

    answer = a * x + b

    print(f"{i + 1}. If f(x) = {a}x + {b}, find f({x}).")

    if show_answers == "y":
        print(f"   Answer: {answer}")

print("\nDone!")
