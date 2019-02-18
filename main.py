import helpers


def input_integers(number):
    l = list()
    start = 0
    while True:
        try:
            for i in range(start, number):
                start = i
                l.append(int(input("input integers: ")))
            break
        except ValueError:
            print("type error")
    return l


a, b = input_integers(2)
s = input("input operation")
print(helpers.arithmetic(a, b, s))

