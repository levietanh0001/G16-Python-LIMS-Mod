from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from Database.ConnectToMySQL import *
import pymysql


def lendB():
    con = pymysql.connect(host=db_obj.get_host(), user=db_obj.get_user(),
                password=db_obj.get_pass(), database=db_obj.get_db(),
                port=db_obj.get_port())
    cur = con.cursor()

    book_id = bookID.get()
    copies = int(borrowNum.get())
    user_id = userID.get()
    b_date = borrowDate.get()
    dead_line = deadLine.get()

    try:
        args = [book_id, copies, user_id, b_date, dead_line]
        cur.callproc('LendBook', args)
        messagebox.showinfo("Error","Book %s is lent to %s" % (book_id, user_id))
        con.commit()
    except:
        messagebox.showinfo("Error","Can't fetch Book IDs")
    
def lendBook():
    
    global root, con, cur, cv
    global bookID, userID, borrowNum, borrowDate, deadLine

    root = Tk()
    root.title("Lend Book")
    root.minsize(width=100, height=500)
    root.geometry("500x309")

    # name of book table
    book_table = "books"

    # create canva
    cv = Canvas(root)
    cv.config(bg="black")
    cv.pack(expand=True, fill=BOTH)

    # book id
    lb1 = Label(root, text="Book ID ", bg='black', fg='white')
    lb1.place(relx=0.01, rely=0.1, relheight=0.08)

    # book id query
    bookID = Entry(root)
    bookID.place(relx=0.3, rely=0.1, relwidth=0.62, relheight=0.08)

    # book title
    lb2 = Label(root, text="User ID ", bg='black', fg='white')
    lb2.place(relx=0.01, rely=0.25, relheight=0.08)

    # book title query
    userID = Entry(root)
    userID.place(relx=0.3, rely=0.25, relwidth=0.62, relheight=0.08)

    # author
    lb3 = Label(root, text="Copies Borrowed ", bg='black', fg='white')
    lb3.place(relx=0.01, rely=0.40, relheight=0.08)

    # author id query
    borrowNum = Entry(root)
    borrowNum.place(relx=0.3, rely=0.40, relwidth=0.62, relheight=0.08)

    # author name
    lb4 = Label(root, text="Date ", bg='black', fg='white')
    lb4.place(relx=0.01, rely=0.55, relheight=0.08)

    # author name query
    borrowDate = Entry(root)
    borrowDate.place(relx=0.3, rely=0.55, relwidth=0.62, relheight=0.08)

    # available copies
    lb4 = Label(root, text="Set Deadline ", bg='black', fg='white')
    lb4.place(relx=0.01, rely=0.70, relheight=0.08)

    # available copies query
    deadLine = Entry(root)
    deadLine.place(relx=0.3, rely=0.70, relwidth=0.62, relheight=0.08)

    # submit button
    submit_button = Button(root, text="SUBMIT", bg='#d1ccc0', fg='black', command=lendB)
    submit_button.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    # quit button
    quit_button = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quit_button.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    # initialize GUI
    root.mainloop()