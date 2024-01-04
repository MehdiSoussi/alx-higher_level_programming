#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as x
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, x.add(a, b)))
    print("{} - {} = {}".format(a, b, x.sub(a, b)))
    print("{} * {} = {}".format(a, b, x.mul(a, b)))
    print("{} / {} = {}".format(a, b, x.div(a, b)))
