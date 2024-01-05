#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    sum = 0
    n = len(sys.argv) - 1

    for num in range(n):
        sum += int(sys.argv[num + 1])
    print(sum)
