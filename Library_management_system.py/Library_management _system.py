class Book:
    def __init__(self, title, author, ISBN, available=True):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.available = available

    def borrowbook(self):
        if self.available:
            self.available = False
            print(f"You have borrowed '{self.title}'")
        else:
            print(f"Sorry '{self.title}' is already borrowed.")

    def returnbook(self):
        self.available = True
        print(f"You have returned '{self.title}'")

    def display_info(self):
        status = "Available" if self.available else "Not Available"
        print(f"\n**Book Details:**\n"
              f"Title: {self.title}\n"
              f"Author: {self.author}\n"
              f"ISBN: {self.ISBN}\n"
              f"Status: {status}\n")

# Creating an object 
book1 = Book("The Great Gatsby", "F Scott Fitzgerald", "123-456-789")
book1.borrowbook()
book1.returnbook()
book1.display_info()