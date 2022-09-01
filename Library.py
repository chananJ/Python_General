# this is book department:
#chanan jacobs 316090877
class Book:
    def __init__(self,book_name, author):
        self.book_name=book_name
        self.author=author
# this like toString in java
    def __repr__(self):
        return f"book name is: {self.book_name}, author name is: {self.author}"
    def __eq__(self, other):
        if self.book_name == other.book_name:
            return True
        else:
            return False
# im gonna create a subscribre class
class Subscriber:
    def __init__(self,name=" ", last_name=" "):
        self.name=name
        self.last_name=last_name

    def __eq__(self, other):
        if self.name==other.name and self.last_name==other.last_name:
            return True
        else:
            return False
    # this like toString in java
    def __repr__(self):
        return f"subscriber name is: {self.name} , {self.last_name}"
# soon im gonna figure out what to do with the library:
class Library:
    def __init__(self):
        self.books_list=[]
        self.subscribers_list=[]
        self.taken= {}

    def add_book(self,name,author):
        temp_book =Book(name,author)
        for book in self.books_list:
            if book==temp_book:
                return "book exist"
        self.books_list.append(temp_book)
        return "succes!"
    def add_user(self,first_name,last_name):
        temp_sub = Subscriber(first_name, last_name)
        for sub in self.subscribers_list:
            if sub == temp_sub:
                return "subscriber allready exist!"
        self.subscribers_list.append(temp_sub)
        return "succes!"
    def user_exists(self,first_name,last_name):
        if first_name+last_name in self.subscribers_list:
            return first_name, last_name
        else:
            return ("subscriber dosent exist")
    def take_book(self,book_name,first_name,last_name):
        book_exsits=False
        user_exsits= False
        is_taken = False
        for book in self.books_list:
            if book_name== book.book_name:
                book_exsits =True
        for sub in self.subscribers_list:
            if sub.name==first_name and sub.last_name==last_name:
                user_exsits=True
        for user in self.taken:
            if book_name in self.taken[user]:
                is_taken=True
        if book_exsits:
            if user_exsits:
                if is_taken:
                    return "the book is allready taken"
                else:
                    if first_name+last_name in self.taken:
                        self.taken[first_name + last_name].append(book_name)
                    else:
                        self.taken[first_name+ last_name]=[book_name]
                    return "succes"
            else:
                return "user dosent exist"
        else:
            return "book dosent exsit"
l1= Library()
while num!=6:
    num = int(input("choose action:"))
    if num==1:
        my_book = input("please enter book name and author name")
        my_book = my_book.split(",")
        print(l1.add_book(my_book[0],my_book[1]))
    if num == 2:
        my_user = input("please enter first and last name")
        my_user = my_user.split(",")
        print(l1.add_user(my_user[0], my_user[1]))
    if num == 3:
        my_user = input("please enter first and last name")
        my_user = my_user.split(",")
        my_book = input("please enter book name and author name")
        my_book = my_book.split(",")
        print(l1.add_book(my_book[0],my_book[1]))
        print(l1.take_book(my_book[0],my_user[0], my_user[1]))
    if num == 4:
        #im in to much pressure of time so i didnt finish the whole thing! but i got the logic
    if num == 5:
        my_user = input("please enter first and last name")
        my_user = my_user.split(",")
        print(l1.user_exists(my_user[0], my_user[1]))
    if num == 6:
        print("goodbye!")



