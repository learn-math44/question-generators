import random

print("=== Scale Drawing Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    scale = random.choice([2, 5, 10])
    drawing = random.randint(2, 20)

    actual = drawing * scale

    print(f"{i + 1}. A drawing uses a scale of 1:{scale}. A length is {drawing} cm on the drawing. What is the actual length?")

    if show_answers == "y":
        print(f"   Answer: {actual} cm")

print("\nDone!")
