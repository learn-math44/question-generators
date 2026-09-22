import random

print("=== Geometric Sequences Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    first = random.randint(1, 5)
    ratio = random.randint(2, 4)

    sequence = [first * ratio ** n for n in range(4)]
    answer = first * ratio ** 4

    print(f"{i + 1}. {sequence[0]}, {sequence[1]}, {sequence[2]}, {sequence[3]}, ?")

    if show_answers == "y":
        print(f"   Answer: {answer}")

print("\nDone!")
