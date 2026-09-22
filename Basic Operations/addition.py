import random

print("=== Addition Question Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    answer = a + b

    print(f"{i + 1}. {a} + {b} = ?")

    if show_answers == "y":
        print(f"   Answer: {answer}")

print("\nDone!")
