import tkinter as tk
from tkinter import *
root=tk.Tk()
data=StringVar()
date=StringVar()
du=""
dp=""
ne=""
val=""
n=1
nt=0
bac=0
user1="9141525275"
pass1="1234"
root.geometry('900x600')
root.resizable(0,0)
root.title("Darshan's bank")
frame1=Frame(root)
frame1.pack(expand=True,fill="both")
frame2=Frame(root)
frame2.pack(expand=True,fill="both")
frame3=Frame(root)
frame3.pack(expand=True,fill="both")
row1=Frame(frame3,bg="#ffffff")
row1.pack(expand=True,fill="both")
row2=Frame(frame3,bg="#ffffff")
row2.pack(expand=True,fill="both")
row3=Frame(frame3,bg="#ffffff")
row3.pack(expand=True,fill="both")
row4=Frame(frame3,bg="#ffffff")
row4.pack(expand=True,fill="both")
label=Label(frame2,text="enter the id no",font=("arial",22),anchor="se")
label.pack()
label2=Label(frame2,textvariable=data,font=("arial",22),anchor="se")
label2.pack()
label3=Label(frame2,text="enter the pin",font=("arial",22),anchor="se")
label3.pack()
label4=Label(frame2,textvariable=date,font=("arial",22),anchor="se")
label4.pack()
wel=Label(frame1,text="WELCOME TO THE DARSHAN'S BANK",font=("bold",33),anchor="center")
wel.pack()
def btn1c():
    global ne
    global n
    global val
    if n==1:
       val = val + "1"
       data.set(val)
    if n==2:
        ne = ne + "1"
        date.set(ne)


def btn2c():
    global ne
    global n
    global val
    if n==1:
      val = val + "2"
      data.set(val)
    if n==2:
        ne = ne + "2"
        date.set(ne)
def btn3c():
    global ne
    global n
    global val
    if n==1:
      val = val + "3"
      data.set(val)
    if n==2:
        ne = ne + "3"
        date.set(ne)
def btn4c():
    global ne
    global n
    global val
    if n==1:
      val = val + "4"
      data.set(val)
    if n==2:
        ne = ne + "4"
        date.set(ne)
def btn5c():
    global n
    global ne
    global val
    if n==1:
      val = val + "5"
      data.set(val)
    if n==2:
        ne = ne + "5"
        date.set(ne)
def btn6c():
    global n
    global ne
    global val
    if n==1:
      val = val + "6"
      data.set(val)
    if n==2:
        ne = ne + "6"
        date.set(ne)
def btn7c():
    global val
    global ne
    global n
    if n==1:
      val = val + "7"
      data.set(val)
    if n==2:
        ne = ne + "7"
        date.set(ne)
def btn8c():
    global val
    global n
    global ne
    if n==1:
      val = val + "8"
      data.set(val)
    if n==2:
        ne = ne + "8"
        date.set(ne)
def btn9c():
    global val
    global n
    global ne

    if n==1:
        val = val + "9"
        data.set(val)
    if n==2:
        ne = ne + "9"
        date.set(ne)
def btn0c():
    global val
    global n
    global ne

    if n==1:
      val = val + "0"
      data.set(val)
    if n==2:
        ne=ne+"0"
        date.set(ne)
def balance():
    global l
    global balance
    global wela
    global bn1
    global bn2
    global bn3
    global bn4
    global back
    global bac
    balance=0
    if balance == 0:
        bac=1
        wel.destroy()
        bn1.destroy()
        bn2.destroy()
        bn3.destroy()
        bn4.destroy()
        l=Label(frame2,text="it seems that there is no amount in your account",font=("Algerian",20))
        l.pack()
        back=Button(frame3,text="back",command=newwindow())
        back.pack()



def newwindow():
    global wela
    global bn1
    global bn2
    global bn3
    global bn4
    global l
    global balance
    wela = Label(frame1, text="welcome to the darshan's bank", font=("Algerian", 30))
    wela.pack()
    bn1=Button(frame2,text="balance enquiry",command=balance,)
    bn1.pack(padx=40,pady=20)
    bn2=Button(frame2, text="deposite", command=balance)
    bn2.pack(padx=40,pady=20)
    bn3=Button(frame2, text="withdrawl", command=balance)
    bn3.pack(padx=40,pady=20)
    bn4=Button(frame2, text="change pin", command=balance)
    bn4.pack(padx=40,pady=20)
    l.destroy()
def btnn():
    global nt
    global n
    global val
    global ne
    global data
    n=n+1
    if n == 3:
        print(val)
        print(ne)
        if val=="9141" and ne=="8877":
            print("welcome to the darshan's bank")

            btn1.destroy()
            row1.destroy()
            row2.destroy()
            row3.destroy()
            row4.destroy()
            btn2.destroy()
            btn3.destroy()
            btn5.destroy()
            btn6.destroy()
            btn7.destroy()
            btn9.destroy()
            btn0.destroy()
            btn10.destroy()
            btn11.destroy()
            btn12.destroy()
            btn13.destroy()

            label.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            newwindow()









btn1=Button(row1,text="1",font=("arial",22),command=btn1c,border=0)
btn1.pack(side=LEFT,expand=True,fill="both",)
btn2=Button(row1,text="2",font=("arial",22),command=btn2c,border=0)
btn2.pack(side=LEFT,expand=True,fill="both")
btn3=Button(row1,text="3",font=("arial",22),command=btn3c,border=0)
btn3.pack(side=LEFT,expand=True,fill="both")
btn5=Button(row2,text="4",font=("arial",22),command=btn4c,border=0)
btn5.pack(side=LEFT,expand=True,fill="both")
btn6=Button(row2,text="5",font=("arial",22),command=btn5c,border=0)
btn6.pack(side=LEFT,expand=True,fill="both")
btn7=Button(row2,text="6",font=("arial",22),command=btn6c,border=0)
btn7.pack(side=LEFT,expand=True,fill="both")
btn9=Button(row3,text="7",font=("arial",22),command=btn7c,border=0)
btn9.pack(side=LEFT,expand=True,fill="both")
btn0=Button(row3,text="8",font=("arial",22),command=btn8c,border=0)
btn0.pack(side=LEFT,expand=True,fill="both")
btn10=Button(row3,text="9",font=("arial",22),command=btn9c,border=0)
btn10.pack(side=LEFT,expand=True,fill="both")
btn11=Button(row4,text="0",font=("arial",22),command=btn0c,border=0)
btn11.pack(side=LEFT,expand=True,fill="both")
btn12=Button(row4,text="Cancel",font=("arial",22),border=0)
btn12.pack(side=LEFT,expand=True,fill="both")
btn13=Button(row4,text="next",font=("arial",22),command=btnn,border=0)
btn13.pack(side=LEFT,expand=True,fill="both")

if du == user1 and dp == pass1:
    root.destroy()
    root2 = tk.Tk()
    root2.pack()
    root2.geometry("900x700")
    root2.title("next page")
root.mainloop()

