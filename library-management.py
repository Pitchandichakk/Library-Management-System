              
              
              
              


                                  #  LIBRARY MANAGEMENT PROJECT

Library = []
def add_books(): 
    title = input("Enter The Book Title : ").lower().strip()
    for book_title in Library:
        if book_title["title"] == title:
            print("Book has been already exist")
            return
        
    author = input("Enter The Author Name : ").lower().strip()
    genre = input("Enter The Genere : ")
    Library.append({"title":title,"author":author,"genre":genre ,"status":'available'})
    print(f"{title} book was added ")

    # VIEW BOOKS FUNCTION

def view_book():
    if len(Library) < 1:
        print("Library was Empty")
        return
    for books in Library:
        print(f"Title:{books['title']} \n Author {books['author']} \n Genre : {books['genre']}")

#      SEARCH BOOK FUNCTION
            
def search_books():
    title = input("Enter the title of book : ").strip()
    for books in Library:
        if books['title'].lower() == title.lower():
           print(f"Title : {books['title']} \n Author {books['author']} \n genre : {books['genre']}")
        else:
            print("Book Not Found")

    # BORROW BOOK FUNCTION 
def borrow_books():
    title = input("Enter Book Title : ")
    for books in Library:
        if books['title'].lower() == title.lower():
            if books['status'] == "available":
                books['status'] = "borrowed"
                print(f"You Borrowed book {books['title']}")
            else:
                print(f"Sorry , {books['title']} is not available")
            return
        print(f"{books['title']} is not found in library")


    #  RETURN BOOK FUNCTION
def return_books():
    title = input("Enter Book Title : ")
    for books in Library:
        if books['title'].lower() == title.lower():
            if books['status'] == "borrowed":
                books['status'] = "available"
                print(f"You Returned book {books['title']} successfully")
            else:
                print(f" {books['title']} is available")
            return
        print(f"{books['title']} is not found in library")


        #  DISPLAY FUNCTION

def display_menu():
    print("-------  LIBRARY MANAGEMENT  --------")
    print(" 1. ADD BOOKS ->")
    print(" 2. VIEW BOOKS ->")
    print(" 3. SEARCH BOOKS ->")
    print(" 4. BORROW BOOKS ->")
    print(" 5. RETURN BOOKS ->")
    print(" 6. EXIT  --")

    # MAIN FUNCTION
def main():
    while True:
        display_menu()
        choise = input("Enter The Choise ( 1 - 6 ) : ")
        if choise == "1":
            add_books()
        elif choise == "2":
            view_book()
        elif choise == "3":
            search_books()
        elif choise == '4':
            borrow_books()
        elif choise == '5':
            return_books()
        elif choise == '6':
            print("You Exit the library GOOD BYE ")
            break
        else:
            print('Ivalid Choise Enter ( 1 - 6 )')


main()
    
