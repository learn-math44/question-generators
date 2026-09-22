import random

print("=== Integer Operations Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    a = random.randint(-20, 20)
    b = random.randint(-20, 20)
    operation = random.choice(["+", "-"])

    answer = a + b if operation == "+" else a - b

    print(f"{i + 1}. {a} {operation} ({b}) = ?")

    if show_answers == "y":
        print(f"   Answer: {answer}")

print("\nDone!")
