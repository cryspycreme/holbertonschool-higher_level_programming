#!/usr/bin/env python3

class CountedIterator(iter):
    def __init__(self, object):
        iterator = super().iter(object)
        self.iterator = iterator
        self.count = 0

    def get_count(self):
        return self.count

    def __next__(self):
        try:
            self.count += 1
            return next(self.iterator)
        except:
            raise StopIteration
