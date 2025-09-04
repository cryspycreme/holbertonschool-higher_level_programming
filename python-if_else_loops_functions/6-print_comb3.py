#!/usr/bin/python3

for first_dig in range(10):
    for sec_dig in range(first_dig + 1, 10):
        print("{}{}".format(first_dig, sec_dig), end="")
        if first_dig < 8:
            print(", ", end="")
        else:
            continue
print("")
