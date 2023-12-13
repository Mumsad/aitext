import random

def demonstrate_distributive_law():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)

    left_hand_side = a * (b + c)
    right_hand_side = (a * b) + (a * c)

    print(f"Using the distributive law for a = {a}, b = {b}, c = {c}:")
    print(f"Left-hand side (a * (b + c)): {a} * ({b} + {c}) = {left_hand_side}")
    print(f"Right-hand side ((a * b) + (a * c)): ({a} * {b}) + ({a} * {c}) = {right_hand_side}")

    if left_hand_side == right_hand_side:
        print("The distributive law holds true.")
    else:
        print("The distributive law does not hold true.")

# Demonstrate the distributive law
demonstrate_distributive_law()
