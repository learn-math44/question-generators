import random

print("=== Division Question Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    divisor = random.randint(1, 12)
    answer = random.randint(1, 12)
    dividend = divisor * answer

    print(f"{i + 1}. {dividend} ÷ {divisor} = ?")

    if show_answers == "y":
        print(f"   Answer: {answer}")

print("\nDone!")
