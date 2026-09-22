import random

print("=== Fact Family Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    total = a + b

    print(f"{i + 1}. Complete the fact family: {a} + {b} = {total}, {b} + {a} = ___")

    if show_answers == "y":
        print(f"   Answer: {total}")

print("\nDone!")
