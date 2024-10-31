#### Homework for Module 8 that we're instructed to call HW09 (typo?)
#### Brian Nolton
#### frv3fp
#### github link: https://github.com/bnolton/DS5100-bnolton/blob/main/lessons/M08/HW08.pdf

import pandas as pd

class BookLover():
    """ Creates a class to keep track of books read and favorite books"""


    def __init__(self, name, email, fav_genre):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = 0
        self.book_list = pd.DataFrame({'book_name': [], 'book_rating': []})

    def add_book(self, book_name, book_rating):
        if book_name in self.book_list['book_name'].values:
            print("This book is already in the list.")
        else:
            new_book = pd.DataFrame({
                'book_name': [book_name],
                'book_rating': [book_rating]
            })
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books += 1
            print(f"{book_name} has been added to your book list.")

    def has_read(self, book_name):
        if book_name in self.book_list['book_name'].values:
            return True
        else:
            return False

    def num_books_read(self):
        return self.num_books

    def fav_books(self):
        return self.book_list[self.book_list['book_rating'] > 3]