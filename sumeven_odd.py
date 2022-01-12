def sum_eo(n,t):
    if t == 'e':
        for num in range(0, n, 2):
            sum_num = sum(num for num in range(0, n, 2) if num % 2 == 0)
        print(sum_num)
    elif t == 'o':
        for num in range(0, n, 1):
            sum_num = sum(num for num in range(0, n, 1) if num % 2 != 0)
        print(sum_num)
    else:
        return -1

x = sum_eo(10,'e')

