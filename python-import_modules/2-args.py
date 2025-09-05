#!/usr/bin/python3
from sys import argv


def main():
    length = len(argv)
    if length > 2:
        print("{} arguments:".format(length - 1))
    elif length == 1:
        print("0 arguments.")
    else:
        print("{} argument:".format(length - 1))

    i = 1
    while i < length:
        print("{}: {}".format(i, argv[i]))
        i += 1


if __name__ == "__main__":
    main()
