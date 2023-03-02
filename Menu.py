from Book import Book
from Library import Library

if(__name__ == "__main__"):
    try:
        mgmt = Library()
        print()
        print("------------------Welcome to Library Management System----------------")
        print()
        inp = input("For Admin section type 'a',for Student section type 's' or type any key to exit : ")
        while(inp =='a' or inp == 's'):
            if (inp == 'a'):
                cntue = 'y'
                choice = 0
                while(cntue.lower() != 'n' and choice != '20'):
                    print("Please enter the Username and Password ")
                    id = input("Enter the Username : ")   
                    password = input("Enter the Password : ")
                    if(id.lower() =="python" and password.lower() == "1234"): 
                        while(choice!="10"): 
                            print("\n------------------------Admin Section-------------------------------------\n")
                            print("------------------Welcome to Library Management System----------------\n")
                            print("\t\t1.Display all Books in Library")
                            print("\t\t2.Display all Available Books in Library")
                            print("\t\t3.Add Book")
                            print("\t\t4.Search Book by Book id")
                            print("\t\t5.Search Book by Book Name")
                            print("\t\t6.Display all Issued Books")
                            print("\t\t7.Issue Book")
                            print("\t\t8.Return Book")
                            print("\t\t9.Edit details of book")
                            print("\t\t10.Delete Book from Library")
                            print("\t\t20.Exit")
                            choice = int(input("Enter your Choice : "))
                            if (choice == 1):
                                mgmt.display_books()
                            elif (choice == 2):
                                mgmt.available_Book()
                            elif (choice == 3):
                                bname = input("Enter the Book Name : ")
                                author = input("Enter the Author name : ")
                                b1 = Book(bname,author)
                                mgmt.add(b1)
                            elif (choice == 4):
                                mgmt.search_id()
                            elif (choice == 5):
                                mgmt.search_name()
                            elif (choice == 6):
                                mgmt.issued_Book()
                            elif(choice == 7):
                                mgmt.issue_Book()
                            elif(choice == 8):
                                mgmt.return_Book()
                            elif(choice == 9):
                                mgmt.edit()
                            elif(choice == 10):
                                mgmt.delete()
                            elif (choice == 20):
                                print("======End of program=========")
                                exit()
                            else:
                                print("Please Enter a Correct choice")
                    else:
                        print("You have entered an incorrect Password ")
                        cntue = input("Do you want to continue again (y/n) : ")
            elif (inp == 's'):
                choice = 0
                #while (choice != 10):
                print("\n------------------------Student Section-------------------------------------\n")
                print("------------------Welcome to Library Management System----------------\n")
                print("\t\t1.Display all Books in Library")
                print("\t\t2.Display all Available Books in Library")
                print("\t\t3.Issue Book")
                print("\t\t4.Return Book")
                print("\t\t5.Search Book by Book Name")
                print("\t\t20.Exit")
                choice = int(input("Enter your Choice : "))
                if (choice == 1):
                    mgmt.display_books()
                elif(choice == 2):
                    mgmt.available_Book()
                elif(choice == 3):
                    mgmt.issue_Book()
                elif(choice == 4):
                    mgmt.return_Book()
                elif (choice == 5):
                    mgmt.search_name()
                elif(choice == 20):
                    print("======End of program=========")
                    exit()
                else:
                    print("Please Enter a Correct choice")
            else:
                print(" Please enter a valid choice !!! Thank You")
        else:
            print("Thank You")
    except ValueError :
        print("Please enter a valid choice")
