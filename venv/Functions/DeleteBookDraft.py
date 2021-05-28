from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from Database.ConnectToMySQL import *
import pymysql


def delB():
    con = pymysql.connect(host=db_obj.get_host(), user=db_obj.get_user(),
                          password=db_obj.get_pass(), database=db_obj.get_db(),
                          port=db_obj.get_port())
    cur = con.cursor()

    book_id = bookID.get()

    # deleteSql = "delete from "+bookTable+" where bid = '"+book_id+"'"
    # deleteIssue = "delete from "+issueTable+" where bid = '"+book_id+"'"

    # error message if unable to delete book
    try:
        args = [book_id]
        cur.callproc('DeleteBookByID', args)
        con.commit()
        messagebox.showinfo('Success', "Book Record Deleted Successfully")
    except:
        messagebox.showinfo("Failed to delete!")

    root.destroy()


def deleteBook(frame_remove_book):
    global bookID, bookTitle, bookAuthor, bookStatus, cv, con, cur, book_table, root
    frame_remove_book.tkraise()
    frame_remove_book.pack(fill=BOTH, expand="yes")

    lb2 = Label(frame_remove_book, text="Book ID ", bg='black', fg='white')
    lb2.place(relx=0.01, rely=0.42, relwidth=0.08, relheight=0.08)

    bookID = Entry(frame_remove_book)
    bookID.place(relx=0.1, rely=0.42, relwidth=0.8, relheight=0.08)

        # quit button
    submit_button = Button(frame_remove_book,text="Submit",bg='black', fg='white', command=delB)
    submit_button.place(relx=0.3,rely=0.84, relwidth=0.2, relheight=0.08)

        # quit button
    quit_button = Button(frame_remove_book,text="Back",bg='black', fg='white', command=frame_remove_book.pack_forget)
    quit_button.place(relx=0.5,rely=0.84, relwidth=0.2, relheight=0.08)

    # root.mainloop()