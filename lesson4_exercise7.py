from math import factorial

def fact(n):
    for i in range(n):
        if i == 1:
            continue
        else:
            yield factorial(i)

my_list = [i for i in fact(10)]

print(my_list)

