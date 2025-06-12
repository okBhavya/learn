a = 0
b = 1

for i in range(10):
    print(a)
    next = a + b
    a = b
    b = next


def get_nth_fibnocci(n):
    if n <= 0:
        return 0

    nth_fibanocci = 1 # find the nth nth_fibanocci HERE
    return nth_fibanocci



print('The fifth fibanocci number is', get_nth_fibnocci(5))


