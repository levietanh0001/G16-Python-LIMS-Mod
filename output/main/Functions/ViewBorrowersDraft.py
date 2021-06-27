from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, filedialog
import mysql.connector
from PIL import ImageTk, Image
import pymysql
from Database.ConnectToMySQL import *

def viewBorrowers(frame_view_borrowers):
        # connect to database
    con = pymysql.connect(host=db_obj.get_host(), user=db_obj.get_user(),
                password=db_obj.get_pass(), database=db_obj.get_db(),
                port=db_obj.get_port())
    cur = con.cursor()
    cur.callproc('ShowAllBorrowers')
    rows = cur.fetchall()
    num_of_rows = cur.rowcount
    if num_of_rows > 20:
        num_of_rows = 20

        # show frame_view_books
    frame_view_borrowers.tkraise()
    frame_view_borrowers.pack(fill=BOTH, expand="yes")

        # treeview table
    trv = ttk.Treeview(frame_view_borrowers, columns=(1,2,3,4,5,6), height=num_of_rows)
    trv_style = ttk.Style(trv)
    trv_style.configure('Treeview', background="black",
                fieldbackground="black", foreground="white", bordercolor="black", borderwidth=0, rowheight=27)
    trv.pack(side=LEFT)
    trv.place(x=0, y=0)
    trv.heading('#0', text='')
    trv.heading('#1', text='User ID')
    trv.heading('#2', text='User Name')
    trv.heading('#3', text='Date of Birth')
    trv.heading('#4', text='Book ID')
    trv.heading('#5', text='Book Title')
    trv.heading('#6', text='Copies Borrowed')
    trv.column('#0', width=0, minwidth=0)
    trv.column('#1', width=166, minwidth=166)
    trv.column('#2', width=166, minwidth=166)
    trv.column('#3', width=166, minwidth=166)
    trv.column('#4', width=166, minwidth=166)
    trv.column('#5', width=166, minwidth=166)
    trv.column('#6', width=166, minwidth=166)
    trv.delete(*trv.get_children())
    for i in rows:
        trv.insert('', 'end', values=i, tags='unchecked')

        # quit button
    quit_button = Button(frame_view_borrowers,text="Back",bg='black', fg='white', command=frame_view_borrowers.pack_forget)
    quit_button.place(relx=0.8,rely=0.92, relwidth=0.2, relheight=0.08)

