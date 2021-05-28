from tkinter import *
from PIL import ImageTk, Image
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
        messagebox.showinfo("Error", "Book %s is lent to %s" % (book_id, user_id))
        con.commit()
    except:
        messagebox.showinfo("Error", "Can't fetch Book IDs")

def lendBook(frame_lend_book):
    global root, con, cur, cv
    global bookID, userID, borrowNum, borrowDate, deadLine

        # show frame_view_books
    frame_lend_book.tkraise()
    frame_lend_book.pack(fill=BOTH, expand="yes")

    # book id
    lb1 = Label(frame_lend_book, text="Book ID ", bg='black', fg='white')
    lb1.place(relx=0.01, rely=0.1, relheight=0.08)

    # book id query
    bookID = Entry(frame_lend_book)
    bookID.place(relx=0.3, rely=0.1, relwidth=0.62, relheight=0.08)

    # book title
    lb2 = Label(frame_lend_book, text="User ID ", bg='black', fg='white')
    lb2.place(relx=0.01, rely=0.25, relheight=0.08)

    # book title query
    userID = Entry(frame_lend_book)
    userID.place(relx=0.3, rely=0.25, relwidth=0.62, relheight=0.08)

    # author
    lb3 = Label(frame_lend_book, text="Copies Borrowed ", bg='black', fg='white')
    lb3.place(relx=0.01, rely=0.40, relheight=0.08)

    # author id query
    borrowNum = Entry(frame_lend_book)
    borrowNum.place(relx=0.3, rely=0.40, relwidth=0.62, relheight=0.08)

    # author name
    lb4 = Label(frame_lend_book, text="Date ", bg='black', fg='white')
    lb4.place(relx=0.01, rely=0.55, relheight=0.08)

    # author name query
    borrowDate = Entry(frame_lend_book)
    borrowDate.place(relx=0.3, rely=0.55, relwidth=0.62, relheight=0.08)

    # available copies
    lb4 = Label(frame_lend_book, text="Set Deadline ", bg='black', fg='white')
    lb4.place(relx=0.01, rely=0.70, relheight=0.08)

    # available copies query
    deadLine = Entry(frame_lend_book)
    deadLine.place(relx=0.3, rely=0.70, relwidth=0.62, relheight=0.08)

    # quit button
    submit_button = Button(frame_lend_book, text="Submit", bg='black', fg='white', command=lendB)
    submit_button.place(relx=0.3, rely=0.84, relwidth=0.2, relheight=0.08)

    # quit button
    quit_button = Button(frame_lend_book, text="Back", bg='black', fg='white', command=frame_lend_book.pack_forget)
    quit_button.place(relx=0.5, rely=0.84, relwidth=0.2, relheight=0.08)
