from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql
from Database.ConnectToMySQL import *

def updU():
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
        cur.callproc('UpdateUser', args)
        con.commit()
        messagebox.showinfo('Success', "User updated successfully")
    except:
        messagebox.showinfo("Error", "Can't add data into Database")

    root.destroy()


def updateUser(frame_update_user):
    global root, con, cur, cv
    global userID, userName, DOB, phoneNum, emailAddr

    frame_update_user.tkraise()
    frame_update_user.pack(fill=BOTH, expand="yes")

    lb1 = Label(frame_update_user, text="User ID ", bg='black', fg='white')
    lb1.place(relx=0.01, rely=0.1, relheight=0.08)

    userID = Entry(frame_update_user)
    userID.place(relx=0.3, rely=0.1, relwidth=0.62, relheight=0.08)

    lb2 = Label(frame_update_user, text="User Name ", bg='black', fg='white')
    lb2.place(relx=0.01, rely=0.25, relheight=0.08)

    userName = Entry(frame_update_user)
    userName.place(relx=0.3, rely=0.25, relwidth=0.62, relheight=0.08)

    lb3 = Label(frame_update_user, text="Date of Birth ", bg='black', fg='white')
    lb3.place(relx=0.01, rely=0.40, relheight=0.08)

    DOB = Entry(frame_update_user)
    DOB.place(relx=0.3, rely=0.40, relwidth=0.62, relheight=0.08)

    lb4 = Label(frame_update_user, text="Phone Number ", bg='black', fg='white')
    lb4.place(relx=0.01, rely=0.55, relheight=0.08)

    phoneNum = Entry(frame_update_user)
    phoneNum.place(relx=0.3, rely=0.55, relwidth=0.62, relheight=0.08)

    lb4 = Label(frame_update_user, text="Email: ", bg='black', fg='white')
    lb4.place(relx=0.01, rely=0.70, relheight=0.08)

    emailAddr = Entry(frame_update_user)
    emailAddr.place(relx=0.3, rely=0.70, relwidth=0.62, relheight=0.08)

        # quit button
    submit_button = Button(frame_update_user,text="Submit",bg='black', fg='white', command=updU)
    submit_button.place(relx=0.3,rely=0.84, relwidth=0.2, relheight=0.08)

        # quit button
    quit_button = Button(frame_update_user,text="Back",bg='black', fg='white', command=frame_update_user.pack_forget)
    quit_button.place(relx=0.5,rely=0.84, relwidth=0.2, relheight=0.08)
