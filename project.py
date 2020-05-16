from tkinter import*
root=Tk()
root.title("HANGMAN GAME")
listbox=Listbox(root,bg="black",fg="yellow",font="Elephant",bd=50,width=35)
listbox.insert(END,"")
listbox.insert(END,"                                        WELCOME")
listbox.insert(END,"")
listbox.insert(END,'                                                TO')
listbox.insert(END,"")
listbox.insert(END,'                                        HANGMAN')
'''img=ImageTk.PhotoImage(Image.open("3.png"))
panel=tk.Label(root,image=img)
panel.pack(side="bottom",fill="both",expand="yes")

PhotoImage(Image.open("3.png"))
listbox.insert(END,PhotoImage)'''

def g():
    root.destroy()
    import page1
b=Button(root,text="LET'S PLAY",bg="green",fg="black",command=g)
b1=Button(root,text=" EXIT ",bg="red",fg="yellow",command=quit)
listbox.pack()
Title=Label(root,text=" Developed By : Saicharan Vustepalli , Avinash Chinnala , Abinay Karnam")

b.pack(side="left",padx=10)
b1.pack(side='right',padx=10, pady=10)
#Title.grid(row=3, column=0)
Title.pack()

root.mainloop()
