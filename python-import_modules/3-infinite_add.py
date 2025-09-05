#!/usr/bin/python3
from sys import argv


# program.name num1[2] num2[5]
# length = 3
# i = 0, 1, 2
# sum = [1] + [2] = 7


def main():
    length = len(argv)

    i = 1
    sum = 0
    while (i < length):
        sum = sum + int(argv[i])
        i += 1
    print(sum)


if __name__ == "__main__":
    main()
