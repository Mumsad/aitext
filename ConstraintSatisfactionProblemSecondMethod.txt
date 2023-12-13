def add_constraint(var):
    constraints[var] = []
    for i in range(9):
        if i != var[0]:
            constraints[var].append((i, var[1]))
        if i != var[1]:
            constraints[var].append((var[0], i))
    sub_i, sub_j = var[0] // 3, var[1] // 3
    for i in range(sub_i * 3, (sub_i + 1) * 3):
        for j in range(sub_j * 3, (sub_j + 1) * 3):
            if (i, j) != var:
                constraints[var].append((i, j))
                  
constraints = {}
for i in range(4):
    for j in range(4):
        add_constraint((i, j))
          
print(set(constraints))
c=len(constraints)
print(c)

#######

even_numbers = []
for i in range(4):
    for j in range(4):
        if ((i% 2 == 0) and (j % 2 == 0 )):
            even_numbers.append((i, j))

print("Even numbers within the constraints:", even_numbers)
d=len(even_numbers)
print(d)

odd_numbers = []
for i in range(4):
    for j in range(4):
        if  ((i% 2 == 1) and (j % 2 == 1)):
            odd_numbers.append((i, j))
print("Odd numbers within the constraints:", odd_numbers)
e=len(odd_numbers)
print (e)



f= d/c
print( "Probability of having an even number from constraints is ", f)
g=e/c
print( "Probability of having a odd number from constraints is ", g)
