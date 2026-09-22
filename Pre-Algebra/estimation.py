import random

print("=== Estimation Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    a = random.randint(10, 99)
    b = random.randint(10, 99)

    estimate = round(a / 10) * 10 + round(b / 10) * 10
    exact = a + b

    print(f"{i + 1}. Estimate {a} + {b} by rounding to the nearest ten.")

    if show_answers == "y":
        print(f"   Answer: Approximately {estimate}")

print("\nDone!")
