#!/usr/bin/env python3
#

class Book:
    def __init__(self, title, page_count):
       
        self.title = title
        self.page_count = page_count
    pass

    def count_page(self):
        return self._page_count    

    def set_page_count(self, page_count):
        if isinstance(page_count, int):
            self._page_count = page_count
        else:
            print("page_count must be an integer")   

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
                 
    page_count = property(count_page,set_page_count)
    
    
        