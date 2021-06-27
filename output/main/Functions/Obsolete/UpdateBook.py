from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql
from Database.ConnectToMySQL import *


def updB():
    con = pymysql.connect(host=db_obj.get_host(), user=db_obj.get_user(),
                password=db_obj.get_pass(), database=db_obj.get_db(),
                port=db_obj.get_port())
    cur = con.cursor()

    author_id = authorID.get()
    author_name = authorName.get()
    book_id = bookID.get()
    title = bookTitle.get()
    copies = int(avail.get())

    # error message if unable to add book
    try:
        args = [book_id, title, copies, author_id]
        cur.callproc('UpdateBook', args)
        con.commit()
        messagebox.showinfo('Success', "Book updated successfully")
    except:
        messagebox.showinfo("Error", "Can't add data into Database")

    root.destroy()


def updateBook():
    global bookID, bookTitle, authorName, authorID, avail, bookStatus, cv, con, cur, book_table, root

    root = Tk()
    root.title("Update Book")
    root.minsize(width=100, height=500)
    root.geometry("500x309")

    # name of book table
    book_table = "books"

    # create canva
    cv = Canvas(root)
    cv.config(bg="black")
    cv.pack(expand=True, fill=BOTH)

    # book id
    lb1 = Label(root, text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.01, rely=0.1, relheight=0.08)

    # book id query
    bookID = Entry(root)
    bookID.place(relx=0.3, rely=0.1, relwidth=0.62, relheight=0.08)

    # book title
    lb2 = Label(root, text="Title : ", bg='black', fg='white')
    lb2.place(relx=0.01, rely=0.25, relheight=0.08)

    # book title query
    bookTitle = Entry(root)
    bookTitle.place(relx=0.3, rely=0.25, relwidth=0.62, relheight=0.08)

    # author
    lb3 = Label(root, text="Author ID : ", bg='black', fg='white')
    lb3.place(relx=0.01, rely=0.40, relheight=0.08)

    # author id query
    authorID = Entry(root)
    authorID.place(relx=0.3, rely=0.40, relwidth=0.62, relheight=0.08)

    # author name
    lb4 = Label(root, text="Author Name : ", bg='black', fg='white')
    lb4.place(relx=0.01, rely=0.55, relheight=0.08)

    # author name query
    authorName = Entry(root)
    authorName.place(relx=0.3, rely=0.55, relwidth=0.62, relheight=0.08)

    # available copies
    lb4 = Label(root, text="Available Copies: ", bg='black', fg='white')
    lb4.place(relx=0.01, rely=0.70, relheight=0.08)

    # available copies query
    avail = Entry(root)
    avail.place(relx=0.3, rely=0.70, relwidth=0.62, relheight=0.08)

    #     # book status
    # lb4 = Label(root,text="Status(Avail/issued) : ", bg='black', fg='white')
    # lb4.place(relx=0.01,rely=0.55, relheight=0.08)
    #
    #     # book status query
    # bookStatus = Entry(root)
    # bookStatus.place(relx=0.3,rely=0.55, relwidth=0.62, relheight=0.08)

    # submit button
    submit_button = Button(root, text="SUBMIT", bg='#d1ccc0', fg='black', command=updB)
    submit_button.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    # quit button
    quit_button = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quit_button.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    # initialize GUI
    root.mainloop()