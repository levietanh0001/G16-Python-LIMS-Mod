import tkinter as tk

root = tk.Tk()
root.state('zoomed')
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=2)
root.columnconfigure(1, weight=3)

def show_frame_2(frame):
    frame.tkraise()
    frame_1.pack_forget()
def show_frame_1(frame):
    frame.tkraise()
    frame_2.pack_forget()


frame_1 = tk.Frame(root, bg='blue')
# frame_1.grid(row=0, column=0, sticky='nsew')
frame_1.place(relx=0, rely=0, relwidth=1, relheight=1)
frame_1_label = tk.Label(frame_1, bg='red', text='This is label of frame number 1')
frame_1_label.pack()

frame_2 = tk.Frame(root, bg="gold")
# frame_2.grid(row=0, column=0, sticky='nsew')
frame_2.place(relx=0, rely=0, relwidth=1, relheight=1)
frame_2_label = tk.Label(frame_2, bg='green', text='This is label of frame number 2')
frame_2_label.pack()

frame_3 = tk.Frame(root)
frame_3.grid(row=0, column=0, sticky='nsew')
frame_3_label = tk.Label(frame_3, bg='yellow', text='This is frame number 3')
frame_3_label.pack()

frame_1_button = tk.Button(frame_1, text='Enter', command=lambda:show_frame_2(frame_2))
frame_1_button.pack()

frame_2_button = tk.Button(frame_2, text='Enter', command=lambda:show_frame_1(frame_1))
frame_2_button.pack()

show_frame_1(frame_1)

root.mainloop()
