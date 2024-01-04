#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    num = len(sys.argv) - 1
    if num >= 1:
        print("{} arguments:".format(num))
        for i in range(num) :
            print("{}: {}".format(i + 1, sys.argv[i + 1]))
    elif num == 0:
        print("0 arguments.")