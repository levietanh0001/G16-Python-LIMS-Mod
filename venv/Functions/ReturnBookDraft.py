from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql
from Database.ConnectToMySQL import *

con = pymysql.connect(host=db_obj.get_host(), user=db_obj.get_user(),
                      password=db_obj.get_pass(), database=db_obj.get_db(),
                      port=db_obj.get_port())
cur = con.cursor()

# Enter Table Names here
issueTable = "books_issued"  # Issue Table
bookTable = "books"  # Book Table

allBid = []  # List To store all Book IDs


def retB():
    book_id = bookID.get()
    copies = int(borrowNum.get())
    user_id = userID.get()

    try:
        args = [book_id, user_id, copies]
        cur.callproc('ReturnBook', args)
        con.commit()
        messagebox.showinfo("Error", "Book ID not present")
    except:
        messagebox.showinfo("Error", "Can't fetch Book IDs")

    root.destroy()


def returnBook(frame_return_book):
    global root, con, cur, cv
    global bookID, userID, borrowNum

        # show frame_view_books
    frame_return_book.tkraise()
    frame_return_book.pack(fill=BOTH, expand="yes")

    # book id
    lb1 = Label(frame_return_book, text="Book ID ", bg='black', fg='white')
    lb1.place(relx=0.01, rely=0.1, relheight=0.08)

    # book id query
    bookID = Entry(frame_return_book)
    bookID.place(relx=0.3, rely=0.1, relwidth=0.62, relheight=0.08)

    # book title
    lb2 = Label(frame_return_book, text="User ID ", bg='black', fg='white')
    lb2.place(relx=0.01, rely=0.25, relheight=0.08)

    # book title query
    userID = Entry(frame_return_book)
    userID.place(relx=0.3, rely=0.25, relwidth=0.62, relheight=0.08)

    # author
    lb3 = Label(frame_return_book, text="Copies Borrowed ", bg='black', fg='white')
    lb3.place(relx=0.01, rely=0.40, relheight=0.08)

    # author id query
    borrowNum = Entry(frame_return_book)
    borrowNum.place(relx=0.3, rely=0.40, relwidth=0.62, relheight=0.08)

    # quit button
    submit_button = Button(frame_return_book, text="Submit", bg='black', fg='white', command=retB)
    submit_button.place(relx=0.3, rely=0.84, relwidth=0.2, relheight=0.08)

    # quit button
    quit_button = Button(frame_return_book, text="Back", bg='black', fg='white', command=frame_return_book.pack_forget)
    quit_button.place(relx=0.5, rely=0.84, relwidth=0.2, relheight=0.08)
