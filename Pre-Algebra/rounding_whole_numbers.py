import random

print("=== Rounding Whole Numbers Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    number = random.randint(100, 99999)
    place = random.choice([10, 100, 1000])

    answer = round(number / place) * place

    print(f"{i + 1}. Round {number} to the nearest {place}.")

    if show_answers == "y":
        print(f"   Answer: {answer}")

print("\nDone!")
