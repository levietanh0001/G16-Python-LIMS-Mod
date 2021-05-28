from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql
from Database.ConnectToMySQL import *


def submitBook():
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
        args = [author_id, author_name, book_id, title, copies]
        # get con cur tu class ConnectToDB
        cur.callproc('InsertAuthorsAndBooks', args)
        con.commit()
        messagebox.showinfo('Success', "Book added successfully")
    except:
        messagebox.showinfo("Error", "Can't add data into Database")

    root.destroy()


def addBook(frame_add_book):
    global bookID, bookTitle, authorName, authorID, avail, bookStatus, cv, con, cur, book_table, root
    frame_add_book.tkraise()
    frame_add_book.pack(fill=BOTH, expand="yes")

    # frame_add_book = Tk()
    # frame_add_book.title("Add Book")
    # root.minsize(width=100, height=500)
    # root.geometry("500x309")
    #
    # # name of book table
    # book_table = "books"
    # #
    # # # create canva
    # # cv = Canvas(root)
    # # cv.config(bg="black")
    # # cv.pack(expand=True, fill=BOTH)

    # book id
    lb1 = Label(frame_add_book, text="Book ID  ", bg='black', fg='white')
    lb1.place(relx=0.01, rely=0.1, relheight=0.08)

    # book id query
    bookID = Entry(frame_add_book)
    bookID.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.08)

    # book title
    lb2 = Label(frame_add_book, text="Title  ", bg='black', fg='white')
    lb2.place(relx=0.01, rely=0.25, relheight=0.08)

    # book title query
    bookTitle = Entry(frame_add_book)
    bookTitle.place(relx=0.1, rely=0.25, relwidth=0.8, relheight=0.08)

    # author
    lb3 = Label(frame_add_book, text="Author ID  ", bg='black', fg='white')
    lb3.place(relx=0.01, rely=0.40, relheight=0.08)

    # author id query
    authorID = Entry(frame_add_book)
    authorID.place(relx=0.1, rely=0.40, relwidth=0.8, relheight=0.08)

    # author name
    lb4 = Label(frame_add_book, text="Author Name  ", bg='black', fg='white')
    lb4.place(relx=0.01, rely=0.55, relheight=0.08)

    # author name query
    authorName = Entry(frame_add_book)
    authorName.place(relx=0.1, rely=0.55, relwidth=0.8, relheight=0.08)

    # available copies
    lb4 = Label(frame_add_book, text="Avail. Copies ", bg='black', fg='white')
    lb4.place(relx=0.01, rely=0.70, relheight=0.08)

    # available copies query
    avail = Entry(frame_add_book)
    avail.place(relx=0.1, rely=0.70, relwidth=0.8, relheight=0.08)

    #     # book status
    # lb4 = Label(frame_add_book,text="Status(Avail/issued)  ", bg='black', fg='white')
    # lb4.place(relx=0.01,rely=0.55, relheight=0.08)
    #
    #     # book status query
    # bookStatus = Entry(frame_add_book)
    # bookStatus.place(relx=0.3,rely=0.55, relwidth=0.62, relheight=0.08)

        # quit button
    submit_button = Button(frame_add_book,text="Submit",bg='black', fg='white', command=submitBook)
    submit_button.place(relx=0.4,rely=0.84, relwidth=0.2, relheight=0.08)

        # quit button
    quit_button = Button(frame_add_book,text="Back",bg='black', fg='white', command=frame_add_book.pack_forget)
    quit_button.place(relx=0.8,rely=0, relwidth=0.2, relheight=0.08)

    # initialize GUI
    # root.mainloop()