#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    summing = 0
    for i in range(1, len(sys.argv)):
        summing = summing + int(sys.argv[i])
    print("{}".format(summing))
