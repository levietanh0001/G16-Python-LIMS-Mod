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


def deleteUser():
    global root, con, cur, cv
    global userID

    root = Tk()
    root.title("Delete User")
    root.minsize(width=300, height=100)
    root.geometry("400x247")

    cv = Canvas(root)

    cv.config(bg="black")
    cv.pack(expand=True, fill=BOTH)

    # headingLabel = Label(root, text="Delete Book", bg='grey', fg='white', font=('Courier',15))
    # headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    #
    # labelFrame = Frame(root,bg='black')
    # labelFrame.place(relx=0.1,rely=0.3,relwidth=0.9,relheight=0.9)

    lb2 = Label(root, text="User ID ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.4)

    userID = Entry(root)
    userID.place(relx=0.2, rely=0.4, relwidth=0.7, relheight=0.1)

    submit_button = Button(root, text="SUBMIT", bg='#d1ccc0', fg='black', command=delU)
    submit_button.place(relx=0.2, rely=0.85, relwidth=0.25, relheight=0.12)

    quit_button = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quit_button.place(relx=0.53, rely=0.85, relwidth=0.25, relheight=0.12)

    root.mainloop()