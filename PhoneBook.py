class Address:
    def __init__(self, street, city, state, zipcode, street2=''):
        self.street = street
        self.street2 = street2
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def __str__(self):
        lines = [self.street]
        if self.street2:
            lines.append(self.street2)
        lines.append(f'{self.city}, {self.state} zip_code: {self.zipcode}')
        return '\n'.join(lines)

class Category:
    def __init__(self,category) -> None:
        self.category = category

    def __str__(self) -> str:
        return f"{self.category}"
class Contact:
    def __init__(self,telnumber='') -> None:
        self.telnumber = telnumber
    @property
    def telnumber(self):
        return self._telnumber
    @telnumber.setter
    def telnumber(self,value):
        if (len(value) != 11):
            # while True:
            print("the phone number can not be less than 11 number")
                # a = input("Do you want save this anymore ? ")
                # if a =="yes":
            self._telnumber= ""
                    
        # except ValueError as ve:
        #     print(ve)
        else:
            print("the contact successfully added .")
            self._telnumber = value  

    @property
    def email(self):
        return self._email
    @email.setter
    def email(self,value):
        import re
        regex = "^[a-zA-Z0-9-_.]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
        if (re.match(regex, value)):
            print("the Email successfully added .")
            self._email = value
        else:
            print("this email is not valid ")  
    def __str__(self) -> str:
        return f"{self.telnumber}\nEmail: {self.email}"
    
class Person:
    def __init__(self, id, fname,lname,category,contact):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.address = None
        self.contact = Contact(contact)
        self.category = Category(category)
        
    def __str__(self) -> str:
        return f"{self.id+1} : name : {self.fname} {self.lname}\naddress: {self.address}\ncategory : {self.category}\ncontact details : {self.contact}"


class Phone_book:
    records = []

    def add(self):
        id = len(Phone_book.records)
        fname = input("pleade enter first name :")
        lname = input("pleade enter last name :")
        print("Categori :\n1) Family\n2)coworker\n3) Friends")
        cat = input("select category :")
        if cat == "1":
            category = "Family"
        elif cat == "2":
            category = "coworker"
        elif cat == "3":
            category = "Friends"
        contact = input("pleade enter contact number :")
        obj = Person(id, fname,lname,category,contact)
        answer = input("Do want add address to this contact ? yes / any key to dismiss\n")
        if answer == 'yes':
            city = input("please enter city :")
            street = input("please enter street :")
            state = input("please enter state :")
            zipcode = input("please enter zipcode :")
            obj.address=Address(street, city, state, zipcode)
        else:
            obj.address=Address("", "", "", "")
        answer = input("Do want add Email address to this contact ? yes / any key to dismiss\n")
        if answer == 'yes':
            email = input("please enter Email :")
            obj.contact.email = email 
        else:
            obj.contact.email = "example@email.com"
        self.records.append(obj)

    def update_contact(self,name):
        for r in self.records:
            if name ==r.fname:
                index = r.id
                print(self.records[index-1])
                print("1) first name")
                print("2) last name")
                print("3) phone number")
                print("4) Email address")
                print("5) city")
                print("6) street")
                print("7) state")
                print("8) Zip_Code")
                print("return to contact) press 0 to exit")
                a = input("which field do you want to edit ?\n")
                while a!= "0":
                    if a == "1":
                        new_fname = input("please rename : \n")
                        if new_fname != "":
                            (self.records[index-1]).fname = new_fname
                        else: 
                            (self.records[index-1]).fname = (self.records[index-1]).fname
                        break
                    elif a=="2":
                        new_lname = input("please rename : \n")
                        if new_lname != "":
                            (self.records[index-1]).lname = new_lname
                        else: 
                            (self.records[index-1]).lname = (self.records[index-1]).lname
                        break
                    elif a=="3":
                        new_phone = input("enter new phone number : \n")
                        if new_phone != "":
                            (self.records[index-1]).contact = new_phone
                        else: 
                            (self.records[index-1]).contact = (self.records[index-1]).contact
                        break
                    elif a=="4":
                        new_Email = input("enter new Email address : \n")
                        if new_Email != "":
                            (self.records[index-1]).email = new_Email
                        else: 
                            (self.records[index-1]).email = (self.records[index-1]).email
                        break
                    elif a=="5":
                        new_city = input("enter new City : \n")
                        if new_city != "":
                            (self.records[index-1]).city = new_city
                        else: 
                            (self.records[index-1]).city = (self.records[index-1]).city
                        break
                    elif a=="8":
                        new_ZipCode = input("enter new Zip-code : \n")
                        if new_ZipCode != "":
                            (self.records[index-1]).zipcode = new_ZipCode
                        else: 
                            (self.records[index-1]).zipcode = (self.records[index-1]).zipcode
                        break
            else:
                print("can find any contact related your name ")
            
    def show(self):
        if len(self.records)== 0:
            print("no contact")
        else:
            for r in self.records:
                print(r)
                print("-"*40)
    def remove(self,name):
        for r in self.records:
            if name ==r.fname:
                index = r.id
                del self.records[index-1]