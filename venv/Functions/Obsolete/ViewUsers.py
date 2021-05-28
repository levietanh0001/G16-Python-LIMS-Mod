from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, filedialog
import mysql.connector
from PIL import ImageTk, Image
import pymysql
from Database.ConnectToMySQL import *

def viewUsers():

    root = Tk()
    root.title("Scrollable Tree View")
    root.resizable(False, False)
    root.geometry("700x400")
    q = StringVar()
    t1 = StringVar()
    t2 = StringVar()
    t3 = StringVar()
    t4 = StringVar()

    wrapper1 = Frame(root)
    wrapper2 = LabelFrame(root, text="")
    # wrapper3 = LabelFrame(root, text="Book Details")

    wrapper1.pack(fill="both", expand="yes", padx=20, pady=10)
    # wrapper2.pack(fill="both", expand="yes", padx=20, pady=10)
    # wrapper3.pack(fill="both", expand="yes", padx=20, pady=10)

    trv = ttk.Treeview(wrapper1, columns=(1,2,3,4,5))
    style = ttk.Style(trv)
    style.configure('Treeview', rowheight=30)

    trv.pack(side=LEFT)
    trv.place(x=0, y=0)
    trv.heading('#0', text='')
    trv.heading('#1', text='User ID')
    trv.heading('#2', text='User Name')
    trv.heading('#3', text='Date of Birth')
    trv.heading('#4', text='Phone Number')
    trv.heading('#5', text='Email')
    trv.column('#0', width=50, minwidth=100)
    trv.column('#1', width=120, minwidth=200)
    trv.column('#2', width=120, minwidth=200)
    trv.column('#3', width=120, minwidth=200)
    trv.column('#4', width=120, minwidth=200)
    trv.column('#5', width=120, minwidth=200)

        # vertical scroll bar
    yscrollbar = ttk.Scrollbar(wrapper1, orient="vertical", command=trv.yview)
    yscrollbar.pack(side=RIGHT, fill=Y)

        # horizontal scroll bar
    xscrollbar = ttk.Scrollbar(wrapper1, orient="horizontal", command=trv.xview)
    xscrollbar.pack(side=BOTTOM, fill=X)

    trv.configure(yscrollcommand=yscrollbar.set, xscrollcommand=xscrollbar)

        # database details
    my_pass = "123321"
    my_db = "g16_db"

        # connect to database
    con = pymysql.connect(host=db_obj.get_host(), user=db_obj.get_user(),
                password=db_obj.get_pass(), database=db_obj.get_db(),
                port=db_obj.get_port())
    cur = con.cursor()
    book_table = "books"

    query = "select * from users"
    cur.execute(query)
    rows = cur.fetchall()

    trv.delete(*trv.get_children())
    for i in rows:
        trv.insert('', 'end', values=i, tags='unchecked')

    root.mainloop()
