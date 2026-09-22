import random

print("=== Percent Equations Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    percent = random.choice([10, 20, 25, 50, 75])
    number = random.randint(10, 100)

    answer = percent / 100 * number

    print(f"{i + 1}. What is {percent}% of {number}?")

    if show_answers == "y":
        print(f"   Answer: {answer}")

print("\nDone!")
