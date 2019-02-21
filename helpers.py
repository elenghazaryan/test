import math


def arithmetic(a, b, s):
    if s == '+':
        return '{a}+{b}={sum}'.format(a=a, b=b, sum=a + b)
    elif s == '-':
        return 'a-b={}'.format(a - b)
    elif s == '/':
        if b != 0:
            return 'a/b={}'.format(a / b)
        else:
            return "unknown operation"
    elif s == '*':
        return 'a*b={}'.format(a * b)
    else:
        return "unknown operation"


def square(a):
    p = a * 4
    an = (2 ** 0.5) * a
    s = a * a
    return p, an, s


def season(a):
    if 2 <= a <= 4:
        return "spring"
    elif 5 <= a <= 7:
        return "summer"
    elif 8 <= a <= 10:
        return "autumn"
    else:
        return "winter"


def bank(a, years):
    a += a * 0.1
    for i in range(years - 1):
        a += a * 0.1
    return a


def is_prime(a):
    if a < 2:
        return False
    if a < 4:
        return True

    b = math.ceil(a ** 0.5)
    for i in range(2, b + 1, 1):
        if a % i == 0:
            return False
    return True

