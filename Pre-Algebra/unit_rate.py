import random

print("=== Unit Rate Generator ===")

amount = int(input("How many questions do you want? "))
show_answers = input("Do you want the correct answers included? (y/n): ").lower()

print("\n--- Questions ---")

for i in range(amount):
    quantity = random.randint(2, 20)
    price = random.randint(5, 100)

    answer = price / quantity

    print(f"{i + 1}. {quantity} items cost ${price}. What is the cost per item?")

    if show_answers == "y":
        print(f"   Answer: ${answer:.2f}")

print("\nDone!")
