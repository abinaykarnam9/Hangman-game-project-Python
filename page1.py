from tkinter import*
global root
root=Tk()
root.title("HANGMAN GAME")

def g():
    root.destroy()
    import page2
def h():
    root.destroy()
    import page3
    
frame=Frame(root)

frame.pack()
pp=Entry(frame,bg="black") 
topframe=Frame(root)
topframe.pack()


root.geometry('400x400+400+400')
l=Label(root,text="PLAYING OPTIONS", font=("bold"),width=35)
b0=Button(root,text="SINGLE PLAYER",font=("bold"),width=25,height=5,bg="gold",command=g,cursor='man',relief=RAISED)
b1=Button(root,text="DOUBLE PLAYER",font=("bold"),width=25,height=5,bg="gold",command=h,cursor='man',relief=RAISED)

l.pack(padx=5,pady=20)
b0.pack(padx=20,pady=20)
b1.pack(padx=20,pady=20)




root.mainloop()




'''

from Tkinter import * #this imports the tkinter module 

root = Tk()

listbox = Listbox(root)

listbox.pack()

b0=Button(root,text="SINGLE PLAYER")

b1=Button(root,text="DOUBLE PLAYER")

b0.pack()
b1.pack()



root.mainloop()'''
