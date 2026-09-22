import random

print("=== Order of Operations Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    a = random.randint(2, 10)
    b = random.randint(2, 10)
    c = random.randint(1, 20)

    answer = a * b + c

    print(f"{i + 1}. {a} × {b} + {c} = ?")

    if show_answers == "y":
        print(f"   Answer: {answer}")

print("\nDone!")
