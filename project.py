# Project Name : {{ STUDENT LIBRARY }}


class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks
    
    def displayAvailableBooks(self):
        print("Books present in this library are: ")
        for book in self.books:
            print("==> " + book)


    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. Please keep it safe and return it return it within 30 days")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry, this book has already been issued to someone else. Please wait until the book is returned")
            return False


    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returing this book! Hope you enjoyed reading it.")


class Student:
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book
    

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book
        


if __name__ == "__main__":
    centralLibrary = Library(["Python", "C++", "Django", "ICT", "AI", "Matchin Lerning"])

    student = Student()

    while (True):
        welcomeMsg = '''
        (( Welcome to Central Library ))

        Please choose an option:
        1. List all the books
        2. Request a book
        3. Return a book
        4. Exit the Library
        '''
        print(welcomeMsg)

        a = int(input("Enter a choice: "))

        if a == 1:
            centralLibrary.displayAvailableBooks()
        elif a == 2:
            centralLibrary.borrowBook(Student.requestBook())
        elif a == 3:
            centralLibrary.returnBook(Student.returnBook())
        elif a == 4:
            print("Thanks for choosing Central Library!")
            exit()
        else:
            print("Invalid Choice")