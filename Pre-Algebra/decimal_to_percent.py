import random

print("=== Decimal to Percent Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    decimal = random.randint(1, 99) / 100

    print(f"{i + 1}. Convert {decimal} to a percent.")

    if show_answers == "y":
        print(f"   Answer: {decimal * 100}%")

print("\nDone!")
