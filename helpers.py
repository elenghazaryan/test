import math
import random


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
