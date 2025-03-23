#Name: Emmanuel Gyamfi, ID: asw4uc
#GitHub:https://github.com/egyamfi6/DS5100-asw4uc/blob/main/lessons/M08/HW09.pdf

#booklover_test.py

#import
import pandas as pd
from booklover import BookLover
import unittest
 

class BookLoverTestSuite(unittest.TestCase):
    def test_1_add_book(self):
        # add a book and test if it is in `book_list`.
        BookLover_instance = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi") #instantiate
        BookLover_instance.add_book("Fight Club", 4)  # Adding a book
        self.assertTrue(BookLover_instance.has_read("Fight Club"))  #assertTrue for added successfullly
        
 
    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        """
        This adds the same book twice and tests if the book is added once
        """
        BookLover_instance = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi") #instantiate
        BookLover_instance.add_book("The Divine Comedy",3)  # Adding the book
        BookLover_instance.add_book("The Divine Comedy",3)  # Adding the same book
        self.assertTrue(BookLover_instance.has_read("The Divine Comedy"))  #True for book already exist.
                
    def test_3_has_read(self):
        
        # pass a book in the list and test if the answer is `True`.
        """
        This passes a book that is already in the list. Expects the answer to be True
        """
        BookLover_instance = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi") #instantiate
        BookLover_instance.add_book("Fight Club", 4)  # Adding a book 
        self.assertTrue(BookLover_instance.has_read("Fight Club"))  # Expects the answer to be True

        
    def test_4_has_read(self):
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        """
        This passes a book Not in the list and uses assert False to test if the answer is True
        """
        BookLover_instance = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi") #instantiate
        BookLover_instance.add_book("The Educationist", 5)  # Add a book
        self.assertFalse(BookLover_instance.has_read("The Ancestral Sacrifice")) #Expects to returnTrue.

    def test_5_num_books_read(self):
        # add some books to the list, and test num_books matches expected.
        BookLover_instance = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi") #instantiate
        BookLover_instance.add_book("The gods are not to blame", 5)  # Add a book
        BookLover_instance.add_book("The Tragical History of Dr. Festus", 5)  # Add another book
        BookLover_instance.add_book("The Ontolologist", 5)  # Add another book
        BookLover_instance.add_book("Homa Away from Roma", 1)
        BookLover_instance.add_book("The AI Scientist", 5)
        counts_expected: int = 5
        num_books_read: int = BookLover_instance.num_books_read()
 
        self.assertEqual(num_books_read, 5)
 

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        BookLover_instance = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")  #instantiate
        BookLover_instance.add_book("The gods are not to blame", 5)  # Add a book
        BookLover_instance.add_book("The Tragical History of Dr. Festus", 5)  # Add another book
        BookLover_instance.add_book("The Ontolologist", 3)  # Add another book
        BookLover_instance.add_book("Homa Away from Roma", 1)
        BookLover_instance.add_book("The AI Scientist", 2)
        df=pd.DataFrame(BookLover_instance.fav_books())
        self.assertTrue((df['book_rating'] > 3).all(), "filtered books with rating > 3" )
 
 
if __name__ == '__main__':
    unittest.main(verbosity=3)
