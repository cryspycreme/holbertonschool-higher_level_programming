#!/usr/bin/env python3

class VerboseList(list):
    def append(self, item):
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, num_items):
        super().extend(num_items)
        print("Extended the list with [{}] items.".format(len(num_items)))

    def remove(self, item):
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, pos=-1):
        print("Popped [{}] from the list.".format(self[pos]))
        return super().pop(pos)
