from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql
from Database.ConnectToMySQL import *


def addU():
    con = pymysql.connect(host=db_obj.get_host(), user=db_obj.get_user(),
                password=db_obj.get_pass(), database=db_obj.get_db(),
                port=db_obj.get_port())
    cur = con.cursor()

    user_id = userID.get()
    user_name = userName.get()
    dob = DOB.get()
    phone_number = phoneNum.get()
    email = emailAddr.get()

    # error message if unable to add book
    try:
        args = [user_id, user_name, dob, phone_number, email]
        cur.callproc('AddUser', args)
        con.commit()
        messagebox.showinfo('Success', "User added successfully")
    except:
        messagebox.showinfo("Error", "Can't add data into Database")

    root.destroy()


def addUser():
    global root, con, cur, cv
    global userID, userName, DOB, phoneNum, emailAddr
    root = Tk()
    root.title("Add User")
    root.minsize(width=100, height=500)
    root.geometry("500x309")

    # name of book table
    book_table = "books"

    # create canva
    cv = Canvas(root)
    cv.config(bg="black")
    cv.pack(expand=True, fill=BOTH)

    # book id
    lb1 = Label(root, text="User ID ", bg='black', fg='white')
    lb1.place(relx=0.01, rely=0.1, relheight=0.08)

    # book id query
    userID = Entry(root)
    userID.place(relx=0.3, rely=0.1, relwidth=0.62, relheight=0.08)

    # book title
    lb2 = Label(root, text="User Name ", bg='black', fg='white')
    lb2.place(relx=0.01, rely=0.25, relheight=0.08)

    # book title query
    userName = Entry(root)
    userName.place(relx=0.3, rely=0.25, relwidth=0.62, relheight=0.08)

    # user
    lb3 = Label(root, text="Date of Birth ", bg='black', fg='white')
    lb3.place(relx=0.01, rely=0.40, relheight=0.08)

    # user id query
    DOB = Entry(root)
    DOB.place(relx=0.3, rely=0.40, relwidth=0.62, relheight=0.08)

    # user name
    lb4 = Label(root, text="Phone Number ", bg='black', fg='white')
    lb4.place(relx=0.01, rely=0.55, relheight=0.08)

    # author name query
    phoneNum = Entry(root)
    phoneNum.place(relx=0.3, rely=0.55, relwidth=0.62, relheight=0.08)

    # available copies
    lb4 = Label(root, text="Email ", bg='black', fg='white')
    lb4.place(relx=0.01, rely=0.70, relheight=0.08)

    # available copies query
    emailAddr = Entry(root)
    emailAddr.place(relx=0.3, rely=0.70, relwidth=0.62, relheight=0.08)

    # submit button
    submit_button = Button(root, text="SUBMIT", bg='#d1ccc0', fg='black', command=addU)
    submit_button.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    # quit button
    quit_button = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quit_button.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    # initialize GUI
    root.mainloop()
