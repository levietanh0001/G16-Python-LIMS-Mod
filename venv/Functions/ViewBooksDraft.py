from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, filedialog
import mysql.connector
from PIL import ImageTk, Image
import pymysql
from Database.ConnectToMySQL import *
# from main_draft import *

def viewBooks(frame_view_books):

        # connect to database
    con = pymysql.connect(host=db_obj.get_host(), user=db_obj.get_user(),
                password=db_obj.get_pass(), database=db_obj.get_db(),
                port=db_obj.get_port())
    cur = con.cursor()
    query = "select book_id, book_title, author_id, available_copies from books"
    cur.execute(query)
    rows = cur.fetchall()
    num_of_rows = cur.rowcount
    if num_of_rows > 20:
        num_of_rows = 20

        # show frame_view_books
    frame_view_books.tkraise()
    frame_view_books.pack(fill=BOTH, expand="yes")

        # treeview table
    trv = ttk.Treeview(frame_view_books, columns=(1,2,3,4), height=num_of_rows)
    trv_style = ttk.Style(trv)
    trv_style.configure('Treeview', background="black",
                fieldbackground="black", foreground="white", bordercolor="black", borderwidth=0, rowheight=27)
    trv.pack(side=LEFT)
    trv.place(x=0, y=0)
    trv.heading('#0', text='')
    trv.heading('#1', text='Book ID')
    trv.heading('#2', text='Title')
    trv.heading('#3', text='Author')
    trv.heading('#4', text='Copies')
    trv.column('#0', minwidth=0, width=0)
    trv.column('#1', minwidth=100, width=250)
    trv.column('#2', minwidth=100, width=250)
    trv.column('#3', minwidth=100, width=250)
    trv.column('#4', minwidth=100, width=250)
    trv.delete(*trv.get_children())
    for i in rows:
        trv.insert('', 'end', values=i, tag="unchecked")

        # scroll bar - vertical
    # yscrollbar = ttk.Scrollbar(frame_view_books, orient="vertical", command=trv.yview)
    # yscrollbar.pack(side=RIGHT, fill=Y)

        # quit button
    quit_button = Button(frame_view_books,text="Back",bg='black', fg='white', command=frame_view_books.pack_forget)
    quit_button.place(relx=0.8,rely=0.92, relwidth=0.2, relheight=0.08)
    # root.mainloop()
