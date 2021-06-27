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


def addUser(frame_add_user):
    global root, con, cur, cv
    global userID, userName, DOB, phoneNum, emailAddr

    frame_add_user.tkraise()
    frame_add_user.pack(fill=BOTH, expand="yes")

    # book id
    lb1 = Label(frame_add_user, text="User ID ", bg='black', fg='white')
    lb1.place(relx=0.01, rely=0.1, relheight=0.08)

    # book id query
    userID = Entry(frame_add_user)
    userID.place(relx=0.3, rely=0.1, relwidth=0.62, relheight=0.08)

    # book title
    lb2 = Label(frame_add_user, text="User Name ", bg='black', fg='white')
    lb2.place(relx=0.01, rely=0.25, relheight=0.08)

    # book title query
    userName = Entry(frame_add_user)
    userName.place(relx=0.3, rely=0.25, relwidth=0.62, relheight=0.08)

    # user
    lb3 = Label(frame_add_user, text="Date of Birth ", bg='black', fg='white')
    lb3.place(relx=0.01, rely=0.40, relheight=0.08)

    # user id query
    DOB = Entry(frame_add_user)
    DOB.place(relx=0.3, rely=0.40, relwidth=0.62, relheight=0.08)

    # user name
    lb4 = Label(frame_add_user, text="Phone Number ", bg='black', fg='white')
    lb4.place(relx=0.01, rely=0.55, relheight=0.08)

    # author name query
    phoneNum = Entry(frame_add_user)
    phoneNum.place(relx=0.3, rely=0.55, relwidth=0.62, relheight=0.08)

    # available copies
    lb4 = Label(frame_add_user, text="Email ", bg='black', fg='white')
    lb4.place(relx=0.01, rely=0.70, relheight=0.08)

    # available copies query
    emailAddr = Entry(frame_add_user)
    emailAddr.place(relx=0.3, rely=0.70, relwidth=0.62, relheight=0.08)

        # quit button
    submit_button = Button(frame_add_user,text="Submit",bg='black', fg='white', command=addU)
    submit_button.place(relx=0.3,rely=0.84, relwidth=0.2, relheight=0.08)

        # quit button
    quit_button = Button(frame_add_user,text="Back",bg='black', fg='white', command=frame_add_user.pack_forget)
    quit_button.place(relx=0.5,rely=0.84, relwidth=0.2, relheight=0.08)
