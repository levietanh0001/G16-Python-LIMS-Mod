from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, filedialog
import mysql.connector
from PIL import ImageTk, Image
import pymysql

def viewBooks2(view_books_frame):

    root = Tk()
    root.title("Scrollable Tree View")
    root.resizable(False, False)
    root.geometry("700x400")
    q = StringVar()
    t1 = StringVar()
    t2 = StringVar()
    t3 = StringVar()
    t4 = StringVar()

    # wrapper1 = Frame(root)
    wrapper2 = LabelFrame(root, text="")
    # wrapper3 = LabelFrame(root, text="Book Details")

    view_books_frame.pack(fill="both", expand="yes")
    # wrapper2.pack(fill="both", expand="yes", padx=20, pady=10)
    # wrapper3.pack(fill="both", expand="yes", padx=20, pady=10)

    trv = ttk.Treeview(view_books_frame, columns=(1,2,3,4))
    style = ttk.Style(trv)
    style.configure('Treeview', rowheight=30)

    trv.pack(side=LEFT)
    trv.place(x=0, y=0)
    trv.heading('#0', text='')
    trv.heading('#1', text='Book ID')
    trv.heading('#2', text='Title')
    trv.heading('#3', text='Author')
    trv.heading('#4', text='Copies')
    trv.column('#0', width=50, minwidth=100)
    trv.column('#1', width=150, minwidth=200)
    trv.column('#2', width=150, minwidth=200)
    trv.column('#3', width=150, minwidth=200)
    trv.column('#4', width=150, minwidth=200)

        # vertical scroll bar
    yscrollbar = ttk.Scrollbar(view_books_frame, orient="vertical", command=trv.yview)
    yscrollbar.pack(side=RIGHT, fill=Y)

        # horizontal scroll bar
    xscrollbar = ttk.Scrollbar(view_books_frame, orient="horizontal", command=trv.xview)
    xscrollbar.pack(side=BOTTOM, fill=X)

    trv.configure(yscrollcommand=yscrollbar.set, xscrollcommand=xscrollbar)

        # database details
    my_pass = "123321"
    my_db = "g16_db"

        # connect to database
    con = pymysql.connect(host="localhost", user="root", password=my_pass, database=my_db, port=3306)
    cur = con.cursor()
    book_table = "books"

    query = "select book_id, book_title, author_id, available_copies from books"
    cur.execute(query)
    rows = cur.fetchall()

    trv.delete(*trv.get_children())
    for i in rows:
        trv.insert('', 'end', values=i, tags='unchecked')

    root.mainloop()
