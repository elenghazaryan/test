import helpers
import sympy


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


# print(helpers.is_prime(3))

import time

start_time = time.clock()
for i in range(2, 1000000):
    sympy.isprime(i)
end_time = time.clock()

print(end_time - start_time)

