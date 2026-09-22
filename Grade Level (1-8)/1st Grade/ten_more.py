import random

print("=== Ten More Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    number = random.randint(0, 90)

    print(f"{i + 1}. What is 10 more than {number}?")

    if show_answers == "y":
        print(f"   Answer: {number + 10}")

print("\nDone!")
