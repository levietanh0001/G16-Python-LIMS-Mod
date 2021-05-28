from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
import cryptography
import mysql.connector as mysql
import cryptography
# import mysql-connector-python !

def insert():
    id = e_id.get()
    name = e_name.get()
    if(id=="" or name==""):
        messagebox.showinfo("Status", "Empty entry")
    else:
        con = mysql.connect(host="localhost", user="root", password="123321", database="pythonTkinter")
        cursor = con.cursor()
        cursor.execute("insert into student values ('" +id + "', '" +name + "')")
        cursor.execute("commit")

        messagebox.showinfo("Status", "Inserted")
        con.close()

root = Tk()
root.geometry("600x300")
root.title("My First App")
    # frame cont. others like labels, images...
# headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
# headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

    # texts, images...
id = Label(root, text='Enter ID:', font=('bold', 10))
id.place(x=0, y=0)

name = Label(root, text='Enter name:', font=('bold', 10))
name.place(x=0, y=20)

e_id = Entry()
e_id.place(x=150, y=0)

e_name = Entry()
e_name.place(x=150, y=20)

insert = Button(root, text="insert", font=('italic', 10), bg="white", command=insert)
insert.place(x=0, y=40)

root.mainloop()


