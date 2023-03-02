from datetime import date,datetime
from prettytable import PrettyTable

class Library:
    def display_books(self):
        print("\n-----------------------------Display Section--------------------------------\n")
        try:
            #print("Book id"," |\t","\tBook Name ","\t\t", "\t|","Author Name")
            table = PrettyTable(["Book ID", "Book Name", "Author Name", "Lender Name ", "Issue Date"])
            with open("LibraryData.txt","r") as fp:
                for line in fp:
                    line = line.split(',')
                    table.add_row([line[0], line[1],line[2],line[4],line[5]])
                    #print(line[0],"\t |\t",line[1],"\t\t","\t|",line[2])
                print(table)
                print("*** N/I - Not Issued")
            return
        except FileNotFoundError:
            print("File does not exist")

    def issue_Book(self):
        print("\n----------------------------Issue Book Section-----------------------------------\n")
        try:
            book_id = input("Enter the Book id : ")
            all = []
            found = False
            with open("LibraryData.txt","r") as fp:
                for line in fp:
                    line = line.split(',')
                    if(line[0] == book_id):
                        if(line[3] == '0'):
                            print("Book has already been issued to",line[4],"on",line[5])
                            choice = input("Enter 'c' to continue or 'q' to quit : ")
                            if (choice.lower() == 'q'):
                                return 
                            elif(choice.lower() == 'c'):
                                return Library.issue_Book(self)
                            else:
                                print("Please enter a Valid choice")
                                return
                        else:
                            name = input("Enter Your Name : ")
                            issue_date = input("Enter date in dd-mm-yyyy format : ")
                            issue_date = issue_date.split("-")
                            issue_date = date(int(issue_date[2]),int(issue_date[1]),int(issue_date[0]))
                            line[3] = '0'
                            line[4] = name
                            line[5] = str(issue_date) + str("\n")
                            line = ",".join(line)
                            all.append(line)
                            found = True
                            print()
                            print("Book Issued Successfully")
                            print("Please return the book within 7 days ")
                            print("After which a fine of 20 rs will be added per day")
                            print()
                    else:
                        line = ",".join(line)   
                        all.append(line)
            if(found):
                with open("LibraryData.txt","w") as fp:
                    for book in all:
                        fp.write(book)
            else:
                print("Please enter a Valid Book ID")
        except FileNotFoundError:
            print("File does not exist")

    def return_Book(self):
        print("\n----------------------Return Book Section----------------------------\n")
        try:
            book_id = input("Enter the Book ID : ")
            all = []
            found = False
            present = False
            with open("LibraryData.txt","r") as fp:
                for line in fp:
                    line = line.split(',')
                    if(line[0] == book_id):
                        if(line[3] == '1'):
                            print("The Book is already present in the Library.")
                            return
                        else:
                            submit_date = input("Enter date in dd-mm-yyyy format : ")
                            submit_date = submit_date.split("-")
                            submit_date = date(int(submit_date[2]),int(submit_date[1]),int(submit_date[0]))
                            issue_date = line[5].strip()
                            format = "%Y-%m-%d"
                            issue_date = datetime.strptime(issue_date, format).date()
                            days = (submit_date-issue_date).days
                            remain = (days - 7)
                            line[3] = '1'
                            line[4] = 'N/I'
                            line[5] = '-' + str("\n")
                            line = ",".join(line)
                            all.append(line)
                            present = True
                            if(days >= 0):
                                found = True
                                if(remain > 0):
                                    print()
                                    print("You are returning the book",remain,"days late")
                                    print("You have to pay fine of",remain*20,"Rs as a late fee\n")
                                    print("Book returned Successfully")
                                else:
                                    print()
                                    print("You Don't have any fine")
                                    print("Book returned Successfully\n")
                            else:
                                print()
                                print("You Have entered an invalid date")
                    else:
                        line = ",".join(line)
                        all.append(line)
            if(present):    
                if(found):
                    with open("LibraryData.txt","w") as fp:
                        for book in all:
                            fp.write(book)        
                else:
                    print("Please enter valid details regarding submission")
            else:
                print()
                print("Please enter a Valid Book ID")
        except FileNotFoundError:
            print("File does not exist")
    
    def available_Book(self):
        print("\n------------------------Available Book Section-----------------------------\n")
        try:
            table = PrettyTable(["Book ID", "Book Name", "Author Name"])
            with open("LibraryData.txt","r") as fp:
                for line in fp:
                    line = line.split(',')
                    if(line[3] == '1'):
                        table.add_row([line[0], line[1],line[2]])
                print(table)
        except FileNotFoundError:
            print("File does not exist")
    
    def add(self,b1):
        print("\n-------------------------Add Book Section---------------------------\n")
        with open("LibraryData.txt","a") as fp:
            data = str(b1)
            fp.write(data)
            fp.write("\n")
        print("Book has been added successfully")
        
    def search_id(self):
        print("\n-------------------------Search by ID Section----------------------------\n")
        try:
            book_id = input("Enter the id of the Book : ")
            with open("LibraryData.txt","r") as fp:
                for line in fp:
                    line = line.split(',')
                    if (book_id == line[0]):
                        if(line[3] == '0'):
                            table = PrettyTable(["Book ID", "Book Name", "Author Name", "Lender Name ", "Issue Date"])
                            table.add_row([line[0], line[1],line[2],line[4],line[5]])
                            print(table)
                            break
                        else:
                            table = PrettyTable(["Book ID", "Book Name", "Author Name"])
                            table.add_row([line[0], line[1],line[2]])
                            print(table)
                            break
                else:
                    print("No Book Found with Book ID :",book_id)  
                    inp = input("Do you wish to continue (y/n) : ")
                    if(inp.lower() == 'y'):
                        return Library.search_id(self)
                    else:
                        return 
        except FileNotFoundError :
            print("File Not found")    

    def search_name(self):
        print("\n---------------------------Search by Name Section------------------------------\n")
        try:
            name = input("Enter the name of the Book : ")
            with open("LibraryData.txt","r") as fp:
                for line in fp:
                    line = line.split(',')
                    if (name.lower() == line[1].lower()):
                        print()
                        if(line[3] == '0'):
                            table = PrettyTable(["Book ID", "Book Name", "Author Name", "Lender Name ", "Issue Date"])
                            table.add_row([line[0], line[1],line[2],line[4],line[5]])
                            print(table)
                            break
                        else:
                            table = PrettyTable(["Book ID", "Book Name", "Author Name"])
                            table.add_row([line[0], line[1],line[2]])
                            print(table)
                            break
                else:
                    print("Book with name ",name," not Found")  
                    inp = input("Do you wish to continue (y/n) : ")
                    if(inp.lower() == 'y'):
                        return Library.search_name(self)
                    else:
                        return
        except FileNotFoundError :
            print("File Not found")
    
    def issued_Book(self):
        print("\n---------------------------Total Book Issued Section-------------------------------\n")
        try:
            table = PrettyTable(["Book ID", "Book Name", "Author Name", "Lender Name ", "Issue Date"])
            with open("LibraryData.txt","r") as fp:
                count = 0
                for line in fp:
                    line = line.split(',')
                    if(line[3] == '0'):
                        table.add_row([line[0], line[1],line[2],line[4],line[5]])
                        count += 1
                if (count == 0):
                    print()
                    print("No Book has been issued to anyone")
                else:
                    print(table)
        except FileNotFoundError:
            print("File does not exist")
    
    def edit(self):
        print("\n---------------------------Edit by Book Name Section-------------------------------\n")
        try:
            book_id = input("Enter the Book ID : ")
            all = []
            found = False
            with open("LibraryData.txt","r") as fp:
                for line in fp:
                    line = line.split(',')
                    if(line[0] == book_id):
                        inp = input("Enter 'a' for book name 'b' for author name or 'c' for both : ")
                        if(inp == 'a'):
                            line[1] = input("Enter the name of Book : ")
                        elif(inp == 'b'):
                            line[2] = input("Enter the author name : ")
                        elif(inp == 'c'):
                            line[1] = input("Enter the name of Book : ")
                            line[2] = input("Enter the author name : ")
                        else:
                            print("Enter the valid option")
                            return Library.edit(self)
                        line = ",".join(line)
                        all.append(line)
                        found = True
                    else:
                        line = ",".join(line)
                        all.append(line)
            if(found):
                with open("LibraryData.txt","w") as fp:
                    for book in all:
                        fp.write(book) 
                print("Details updated Successfully")
            else:
                print()
                print("Please enter a Valid Book ID")
                inp = input("Do you wish to continue (y/n) : ")
                if(inp.lower() == 'y'):
                    return Library.edit(self)
                else:
                    return

        except FileNotFoundError:
            print("File does not exist")
    
    def delete(self):
        print("\n---------------------------Delete Book Section-------------------------------\n")
        try :
            inpt = input("Enter 'a' to delete by book id or 'b' to delete by book name : ")
            all =[]
            found = False
            if (inpt == 'a'):
                id = input("Enter the Book id of the Book to be deleted : ")
                with open("LibraryData.txt","r") as fp:
                    for line in fp:
                        line = line.split(',')
                        if(id != line[0]):
                            line = ",".join(line)
                            all.append(line)
                        else:
                            found = True
            elif(inpt == 'b'):
                name = input("Enter the name of the Book to be deleted : ")
                with open("LibraryData.txt","r") as fp:
                    for line in fp:
                        line = line.split(',')
                        if(name.lower() != line[1].lower()):
                            line = ",".join(line)
                            all.append(line)
                        else:
                            found = True
            else:
                print("Enter the valid choice ")
                return Library.delete(self)

            if(found):
                with open("LibraryData.txt","w") as fp:
                    for book in all:
                        fp.write(book) 
                print("Details Deleted Successfully")
            else:
                print()
                print("Please enter Valid Book details")
                inp = input("Do you wish to continue (y/n) : ")
                if(inp.lower() == 'y'):
                    return Library.delete(self)
                else:
                    return

        except FileNotFoundError :
            print("File does not exist")