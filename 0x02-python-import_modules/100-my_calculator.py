#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    c = sys.argv[2]
    if c == "*":
        x = calculator_1.mul(a, b)
        print("{} {} {} = {}".format(a, "*", b, x))
    elif c == "-":
        x = calculator_1.sub(a, b)
        print("{} {} {} = {}".format(a, "-", b, x))
    elif c == "+":
        x = calculator_1.add(a, b)
        print("{} {} {} = {}".format(a, "+", b, x))
    elif c == "/":
        x = calculator_1.div(a, b)
        print("{} {} {} = {}".format(a, "/", b, x))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
