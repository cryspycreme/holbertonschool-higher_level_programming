#!/usr/bin/env python3

class CountedIterator:
    def __init__(self, object):
        self.object = iter(object)
        self.count = 0

    def get_count(self):
        return self.count

    def __next__(self):
        try:
            next_obj = next(self.object)
            self.count += 1
            return next_obj
        except StopIteration:
            raise StopIteration
