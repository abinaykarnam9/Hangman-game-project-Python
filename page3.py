from tkinter import*
global root
root=Tk()
root.title("HANGMAN GAME")
root.geometry('400x400+400+400')
frame = Frame(root,padx = 20, pady=20)
E1 = Entry(frame, bd =5, width = 40)
L1 = Label(frame, text="Enter the word : ")
L1.pack( side = LEFT)

E1.pack(side = RIGHT)
frame.pack()
frame = Frame(root)
E2 = Entry(frame, bd =5, width=40)
L2 = Label(frame, text="Enter a hint : ")
L2.pack( side = LEFT)

E2.pack(side = RIGHT)
frame.pack()
#b1 = button()

#print E1.get()    

s = ""
def nex():
    global s
    s=E1.get()
    s =s.upper()
    f1=open("word.txt","w")
    #print s
    f1.write(s+'\n')
    s=E2.get()
    s=s.upper()
    f1.write(s)
    f1.close()
    root.destroy()
    import page4

'''
def pas():
    return s
'''
frame = Frame(root)
b=Button(frame,text="Submit",bg="green",fg="black",command=nex)
b.pack(side="bottom",padx=10)
frame.pack()
root.mainloop()
