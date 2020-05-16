#import tkFont
import random
from tkinter import*
from winsound import *
import threading

'''
import tkFont
    helv36 = tkFont.Font(family="Helvetica",size=36,weight="bold")
'''
global home
home=[] #to stores the word being guessed by the player from the database
g_list=[]
t_list=[]
k_list=[]
count=1



def game():
    #root.geometry("400*800")
    global root
    root=Tk()
    
    root.title("HANGMAN GAME")
    play1 = lambda: PlaySound('red.wav', SND_FILENAME)
    play2 = lambda: PlaySound('button4.wav', SND_FILENAME)
    play3 = lambda: PlaySound('VICTORY.wav', SND_FILENAME)
    play4 = lambda: PlaySound('looser.wav', SND_FILENAME)
    #sounds
    def playr():
        #sleep(1)
        play1()
    def playb():
        #sleep(1);
        play2()
    def playv():
        #sleep(1);
        play3()
    def playl():
        #sleep(1);
        play4()
    
    def graph(k):
        #playu = lambda: PlaySound('red.wav', SND_FILENAME)
        threading.Thread(target=playr).start()
        coord=10,20,140,110
        #k is another list for displaying the hangman
        if 1 in k:
            line=Ci.create_line(20,250,160,250,fill='green',width=5) #line 1
        if 2 in k:
            line1=Ci.create_line(60,250,60,18,fill='green',width=5) #line 2
        if 3 in k:
            line=Ci.create_line(80,25,60,45,fill='green',width=5) #3rd line
        if 4 in k:
            line=Ci.create_line(55,25,200,25,fill='green',width=5) #line 4
        if 5 in k:
            line=Ci.create_line(200,25,200,55,fill='green',width=5) #line 5
        if 6 in k:
            ovl=Ci.create_oval(180,55,220,85,fill="#fb0",width=0)    #Circle 6
        if 7 in k:
            line=Ci.create_line(200,160,200,85,fill='#fb0',width=8) #line 7
        if 8 in k:
            line=Ci.create_line(200,160,155,200,fill='#fb0',width=8) #line 8
        if 9 in k:
            line=Ci.create_line(200,160,245,200,fill='#fb0',width=8) #line 9
        if 10 in k:
            line=Ci.create_line(200,105,150,75,fill='#fb0',width=8)  #line 10
        if 10 in k:
            line=Ci.create_line(200,105,250,75,fill='#fb0',width=8)  #line 11
        Ci.pack()
   #function will display the no of entry box that is been guessed
    def empty(l):
        frame=Frame(root)
        frame.pack()
        global em
        em=[]
        for x in range(0,l,1):
            em.append('em'+str(x))
            em[x]=Entry(frame,bg="skyblue",width=2)#bd=10
            em[x].pack(side=LEFT)
    def p_disp():       #run once at begning randomly select one and display spaces
        global home
        f1=open("soprts.txt","r")
        while True:
            text=f1.readline(50)
            if text=="":
                break
            text=text[:-1]
            t_list.append(text)
        f1.close()
        home.append(random.choice(t_list))
        home=home[0]
        length=len(home)
        empty(length)  
    def f_check(xx):
        global k_list
        global count
        global win_word
        win_word=''
        flg=0
        tmp=home
        ln=len(tmp)
        if(len(k_list)==9):
            topframe.destroy()
            leftframe.destroy()
            rightframe.destroy()
            bottomframe.destroy()
            pp.destroy()
            msg=Label(root,text="All Attempts Consumed .\nYou are sentenced to death. ",font="Elephant")
            http="CORRECT WORD IS \n"+home
            msg1=Label(root,text=http,padx=5,font="Elephant")
            threading.Thread(target=playl).start()
            bb1=Button(root,text="Play Again",bg="blue",fg="yellow",command=play_again)
            bb2=Button(root,text=" EXIT ",bg="red",fg="yellow",command=quit)
            msg1.pack()
            msg.pack(side="bottom")
            bb1.pack(side=LEFT,padx=10)
            bb2.pack(side='right',padx=10, pady=10)  
        for ii in range(ln):
            if(xx==tmp[ii]):
                em[ii].insert(0,xx)
                flg=1
        if(flg==0):             #call hang function
            k_list.append(count)
            graph(k_list)
            count=count+1
        else:
            threading.Thread(target=playb).start()
            
        for ii in range(ln):
            win_word=win_word+em[ii].get()
        if(win_word==home):
            topframe.destroy()
            leftframe.destroy()
            rightframe.destroy()
            bottomframe.destroy()
            pp.destroy()
            msg=Label(root,text="CONGRATS \n YOU WON !!",font="Elephant")
            bb1=Button(root,text="Play Again",bg="blue",fg="yellow",command=play_again)
            bb2=Button(root,text=" EXIT ",bg="red",fg="yellow",command=quit)
            msg.pack(side="bottom")
            threading.Thread(target=playv).start()
            bb1.pack(side=LEFT,padx=10)
            bb2.pack(side='right',padx=10, pady=10)
    def A():
        if 'A' not in g_list:
            g_list.append('A')
            pp.insert(0,'A')
            f_check('A')
            a['fg']='RED'
            a['bg']='white'
    def B():
        if 'B' not in g_list:
            g_list.append('B')
            pp.insert(0,'B')
            f_check('B')
            b['fg']='RED'
            b['bg']='white'
    def C():
        if 'C' not in g_list:
            g_list.append('C')
            pp.insert(0,'C')
            f_check('C')
            c['fg']='RED'
            c['bg']='white'
    def D():
        if 'D' not in g_list:
            g_list.append('D')
            pp.insert(0,'D')
            f_check('D')
            d['fg']='RED'
            d['bg']='white'
    def E():
        if 'E' not in g_list:
            g_list.append('E')
            pp.insert(0,'E')
            f_check('E')
            e['fg']='RED'
            e['bg']='white'
    def F():
        if 'F' not in g_list:
            g_list.append('F')
            pp.insert(0,'F')
            f_check('F')
            f['fg']='RED'
            f['bg']='white'
    def G():
        if 'G' not in g_list:
            g_list.append('G')
            pp.insert(0,'G')
            f_check('G')
            g['fg']='RED'
            g['bg']='white'
    def H():
        if 'H' not in g_list:
            g_list.append('H')
            pp.insert(0,'H')
            f_check('H')
            h['fg']='RED'
            h['bg']='white'
    def I():
        if 'I' not in g_list:
            g_list.append('I')
            pp.insert(0,'I')
            f_check('I')
            i['fg']='RED'
            i['bg']='white'
    def J():
        if 'J' not in g_list:
            g_list.append('J')
            pp.insert(0,'J')
            f_check('J')
            j['fg']='RED'
            j['bg']='white'
    def K():
        if 'K' not in g_list:
            g_list.append('K')
            pp.insert(0,'K')
            f_check('K')
            k['fg']='RED'
            k['bg']='white'
    def L():
        if 'L' not in g_list:
            g_list.append('L')
            pp.insert(0,'L')
            f_check('L')
            l['fg']='RED'
            l['bg']='white'
    def M():
        if 'M' not in g_list:
            g_list.append('M')
            pp.insert(0,'M')
            f_check('M')
            m['fg']='RED'
            m['bg']='white'
    def N():
        if 'N' not in g_list:
            g_list.append('N')
            pp.insert(0,'N')
            f_check('N')
            n['fg']='RED'
            n['bg']='white'
    def O():
        if 'O' not in g_list:
            g_list.append('O')
            pp.insert(0,'O')
            f_check('O')
            o['fg']='RED'
            o['bg']='white'
    def P():
        if 'P' not in g_list:
            g_list.append('P')
            pp.insert(0,'P')
            f_check('P')
            p['fg']='RED'
            p['bg']='white'
    def Q():
        if 'Q' not in g_list:
            g_list.append('Q')
            pp.insert(0,'Q')
            f_check('Q')
            q['fg']='RED'
            q['bg']='white'
    def R():
        if 'R' not in g_list:
            g_list.append('R')
            pp.insert(0,'R')
            f_check('R')
            r['fg']='red'
            r['bg']='white'
    def S():
        if 'S' not in g_list:
            g_list.append('S')
            pp.insert(0,'S')
            f_check('S')
            s['fg']='RED'
            s['bg']='white'
    def T():
        if 'T' not in g_list:
            g_list.append('T')
            pp.insert(0,'T')
            f_check('T')
            t['fg']='RED'
            t['bg']='white'
    def U():
        if 'U' not in g_list:
            g_list.append('U')
            pp.insert(0,'U')
            f_check('U')
            u['fg']='RED'
            u['bg']='white'
    def V():
        if 'V' not in g_list:
            g_list.append('V')
            pp.insert(0,'V')
            f_check('V')
            v['fg']='RED'
            v['bg']='white'
    def W():
        if 'W' not in g_list:
            g_list.append('W')
            pp.insert(0,'W')
            f_check('W')
            w['fg']='RED'
            w['bg']='white'
    def X():
        if 'X' not in g_list:
            g_list.append('X')
            pp.insert(0,'X')
            f_check('X')
            x['fg']='RED'
            x['bg']='white'
    def Y():
        if 'Y' not in g_list:
            g_list.append('Y')
            pp.insert(0,'Y')
            f_check('Y')
            y['fg']='RED'
            y['bg']='white'
    def Z():
        if 'Z' not in g_list:
            g_list.append('Z')
            pp.insert(0,'Z')
            f_check('Z')
            z['fg']='RED'
            z['bg']='white'
    def play_again():
        
        global root
        global g_list
        global home
        global k_list
        global t_list
        global count
        home=[] #to stores the word being guessed by the player from the database
        g_list=[]
        t_list=[]
        k_list=[]
        g_list=[]
        count=1
        root.destroy()
        #import page1
        game()
    #-weight bold    
    text_box=Label(root,text="Guess The Name Of \nSPORTS ",font="Georgia",bg="cyan")
    text_box.pack(side="top")
    
    Ci=Canvas(root,bg="black",height=300,width=350)
    Ci.pack(side=TOP)
  
    p_disp()
    frame=Frame(root)
    frame.pack()
    pp=Entry(frame,bg="gray80")#bd=10  
    topframe=Frame(root)
    topframe.pack()
    leftframe=Frame(root)
    leftframe.pack()
    rightframe=Frame(root)
    rightframe.pack()
    bottomframe=Frame(root)
    bottomframe.pack()
    a=Button(topframe,text="A",bg="Green",activebackground="blue",width="4",height="2",command=A)
    b=Button(topframe,text="B",bg="Green",activebackground="blue",width="4",height="2",command=B)
    c=Button(topframe,text="C",bg="Green",activebackground="blue",width="4",height="2",command=C)
    d=Button(topframe,text="D",bg="Green",activebackground="blue",width="4",height="2",command=D)
    e=Button(topframe,text="E",bg="Green",activebackground="blue",width="4",height="2",command=E)
    f=Button(topframe,text="F",bg="Green",activebackground="blue",width="4",height="2",command=F)
    g=Button(topframe,text="G",bg="Green",activebackground="blue",width="4",height="2",command=G)
    h=Button(topframe,text="H",bg="Green",activebackground="blue",width="4",height="2",command=H)
    i=Button(topframe,text="I",bg="Green",activebackground="blue",width="4",height="2",command=I)
    j=Button(topframe,text="J",bg="Green",activebackground="blue",width="4",height="2",command=J)
    k=Button(leftframe,text="K",bg="yellow",activebackground="blue",width="4",height="2",command=K)
    l=Button(leftframe,text="L",bg="yellow",activebackground="blue",width="4",height="2",command=L)
    m=Button(leftframe,text="M",bg="yellow",activebackground="blue",width="4",height="2",command=M)
    n=Button(leftframe,text="N",bg="yellow",activebackground="blue",width="4",height="2",command=N)
    o=Button(leftframe,text="O",bg="yellow",activebackground="blue",width="4",height="2",command=O)
    p=Button(leftframe,text="P",bg="yellow",activebackground="blue",width="4",height="2",command=P)
    q=Button(leftframe,text="Q",bg="yellow",activebackground="blue",width="4",height="2",command=Q)
    r=Button(leftframe,text="R",bg="yellow",activebackground="blue",width="4",height="2",command=R)
    s=Button(leftframe,text="S",bg="yellow",activebackground="blue",width="4",height="2",command=S)
    t=Button(rightframe,text="T",bg="green",activebackground="blue",width="4",height="2",command=T)
    u=Button(rightframe,text="U",bg="green",activebackground="blue",width="4",height="2",command=U)
    v=Button(rightframe,text="V",bg="green",activebackground="blue",width="4",height="2",command=V)
    w=Button(rightframe,text="W",bg="green",activebackground="blue",width="4",height="2",command=W)
    x=Button(rightframe,text="X",bg="green",activebackground="blue",width="4",height="2",command=X)
    y=Button(rightframe,text="Y",bg="green",activebackground="blue",width="4",height="2",command=Y)
    z=Button(rightframe,text="Z",bg="green",activebackground="blue",width="4",height="2",command=Z)
    bb1=Button(bottomframe,text="Play Again",height="1",width="10",bg="black",fg="white",command=play_again)
    bb2=Button(bottomframe,text=" EXIT ",height="1",width="10",bg="red",fg="white",command=quit,padx="5")
    pp.pack(side=TOP)
    a.pack(side=LEFT)
    b.pack(side=LEFT)
    c.pack(side=LEFT)
    d.pack(side=LEFT)
    e.pack(side=LEFT)
    f.pack(side=LEFT)
    g.pack(side=LEFT)
    h.pack(side=LEFT)
    i.pack(side=LEFT)
    j.pack(side=LEFT)
    k.pack(side=LEFT)
    l.pack(side=LEFT)
    m.pack(side=LEFT)
    n.pack(side=LEFT)
    o.pack(side=LEFT)
    p.pack(side=LEFT)
    q.pack(side=LEFT)
    r.pack(side=LEFT)
    s.pack(side=LEFT)
    t.pack(side=LEFT)
    u.pack(side=LEFT)
    v.pack(side=LEFT)
    w.pack(side=LEFT)
    x.pack(side=LEFT)
    y.pack(side=LEFT)
    z.pack(side=LEFT)
    bb1.pack(side=LEFT)
    bb2.pack(side='right',padx=50, pady=10)
game()
root.mainloop()
