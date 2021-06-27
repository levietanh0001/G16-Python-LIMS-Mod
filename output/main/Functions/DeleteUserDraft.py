from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from Database.ConnectToMySQL import *
import pymysql

def delU():

    con = pymysql.connect(host=db_obj.get_host(), user=db_obj.get_user(),
                password=db_obj.get_pass(), database=db_obj.get_db(),
                port=db_obj.get_port())
    cur = con.cursor()

    user_id = userID.get()

    # error message if unable to delete book
    try:
        args = [user_id]
        cur.callproc('DeleteBookByID', args)
        con.commit()
        messagebox.showinfo('Success', "User Record Deleted Successfully")
    except:
        messagebox.showinfo("Failed to delete!")

    root.destroy()


def deleteUser(frame_delete_user):
    global root, con, cur, cv
    global userID

    frame_delete_user.tkraise()
    frame_delete_user.pack(fill=BOTH, expand="yes")

    lb2 = Label(frame_delete_user, text="User ID ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.4)

    userID = Entry(frame_delete_user)
    userID.place(relx=0.2, rely=0.4, relwidth=0.7, relheight=0.1)

        # quit button
    submit_button = Button(frame_delete_user,text="Submit",bg='black', fg='white', command=delU)
    submit_button.place(relx=0.3,rely=0.84, relwidth=0.2, relheight=0.08)

        # quit button
    quit_button = Button(frame_delete_user,text="Back",bg='black', fg='white', command=frame_delete_user.pack_forget)
    quit_button.place(relx=0.5,rely=0.84, relwidth=0.2, relheight=0.08)

