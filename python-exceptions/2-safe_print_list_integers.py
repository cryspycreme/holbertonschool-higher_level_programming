#!/usr/bin/python3

# x = no of elements to access
# x can be bigger than then length of my_list, however results in
# exception error

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except ValueError:
            continue
        except TypeError:
            pass
    print("")
    return count
