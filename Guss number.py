import random as rd
from tkinter import *

root=Tk()
root.title('Guess game')
root.configure(bg='#000000')
root.geometry('400x160')

class guss_number():
    def __init__(self,h,r):    
        root.geometry('400x350')    
        Label(root,width=400,height=350,bg='black').place(x=0,y=0)
        self.massage=StringVar()
        self.anwerr=StringVar()
        self.heart=StringVar()
        self.r = r
        self.h = h
        self.anwer = rd.randint(1,self.r)
        self.e = Entry(root,width=4,font=("Franklin Gothic Demi",18),bg='#FFFFFF',fg='#000000')
        self.e.place(x=165,y=50)
        self.b4 = Button(text='click',width=4,font=("Franklin Gothic Demi",17),bg='#000000',fg='#FFFFFF',command = self.guesss)
        self.b4.place(x=165,y=85)
        self.f1 = Frame(root,bg="#FFFFFF",width=350,height=105)
        self.f1.place(x=25,y=150)
        self.f2 = Frame(root,bg="#000000",width=348,height=102)
        self.f2.place(x=26,y=152)   
        self.heart.set('10')   
        self.l2 = Label(root,text=f'Guess a number between 1 to {r}',font=("Franklin Gothic Demi",17),bg='#000000',fg='#FFFFFF')
        self.l2.place(x=30,y=10)
        self.l3 = Label(root,textvariable=self.massage,font=("Franklin Gothic Demi",17),bg='#000000',fg='#FFFFFF')
        self.l3.place(x=30,y=170)
        self.l4 = Label(root,text='Heart:',font=("Franklin Gothic Demi",17),bg='#000000',fg='#FFFFFF')
        self.l4.place(x=30,y=200)
        self.l5 = Label(root,textvariable=self.heart,font=("Franklin Gothic Demi",17),bg='#000000',fg='#FFFFFF')
        self.l5.place(x=100,y=200)   
        self.b5 = Button(text='play again',width=8,font=("Franklin Gothic Demi",17),bg='#FFFFFF',fg='#000000',command = a)
        self.b5.place(x=140,y=270)   

    def guesss(self):    
        self.h-=1   
        self.heart.set(self.h)
        self.guess1 = self.e.get()
        if int(self.guess1)==self.anwer:
            self.massage.set('You win')   
        elif int(self.guess1)>self.anwer:
            self.massage.set('Your anwer is bigger than anwer')
            self.e.delete(0, END)    
        elif int(self.guess1)<self.anwer:
            self.massage.set('Your anwer is smaller than anwer')
            self.e.delete(0, END)    
        if self.h==0:
            self.massage.set('You lose, the anwer is')
            self.anwerr.set(self.anwer)
        Label(root,textvariable=self.anwerr,font=("Franklin Gothic Demi",17),bg='#000000',fg='#FFFFFF').place(x=260,y=170)

def a():
    Label(root,width=400,height=160,font=("Franklin Gothic Demi",19),bg='#000000').place(x=0,y=0)
    Label(root,text='Choose level',font=("Franklin Gothic Demi",19),bg='#000000',fg='#FFFFFF').place(x=125,y=20)
    Button(root,text='Hard',width=5,font=("Franklin Gothic Demi",17),bg='#FFFFFF',fg='#000000',command = lambda : guss_number(10,500) ).place(x=65,y=70)
    Button(root,text='Medium',width=7,font=("Franklin Gothic Demi",17),bg='#FFFFFF',fg='#000000',command = lambda : guss_number(7,100)).place(x=153,y=70)
    Button(root,text='Easy',width=5,font=("Franklin Gothic Demi",17),bg='#FFFFFF',fg='#000000',command = lambda : guss_number(5,10)).place(x=265,y=70)    
    root.geometry('400x160')
a()

mainloop()