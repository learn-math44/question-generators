import random

print("=== Perimeter Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    length = random.randint(2, 20)
    width = random.randint(2, 20)

    answer = 2 * (length + width)

    print(f"{i + 1}. Find the perimeter of a rectangle with length {length} and width {width}.")

    if show_answers == "y":
        print(f"   Answer: {answer}")

print("\nDone!")
