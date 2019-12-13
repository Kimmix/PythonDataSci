# ----------------------------------------------  Example 01 ----------------------------------------------------------------
x = int(input('Function digital root =>  '))


def sum(x):
    y = 0
    for i in range(len(str(x))):
        y += int(str(x)[i])
    return y


print(sum(x))

# ----------------------------------------------  Example 02 ----------------------------------------------------------------
# Function called binom
n = int(input('n => '))
k = int(input('k => '))


def factorial(n):
    if n < 0:
        raise Exception('In factorail n must not negative! ')
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(n)/factorial(k)*factorial(n-k))

# ----------------------------------------------  Example 03 ----------------------------------------------------------------
x = input('input data separated by space => ')
list = x.split()
k = int(input('key => '))


def sum(list, k):
    y = 0
    for i in list:
        if (y < int(i) < k):
            y = int(i)
    return y


print(sum(list, k))
# ----------------------------------------------  Example 04 ----------------------------------------------------------------
x = input('Upper case =>')


def change_case(x):
    return x.lower()


print(change_case(x))
