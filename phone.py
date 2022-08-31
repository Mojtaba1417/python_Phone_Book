from PhoneBook import *
def main_menu():
        print("-"*40)
        print("| ","1 ) Add a new contact")
        print("| ","2 ) show contacts")
        print("| ","3 ) edit contact")
        print("| ","4 ) delete contact")
        print("| ","5 ) Exit")
        print("-"*40)


current = 0
while current != "5":
    p1 = Phone_book()
    import os
    os.system('cls')
    main_menu()
    current=input()
    if current == "1":
        os.system('cls')
        print(" "*10,"add a new contact menu")
        p1.add()
        os.system('cls')
        main_menu
    elif current=="2":
        print(" "*10,"show all contacts")
        os.system('cls')
        p1.show()
        print()
        print()
        answer = input("do you want back to main menu ? ")
        if answer.lower() == "yes" :
            main_menu
        else:
            p1.show()
    elif current=="3":
        os.system('cls')
        name= input("which contact would you like to edit ? ")
        p1.update_contact(name)
    elif current=="4":
        os.system('cls')
        name= input("which contact would you like to delete ? ")
        p1.remove(name)
            