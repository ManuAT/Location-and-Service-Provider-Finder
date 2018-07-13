# inserting header files
from Tkinter import*
import tkFont as tkfont
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title("FIND SERVICE PROVIDER AND LOCATION AND LOCTION VIA STD & ISD")
root.resizable(width=FALSE,height=FALSE)
root.geometry('640x720')
title_font = tkfont.Font(family='Helvetica', size=20, weight="bold", slant="italic")
sub_font = tkfont.Font(family='arial', size=12, slant="italic")
sub_font1 = tkfont.Font(family='arial', size=10, slant="italic")

# variable intialization
value = StringVar()
value1 = StringVar()
ovalue =StringVar()

# insering icons and make it as global
idea = ImageTk.PhotoImage(Image.open("idea.png"))
im1 = Label(root, image=idea)
airtel = ImageTk.PhotoImage(Image.open("airtel.png"))
im2 = Label(root, image=airtel)
bsnl = ImageTk.PhotoImage(Image.open("bsnlgsm.png"))
im3 = Label(root, image=bsnl)
vodafone = ImageTk.PhotoImage(Image.open("vodafone.png"))
im4 = Label(root, image=vodafone)
tata = ImageTk.PhotoImage(Image.open("tatadocomo.png"))
im5 = Label(root, image=tata)
jio = ImageTk.PhotoImage(Image.open("reliancejio.png"))
im6 = Label(root, image=jio)
reliance = ImageTk.PhotoImage(Image.open("reliancemobilegsm.png"))
im7 = Label(root, image=reliance)
ukn = ImageTk.PhotoImage(Image.open("invalid.png"))
im8 = Label(root, image=ukn)

# funtion to call icon of service provider
def icon(x):
    global  ImageTk
    if x==8:
        im1.pack()
    elif x==2:
        im2.pack()
    elif x==3:
        im3.pack()
    elif x==22:
        im4.pack()
    elif x==17:
        im5 .pack()
    elif x==24:
        im6.pack()
    elif x==12:
        im7.pack()
    else:
        im8.pack()

label1 = Label(root, text="");
label2 = Label(root, text="");
label3 = Label(root, text="");
label4 = Label(root, text="");
label5 = Label(root, text="");
tx = Label(root, text="");

# function for call indian numbers
def india():
    global label1, label2, label3, label4 ,label5
    global icon
    xtext = value.get()

    l = []
    l = xtext
    le = len(l)
    num = l[0:4]
    con = sqlite3.connect('data.db')
    cursor = con.cursor()
    nam1 = ("SELECT * FROM mobileNumberfinder where mobilenumber = ?")
    cursor.execute(nam1, [(num)])
    result = cursor.fetchall()
    if result:
        for i in result:
            tx.pack()
            label2.config(text="LOCATION :"+i[2]);
            label3.config(text="LATITUDE :"+i[4]+" "+"LONGITUDE :"+i[5]);
            label2.pack()
            label3.pack()
            tx.pack()
            label1.config(text="SERVICE PROVIDER :"+i[1]);
            label1.pack()
            tx.pack()
            icon(i[3])

# funtion for other numbers
def other():
    global label1, label2, label3, label4, label5
    xtext = value.get()
    l = []
    l = xtext
    le = len(l)
    num = l[0:3]
    con = sqlite3.connect('data.db')
    cursor = con.cursor()
    nam1 = ("SELECT * FROM mobileNumberfinder where mobilenumber = ?")
    cursor.execute(nam1, [(num)])
    result = cursor.fetchall()
    if result:
        for i in result:
            tx.pack()
            label2.config(text="LOCATION :" + i[2]);
            label3.config(text="LATITUDE :" + i[4] + " " + "LONGITUDE :" + i[5]);
            label2.pack()
            label3.pack()
            tx.pack()
            label1.config(text="SERVICE PROVIDER :" + i[1]);
            label1.pack()
            tx.pack()
            icon(i[3])
# funtion of isd
def isd():
    global label1, label2, label3, label4, label5
    xtext = value1.get()
    l = []
    l = xtext
    le = len(l)
    num = l[0:4]
    con = sqlite3.connect('data.db')
    cursor = con.cursor()
    nam1 = ("SELECT * FROM isdcodes where isdcode = ?")
    cursor.execute(nam1, [(num)])
    result = cursor.fetchall()
    if result:
        l = "LOCATION  \n _______________\n"
        for i in result:
            l+=i[0]+"\n"
        label1.config(text=l);
        label1.pack()
# function of std()
def std():
    global label1, label2, label3, label4, label5
    xtext = value1.get()
    l = []
    l = xtext
    le = len(l)
    num = l[0:4]
    con = sqlite3.connect('data.db') #connecting data base
    cursor = con.cursor()
    nam1 = ("SELECT * FROM stdcodes where stdcode = ?")   #query for sqllite
    cursor.execute(nam1, [(num)])
    result = cursor.fetchall()
    if result:
        for i in result:
            label1.config(text="LOCATION :"+i[0]);
            label1.pack()
# function to  call std and isd
def fn2():
    value.set("")
    im1.pack_forget()
    im2.pack_forget()
    im3.pack_forget()
    im4.pack_forget()
    im5.pack_forget()
    im6.pack_forget()
    im7.pack_forget()
    im8.pack_forget()
    label1.pack_forget()
    label2.pack_forget()
    label3.pack_forget()
    label4.pack_forget()
    label5.pack_forget()
    ovalue = selected1.get()
    if ovalue == "STD":
        std()
    else:
        isd()
    return

# function to call fs
def fn():
    value1.set("")
    im1.pack_forget()
    im2.pack_forget()
    im3.pack_forget()
    im4.pack_forget()
    im5.pack_forget()
    im6.pack_forget()
    im7.pack_forget()
    im8.pack_forget()
    label1.pack_forget()
    label2.pack_forget()
    label3.pack_forget()
    label4.pack_forget()
    label5.pack_forget()
    ovalue = selected.get()
    if ovalue == "INDIA":
        india()
    else:
        other()
    return
# for triger using Enter key
def callback(event):
    z ='{k!r}'.format(k=event.char)
    if(ord(event.char) ==13):
        fn()
def callback1(event):
    z ='{k!r}'.format(k=event.char)
    if(ord(event.char) ==13):
        fn2()

# fs widgets......
Label(root,text=" ").pack()
label = Label(root, text="FIND SERVICE PROVIDER AND LOCATION",font=title_font).pack()
Label(root,text=" ").pack()
list = ["INDIA","US","CANDA","PAKISTAN"]
selected = StringVar()
selected.set(list[0])
Label(root,text="SELECT A COUNTRY",font=sub_font).pack()
menu = OptionMenu(root,selected,*list)
menu.pack()
Label(root,text=" ").pack()
Label(root,text="ENTER THE MOBILE NUMBER",font=sub_font1).pack()
text = Entry(root,textvariable=value,font=sub_font)
text.bind('<Key>',callback)
text.pack()
Label(root,text=" ").pack()
but = Button(root,text="SEARCH",font=sub_font,command=fn).pack()
# std&sd.widgets ...........

Label(root,text=" ").pack()
labels = Label(root, text="FIND LOCATION VIA STD & ISD",font=title_font).pack()
Label(root,text=" ").pack()
list = ["STD","ISD"]
selected1 = StringVar()
selected1.set(list[0])
Label(root,text="SELECT ISD OR ISD",font=sub_font).pack()
menu1 = OptionMenu(root,selected1,*list)
menu1.pack()
Label(root,text=" ").pack()
Label(root,text="ENTER THE CODE",font=sub_font1).pack()
text1 = Entry(root,textvariable=value1,font=sub_font)
text1.bind('<Key>',callback1)
text1.pack()
Label(root,text=" ").pack()
but1 = Button(root,text="SEARCH",font=sub_font,command=fn2).pack()
Label(root,text=" ").pack()
root.mainloop()
