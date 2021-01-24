import mysql.connector as m1
import time
import os,sys

######
######
PASSWORD = 'toor' # Enter the correct MySQL Password
######
######

def Display():
    '''
    Display data
        ARGUMENT : NONE
        RETURNS  : NONE
    '''
    global PASSWORD
    try:
        wire=m1.connect(host="localhost",
			user="root",
			password=PASSWORD,
			database="BOOKSTORE")
        if wire.is_connected():
            driver = wire.cursor()
            driver.execute("select Book_No , Book_Name , Available_Stock from stock")
            data = driver.fetchall()
            if not(data):
                print("\n\t!!! no record found !!!")
            else:
                print("\n\n\n")
                print("\t"+"{:<15}{:<50}{:<13}".format('Book Number  ','Book Name  ','No. of Stocks'))
                print()
                for row in data:
                    print("\t"+"{:<15}{:<50}{:<13}".format(row[0],row[1],row[2]))
                print("\n\n\n")
        else:
            print("\n\t!!!!! Connection error !!!!!")

    except Exception as e:
        print("\n\t!!!!! Erorr found !!!!!")
        print("\t",e)
        time.sleep(5)

#######################
#                     #
#   DISPLAY OPTION    #
#                     #
#######################


def SALES_OPTIONS():
    print("\n\t\t[1] Sell a Book")
    print("\t\t[2] View sales")
    print("\t\t[0] Back\n")
    choice1 = int(input(": : > "))
    if choice1 == 1:
        sell_book()
    elif choice1 == 2:
        view_sales()
    else:
        main()
def STOCK_OPTIONS():
    print("\n\t\t[1] View All Stock")
    print("\t\t[2] Add New Stock")
    print("\t\t[3] Update Stock")
    print("\t\t[0] Back\n")
    choice1 = int(input(": : > "))
    if choice1 == 1:
        view_all_stock()
    elif choice1 == 2:
        add_stock()
    elif choice1 == 3:
        update_stock()
    else:
        main()

def SETTING_OPTIONS():
    print("\n\t[1] Add Database")
    print("\t[2] Delete Database")
    print("\t[0] Back\n")
    choice1 = int(input(": : > "))
    if choice1 == 1:
        Add_database()
    elif choice1 == 2:
        Delete_Database()
    else:
        main()
        
        
#######################
#                     #
# BOOKS STOCK OPTIONS #
#                     #
#######################


def view_all_stock():
    '''
    Shows all the books in the Store
        ARGUMENT : NONE
	RETURNS  : NONE
    '''
    global PASSWORD
    try:
        wire=m1.connect(host="localhost",
			user="root",
			password=PASSWORD,
			database="BOOKSTORE")
        if wire.is_connected():
            driver = wire.cursor()
            driver.execute("select Book_No , Book_Name , Available_Stock from stock")
            data = driver.fetchall()
            if not(data):
                print("\n\t!!! no record found !!!")
            else:
                print("\n\n\n")
                print("\t"+"{:<15}{:<50}{:<13}".format('Book Number  ','Book Name  ','No. of Stocks'))
                print()
                for row in data:
                    print("\t"+"{:<15}{:<50}{:<13}".format(row[0],row[1],row[2]))
                print("\n\n\n")
        else:
            print("\n\t!!!!! Connection error !!!!!")

    except Exception as e:
        print("\n\t!!!!! Erorr found !!!!!")
        print("\t",e)
        time.sleep(5)

    STOCK_OPTIONS()

def add_stock():
    '''
    Add a single row of data from the user's input
        ARGUMENT : NONE
        RETURNS  : NONE
    '''
    global PASSWORD
    wire=m1.connect(host="localhost",
		    user="root",
		    password=PASSWORD,
                    database="BOOKSTORE")
    try:
        if wire.is_connected():
            driver = wire.cursor()
            wire.autocommit = True
            bno =        input("Book Number                     : ")
            bname =      input("Enter Book name                 : ")
            auth = 		 input("Enter the Author of the Book    : ")
            publ = 		 input("Enter the Publisher of the Book : ")
            cost = 	eval(input("Enter the Cost per Book         : "))
            salesp= eval(input("Enter the selling price of Book : "))
            stock =  int(input("Enter the Quantity purchased    : "))
            driver.execute("insert into stock values ({} , '{}' , '{}' , '{}' , {} , {} , {} , {} )".format(bno , bname , auth , publ , cost , salesp ,  stock , 0))
            print("\n\tInserted Sucessfully !!!")
            wire.close()
            driver.close()
        else:
            print("\n\t!!!!! Connection error !!!!!")
    except Exception as e:
        print("\n\t!!!!! Erorr found !!!!!")
        print("\t",e)
        time.sleep(5)

    STOCK_OPTIONS()

def update_stock():
    '''
    Updates the available stock with respect to the Book no. given
        ARGUMENT : NONE
        RETURNS  : NONE
    '''
    global PASSWORD
    wire=m1.connect(host="localhost",
                    user="root",
                    password=PASSWORD,
                    database="BOOKSTORE")
    try:
        if wire.is_connected():
            driver = wire.cursor()
            wire.autocommit = True
            bno = int(input("\n\nEnter the Book number: "))
            driver.execute("select Book_Name ,Available_Stock from stock where Book_No = {}".format(bno))
            data = driver.fetchall()
            print("\tBook Name       :",data[0][0])
            print("\tAvailable Stock :",data[0][1])
            stock = int(input("\n\tEnter the new stock purchased : "))
            driver.execute("update stock set Available_Stock = Available_Stock + {} where Book_No = {}".format(stock,bno))
            print("\n\tInserted Sucessfully !!!")
        else:
            print("\n\t!!!!! Connection error !!!!!")
            
    except Exception as e:
        print("\n\t!!!!! Erorr found !!!!!")
        print("\t",e)
        time.sleep(5)
    STOCK_OPTIONS()

    
#######################
#                     #
#   SALES OPTIONS     #
#                     #
#######################


def sell_book():
    '''
    Requests customer details and records the sales
        ARGUMENT : NONE
        RETURNS  : NONE
    '''
    global PASSWORD
    wire=m1.connect(host="localhost",
                    user="root",
                    password=PASSWORD,
                    database="BOOKSTORE")
    try:
        if wire.is_connected():
            driver=wire.cursor()
            wire.autocommit = True
            os.system('cls')
            print()
            print()
            Display()
            print()
            print()
            cname=    input("Enter Customer Name    : ")
            phno= int(input("Enter the Phone Number : "))
            bno=  int(input("Enter the Book no      : "))
            driver.execute("select Book_Name,Selling_price_rate from stock where Book_no = {}".format(bno))
            data = driver.fetchall()
            print("Book Name              :",data[0][0])
            print("Book Cost              :",data[0][1])
            driver.execute("insert into purchased values({} , '{}')".format(bno , data[0][0]))
            driver.execute("update stock set qty_purchased = qty_purchased + 1 where Book_No = {}".format(bno))
            driver.execute("update stock set Available_Stock = Available_Stock - 1 where Book_No = {}".format(bno))
            print("\n\tData Recorded Sucessfully !!!")
        else:
            print("\n\t!!!!! Connection error !!!!!")
    except Exception as e:
        print("\n\t!!!!! Erorr found !!!!!")
        print("\t",e)
        time.sleep(5)
    SALES_OPTIONS()

def view_sales():
    '''
    Show sales data
        ARGUMENT : NONE
        RETURNS  : NONE
    '''
    global PASSWORD
    wire=m1.connect(host="localhost",
                    user="root",
                    password=PASSWORD,
                    database="BOOKSTORE")
    try:
        if wire.is_connected():
            driver = wire.cursor()
            driver.execute("select distinct p.Book_Name , s.qty_purchased from stock s , purchased p where s.Book_No = p.Book_No ")
            data = driver.fetchall()
            print()
            print()
            print("\t"+"{:<50}{:<13}".format('Book Name','Sales'))
            for row in data:
                print("\t"+"{:<50}{:<13}".format(row[0],row[1]))
        else:
            print("\n\t!!!!! Connection error !!!!!")
    except Exception as e:
        print("\n\t!!!!! Erorr found !!!!!")
        print("\t",e)
        time.sleep(5)
    SALES_OPTIONS()
    
        
#######################
#                     #
#   SignUp & Login    #
#                     #
#######################

        
def login():
    '''
    Checks weather the user and password exist in the database
        ARGUMENT : NONE
        RETURNS  : BOOLEAN {True if data exist and vice verse}
    '''
    global PASSWORD
    wire=m1.connect(host = 'localhost' ,
    				user = 'root' ,
    				passwd = PASSWORD , 
    				database = 'BOOKSTORE')
    driver = wire.cursor()
    user = input("Enter the username : ")
    pwd =  input("Enter the password : ")
    driver.execute("Select * from users where username = '{}' and password = '{}'".format(user,pwd))
    data = driver.fetchall()
    if data:
    	return True
    else:
    	print("\n\t !+!+!+! ENTERED Username/Password is INCORRECT !+!+!+!")
    	time.sleep(2)
    	main()
def Add_user():
    '''
    Add new user for the BOOKSTORE software
	ARGUMENT : NONE
	RETURNS  : NONE
    '''
    global PASSWORD
    wire=m1.connect(host = 'localhost' ,
	 	    user = 'root' ,
	 	    passwd = PASSWORD ,
	   	    database = 'BOOKSTORE')
    try:
        if wire.is_connected():
            driver = wire.cursor()
            wire.autocommit = True
            user = 		input("\tNew Username     : ")
            passwd = 	input("\tEnter a Password : ")
            passwd2 = 	input("\tConfrim Password : ")
            if passwd == passwd2 :
                driver.execute("insert into users values('{}' , '{}')".format(user , passwd))
                print("\n\t!!! Created Successfully !!!")
                time.sleep(3)
            elif passwd != passwd2 :
                print("You've entered different passwords")
                wire.close()
                driver.close()
                time.sleep(3)
        else:
            print("\n\t!!!!! Connection error !!!!!")
            time.sleep(5)
    except Exception as e:
        print("\n\t!!!!! Erorr found !!!!!")
        print("\t",e)
        time.sleep(5)

    main()


def Remove_user():
    '''
    Remove users for the BOOKSTORE software
    ARGUMENT : NONE
    RETURNs  : NONE
    '''
    global PASSWORD
    print("!!! FOLLOWING ACTION MAY DELETE SOME DATA IN DATABASE 'BOOKSTORE' !!!")
    ans = input("Do you really want procced (y/n): ")
    if ans in 'yY':
        print("mySQL Username : root")
        pswd = input("mySQL Password : ")
        if pswd == PASSWORD:
            try:
                username = input("\n\tEnter Username of user to be Deleted: ")
                wire=m1.connect(host="localhost",
				user="root",
				password=pswd,
				database="BOOKSTORE")
                if wire.is_connected():
                    wire.autocommit = True
                    driver = wire.cursor()
                    driver.execute("DELETE FROM users WHERE username = '{}'".format(username))
                    print("\n\t+ ! + User Deleted + ! +")
                    time.sleep(3)
                    driver.close()
                    wire.close()
                else:
                    print("\n\t!!!!! Connection error !!!!!")
                    time.sleep(5)
            except Exception as e:
                print("\n\t!!!!! Erorr found !!!!!")
                print("\t",e)
                time.sleep(5)
        else:
            print("\n\t!!!! WRONG PASSWORD !!!!\n\n")
            time.sleep(3)
            
    main()

#######################
#                     #
#      SETTINGS       #
#                     #
#######################


def Add_database():
    '''
    Adds new database to mysql server
	ARGUMENT: NONE
	RETURNS : NONE
    '''
    global PASSWORD
    wire = m1.connect(host="localhost",user="root",password=PASSWORD)
    try:
        if wire.is_connected():
            wire.autocommit = True
            driver = wire.cursor()
            driver.execute("create database BOOKSTORE")
            driver.execute("use BOOKSTORE")
            driver.execute("create table stock\
                            (Book_no bigint primary key,\
                             Book_Name varchar(255),\
                            Author varchar(255),\
                            Publisher varchar(255),\
                            Cost_per_book float,\
                            Selling_price_rate float,\
                            Available_stock bigint,\
                            qty_purchased bigint)")

            driver.execute("create table users\
                            (username varchar(255) ,\
                     password varchar(255) ,\
              check (username <> 'ADMIN'))")

            driver.execute("create table purchased \
                            (Book_no bigint ,\
                            Book_Name varchar(255) ,\
                             foreign key(Book_no) references stock(Book_No))")

            driver.execute("insert into users values ('user1','a')")
            print("\n\t+ Database and Tables Created Successfully +")
            driver.close()
            wire.close()
        else:
            print("\n\t!!!!! Connection error !!!!!")
    except Exception as e:
        print("\n\t!!!!! Erorr found !!!!!")
        print("\t",e)
        time.sleep(5)

    SETTING_OPTIONS()


def Add_Inbuilt_data(filename):
	'''
	Add data to mySQL from external csv file

	    ARGUMENT : filename { filename of csv file}
            RETURNS  : NONE
	'''
	pass


def Delete_Database():
    '''
    To delete all the database
	ARGUMENT : NONE
	RETURNS  : NONE
    '''
    global PASSWORD
    print("!!! FOLLOWING ACTION MAY DELETE THE DATEBASE 'BOOKSTORE' !!!")
    ans = input("Do you really want delete database (y/n): ")
    if ans in 'yY':
        print("mySQL Username : root")
        pswd = input("mySQL Password : ")
        if pswd == PASSWORD:
            try:
                wire=m1.connect(host="localhost",user="root",password=pswd)
                if wire.is_connected():
                    wire.autocommit = True
                    driver = wire.cursor()
                    driver.execute("drop database BOOKSTORE")
                    print("\n\t+ ! + Database Deleted + ! +")
                    driver.close()
                    wire.close()
                    time.sleep(3)
                    SETTING_OPTIONS()
                else:
                    print("\n\t!!!!! Connection error !!!!!")


            except Exception as e:
                print("\n\t!!!!! Erorr found !!!!!")
                print("\t",e)
                time.sleep(5)
        else:
            print("\n\t!!!! WRONG PASSWORD !!!!\n\n")
            time.sleep(5)

    SETTING_OPTIONS()



#######################
#                     #
#       _main_        #
#                     #
#######################



def main():
    global PASSWORD
    os.system('cls')
    print('''
\t██████╗░░█████╗░░█████╗░██╗░░██╗  ░██████╗████████╗░█████╗░██████╗░███████╗
\t██╔══██╗██╔══██╗██╔══██╗██║░██╔╝  ██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██╔════╝
\t██████╦╝██║░░██║██║░░██║█████═╝░  ╚█████╗░░░░██║░░░██║░░██║██████╔╝█████╗░░
\t██╔══██╗██║░░██║██║░░██║██╔═██╗░  ░╚═══██╗░░░██║░░░██║░░██║██╔══██╗██╔══╝░░
\t██████╦╝╚█████╔╝╚█████╔╝██║░╚██╗  ██████╔╝░░░██║░░░╚█████╔╝██║░░██║███████╗
\t╚═════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝  ╚═════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚══════╝

\t███╗░░░███╗░█████╗░███╗░░██╗░█████╗░░██████╗░███████╗███╗░░░███╗███████╗███╗░░██╗████████╗
\t████╗░████║██╔══██╗████╗░██║██╔══██╗██╔════╝░██╔════╝████╗░████║██╔════╝████╗░██║╚══██╔══╝
\t██╔████╔██║███████║██╔██╗██║███████║██║░░██╗░█████╗░░██╔████╔██║█████╗░░██╔██╗██║░░░██║░░░
\t██║╚██╔╝██║██╔══██║██║╚████║██╔══██║██║░░╚██╗██╔══╝░░██║╚██╔╝██║██╔══╝░░██║╚████║░░░██║░░░
\t██║░╚═╝░██║██║░░██║██║░╚███║██║░░██║╚██████╔╝███████╗██║░╚═╝░██║███████╗██║░╚███║░░░██║░░░
\t╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝░╚═════╝░╚══════╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░''')
    print("\n\n\n")
    print("[1] Login")
    print("[2] Registration")
    print("[3] Settings")
    print("[0] Exit")
    choice = int(input(": : > "))
    if choice == 1:
        if login():
            print("\n\t[1] Stock options")
            print("\t[2] Sales options")
            print("\t[0] Back")
            choice1 = choice = int(input(": : >"))
            if choice1 == 1:
                STOCK_OPTIONS()
            elif choice1 == 2:
                SALES_OPTIONS()
            else:
                main()
    elif choice == 2:
        print("\n\t[1] Add new user")
        print("\t[2] Remove user")
        print("\t[0] Back")
        choice1 = choice = int(input(": : > "))
        if choice1 == 1:
            Add_user()
        elif choice1 == 2:
            Remove_user()
        else:
            main()

    elif choice == 3:
        SETTING_OPTIONS()
    else:
        sys.exit()

main()
