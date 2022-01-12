set = {1, 2, 3, 4, 4, 4, 4, 3, 2, 1, 4, 5, 6, 2, 2, 1, 2, 2, 3, 4}
# Sets will remove all duplicates once printing
print(set)


def lambda_func(n):
    return lambda a: a * n


mydoubler = lambda_func(2)

print(mydoubler(11))


def map_func(a):
    return len(a)


x = map(map_func, ('apple', 'banana', 'cherry'))

print(x)

#convert the map into a list, for readability:
print(list(x))

print(5 % 1.5)