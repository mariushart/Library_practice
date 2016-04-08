#!/usr/bin/env python3

from IPython import embed


class Book(object):

    def __init__(self, title, isbn, genre):
        self.title = title
        self.isbn = isbn
        self.genre = genre
        
    def is_isbn_same_as_title(self):
        if self.title == self.isbn:
            return True
        return False

class Author(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def is_scifi_author(self):
        pass
        
if __name__ == "__main__":
    embed()
