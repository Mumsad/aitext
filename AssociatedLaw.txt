#Code for associative law.

# Left-right associativity
# 100 / 10 * 10 is calculated as
# (100 / 10) * 10 and not
# as 100 / (10 * 10)
print(100 / 10 * 10)
 
# Left-right associativity
# 5 - 2 + 3 is calculated as
# (5 - 2) + 3 and not
# as 5 - (2 + 3)
print(5 - 2 + 3)
 
# left-right associativity
print(5 - (2 + 3))
 
# right-left associativity
# 2 ** 3 ** 2 is calculated as
# 2 ** (3 ** 2) and not
# as (2 ** 3) ** 2
print(2 ** 3 ** 2)

"""

def associative_law_example(a, b, c):
    # Using parentheses as per the Associative Law
    result1 = (a + b) + c
    result2 = a + (b + c)

    # Check if the results are equal
    if result1 == result2:
        print(f'The expression ({a} + {b}) + {c} is equal to {a} + ({b} + {c})')
        print(f'Result: {result1} == {result2}')
    else:
        print(f'The expression ({a} + {b}) + {c} is NOT equal to {a} + ({b} + {c})')
        print(f'Result: {result1} != {result2}')

# Example usage
associative_law_example(2, 3, 4)

""""
