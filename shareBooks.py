import tkinter as tk
import sys

#create window
root = tk.Tk()
root.title('Share A Book')
#disable ability to resize
root.resizable(False, False)

#create canvas to display basic menu options
canvas = tk.Canvas(root, width=800, height=500, bg="#FFECF0")
canvas.grid(columnspan=5, rowspan=5)

#display instructions for main main console
instructions = tk.Label(root, text="Would you like to receive or donate a book?", font=("Raleway", 25), bg="#FFECF0", fg="#FD728D")
instructions.grid(columnspan=5, column=0, row=1)

#donate button on main menu
browse_text = tk.StringVar()
donate_button = tk.Button(root, textvariable=browse_text, command=lambda:showTextBox("Donate"), font=("Raleway", 20), borderwidth=20, fg="#4786BD", height=3, width=16)
browse_text.set("Donate")
donate_button.grid(column=1, row=2)

#receive button on main menu
browse_text2 = tk.StringVar()
get_button = tk.Button(root, textvariable=browse_text2, command=lambda:showTextBox("Receive"), font=("Raleway", 20), borderwidth=20, fg="#4786BD", height=3, width=16)
browse_text2.set("Receive")
get_button.grid(column=3, row=2)

#quit button on main menu
browse_text3 = tk.StringVar()
quit_button = tk.Button(root, textvariable=browse_text3, command=lambda:quitImmediate(), font=("Raleway", 20), borderwidth=20, fg="#4786BD", height=3, width=16)
browse_text3.set("Quit")
quit_button.grid(column=2, row=3)

#redirect user to console after button is pressed, execute appropriate workflow
def showTextBox(directions):
    redirect = tk.Label(root, text="Go to console", font=("Raleway", 20), bg="white", fg="black")
    redirect.grid(columnspan=5, column = 0, row = 4, ipadx=5, ipady=5)

    if directions == "Donate":
        handleDonate()
    else:
        handleReceive()

#define global variable called books to hold list of availible books
global books
books = []

#storing colors
class colors:
    green = '\033[32m' 
    red = '\033[31m'
    purple = '\033[35m'
    blue = "\033[34m"
    cyan = '\033[36m'
    reset = '\033[m'

#create list of books from text file at start of program
def createBooksList():
  fh = open("books.txt", 'r')
  for line in fh:
    bookInfo = line.split("**")
    #each book is represented by a dictionary
    newBook = {
      "title": bookInfo[0],
      "author": bookInfo[1],
      "genre": bookInfo[2],
      "length": bookInfo[3],
      "email": bookInfo[4]
    }
    books.append(newBook)

#write changed list of books to text file at end of program
def writeUpdatedBooksList():
  fh = open("books.txt", 'w')
  for book in books:
    bookLine = ""
    bookLine += book.get("title") + "**"
    bookLine += book.get("author") + "**"
    bookLine += book.get("genre") + "**"
    bookLine += book.get("length") + "**"
    bookLine += book.get("email")
    fh.write(bookLine)  

#print out a list of books in table format
def printBooks(books):
  print("-----------------------------------------------------------------------------------------------------------")
  print (colors.green + "{:<8} {:<30} {:<30} {:<20} {:<10}".format('Index','Title','Author','Genre','Page Length') + colors.reset)
  index = 1
  for book in books:
    print ("{:<8} {:30} {:<30} {:<20} {:<10}".format(index,book.get("title"),book.get("author"),book.get("genre"),book.get("length")))
    index += 1
  print("-----------------------------------------------------------------------------------------------------------")

#print out book options with formatting
def printItems(itemList):
  print("------------------------------------------------------------")
  index = 1
  for item in itemList:
    print("{:<8} {:20}".format(index,item))
    index += 1
  print("------------------------------------------------------------")

  
#search books by genre and return result
def searchByGenre(genre):
  booksFound = []
  for book in books:
    if book.get("genre") == genre:
      booksFound.append(book)
  return booksFound

#gets all book genres 
def getGenres():
  genres = []
  for book in books:
    genre = book["genre"]
    if genre not in genres:
      genres.append(genre)
  return genres

#searches for books of certain length and return result
def searchByLength(minLen, maxLen): 
  booksFound = []
  for book in books:
    length = int(book["length"])
    if maxLen == "NA" and minLen == 500:
      if length >= minLen:
        booksFound.append(book)
    elif length >= minLen and length <= maxLen:
      booksFound.append(book)
  return booksFound

#allows the user to reserve a book
def getBook(booksFound):
  chosenBookNum = input(colors.blue + "Choose your book: " + colors.reset)
  while checkValidInput(chosenBookNum, len(booksFound)) == False:
      print(colors.red + "Please enter a valid number." + colors.reset)
      chosenBookNum = input("Choose your book: ")
  chosenBook = booksFound[int(chosenBookNum) - 1]
  print(colors.green + "Successfully reserved!" + colors.reset)
  print("Contact the owner to receive this book: " + chosenBook.get("email").rstrip()) 
#   books.remove(chosenBook) #remove book from book list

#checks if a user entry is valid, if not will give error message
def checkValidInput(entry, numberOfOptions):
  try:
    intEntry = int(entry)
  except ValueError:
    return False

  if numberOfOptions == "NA" and intEntry > 0:
      return True
  elif intEntry <= 0:
      return False
  elif intEntry <= numberOfOptions and intEntry > 0:
      return True
  return False

#Checks if books matching user's search are available, handles appropriately
def checkBookAvailability(booksFound):
  if (len(booksFound) != 0):
    printBooks(booksFound)
    getBook(booksFound)
  else:
    print("No books currently available that match your search :(")
  
createBooksList()

backToMain = 1		#default

#execute function if user would like to donate a book
def handleDonate():
    donate_button["state"] = "disabled"
    get_button["state"] = "disabled"
    print("-------------------Donate a Book-------------------")
    title = input(colors.cyan + "Title: " + colors.reset)
    author = input(colors.cyan + "Author: " + colors.reset)
    genre = input(colors.cyan + "Genre: " + colors.reset) 
    length = input(colors.cyan + "Page length: " + colors.reset)
    while checkValidInput(length, "NA") == False:
        print(colors.red + "Please enter a valid number." + colors.reset)
        length = input(colors.cyan + "Page length: " + colors.reset)
    email = input(colors.blue + "Enter your email: " + colors.reset)
    #add book to database
    addBook = {
        "title": title,
        "author": author,
        "genre": genre,
        "length": length,
        "email": email + "\n"
    }
    books.append(addBook)
    printBooks(books)
    print(colors.green + "Successfully added!" + colors.reset)
    handleProgramEnd()

#execute function if user would like to receive a book
def handleReceive():
    donate_button["state"] = "disabled"
    get_button["state"] = "disabled"
    print("-------------------Get a Book-------------------")
    print(colors.purple + "Would you like to search by genre or book length?" + colors.reset)
    print("1) Genre")
    print("2) Book Length")
    searchBy = input(colors.blue + "Enter your choice: " + colors.reset)
    while checkValidInput(searchBy, 2) == False:
        print(colors.red + "Error. Please enter a valid number." + colors.reset)
        searchBy = input(colors.blue + "Enter your choice: " + colors.reset)
        
    #user chooses to search by genre
    if int(searchBy) == 1:
        genres = getGenres()
        printItems(genres)
        genreNum = input(colors.blue + "Enter your choice: " + colors.reset)
        while checkValidInput(genreNum, len(genres)) == False:
            print(colors.red + "Please enter a valid number." + colors.reset)
            genreNum = input(colors.blue + "Enter your choice: " + colors.reset)
        booksFound = searchByGenre(genres[int(genreNum) - 1])
        # printBooks(booksFound)
        # getBook(booksFound)
        checkBookAvailability(booksFound)
    
    #user chooses to search by length
    elif int(searchBy) == 2:
        lengthOptions = ["0-100", "100-200", "200-300", "300-400", "400-500", "500+"]
        printItems(lengthOptions)
        selection = input(colors.blue + "Enter your choice: " + colors.reset)
        while checkValidInput(selection, 6) == False:
            print(colors.red + "Please enter a valid number." + colors.reset)
            selection = input(colors.blue + "Enter your choice: " + colors.reset)
        if int(selection) == 6:
            booksFound = searchByLength(500, "NA")
        else:  
            parameters = lengthOptions[int(selection)-1].split("-")
            booksFound = searchByLength(int(parameters[0]), int(parameters[1]))
        checkBookAvailability(booksFound)
    handleProgramEnd()

#quit program
def quitImmediate():
    writeUpdatedBooksList()
    print(colors.purple + "Goodbye." + colors.reset)
    sys.exit()


#end of program
def handleProgramEnd():
    quitProgram = input("Now, enter 'continue' to go to main menu, or type 'quit' to exit: ")
    if (quitProgram.lower() == "quit"):
        #writing updated booklist to text file
        quitImmediate()
    else:
        print(colors.green + "Return to main window" + colors.reset)
        donate_button["state"] = "normal"
        get_button["state"] = "normal"

root.mainloop()