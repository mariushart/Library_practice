#!/usr/bin/env python3

from IPython import embed


class Bog(object):

    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn

    def is_isbn_same_as_title(self):
        if self.title == self.isbn:
            return True
        return False


if __name__ == "__main__":
    embed()
