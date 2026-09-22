import random

print("=== Sequence Patterns Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    start = random.randint(1, 20)
    difference = random.randint(2, 10)

    sequence = [
        start + difference * j
        for j in range(4)
    ]

    answer = start + difference * 4

    print(f"{i + 1}. {sequence[0]}, {sequence[1]}, {sequence[2]}, {sequence[3]}, ?")

    if show_answers == "y":
        print(f"   Answer: {answer}")

print("\nDone!")
