#!/usr/bin/python3
def uppercase(str):
    for c in str:
        ucp = ord(c)
        if ord(c) >= 97 and ord(c) <= 122:
            ucp = ord(c) - 32
        print("{}".format(chr(ucp)), end="")
    print("")
