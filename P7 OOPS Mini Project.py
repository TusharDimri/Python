import  pyttsx3


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()




class Library:
    dict = {}
    def __init__(self, lib_name, list):
        self.username = lib_name
        self.books = list

    def display(self):
          return f"BOOKS CURRENTLY PRESENT IN THE LIBRARY:- \n{self.books}"

    @classmethod
    def details(cls, detail):
        cls.dict = detail

    @classmethod
    def access(cls):
        return cls.dict


    def lend(self, nm, book):
        nm = nm.capitalize()
        book = book.upper()
        d = {}
        name = nm.capitalize()
        book = book.upper()
        for bk in self.books:
            td = -1
            if bk == book:
                td = 1
                break

        if td == -1:
             print("SORRY,the book you want is not currently present in our library")
        else:
             self.books.remove(book)
             d[nm] = book
             self.details(d)
             print(f"Book successfully borrowed by {name}")
             print(self.access())

    def add_book(self, nm2, bknm2):
        nm2 = nm2.capitalize()
        bknm2 = bknm2.upper()
        td = 1
        for i in self.books:
            if bknm2 == i:
                td = -1
                break

        if td == -1:
            print("Thanks for your kind gesture but we already have that book in our library")
        else:
            self.books.append(bknm2)
            print(f"{bknm2} donated by {nm2}")

    def return_book(self, nm3, bknm3):
        nm3 = nm3.capitalize()
        bknm3 = bknm3.upper()
        td = 1
        a = self.access()
        for (name,book) in a.items():
            if (name,book) == (nm3,bknm3):
               td = -1
               break
        if td == -1:
            b = a.pop(nm3)
            self.books.append(b)
            print(f"Book successfully returned by {nm3}")
        else:
            print("We have no record of you borrowing book from our library,please check again")


# This chunk of code is for Library owner to create his own library
l = ["THE DEVIL WEARS PRADA", "A THOUSAND SPLENDID SUNS", "TWO BY TWO", "THE BEST OF RUSKIN BOND"]
a = Library("Ace Library", l)


if __name__ == '__main__':
   i=1
   speak(f"Welcome to {a.username}")
   speak(f"I am Stella and i'll tell you the instructions to use {a.username}:-")
   speak("Press D to see the books currently present in our library")
   speak("Press L to lend a book(if present) from our library")
   speak("Press A to donate a book to our library")
   speak("Press R to return a book you borrowed from our library")
   speak("Press H to give feedback")
   speak("Press Q to request the library for a book to be made available")
   speak("Press I to check instructions of use")
   speak("Press E to exit")
   speak("i will now show you the instructions in the screen")
   print(f"Welcome to {a.username}")
   print("How can we help you:-")
   print("1. Press D to see the books currently present in our library")
   print("2. Press L to lend a book(if present) from our library")
   print("3 Press A to donate a book to our library")
   print("4. Press R to return a book you borrowed from our library")
   print("5. Press H to give feedback ")
   print("6. Press Q to request the library for a book to be made available")
   print("7. Press I to check instructions of use")
   print("8. Press E to exit")
   while i == 1:
       choice = input("Enter Your Choice")
       if choice == 'D' or choice == 'd':
           print(a.display())

       elif choice == 'L' or choice == 'l':
           nm1 = input("Please Enter your name")
           book1 = input("Enter name of the book you want to lend from our library")
           a.lend(nm1, book1)

       elif choice == 'A' or choice == 'a':
           nm2 = input("Please Enter your name")
           book2 = input("Enter name of the book you want to donate to library")
           a.add_book(nm2, book2)

       elif choice == 'R' or choice == 'r':
           nm3 = input("Please Enter your name")
           book3 = input("Enter name of the book you want to return back to the library")
           a.return_book(nm3, book3)

       elif choice == 'H' or choice == 'h':
           f = input("Please give your feedback")
           lib = open("User Feedback.txt", "a")
           speak("i'm stella and i thank you on the behalf of my owner for giving us your feedback")
           lib.write(f"{f},\n")

       elif choice == 'q' or choice == 'q':
           f = input("type the name of the book you want in our library")
           n = input("enter your username")
           req = open("Book Requests", "a")
           req.write(f"{n} made a request for the book '{f}' to be made available")
           print("we will try our best to make that book available")
           speak("I'm stella, the manager of this library")
           speak("i'll make sure that i inform the owner about your request")


       elif choice == 'I' or choice == 'i':
           speak(f"Welcome to {a.username}")
           speak(f"I am Stella and i'll tell you the instructions to use {a.username}:-")
           speak("Press D to see the books currently present in our library")
           speak("Press L to lend a book(if present) from our library")
           speak("Press A to donate a book to our library")
           speak("Press R to return a book you borrowed from our library")
           speak("Press H to give feedback")
           speak("Press R to request the library for a book to be made available")
           speak("Press I to check instructions of use")
           speak("Press E to exit")

           print(f"Welcome to {a.username}")
           print("How can we help you:-")
           print("1. Press D to see the books currently present in our library")
           print("2. Press L to lend a book(if present) from our library")
           print("3 Press A to donate a book to our library")
           print("4. Press R to return a book you borrowed from our library")
           print("5. Press H to give feedback or request for a book.")
           print("6. Press Q to request the library for a book to be made available")
           print("7. Press I to check instructions of use")
           print("8. Press E to exit")



       elif choice == 'E' or choice == 'e':
           print(f"Thank You Very Much For Using {a.username}")
           speak("thank you very much for using our library")
           i = 2
           break

       else:
           print("Wrong Input")

