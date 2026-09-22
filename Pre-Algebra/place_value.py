import random

print("=== Place Value Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

places = [
    ("ones", 0),
    ("tens", 1),
    ("hundreds", 2),
    ("thousands", 3)
]

for i in range(amount):
    number = random.randint(1000, 99999)
    place_name, power = random.choice(places)

    answer = (number // (10 ** power)) % 10

    print(f"{i + 1}. What digit is in the {place_name} place in {number}?")

    if show_answers == "y":
        print(f"   Answer: {answer}")

print("\nDone!")
