import random

print("=== Rectangular Prism Volume Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    length = random.randint(2, 10)
    width = random.randint(2, 10)
    height = random.randint(2, 10)

    answer = length * width * height

    print(f"{i + 1}. Find the volume of a rectangular prism with dimensions {length}, {width}, and {height}.")

    if show_answers == "y":
        print(f"   Answer: {answer} cubic units")

print("\nDone!")
