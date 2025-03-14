user_data = {"name":"","age":"","phone":""}
books = [{'Title': 'arisha ki kahani', 'Author': 'arisha', 'Model': '1992', 'Status': 'Read', 'User': 'admin', 'Age': '22', 'Phone': '033efwe'}]
print("Welcome to your Personal Library Manager!")
user_name = input("Enter Your Name:")
user_age = input("Enter Your Age:")
user_phone = input("Enter Your Phone Number:")
start = True
while (start):
    
    if(user_name and user_phone and user_age):
        user_data["name"] = user_name
        user_data["age"] = user_age
        user_data["phone"] = user_phone
        print(user_data)
        print("1. Add a book")
        print("2. Remove a book  ")
        print("3. Search for a book")
        print("4. Display all books  ")
        print("5. Display statistics")
        print("6. Exit")

        def addbook():
            book_title = input("Enter the book title:")   
            book_author = input("Enter the author:")  
            book_model = int(input("Enter the publication year:"))  
            book_status = input("Have you read this book? (Read/Unread):") 
            

            books.append({"Title":book_title,"Author":book_author,"Model":book_model,"Status":book_status,"User":user_name,"Age":user_age,"Phone":user_phone})
            print("Book Added Successfully!!")
            print(books)

        def removebook():
            print(books)
            remove_book_title = str(input("Enter the book title:"))
            book_phone = input("Enter your phone #:")
            your_name = input("Enter your name")

            for book in books:
                if(book["Title"] == remove_book_title):
                    if(book_phone == user_data["phone"] and your_name == user_data["name"]):
                        books.remove(book)
                    else:
                        print("ky bhai apni book delete krna")
            print(books)
            print("Book removed successfully!")

 

        def searchbook():
            print("1. Title")
            print("2. Author")
            search = input("Enter your choice:")
            
            if(search == "1"):
                search_Title = input("Enter your Title:")
                book_Titles = list(map(lambda book:book["Title"],books))
                if(search_Title in book_Titles):
                    for book in books:
                        if(book["Title"] == search_Title):
                            print(book)
                            break 
                else:
                    print(f"No, '{search_author}' is not found in the books.")
            elif(search == "2"):
                search_author = input("Enter your author:")
                book_authors = list(map(lambda book:book["Author"],books))
                if(search_author in book_authors):
                    for book in books:
                        
                            if(book["Author"] == search_author):
                                print(book)
                                break 
                else:
                    print(f"No, '{search_author}' is not found in the books.")
            
        def displaybook():
            print("Following are the books in my library")
            print(books)

        def displaystats():
            print(f"Total Books: {len(books)}")
            read_books = list(map(lambda book:book["Status"] == "Read" , books))
            
            print(f"Percentage of books that have been read: {(len(read_books)/len(books))*100}%")


        input_choice = int(input("Enter your choice:"))

        if(input_choice == 1):
            addbook()
        elif(input_choice == 2):
            removebook()
        elif(input_choice == 3):
            searchbook()
        elif(input_choice == 4):
            displaybook()
        elif(input_choice == 5):
            displaystats()
        elif(input_choice == 6):
            print("Library saved to file. Goodbye!")
            start = False
    else:
        print("Register yourself first")
        




            
            
