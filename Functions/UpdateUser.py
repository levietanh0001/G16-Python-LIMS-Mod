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


def updateUser():
    global root, con, cur, cv
    global userID, userName, DOB, phoneNum, emailAddr

    root = Tk()
    root.title("Update User")
    root.minsize(width=100, height=500)
    root.geometry("500x309")

    # name of book table
    book_table = "books"

    # create canva
    cv = Canvas(root)
    cv.config(bg="black")
    cv.pack(expand=True, fill=BOTH)

    lb1 = Label(root, text="User ID : ", bg='black', fg='white')
    lb1.place(relx=0.01, rely=0.1, relheight=0.08)

    userID = Entry(root)
    userID.place(relx=0.3, rely=0.1, relwidth=0.62, relheight=0.08)

    lb2 = Label(root, text="User Name : ", bg='black', fg='white')
    lb2.place(relx=0.01, rely=0.25, relheight=0.08)

    userName = Entry(root)
    userName.place(relx=0.3, rely=0.25, relwidth=0.62, relheight=0.08)

    lb3 = Label(root, text="Date of Birth : ", bg='black', fg='white')
    lb3.place(relx=0.01, rely=0.40, relheight=0.08)

    DOB = Entry(root)
    DOB.place(relx=0.3, rely=0.40, relwidth=0.62, relheight=0.08)

    lb4 = Label(root, text="Phone Number : ", bg='black', fg='white')
    lb4.place(relx=0.01, rely=0.55, relheight=0.08)

    phoneNum = Entry(root)
    phoneNum.place(relx=0.3, rely=0.55, relwidth=0.62, relheight=0.08)

    lb4 = Label(root, text="Email: ", bg='black', fg='white')
    lb4.place(relx=0.01, rely=0.70, relheight=0.08)

    emailAddr = Entry(root)
    emailAddr.place(relx=0.3, rely=0.70, relwidth=0.62, relheight=0.08)

    submit_button = Button(root, text="SUBMIT", bg='#d1ccc0', fg='black', command=updU)
    submit_button.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quit_button = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quit_button.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    # initialize GUI
    root.mainloop()