import random

print("=== Expanded Form Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    number = random.randint(1000, 99999)

    digits = list(str(number))
    terms = []

    for position, digit in enumerate(digits):
        value = int(digit) * (10 ** (len(digits) - position - 1))
        if value != 0:
            terms.append(str(value))

    answer = " + ".join(terms)

    print(f"{i + 1}. Write {number} in expanded form.")

    if show_answers == "y":
        print(f"   Answer: {answer}")

print("\nDone!")
