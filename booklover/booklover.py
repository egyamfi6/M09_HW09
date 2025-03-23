#Name: Emmanuel Gyamfi, ID: asw4uc
#GitHub:https://github.com/egyamfi6/DS5100-asw4uc/blob/main/lessons/M08/HW09.pdf

#booklover.py

import pandas as pd

class BookLover:
    """
    A class of booklovers with 5 attributes, including name, email, fav_genre,
    num_books and book_list
    """
    num_books=0
    book_list= pd.DataFrame({'book_name':[], 'book_rating':[]})
    
    def __init__(self, name, email, fav_genre):
        self.name=str(name)
        self.email=str(email)
        self.fav_genre=str(fav_genre)
        
        
    def add_book(self, book_name, rating):
        """
        This function takes a book name (string) and rating (integer from 0 to 5)
        It tries to add the book to book_list. It only adds a book to the 
        person’s book_list if that book doesn’t already exist.If it does exist,
        the function tells tell the user.
        """
       
        if not isinstance(book_name, str):            # this checks to ensure entry is a string
            raise typeError("entry must be a string") # raises error if entry is not a string
        if not isinstance(rating, int):                # this checks to ensure entry is an integer
            raise typeError("rating must be an integer.") #raises error id entry is not an integer
        if not 0 <= rating <= 5:                           #checking to see if entry is a number from 0 to 5
            raise ValueError("rating must be from 0 to 5.") # raise error if entry is not from 0 to 5
        if len(self.book_list[self.book_list['book_name'].isin([book_name])]): #checks if book is in book_list
            return f"Book already exist"      #tell user the entry exists                  
        new_book = pd.DataFrame({'book_name': [book_name], 'book_rating': [rating]}) #add new book
        self.book_list:pd.DataFrame = pd.concat([self.book_list, new_book], ignore_index=True)  
        return f"Book '{book_name}' added " # tells the user the books is added
           
        
    def has_read(self, book_name):
        """
        This function takes book_name (string) as input and 
        determines if the person has read the book.
        That is, if that book name is in book_list.
        The method return True if the person has read the book, False otherwise.
        """
        self.book_name=str(book_name)
        if len(self.book_list.loc[self.book_list['book_name'] == book_name])==1: #checks if book is read
            return True
        return False
       
        
    def num_books_read(self):
        """
        This function takes no parameters and just returns 
        the total number of books the person has read.
        """
        self.num_books = len(self.book_list) #uses len() to check the total number of books
        return self.num_books
    
    
    def fav_books(self):
        
        """
        This function takes no parameters and returns the 
        filtered dataframe of the person’s most favorite books.
        Books in this list have a rating > 3.
        """
        return self.book_list[self.book_list['book_rating'] > 3] # filters for books with ratings above 3.

if __name__ == '__main__':
    
    BookLover_instance = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
    result1=BookLover_instance.add_book("Fight Club", 4)
    print(result1)
    result=BookLover_instance.add_book("The Divine Comedy", 3)
    print(result)
    result2=BookLover_instance.add_book("The gods are not to blame", 5)
    print(result2)
    result3=BookLover_instance.add_book("Fight Club", 4)
    print(result3)
    print(f"BookLover's filtered books: {BookLover_instance.fav_books()}")
    
    #BookLover_instance2 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi") #instantiate 
    #BookLover_instance2.add_book("The Educationist", 5)  # Add a book
    #print(BookLover_instance2.has_read("The Ancestral Sacrifice"))  # Expects to return True.

   

