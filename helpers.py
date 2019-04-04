import math
import random

from sympy.strategies.core import switch


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


def is_leap(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False


def date_is_valid(day, month, year):
    max_month = 31
    if month in [4, 6, 9, 11]:
        max_month = 30
    elif month == 2:
        if is_leap(year):
            max_month = 29
        else:
            max_month = 28
    if 1 <= day <= max_month:
        return True
    else:
        return False


def xor_cipher(text, key):
    encrypted_symbols = []
    for i in text:
        encrypted_symbols.append(chr(ord(i) ^ key))
    return ''.join(encrypted_symbols)


def xor_uncipher(text, key):
    return xor_cipher(text, key)


def rand(n):
    number = random.randint(-10, n)
    return number


# if __name__ == '__main__':
#     print('i am main')

def get_multiplier():
    def inner(a, b):
        return a * b

    return inner


# multiplier = get_multiplier()
# print(multiplier(10, 11))
# print(str(multiplier))


def logger(func):
    def wrapped(num_list):
        result = func(num_list)
        with open('log.txt', 'w') as f:
            f.write(str(result))

        return result
    return wrapped


@logger
def summator(num_list):
    return sum(num_list)

# with open('log.txt', 'r') as f:
#     print('log.txt: {}'.format(f.read()))


# x = input("input x=")
# y = input("input y=")
# r = input("input r=")


def in_circle(x0, y0, r, x, y):
    if ((x - x0) ** 2 + (y - y0) ** 2) ** 0.5 == r:
        return True
    else:
        return False


class Circle():
    s = None

    def __init__(self, x0, y0, r):
        self.__x0 = x0
        self.__y0 = y0
        if r <= 0:
            raise ValueError("invalid radius value")
        self.__r = r

    def on_circle(self, x, y):
        if ((x - self.__x0) ** 2 + (y - self.__y0) ** 2) ** 0.5 == self.__r:
            return True
        return False

    def get_radius(self):
        return self.__r

    def __repr__(self):
        return "x: {} \ny: {} \nradius: {}\n".format(self.__x0, self.__y0, self.__r)

    def in_circle(self, x, y):
        if ((x - self.__x0) ** 2 + (y - self.__y0) ** 2) ** 0.5 < self.__r:
            return True
        return False

    def area(self, __r):
        if self.s:
            return self.s
        self.s = math.pi * self.__r ** 2
        return self.s

    def length(self, __r):
        erk = 2 * math.pi * self.__r
        return erk

# c = Circle(1, 1, 3)
# print(c.area(3))


def return_the_reverse(num):
    n = 0
    while num > 0:
        a = num % 10
        num = num // 10
        n *= 10
        n += a
    return n


#print(return_the_reverse(int(input("input integer: "))))
#degree(10, 2)
#print(syracuse_hypotheses(int(input("input an integer"))))


def degree(num, deg): #minchev num-y exac tveri deg astichannery
    i = 1
    while i ** deg <= num:
        print(i ** deg, end=' ')
        i += 1


def syracuse_hypotheses(num):
    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = (3 * num + 1) // 2
        print(num, end=' ')
    return num


def range_probability(d):
    rand_value = random.random()
    f = 0
    for i in d.keys():
        f += d[i] / 100
        if rand_value < f:
            return i


def count():
    d = {}
    for i in range(1000000):
        range_value = range_probability({'one': 20, 'two': 10, 'three': 40, 'four': 30})
        d[range_value] = d.get(range_value, 0) + 1
    print(d)


# if __name__ == '__main__':
#     count()


def return_one_or_two(a):
    return 3-a


#print(return_one_or_two(1))


def vers1(n):
    return (3 * (n % 2)) + (n - 1) % 2 + n - 2


def vers2(n):
    return n - (n + 1) % 2 + n % 2


def vers3(n):
    return n - (-(n % 2)) ** (n % 2)


print(func3(12))





