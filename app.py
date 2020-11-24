"""
___________________________________________________________________
Group Members                 |     Roll Number                  
_________________________________|_________________________________
Vishnu M                            | AM.EN.U4ELC19037          
Vukkum Sri Charan              | AM.EN.U4ELC19038           
Vyshnav P                           | AM.EN.U4ELC19039
Vyshnavi Guntur                  | AM.EN.U4ELC19040
_________________________________|__________________________________
"""

class Library:
    def __init__(self, list, name):
        #copying the list
        self.booksList = list
        #name is just an option if the library has a name
        self.name = name
        #lendDict is a dictionary that stores the name and book name 
        self.lendDict = {}
#-----------------------------------------------------------------------------------------------------
    def displayBooks(self):
        print(f"\nWe have following books in our library: {self.name}")
        i=1
        self.booksList.sort()       #list is sorted
        for book in self.booksList:     #book is just an iterating variable
            print(i,book)
            i+=1
        print("\t\t\t\t\t-=-=-=-=-=-=-=-=-")
#-----------------------------------------------------------------------------------------------------
    def lendBook(self, user, book):
        booka=""
        booka=book.lower()      #copying the name of the book received from the function call(line 72) and then converted to lower case characters to compare
        flag=0
        for i in range(len(self.booksList)):
            book_name=""
            book_name=self.booksList[i].lower()     #copying the name of the book in the list so that we can compare it with "booka"
            set1 = set(booka.split(' '))                    #set is an inbuilt function to make any sentence into a single set
            set2 = set(book_name.split(' '))
            if set1==set2:                                      #comparing the 2 sets
                self.lendDict.update({book:user.lower()})               #here we are adding the book name and the name of the person who took the book into the dictionary 
                print("Lender-Book database has been updated. You can take the book now\n")
                self.booksList.remove(self.booksList[i])                #after the book is taken, the book is removed from the list
                flag=1
                break
        if flag==0:
            print("Book is not available\n")
        print("\t\t\t\t\t-=-=-=-=-=-=-=-=-")
#-----------------------------------------------------------------------------------------------------      
    def addBook(self, book):                        #basic programme appending an element into the booksList
        self.booksList.append(book)
        print("Book has been added to the Library\n")
        print("\t\t\t\t\t-=-=-=-=-=-=-=-=-")    
#-----------------------------------------------------------------------------------------------------
    def returnBook(self, book,user):            # programme to adding the book back to the list and removing the content from the dictionary
        if book in self.lendDict:
            self.addBook(book)
            self.lendDict.pop(book)
        else:
            print("User has no Dues")
            print("\t\t\t\t\t-=-=-=-=-=-=-=-=-") 
#-----------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    books = Library(['William Shakespeare First Folio', 'Harry Potter and the Philosopher’s/Sorcerer’s Stone', 'Pride and Prejudice', 'Ulysses', 'Casino Royale','The Fountainhead','Jane Eyre','The Tale of Peter Rabbit','Dracula'],"The Chronicles")        #here "books" is the instance, "Library" is the class, the list and the name of the library are the arguments
    print(f"\t\t\tWelcome to the Library Management Application\nIn this library you can find the first edition of every great book ever written in history, some books costs millions. \n\nEnter operation code (watchout for indentation)\n")
  
    print("1. Display Books")
    print("2. Lend a Book")
    print("3. Add a Book")
    print("4. Return a Book")
    print("0. Quit \n")
    while(True):
        user_choice = input()
        if user_choice not in ['1','2','3','4','0']:
            print("Please enter a valid option")
            continue
        else:
            user_choice = int(user_choice)
        if user_choice == 1:
            books.displayBooks()                    #calling the function to display the books
        elif user_choice == 2:
            book =input("Enter the name of the book you want to lend : ")
            user = input("Enter your name : ")
            books.lendBook(user, book)          #calling the function to lend the books
        elif user_choice == 3:
            book = input("Enter the name of the book you want to add : ")
            books.addBook(book)                 #calling the function to add the books
        elif user_choice == 4:
            book = input("Enter the name of the book you want to return : ")
            user=input("Enter your name :  ")
            books.returnBook(book,user)         #calling the function to return the books
        elif user_choice == 0:
            exit()
        else:
            print("Not a valid option")
            continue
        print("Enter your operation code ")
