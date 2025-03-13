

user_data = {"name":"","age":"","phone":""}
books = []
start = True
while (start):
    print("Welcome to your Personal Library Manager!")
    user_name = input("Enter Your Name:")
    user_age = input("Enter Your Age:")
    user_phone = input("Enter Your Phone Number:")
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
            book_name = input("Enter the book title:")   
            book_author = input("Enter the author:")  
            book_model = input("Enter the publication year:")  
            book_status = input("Have you read this book? (yes/no):") 
            

            books.append({"Title":book_name,"Author":book_author,"Model":book_model,"Status":book_status,"User":user_name,"Age":user_age,"Phone":user_phone})
            print("Book Added Successfully!!")
            print(books)

        def removebook():
            pass

        def searchbook():
            pass

        def displaybook():
            pass

        def displaystats():
            pass


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
            start = False
    else:
        print("Register yourself first")
        




            
            
