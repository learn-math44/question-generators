import random

print("=== Multiples Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    number = random.randint(2, 12)
    count = 5

    multiples = [number * n for n in range(1, count + 1)]

    print(f"{i + 1}. List the first {count} multiples of {number}.")

    if show_answers == "y":
        print(f"   Answer: {multiples}")

print("\nDone!")
