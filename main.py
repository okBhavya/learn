def get_nth_fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    a = 0
    b = 1
    for i in range(2, n):
        next = a + b
        a = b
        b = next
    return b

n = int(input("Enter a number: "))
print(get_nth_fibonacci(n))
