
print("Welcome to your Personal Library Manager!")
print("1. Add a book")
print("2. Remove a book  ")
print("3. Search for a book")
print("4. Display all books  ")
print("5. Display statistics")
print("6. Exit")

start = True
while (start):
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
        quit()
    def addbook():
        pass

    def removebook():
        pass

    def searchbook():
        pass

    def displaybook():
        pass

    def displaystats():
        pass

    def quit():
        start = False
    




            
            
