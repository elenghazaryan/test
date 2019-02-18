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


# while True:
#     try:
#         a = int(input())
#         b = int(input())
#         s = input()
#         break
#     except ValueError:
#         print("type error")
#
#
# print(arithmetic(a, b, s))

while True:
    try:
        a = int(input())
        break
    except ValueError:
        print("type error")

print(square(a))

def season(a):
    if 2 <= a <= 4:
        return "spring"
    elif 5 <= a <= 7:
        return "summer"
    elif 8 <= a <= 10:
        return "autmn"
    else:
        return "winter"

    print(season(1))