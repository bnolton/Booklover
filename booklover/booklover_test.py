import unittest
from booklover import BookLover


class BookLoverTestSuite(unittest.TestCase):

    def test_1_add_book(self):
    # add a book and test if it is in `book_list`.
        bnolt = BookLover("Brian", "bnolt@email.com", "fantasy")
        bnolt.add_book("The Hobbit", 5)
        book = "The Hobbit"
        self.assertTrue(book in bnolt.book_list)

    def test_2_add_book(self):
    # add the same book twice. Test if it's in `book_list` only once.
        bnolt = BookLover("Brian", "bnolt@email.com", "fantasy")
        bnolt.add_book("The Hobbit", 5)
        bnolt.add_book("The Hobbit", 5)
        self.assertEqual(bnolt.num_books, 1)

    def test_3_has_read(self):
    # pass a book in the list and test if the answer is `True`.
        bnolt = BookLover("Brian", "bnolt@email.com", "fantasy")
        bnolt.add_book("The Hobbit", 5)
        self.assertTrue(bnolt.has_read("The Hobbit"))

    def test_4_has_read(self):
    # pass a book NOT in the list and use `assert False` to test the answer is `True`
        bnolt = BookLover("Brian", "bnolt@email.com", "fantasy")
        bnolt.add_book("The Hobbit", 5)
        bnolt.has_read("The Simarillion", 4)
        self.assertFalse(bnolt.has_read("The Simarillion"))

    def test_5_num_books_read(self):
    # add some books to the list, and test num_books matches expected.
        bnolt = BookLover("Brian", "bnolt@email.com", "fantasy")
        bnolt.add_book("The Hobbit", 5)
        bnolt.add_book("Ender's Game", 5)
        bnolt.add_book("Fight Club", 3)
        bnolt.add_book("Pride and Prejudice", 2)
        actual = bnolt.num_books
        expected = 4
        self.assertTrue(actual, expected)

    def test_6_fav_books(self):
# add some books with ratings to the list, making sure some of them have rating > 3.
# Your test should check that the returned books have rating  > 3
    bnolt = BookLover("Brian", "bnolt@email.com", "fantasy")
    bnolt.add_book("The Hobbit", 5)
    bnolt.add_book("Ender's Game", 5)
    bnolt.add_book("Fight Club", 3)
    bnolt.add_book("Pride and Prejudice", 2)
    fav_books = bnolt.fav_books()

    self.assertEqual(len(fav_books), 2)
    self.assertTrue(all(fav_books['book_rating'] > 3))
    self.assertTrue(set(fav_books['book_name']) == {"The Hobbit", "Ender's Game"})


if __name__ == '__main__':
    unittest.main()
