from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, filedialog
import mysql.connector
from PIL import ImageTk, Image
import pymysql
from Database.ConnectToMySQL import *

def view_borrowers_by_book_name():

    root = Tk()
    root.title("Scrollable Tree View")
    root.resizable(False, False)
    root.geometry("700x400")

    wrapper1 = Frame(root)
    # wrapper2 = LabelFrame(root, text="")
    # wrapper3 = LabelFrame(root, text="Book Details")

    wrapper1.pack(fill="both", expand="yes", padx=20, pady=10)
    # wrapper2.pack(fill="both", expand="yes", padx=20, pady=10)
    # wrapper3.pack(fill="both", expand="yes", padx=20, pady=10)

    trv = ttk.Treeview(wrapper1, columns=(1,2,3,4,5,6))
    style = ttk.Style(trv)
    style.configure('Treeview', rowheight=30)

    trv.pack(side=LEFT)
    trv.place(x=0, y=0)
    trv.heading('#0', text='')
    trv.heading('#1', text='User ID')
    trv.heading('#2', text='User Name')
    trv.heading('#3', text='Date of Birth')
    trv.heading('#4', text='Book ID')
    trv.heading('#5', text='Book Title')
    trv.heading('#6', text='Copies Borrowed')
    trv.column('#0', width=50, minwidth=100)
    trv.column('#1', width=100, minwidth=200)
    trv.column('#2', width=100, minwidth=200)
    trv.column('#3', width=100, minwidth=200)
    trv.column('#4', width=100, minwidth=200)
    trv.column('#5', width=100, minwidth=200)
    trv.column('#6', width=100, minwidth=200)

        # vertical scroll bar
    yscrollbar = ttk.Scrollbar(wrapper1, orient="vertical", command=trv.yview)
    yscrollbar.pack(side=RIGHT, fill=Y)

        # horizontal scroll bar
    xscrollbar = ttk.Scrollbar(wrapper1, orient="horizontal", command=trv.xview)
    xscrollbar.pack(side=BOTTOM, fill=X)

    trv.configure(yscrollcommand=yscrollbar.set, xscrollcommand=xscrollbar)

    con = pymysql.connect(host=db_obj.get_host(), user=db_obj.get_user(),
                          password=db_obj.get_pass(), database=db_obj.get_db(),
                          port=db_obj.get_port())
    cur = con.cursor()

    # error message if unable to view borrowers
    book_name = bookName.get()
    cur.callproc('ShowBorrowersByBookName', [book_name])
    # con.commit()
    rows = cur.fetchall()

    trv.delete(*trv.get_children())
    for i in rows:
        trv.insert('', 'end', values=i, tags='unchecked')

    root.mainloop()

def viewBorrowersByBookName():
    global bookID, bookTitle, bookAuthor, bookStatus, cv, con, cur, book_table, root, bookName

    root = Tk()
    root.title("View Borrowers By Book Name")
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

    lb2 = Label(root, text="Book Title ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.4)

    bookName = Entry(root)
    bookName.place(relx=0.2, rely=0.4, relwidth=0.7, relheight=0.1)

    submit_button = Button(root, text="SUBMIT", bg='#d1ccc0', fg='black', command=view_borrowers_by_book_name)
    submit_button.place(relx=0.2, rely=0.85, relwidth=0.25, relheight=0.12)

    quit_button = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quit_button.place(relx=0.53, rely=0.85, relwidth=0.25, relheight=0.12)

    root.mainloop()