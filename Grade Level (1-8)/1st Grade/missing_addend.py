import random

print("=== Missing Addend Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    total = random.randint(2, 20)
    first = random.randint(0, total)
    answer = total - first

    print(f"{i + 1}. {first} + ___ = {total}")

    if show_answers == "y":
        print(f"   Answer: {answer}")

print("\nDone!")
