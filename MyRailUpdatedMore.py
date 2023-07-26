from ctypes import alignment
from tkinter import *
from tkcalendar import DateEntry
import tkinter.messagebox
import tkinter.font as tkFont
import time
import random
import sqlite3
from turtle import color
global  x1,x2,x3,x4
import tkinter.ttk as ttk

global conn, cursor
conn = sqlite3.connect('Railway.db')
c = conn.cursor()

global LoginId,count
global Password
global Source
global Destination
global Date
global Name
global Age,Gender,IdProof
global variable,variable1,variable2,v2,var
global DepartureTime, TrainNumber, Number
root = Tk()
root.title("Railway reservation")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 1280
height = 720
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.resizable(0, 0)

w = 1280
h = 720
canvas = Canvas(root, width=w, height=h)
canvas.config(bg='gray16')
#canvas.create_line(60, 0, 60, 720, fill="green", width=5)
canvas.pack()

my_image=PhotoImage(file='Train.gif')
my_img = canvas.create_image(400, 0, anchor=NW, image=my_image)

my_imaget=PhotoImage(file='RailLogopng.png')
my_imgt = canvas.create_image(150, 40, anchor=NW, image=my_imaget)

Label(root, text="NATIONAL RAILWAYS",font=('Century Gothic',17),fg='Orange',bg='gray16').place(x=90,y=150)
Label(root, text="Username",font=('Century Gothic',15),fg='white', bg='gray16').place(x=60,y=290)
Label(root, text="Password",font=('Century Gothic',15), fg='white', bg='gray16').place(x=60,y=350)

entry_1 = Entry(root, font=('Comic Sans',10))
entry_1.place(x=180,y=290,height=30)

entry_2 = Entry(root, font=('Slab Serif',10),show="•")
entry_2.place(x=180,y=350,height=30)

def printMsg():
    if((entry_1.get()=='admin' and entry_2.get()=='437') or (entry_1.get()=='user1' and entry_2.get()=='420') or (entry_1.get()=='user2' and entry_2.get()=='1') or (entry_1.get()=='user3' and entry_2.get()=='444')):
        tkinter.messagebox.showinfo('login result', 'Login Successful!')
        root.destroy()
        createWindow()
    else:
        tkinter.messagebox.showinfo('login result', 'Username or Password is incorrect. Please try again!')
    mainloop()        

#---------------------------------------------------------------------------------------------------

def createWindow():
    #root.destroy()
    window = Tk()
    window.title("Login frame")
    customFont = tkFont.Font(family="Comic Sans", size=14)
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    width = 1280
    height =720
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    window.geometry('%dx%d+%d+%d' % (width, height, x, y))
    window.resizable(0, 0)

    window.config(bg='gray16')

    w1 = 1280
    h1 = 720
    canvas1 = Canvas(window, width=w1, height=h1)
    canvas1.config(bg='gray16')
    canvas1.create_line(190, 0, 190, 720, fill="orange", width=0.5)
    my_imaget=PhotoImage(file='RailLogopng.png')
    my_imgt = canvas1.create_image(50, 40, anchor=NW, image=my_imaget)

    my_imaget1=PhotoImage(file='TrackTrain.png')
    my_imgt1 = canvas1.create_image(768, 450, anchor=NW, image=my_imaget1)
    canvas1.pack()

    Label(window, text= "Plan Your Dream Trip!",font=('Century Gothic',24), bg="gray16", fg='white').place(x=430,y=90,width=500)
    Label(window, text= ";)",font=('Century Gothic',24), bg="gray16", fg='orange').place(x=850,y=89,width=20)
    entry1 =Entry(window,justify='center',font=('Comic Sans',3))
    entry1.place(x=420, y=218)

    entry2 = Entry(window, justify='center',font=('Comic Sans', 3))
    entry2.place(x=850,y=218)

    entry3 = Entry(window, justify='center',font=('Comic Sans', 3))
    entry3.place(x=420, y=298)


    def fun_1(*args):
        entry1.insert(10,variable.get())
    def fun_2(*args):
        entry2.insert(10,variable1.get())
    def fun_3(*args):
        entry3.insert(10,variable2.get())
    # def fun_4(*args):
    #     entryd.insert(10,variabled.get())

    variable = StringVar(window)
    choices = {'Amritsar','New Delhi','Howrah','Chennai'}
    variable.set('Select')
    variable.trace("w", fun_1)
    popupMenu = OptionMenu(window, variable, *choices)
    popupMenu.place(x=420, y=218,width=130)
    popupMenu.config(font=('Slab Serif',13),bg="gray16",fg="orange")
    Label(window, text="Source",font=('Slab Serif',14), bg="gray16",fg="white").place(x=330,y=220,width=80)

    variable1 = StringVar(window)
    trains = {'Amritsar','New Delhi','Howrah','Chennai'}
    variable1.set('Select')
    variable1.trace("w", fun_2)
    popupMenu1 = OptionMenu(window, variable1, *trains)
    Label(window, text="Destination",font=('Slab Serif',15), bg="gray16",fg="white").place(x=730,y=220,width=100)
    popupMenu1.config(font=('Slab Serif',13),bg="gray16",fg="orange")
    popupMenu1.place(x=850,y=218,width=130)    

    variable2 = StringVar(window)
    classes = {'All Classes','AC First Class(1A)','AC 2 Tier(2A)','AC 3 Tier(3A)','Sleeper(SL)'}
    variable2.set('All Classes')
    variable2.trace("w", fun_3)

    popupMenu1 = OptionMenu(window, variable2, *classes)
    Label(window, text="Class", font=('Slab Serif', 15), bg="gray16",fg="white").place(x=324, y=300, width=90)
    popupMenu1.config(font=('Slab Serif', 13), bg="gray16",fg="orange")
    popupMenu1.place(x=420, y=298, width=130)

    Label(window,text="Date",font=('Slab Serif',15), bg="gray16",fg="white").place(x=765,y=300,width=80)
    Date=StringVar()
    #XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    variable4=StringVar(window) # declaring string variable 

    l1=Label(window,textvariable=variable4,bg='gray16')  # Label to display date 
    l1.place(x=850,y=305,width=30)
    cal=DateEntry(window, width=12, year=2022, month=10, day=20,background='gold', foreground='black', borderwidth=1,textvariable=variable4)
    cal.place(x=850,y=300,width=130,height=30)
   

    def my_upd(*args): # triggered when value of string varaible changes
        l1.config(text=variable4.get()) # read and display date

    variable4.trace('w',my_upd)
    e1=Entry(window,textvariable=variable4,justify='center')
    #XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

    # e1=Entry(window,textvariable=Date)
    
    
    def Check():
        if len(e1.get()) == 0 or len(entry1.get()) == 0 or len(entry2.get()) == 0 or len(entry3.get()) == 0:
            tkinter.messagebox.showinfo('Error','enter all required fields!')
        else:
            Check1()
    def Check1():
        if (variable.get() == "Amritsar" and variable1.get()== "Amritsar") or (variable1.get() == "Ajmer" and variable.get()== "Ajmer") or (variable1.get() == "Chennai" and variable.get()== "Chennai")or(variable.get() == "New Delhi" and variable1.get()== "New Delhi") or (variable1.get() == "Meerut" and variable.get()== "Meerut")or (variable1.get() == "Howrah" and variable.get()== "Howrah")or(variable1.get() == "Chandigarh" and variable.get()== "Chandigarh"):
                 tkinter.messagebox.showinfo('Error', 'Choose a different destination')
        elif (entry1.get() == "Amritsar" and entry2.get() == "New Delhi" and entry3.get() == "AC 3 Tier(3A)") or (entry1.get() == "New Delhi" and entry2.get() == "Amritsar" and entry3.get() == "AC 3 Tier(3A)"):
            tkinter.messagebox.showinfo('Error','Sorry Class 3A Unavailable!')
        elif (entry1.get() == "Howrah" and entry2.get() == "New Delhi" and entry3.get() == "AC 2 Tier(2A)") or (entry1.get() == "New Delhi" and entry2.get() == "Howrah" and entry3.get() == "AC 2 Tier(2A)"):
            tkinter.messagebox.showinfo('Error','Sorry Class 2A Unavailable!')    
        else:
            ops = e1.get()

            len1 = len(ops)
            if len1==12:
                date1=ops[0]+ops[1]+'/'
                month1=ops[3]+ops[4] +'/'
                year11=ops[6]+ops[7]+ops[8]+ops[9]


            if(len1==12):
                if(int(date1)<=31 and int(date1)>=1):
                    if(int(month1)>=1 and int(month1)<=12):
                        if(int(year11)>=2023 and int(year11)<=2022):
                            print('')
                        else:
                            tkinter.messagebox.showinfo('Error', 'Enter Year Correctly!')
                    else:
                        tkinter.messagebox.showinfo('Error', 'Enter Month Correctly!')
                else:
                    tkinter.messagebox.showinfo('Error', 'Enter date Correctly!')
                window.destroy()
                Search()
              
                   
            else:
                tkinter.messagebox.showinfo('Update', 'Travel route uploaded successfully. Click OK to continue.')
            window.destroy()  
            
            if (variable.get() == "Amritsar" and variable1.get()== "Chennai") or (variable1.get() == "Amritsar" and variable.get()== "Chennai"):
                 Search2()  
            elif (variable.get() == "Chennai" and variable1.get()== "Howrah") or (variable1.get() == "Chennai" and variable.get()== "Howrah"):
                 Search2()                   
            else:
                 Search()          
               

            #print('list1 print',list1)
            #window.destroy()

            #Search()
#---------------------------------------------------------------------------------------------------------            
    def Search2():
        root1 = Tk()
        root1.title("Railway Schedule")

        screen_width1 = root1.winfo_screenwidth()
        screen_height1 = root1.winfo_screenheight()
        width11 = 1280
        height11 = 720
        xx = (screen_width1/2) - (width11/2)
        yy = (screen_height1/2) - (height11/2)
        root1.geometry('%dx%d+%d+%d' % (width11, height11, xx, yy))
        root1.resizable(0, 0)

        w1 = 1280
        h1 = 720
        canvaas = Canvas(root1, width=w1, height=h1)
        canvaas.config(bg='gray16')  
        my_imaget1=PhotoImage(file='NoTrack1.png')
        my_imgt1 = canvaas.create_image(340, 180, anchor=NW, image=my_imaget1)  
        canvaas.pack()
        Label(root1, text= "Sorry, No Direct Trains Found!",font=('Century Gothic',24), bg="gray16", fg='white').place(x=380,y=90,width=500)
        def Backroot():
         root1.destroy()
         createWindow()
         window()

        buttonrt = Button(root1, text="Back",font=('Century Gothic',15),width=60, bg="orange", fg="gray16", command=Backroot)
        buttonrt.place(x=580,y=560,width=100)
        mainloop()
        Label(window,text="Date",font=('Slab Serif',15), bg="gray16",fg="white").place(x=450,y=300,width=80)

        
     

#---------------------------------------------------------------------------------------------------

    def Search():
        global x1

        window1=Tk()
        window1.title("RAILWAY SCHEDULE")
        window1.config(bg='gray16')
        screen_width = window1.winfo_screenwidth()
        screen_height = window1.winfo_screenheight()
        width = 1280
        height = 720
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        window1.geometry('%dx%d+%d+%d' % (width, height, x, y))
        window1.resizable(0, 0)
        
        Label(window1, text= "Choose your Train",font=('Century Gothic',24), bg="gray16", fg='white').place(x=380,y=90,width=500)
        height = 5
        width = 7
        for i in range(height):  # Rows
            for j in range(width):  # Columns
                f1 = Label(window1, text="Train Number",justify="center",font=('Century Gothic',15), bg="orange", fg="gray16")
                f1.place(x=0,y=170,width=165)
                f2 = Label(window1, text="Train Name",justify="center",font=('Century Gothic',15), bg="orange", fg="gray16", width="13")
                f2.place(x=170,y=170,width=165)
                f3 = Label(window1, text="Source",justify="center",font=('Century Gothic',15), bg="orange", fg="gray16", width="13")
                f3.place(x=340,y=170,width=165)
                f4 = Label(window1, text="Departs at",justify="center",font=('Century Gothic',15), bg="orange", fg="gray16", width="13")
                f4.place(x=510,y=170,width=165)
                f5 = Label(window1, text="Destination",justify="center",font=('Century Gothic',15), bg="orange", fg="gray16", width="13")
                f5.place(x=680,y=170,width=165)
                f6 = Label(window1, text="Arrives at",justify="center",font=('Century Gothic',15), bg="orange", fg="gray16", width="13")
                f6.place(x=850,y=170,width=165)
                f7 = Label(window1, text="Class(es)",justify="center",font=('Century Gothic',15), bg="orange", fg="gray16", width="13")
                f7.place(x=1020,y=170,width=165)

                f8 = Entry(window1, justify="center",font=('Arial',12), fg="white",bg="gray24", width="18")
                f8.place(x=0,y=200,height=40,width=165)
                f9 = Entry(window1, justify="center",font=('Arial',12), fg="white",bg="gray24", width="18")
                f9.place(x=170,y=200,height=40,width=165)
                f10 = Entry(window1, justify="center",font=('Arial',12), fg="white",bg="gray24", width="18")
                f10.place(x=340,y=200,height=40,width=165)
                f11 = Entry(window1, justify="center",font=('Arial',12), fg="white",bg="gray24", width="18")
                f11.place(x=510,y=200,height=40,width=165)
                f12 = Entry(window1, justify="center",font=('Arial',12), fg="white",bg="gray24", width="18")
                f12.place(x=680,y=200,height=40,width=165)
                f13 = Entry(window1, justify="center",font=('Arial',12), fg="white",bg="gray24", width="18")
                f13.place(x=850,y=200,height=40,width=165)
                f14 = Entry(window1, justify="center",font=('Arial',12), fg="white",bg="gray24", width="18")
                f14.place(x=1020,y=200,height=40,width=165)

                f15 =Entry(window1, justify="center",font=('Arial',12), fg="white",bg="gray24", width="18")
                f15.place(x=0,y=270,height=40,width=165)
                f16 = Entry(window1, justify="center",font=('Arial',12), fg="white",bg="gray24", width="18")
                f16.place(x=170,y=270,height=40,width=165)
                f17 = Entry(window1, justify="center",font=('Arial',12), fg="white",bg="gray24", width="18")
                f17.place(x=340,y=270,height=40,width=165)
                f18 = Entry(window1, justify="center",font=('Arial',12), fg="white",bg="gray24", width="18")
                f18.place(x=510,y=270,height=40,width=165)
                f19 = Entry(window1, justify="center",font=('Arial',12), fg="white",bg="gray24", width="18")
                f19.place(x=680,y=270,height=40,width=165)
                f20 = Entry(window1, justify="center",font=('Arial',12), fg="white",bg="gray24", width="18")
                f20.place(x=850,y=270,height=40,width=165)
                f21 = Entry(window1, justify="center",font=('Arial',12), fg="white",bg="gray24", width="18")
                f21.place(x=1020,y=270,height=40,width=165)

                f22 = Entry(window1, justify="center",font=('Arial',12), fg="white",bg="gray24", width="18")
                f22.place(x=0,y=340,height=40,width=165)
                f23 = Entry(window1, justify="center",font=('Arial',12), fg="white",bg="gray24", width="18")
                f23.place(x=170,y=340,height=40,width=165)
                f24 = Entry(window1, justify="center",font=('Arial',12), fg="white",bg="gray24", width="18")
                f24.place(x=340,y=340,height=40,width=165)
                f25 = Entry(window1, justify="center",font=('Arial',12), fg="white",bg="gray24", width="18")
                f25.place(x=510,y=340,height=40,width=165)
                f26 = Entry(window1, justify="center",font=('Arial',12), fg="white",bg="gray24", width="18")
                f26.place(x=680,y=340,height=40,width=165)
                f27 = Entry(window1, justify="center",font=('Arial',12), fg="white",bg="gray24", width="18")
                f27.place(x=850,y=340,height=40,width=165)
                f28 = Entry(window1, justify="center",font=('Arial',12), fg="white",bg="gray24", width="18")
                f28.place(x=1020,y=340,height=40,width=165)

                f29 = Entry(window1, justify="center",font=('Arial',12), fg="white",bg="gray24", width="18")
                f29.place(x=0,y=410,height=40,width=165)
                f30 = Entry(window1, justify="center",font=('Arial',12), fg="white",bg="gray24", width="18")
                f30.place(x=170,y=410,height=40,width=165)
                f31 = Entry(window1, justify="center",font=('Arial',12), fg="white",bg="gray24", width="18")
                f31.place(x=340,y=410,height=40,width=165)
                f32 = Entry(window1, justify="center",font=('Arial',12), fg="white",bg="gray24", width="18")
                f32.place(x=510,y=410,height=40,width=165)
                f33 = Entry(window1, justify="center",font=('Arial',12), fg="white",bg="gray24", width="18")
                f33.place(x=680,y=410,height=40,width=165)
                f34 = Entry(window1, justify="center",font=('Arial',12), fg="white",bg="gray24", width="18")
                f34.place(x=850,y=410,height=40,width=165)
                f35 = Entry(window1, justify="center",font=('Arial',12), fg="white",bg="gray24", width="18")
                f35.place(x=1020,y=410,height=40,width=165)
                
            #Howrah->New Delhi...12313,12303,12273,22857
            #New Delhi->Howrah...123131,123031,122731,228571

            #Amritsar->New Delhi...18101,18237,12497,12029
            #New Delhi->Amritsar...181011,182371,124971,120291

            #Howrah->Amritsar...12358,13006,12380,12317
            #Amritsar->Howrah...123581,130061,123801,123171

            #Chennai->New Delhi...12622,12616,16032,12270
            #New Delhi->Chennai...126221,126161,160321,122701
            if variable.get() == "Howrah" and variable1.get()== "New Delhi":
                    f8.insert(10, "12313")

                    f9.insert(10, "Rajdhani Express")
                    f10.insert(10, "Howrah")
                    f11.insert(10, "14:30")
                    f12.insert(10, "New Delhi")
                    f13.insert(10, "7:55")
                    f14.insert(10, "1A,2A,3A")

                    f15.insert(10, "12303")

                    f16.insert(10, "Poorva Express")
                    f17.insert(10, "Howrah")
                    f18.insert(10, "16:30")
                    f19.insert(10, "New Delhi")
                    f20.insert(10, "5:50")
                    f21.insert(10, "1A,2A,3A")

                    f22.insert(10, "12273")
                    f23.insert(10, "New Delhi Duronto")
                    f24.insert(10, "Howrah")
                    f25.insert(10, "8:35")
                    f26.insert(10, "New Delhi")
                    f27.insert(10, "15:50")
                    f28.insert(10, "1A,2A,3A")

                    f29.insert(10, "22857")
                    f30.insert(10, "SRC ANVT SF")
                    f31.insert(10, "Howrah")
                    f32.insert(10, "12:30")
                    f33.insert(10, "New Delhi")
                    f34.insert(10, "7:20")
                    f35.insert(10, "1A,2A,3A")

            if variable.get() == "New Delhi" and variable1.get()== "Howrah":
                    f8.insert(10, "123131")
                    f9.insert(10, "Rajdhani Express")
                    f10.insert(10, "New Delhi")
                    f11.insert(10, "14:30")
                    f12.insert(10, "Howrah")
                    f13.insert(10, "7:55")
                    f14.insert(10, "1A,2A,3A")

                    f15.insert(10, "123031")

                    f16.insert(10, "Poorva Express")
                    f17.insert(10, "New Delhi")
                    f18.insert(10, "16:30")
                    f19.insert(10, "Howrah")
                    f20.insert(10, "5:50")
                    f21.insert(10, "1A,2A,3A")

                    f22.insert(10, "122731")
                    f23.insert(10, "New Delhi Duronto")
                    f24.insert(10, "New Delhi")
                    f25.insert(10, "8:35")
                    f26.insert(10, "Howrah")
                    f27.insert(10, "15:50")
                    f28.insert(10, "1A,2A,3A")

                    f29.insert(10, "228571")
                    f30.insert(10, "SRC ANVT SF")
                    f31.insert(10, "New Delhi")
                    f32.insert(10, "12:30")
                    f33.insert(10, "Howrah")
                    f34.insert(10, "7:20")
                    f35.insert(10, "1A,2A,3A")              
 
            

            if (variable.get() == "Amritsar" and variable1.get()== "New Delhi"):                   
                    f8.insert(10, "18101")
                    f9.insert(10, "Tata Jat Express")
                    f10.insert(10, "Amritsar")
                    f11.insert(10, "14:30")
                    f12.insert(10, "New Delhi")
                    f13.insert(10, "7:55")
                    f14.insert(10, "1A,2A,3A,SL")

                    f15.insert(10, "18237")
                    f16.insert(10, "Chattisgarh Express")
                    f17.insert(10, "Amritsar")
                    f18.insert(10, "16:30")
                    f19.insert(10, "New Delhi")
                    f20.insert(10, "5:50")
                    f21.insert(10, "1A,2A,3A,SL")

                    f22.insert(10, "12497")
                    f23.insert(10, "Shane Punjab")
                    f24.insert(10, "Amritsar")
                    f25.insert(10, "8:35")
                    f26.insert(10, "New Delhi")
                    f27.insert(10, "15:50")
                    f28.insert(10, "1A,2A,3A")

                    f29.insert(10, "12029")
                    f30.insert(10, "Shatabdi")
                    f31.insert(10, "Amritsar")
                    f32.insert(10, "12:30")
                    f33.insert(10, "New Delhi")
                    f34.insert(10, "7:20")
                    f35.insert(10, "AC,EC")

            if (variable.get() == "New Delhi" and variable1.get()== "Amritsar"):                   
                    f8.insert(10, "181011")
                    f9.insert(10, "Tata Jat Express")
                    f10.insert(10, "New Delhi")
                    f11.insert(10, "14:30")
                    f12.insert(10, "Amritsar")
                    f13.insert(10, "7:55")
                    f14.insert(10, "1A,2A,3A,SL")

                    f15.insert(10, "182371")
                    f16.insert(10, "Chattisgarh Express")
                    f17.insert(10, "New Delhi")
                    f18.insert(10, "16:30")
                    f19.insert(10, "Amritsar")
                    f20.insert(10, "5:50")
                    f21.insert(10, "1A,2A,3A,SL")

                    f22.insert(10, "124971")
                    f23.insert(10, "Shane Punjab")
                    f24.insert(10, "New Delhi")
                    f25.insert(10, "8:35")
                    f26.insert(10, "Amritsar")
                    f27.insert(10, "15:50")
                    f28.insert(10, "1A,2A,3A")

                    f29.insert(10, "120291")
                    f30.insert(10, "Shatabdi")
                    f31.insert(10, "New Delhi")
                    f32.insert(10, "12:30")
                    f33.insert(10, "Amritsar")
                    f34.insert(10, "7:20")
                    f35.insert(10, "AC,EC")
            
            if variable.get() == "Howrah" and variable1.get()== "Amritsar":
                    f8.insert(10, "12358")
                    f9.insert(10, "Durgiana Express")
                    f10.insert(10, "Howrah")
                    f11.insert(10, "14:40")
                    f12.insert(10, "Amritsar")
                    f13.insert(10, "9:30")
                    f14.insert(10, "1A,2A")

                    f15.insert(10, "13006")
                    f16.insert(10, "ASR HWH Mail")
                    f17.insert(10, "Howrah")
                    f18.insert(10, "00:45")
                    f19.insert(10, "Amritsar")
                    f20.insert(10, "1:00")
                    f21.insert(10, "1A,2A")

                    f22.insert(10, "12380")
                    f23.insert(10, "Jaliwala B Express")
                    f24.insert(10, "Howrah")
                    f25.insert(10, "3:00")
                    f26.insert(10, "Amritsar")
                    f27.insert(10, "11:05")
                    f28.insert(10, "1A,2A")

                    f29.insert(10, "12317")
                    f30.insert(10, "Akal Takhat Express")
                    f31.insert(10, "Howrah")
                    f32.insert(10, "6:45")
                    f33.insert(10, "Amritsar")
                    f34.insert(10, "14:05")
                    f35.insert(10, "1A,2A") 

            if variable.get() == "Amritsar" and variable1.get()== "Howrah":
                    f8.insert(10, "123581")
                    f9.insert(10, "Durgiana Express")
                    f10.insert(10, "Amritsar")
                    f11.insert(10, "14:40")
                    f12.insert(10, "Howrah")
                    f13.insert(10, "9:30")
                    f14.insert(10, "1A,2A")

                    f15.insert(10, "130061")
                    f16.insert(10, "ASR HWH Mail")
                    f17.insert(10, "Amritsar")
                    f18.insert(10, "00:45")
                    f19.insert(10, "Howrah")
                    f20.insert(10, "1:00")
                    f21.insert(10, "1A,2A")

                    f22.insert(10, "123801")
                    f23.insert(10, "Jaliwala B Express")
                    f24.insert(10, "Amritsar")
                    f25.insert(10, "3:00")
                    f26.insert(10, "Howrah")
                    f27.insert(10, "11:05")
                    f28.insert(10, "1A,2A")

                    f29.insert(10, "123171")
                    f30.insert(10, "Akal Takhat Express")
                    f31.insert(10, "Amritsar")
                    f32.insert(10, "6:45")
                    f33.insert(10, "Howrah")
                    f34.insert(10, "14:05")
                    f35.insert(10, "1A,2A")          
            
            if variable.get() == "Chennai" and variable1.get()== "New Delhi":
                    f8.insert(10, "12622")
                    f9.insert(10, "Grand Trunk Express")
                    f10.insert(10, "New Delhi")
                    f11.insert(10, "14:30")
                    f12.insert(10, "Chennai")
                    f13.insert(10, "7:55")
                    f14.insert(10, "1A,2A,3A")

                    f15.insert(10, "12616")

                    f16.insert(10, "Tamil Nadu Express")
                    f17.insert(10, "New Delhi")
                    f18.insert(10, "16:30")
                    f19.insert(10, "Chennai")
                    f20.insert(10, "5:50")
                    f21.insert(10, "1A,2A,3A")

                    f22.insert(10, "16032")
                    f23.insert(10, "Andaman Express")
                    f24.insert(10, "New Delhi")
                    f25.insert(10, "8:35")
                    f26.insert(10, "Chennai")
                    f27.insert(10, "15:50")
                    f28.insert(10, "1A,2A,3A")

                    f29.insert(10, "12270")
                    f30.insert(10, "MAS Duronto Express")
                    f31.insert(10, "New Delhi")
                    f32.insert(10, "12:30")
                    f33.insert(10, "Chennai")
                    f34.insert(10, "7:20")
                    f35.insert(10, "1A,2A,3A") 

            if variable.get() == "New Delhi" and variable1.get()== "Chennai":
                    f8.insert(10, "126221")
                    f9.insert(10, "Grand Trunk Express")
                    f10.insert(10, "Chennai")
                    f11.insert(10, "14:30")
                    f12.insert(10, "New Delhi")
                    f13.insert(10, "7:55")
                    f14.insert(10, "1A,2A,3A")

                    f15.insert(10, "126161")

                    f16.insert(10, "Tamil Nadu Express")
                    f17.insert(10, "Chennai")
                    f18.insert(10, "16:30")
                    f19.insert(10, "New Delhi")
                    f20.insert(10, "5:50")
                    f21.insert(10, "1A,2A,3A")

                    f22.insert(10, "160321")
                    f23.insert(10, "Anadaman Express")
                    f24.insert(10, "Chennai")
                    f25.insert(10, "8:35")
                    f26.insert(10, "New Delhi")
                    f27.insert(10, "15:50")
                    f28.insert(10, "1A,2A,3A")

                    f29.insert(10, "122701")
                    f30.insert(10, "MAS Duronto Express")
                    f31.insert(10, "Chennai")
                    f32.insert(10, "12:30")
                    f33.insert(10, "New Delhi")
                    f34.insert(10, "7:20")
                    f35.insert(10, "1A,2A,3A")
                 

                    
                     
                            
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^                       
#...............................Updated Part as above...........................................................
            

        def PassengerDetails1():
            global x1, xtrainn, xdprtTime

            if f8.get()=="12313":
                x1=12313
            elif f8.get()=="123131":
                x1=123131
            elif f8.get() == "18101":
                x1 = 18101
            elif f8.get() == "181011":
                x1 = 181011
            elif f8.get() == "12358":
                x1 = 12358
            elif f8.get() == "12622":
                x1 = 12622 
            elif f8.get() == "126221":
                x1 = 126221   
            else:
                x1 = 123581

            if f9.get()=="Rajdhani Express":
                xtrainn="Rajdhani Express"
                xdprtTime="14:30"
            elif f9.get()=="Rajdhani Express":
                xtrainn="Rajdhani Express"
                xdprtTime="14:30"
            elif f9.get() == "Tata Jat Express":
                xtrainn = "Tata Jat Express"
                xdprtTime="14:30"
            elif f9.get() == "Tata Jat Express":
                xtrainn = "Tata Jat Express"
                xdprtTime="14:30"
            elif f9.get() == "Durgiana Express":
                xtrainn = "Durgiana Express"
                xdprtTime="14:40"
            elif f9.get() == "Durgiana Express":
                xtrainn = "Durgiana Express"
                xdprtTime="14:40"
            elif f9.get() == "Grand Trunk Express":
                xtrainn = "Grand Trunk Express"
                xdprtTime="14:30"  
            else:
                xtrainn = "Grand Trunk Express"
                xdprtTime="14:30"    

            def PassengerDetails():
                window1.destroy()
                window2 = Tk()
                window2.title("Passenger Details")
                window2.config(bg="gray16")
                screen_width = window2.winfo_screenwidth()
                screen_height = window2.winfo_screenheight()
                width = 1280
                height = 720
                x = (screen_width / 2) - (width / 2)
                y = (screen_height / 2) - (height / 2)
                window2.geometry('%dx%d+%d+%d' % (width, height, x, y))
                window2.resizable(0, 0)
                
                Label(window2, text= "Enter your Details",font=('Century Gothic',24), bg="gray16", fg='white').place(x=380,y=30,width=500)

                height = 5
                width = 5
                for i in range(height):  # Rows
                    for j in range(width):  # Columns
                        e1 = Label(window2, text="Passenger 1",justify="center",font=('Century Gothic',15), bg="gray16", fg="Orange")
                        e1.place(x=0,y=100,width=165)
                        e2 = Label(window2, text="Passenger 2",justify="center",font=('Century Gothic',15), bg="gray16", fg="Orange", width="13")
                        e2.place(x=0,y=230,width=165)
                        e3 = Label(window2, text="Passenger 3",justify="center",font=('Century Gothic',15), bg="gray16", fg="Orange", width="13")
                        e3.place(x=0,y=360,width=165)
                        e4 = Label(window2, text="Passenger 4",justify="center",font=('Century Gothic',15), bg="gray16", fg="Orange", width="13")
                        e4.place(x=0,y=490,width=165)

                        name1=Label(window2, text="Name",justify="center",font=('Century Gothic',13), bg="gray16", fg="White", width="13")
                        name1.place(x=130,y=160,width=100)
                        name2=Label(window2, text="Name",justify="center",font=('Century Gothic',13), bg="gray16", fg="White", width="13")
                        name2.place(x=130,y=290,width=100)
                        name3=Label(window2, text="Name",justify="center",font=('Century Gothic',13), bg="gray16", fg="White", width="13")
                        name3.place(x=130,y=420,width=100)
                        name4=Label(window2, text="Name",justify="center",font=('Century Gothic',13), bg="gray16", fg="White", width="13")
                        name4.place(x=130,y=550,width=100)

                        age1=Label(window2, text="Age",justify="center",font=('Century Gothic',13), bg="gray16", fg="White", width="13")
                        age1.place(x=400,y=160,width=70)
                        age2=Label(window2, text="Age",justify="center",font=('Century Gothic',13), bg="gray16", fg="White", width="13")
                        age2.place(x=400,y=290,width=70)
                        age3=Label(window2, text="Age",justify="center",font=('Century Gothic',13), bg="gray16", fg="White", width="13")
                        age3.place(x=400,y=420,width=70)
                        age4=Label(window2, text="Age",justify="center",font=('Century Gothic',13), bg="gray16", fg="White", width="13")
                        age4.place(x=400,y=550,width=70)

                        gender1=Label(window2, text="Gender",justify="center",font=('Century Gothic',13), bg="gray16", fg="White", width="13")
                        gender1.place(x=600,y=160,width=70)
                        gender2=Label(window2, text="Gender",justify="center",font=('Century Gothic',13), bg="gray16", fg="White", width="13")
                        gender2.place(x=600,y=290,width=70)
                        gender3=Label(window2, text="Gender",justify="center",font=('Century Gothic',13), bg="gray16", fg="White", width="13")
                        gender3.place(x=600,y=420,width=70)
                        gender4=Label(window2, text="Gender",justify="center",font=('Century Gothic',13), bg="gray16", fg="White", width="13")
                        gender4.place(x=600,y=550,width=70)

                        idproof1=Label(window2, text="ID Proof",justify="center",font=('Century Gothic',13), bg="gray16", fg="White", width="13")
                        idproof1.place(x=870,y=160,width=70)
                        idproof2=Label(window2, text="ID Proof",justify="center",font=('Century Gothic',13), bg="gray16", fg="White", width="13")
                        idproof2.place(x=870,y=290,width=70)
                        idproof3=Label(window2, text="ID Proof",justify="center",font=('Century Gothic',13), bg="gray16", fg="White", width="13")
                        idproof3.place(x=870,y=420,width=70)
                        idproof4=Label(window2, text="ID Proof",justify="center",font=('Century Gothic',13), bg="gray16", fg="White", width="13")
                        idproof4.place(x=870,y=550,width=70)

                        enn7 = Entry(window2, justify="center", font=('Slab Serif', 13), bg="white",fg="gray16")
                        enn7.place(x=230,y=164,width=120)
                        enn8 = Entry(window2, justify="center", font=('Slab Serif', 13), bg="white",fg="gray16")
                        enn8.place(x=480,y=164,width=50)
                        enn9 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        enn9.place(x=700,y=164,width=10)
                        e10 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        e10.place(x=970,y=164,width=10)

                        e12 = Entry(window2, justify="center", font=('Slab Serif', 13), bg="white",fg="gray16")
                        e12.place(x=230,y=294,width=120)
                        e13 = Entry(window2, justify="center", font=('Slab Serif', 13), bg="white",fg="gray16")
                        e13.place(x=480,y=294,width=50)
                        e14 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        e14.place(x=700,y=294,width=10)
                        e15 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        e15.place(x=970,y=294,width=10)

                                        


                        e17 = Entry(window2, justify="center", font=('Slab Serif', 13), bg="white",fg="gray16")
                        e17.place(x=230,y=424,width=120)
                        e18 = Entry(window2, justify="center", font=('Slab Serif', 13), bg="white",fg="gray16")
                        e18.place(x=480,y=424,width=50)
                        e19 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        e19.place(x=700,y=424,width=10)
                        e20 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        e20.place(x=970,y=424,width=10)

                        e22 = Entry(window2, justify="center", font=('Slab Serif', 13), bg="white",fg="gray16")
                        e22.place(x=230,y=554,width=120)
                        e23 = Entry(window2, justify="center", font=('Slab Serif', 13), bg="white",fg="gray16")
                        e23.place(x=480,y=554,width=50)
                        e24 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        e24.place(x=700,y=554,width=10)
                        e25 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        e25.place(x=970,y=554,width=10)

                        # e1.insert(10, "S.no")
                        # enn2.insert(10, "Name")
                        # enn3.insert(10, "Age")
                        # enn4.insert(10, "Gender")
                        # e5.insert(10, "IdProof")
                        # e6.insert(10, "1")

                        # e11.insert(10, "2")
                        # e16.insert(10, "3")
                        # e21.insert(10, "4")

                        # e1.grid(row=0, column=0)
                        # enn2.grid(row=0, column=1)
                        # enn3.grid(row=0, column=2)
                        # enn4.grid(row=0, column=3)
                        # e5.grid(row=0, column=4)
                        # e6.grid(row=1, column=0)
                        # enn7.grid(row=1, column=1)
                        # enn8.grid(row=1, column=2)
                        # enn9.grid(row=1, column=3)
                        # e10.grid(row=1, column=4)

                        # e11.grid(row=2, column=0)
                        # e12.grid(row=2, column=1)
                        # e13.grid(row=2, column=2)
                        # e14.grid(row=2, column=3)
                        # e15.grid(row=2, column=4)

                        # e16.grid(row=3, column=0)
                        # e17.grid(row=3, column=1)
                        # e18.grid(row=3, column=2)
                        # e19.grid(row=3, column=3)
                        # e20.grid(row=3, column=4)

                        # e21.grid(row=4, column=0)
                        # e22.grid(row=4, column=1)
                        # e23.grid(row=4, column=2)
                        # e24.grid(row=4, column=3)
                        # e25.grid(row=4, column=4)

                        def fun(*args):
                            enn9.insert(10, v2.get())

                        def fun1(*args):
                            e14.insert(10, v3.get())

                        def fun2(*args):
                            e19.insert(10, v4.get())

                        def fun3(*args):
                            e24.insert(10, v5.get())

                        def fun4(*args):
                            e10.insert(10, v6.get())

                        def fun5(*args):
                            e15.insert(10, v7.get())

                        def fun6(*args):
                            e20.insert(10, v8.get())

                        def fun7(*args):
                            e25.insert(10, v9.get())

                        v2 = StringVar(window2)
                        genderr = {'Male', 'Female'}
                        v2.set('Select')
                        v2.trace("w", fun)
                        popupMenu1 = OptionMenu(window2, v2, *genderr)
                        popupMenu1.config(font=('Slab Serif', 13), bg="gray16", fg="orange")
                        popupMenu1.place(x=700,y=160,width=100)

                        v3 = StringVar(window2)
                        genderr1 = {'Male', 'Female'}
                        v3.set('Select')
                        v3.trace("w", fun1)
                        popupMenu2 = OptionMenu(window2, v3, *genderr1)
                        popupMenu2.config(font=('Slab Serif', 13), bg="gray16", fg="orange")
                        popupMenu2.place(x=700,y=290,width=100)

                        v4 = StringVar(window2)
                        genderr2 = {'Male', 'Female'}
                        v4.set('Select')
                        v4.trace("w", fun2)
                        popupMenu3 = OptionMenu(window2, v4, *genderr2)
                        popupMenu3.config(font=('Slab Serif', 13), bg="gray16", fg="orange")
                        popupMenu3.place(x=700,y=420,width=100)

                        v5 = StringVar(window2)
                        genderr3 = {'Male', 'Female'}
                        v5.set('Select')
                        v5.trace("w", fun3)
                        popupMenu4 = OptionMenu(window2, v5, *genderr3)
                        popupMenu4.config(font=('Slab Serif', 13), bg="gray16", fg="orange")
                        popupMenu4.place(x=700,y=550,width=100)

                        v6 = StringVar(window2)
                        proof = {'Aadhar card', 'Pan card'}
                        v6.set('Select')
                        v6.trace("w", fun4)
                        popup = OptionMenu(window2, v6, *proof)
                        popup.config(font=('Slab Serif', 13), bg="gray16",fg="orange")
                        popup.place(x=970,y=160,width=150)

                        v7 = StringVar(window2)
                        proof = {'Aadhar card', 'Pan card'}
                        v7.set('Select')
                        v7.trace("w", fun5)
                        popup = OptionMenu(window2, v7, *proof)
                        popup.config(font=('Slab Serif', 13), bg="gray16",fg="orange")
                        popup.place(x=970,y=290,width=150)

                        v8 = StringVar(window2)
                        proof = {'Aadhar card', 'Pan card'}
                        v8.set('Select')
                        v8.trace("w", fun6)
                        popup = OptionMenu(window2, v8, *proof)
                        popup.config(font=('Slab Serif', 13), bg="gray16",fg="orange")
                        popup.place(x=970,y=420,width=150)
                        v9 = StringVar(window2)
                        proof = {'Aadhar card', 'Pan card'}
                        v9.set('Select')
                        v9.trace("w", fun7)
                        popup = OptionMenu(window2, v9, *proof)
                        popup.config(font=('Slab Serif', 13), bg="gray16",fg="orange")

                        popup.place(x=970,y=550,width=150)

                        

                        
                        

                def Check1():

                    

                    def Show():
                        global x1,count
                        if enn7.get()!="" and e12.get()=="" and e17.get()=="" and e22.get()=="":
                         
                         
                         count=1
                         window3 = Tk()

                         window3.title("Ticket")
                         screen_width = window3.winfo_screenwidth()
                         screen_height = window3.winfo_screenheight()
                         width = 580
                         height = 480
                         x = (screen_width / 2) - (width / 2)
                         y = (screen_height / 2) - (height / 2)
                         window3.geometry('%dx%d+%d+%d' % (width, height, x, y))
                         window3.resizable(0, 0)
                         window3.config(bg='gray16')

                         w11 = 580
                         h11 = 480
                         canvas3 = Canvas(window3, width=w11, height=h11)
                         canvas3.config(bg='gray16')
                         canvas3.create_rectangle(0, 0,580,30, fill= "orange")
                         canvas3.create_line(40, 90, 270, 90, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 130, 270, 130, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 170, 270, 170, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 210, 270, 210, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 250, 270, 250, fill="gray13", width=0.0000001)

                         canvas3.create_line(320, 90, 550, 90, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 130, 550, 130, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 170, 550, 170, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 210, 550, 210, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 250, 550, 250, fill="gray13", width=0.0000001)
                         canvas3.pack()
                         Label(window3, text="PNR Status Details",bg='orange',fg='gray16', font=('Century Gothic', 11)).place(x=10, y=2)
                         
                         Label(window3, text="Name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=60)
                         Label(window3, text="Gender",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=60)
                         Label(window3, text="Depart at",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=100)
                         Label(window3, text="Age",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=100)
                         Label(window3, text="Class",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=140)
                         Label(window3, text="Train no.",bg='gray16',fg='orange',font=('Century Gothic', 11)).place(x=40, y=140)
                         Label(window3, text="Train name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=180)
                         Label(window3, text="Source",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=220)
                         Label(window3, text="Destination",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=220)
                         # Label(window3, text="No. of tickets",bg='white', font=('Slab Serif', 11)).place(x=60, y=290)

                         Label(window3, text="PNR No.",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=180)

                         # Number = Label(window3, justify="center",bg='white',text=count, font=('Slab Serif', 10))
                         # Number.place(x=170, y=290,  height=25)

                         Name = Label(window3, justify="center",fg='white',bg='gray16',text=enn7.get(), font=('Century Gothic', 10))
                         Name.place(x=150, y=60, height=25)
                         DepartTime = Label(window3, justify="center",fg='white',bg='gray16',text=xdprtTime, font=('Century Gothic', 10))
                         DepartTime.place(x=150, y=100, height=25)
                         TrainName = Label(window3, justify="center",fg='white',bg='gray16',text=xtrainn, font=('Century Gothic', 10))
                         TrainName.place(x=150, y=180, height=25)
                         Age = Label(window3, justify="center",fg='white',bg='gray16',text=enn8.get(), font=('Century Gothic', 10))
                         Age.place(x=430, y=100, height=25)
                         Class = Label(window3, justify="center",fg='white',bg='gray16',text=variable2.get(), font=('Century Gothic', 10))
                         Class.place(x=430, y=140, height=25)
                         Depart = Label(window3, justify="center",fg='white',bg='gray16',text=variable.get(), font=('Century Gothic', 10))
                         Depart.place(x=150, y=220, height=25)
                         Arrive = Label(window3, justify="center",fg='white',bg='gray16',text=variable1.get(), font=('Century Gothic', 10))
                         Arrive.place(x=430, y=220, height=25)
                         Gender = Label(window3, justify="center",fg='white',bg='gray16',text=v2.get(), font=('Century Gothic', 10))
                         Gender.place(x=430, y=60, height=25)
                         TrainNumber = Label(window3, justify="center",fg='white',bg='gray16',text=x1, font=('Century Gothic', 10))
                         TrainNumber.place(x=150, y=140, height=25)
                         
                         a=111111
                         b=999999
                         pnr=(random.randint(a, b))
                         Numberpnr=Label(window3, justify="center",fg='white',bg='gray16',text=pnr, font=('Century Gothic', 10))
                         Numberpnr.place(x=430, y=180, height=25) 


                         #global conn, cursor, x2
                         # passenger_data=[("pnr","enn7.get()","enn9.get()", "enn8.get()","x1")]
                        
                         # passenger_data=[(pnr,enn7.get(),enn9.get(), enn8.get(),x1)]
                         # c.execute("CREATE TABLE rail1 (passen_pnr integer, passen_name text, passen_gender text,passen_age integer,train_number integer)")
                         print("Command executed successfully...")
                         #insertion
                         #c.execute("INSERT INTO rail VALUES(pnr, enn7.get(),enn8.get(), str(enn9.get()
                         c.execute("INSERT INTO rail1 VALUES (?,?,?,?,?)",(pnr,enn7.get(),enn9.get(), enn8.get(),x1))
                         print("Command inserted successfully...")
                         # c.execute("SELECT*FROM rail")
                         c.execute("SELECT rowid,* FROM rail1")
                         print("Command selected successfully...")
                         items=c.fetchall()

                         print("S.No." + "\tPNR"+ "\tTrain No." +"   \tGender"+ "\tAge"+ "\tName")
                         print("-----" + "\t---"+ "\t---------" +"   \t------"+ "\t---"+ "\t----")
                         for item in items:
                             print(item[0] ,"    ",item[1] ," ",item[5],"   \t",item[3] ," ", item[4],"\t", item[2])
                         

                         # for item in items:
                         #     print(item)
                         print("Command fetched successfully...")    
                        


                         Label(window3, text="Have a nice trip!!",fg='white',bg='gray16', font=('Century Gothic', 17)).place(x=200, y=340)

                         mainloop()

                        elif e12.get()!="" and e17.get()=="":
                         
                         count=1
                         window3 = Tk()

                         window3.title("Ticket")
                         screen_width = window3.winfo_screenwidth()
                         screen_height = window3.winfo_screenheight()
                         width = 1160
                         height = 480
                         x = (screen_width / 2) - (width / 2)
                         y = (screen_height / 2) - (height / 2)
                         window3.geometry('%dx%d+%d+%d' % (width, height, x, y))
                         window3.resizable(0, 0)
                         window3.config(bg='gray16')

                         w11 = 1160
                         h11 = 480
                         canvas3 = Canvas(window3, width=w11, height=h11)
                         canvas3.config(bg='gray16')
                         canvas3.create_rectangle(0, 0,1160,30, fill= "orange")
                         canvas3.create_line(40, 90, 270, 90, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 130, 270, 130, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 170, 270, 170, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 210, 270, 210, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 250, 270, 250, fill="gray13", width=0.0000001)

                         canvas3.create_line(320, 90, 550, 90, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 130, 550, 130, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 170, 550, 170, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 210, 550, 210, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 250, 550, 250, fill="gray13", width=0.0000001)

                         canvas3.create_line(560, 90, 790, 90, fill="gray13", width=0.0000001)
                         canvas3.create_line(560, 130, 790, 130, fill="gray13", width=0.0000001)
                         canvas3.create_line(560, 170, 790, 170, fill="gray13", width=0.0000001)
                         canvas3.create_line(560, 210, 790, 210, fill="gray13", width=0.0000001)
                         canvas3.create_line(560, 250, 790, 250, fill="gray13", width=0.0000001)

                         canvas3.create_line(840, 90, 1070, 90, fill="gray13", width=0.0000001)
                         canvas3.create_line(840, 130, 1070, 130, fill="gray13", width=0.0000001)
                         canvas3.create_line(840, 170, 1070, 170, fill="gray13", width=0.0000001)
                         canvas3.create_line(840, 210, 1070, 210, fill="gray13", width=0.0000001)
                         canvas3.create_line(840, 250, 1070, 250, fill="gray13", width=0.0000001)
                         canvas3.pack()
                         Label(window3, text="PNR Status Details",bg='orange',fg='gray16', font=('Century Gothic', 11)).place(x=10, y=2)
                         
                         Label(window3, text="Name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=60)
                         Label(window3, text="Gender",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=60)
                         Label(window3, text="Depart at",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=100)
                         Label(window3, text="Age",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=100)
                         Label(window3, text="Class",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=140)
                         Label(window3, text="Train no.",bg='gray16',fg='orange',font=('Century Gothic', 11)).place(x=40, y=140)
                         Label(window3, text="Train name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=180)
                         Label(window3, text="Source",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=220)
                         Label(window3, text="Destination",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=220)
                         # Label(window3, text="No. of tickets",bg='white', font=('Slab Serif', 11)).place(x=60, y=290)

                         Label(window3, text="PNR No.",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=180)

                         # Number = Label(window3, justify="center",bg='white',text=count, font=('Slab Serif', 10))
                         # Number.place(x=170, y=290,  height=25)

                         Name = Label(window3, justify="center",fg='white',bg='gray16',text=enn7.get(), font=('Century Gothic', 10))
                         Name.place(x=150, y=60, height=25)
                         DepartTime = Label(window3, justify="center",fg='white',bg='gray16',text=xdprtTime, font=('Century Gothic', 10))
                         DepartTime.place(x=150, y=100, height=25)
                         TrainName = Label(window3, justify="center",fg='white',bg='gray16',text=xtrainn, font=('Century Gothic', 10))
                         TrainName.place(x=150, y=180, height=25)
                         Age = Label(window3, justify="center",fg='white',bg='gray16',text=enn8.get(), font=('Century Gothic', 10))
                         Age.place(x=430, y=100, height=25)
                         Class = Label(window3, justify="center",fg='white',bg='gray16',text=variable2.get(), font=('Century Gothic', 10))
                         Class.place(x=430, y=140, height=25)
                         Depart = Label(window3, justify="center",fg='white',bg='gray16',text=variable.get(), font=('Century Gothic', 10))
                         Depart.place(x=150, y=220, height=25)
                         Arrive = Label(window3, justify="center",fg='white',bg='gray16',text=variable1.get(), font=('Century Gothic', 10))
                         Arrive.place(x=430, y=220, height=25)
                         Gender = Label(window3, justify="center",fg='white',bg='gray16',text=v2.get(), font=('Century Gothic', 10))
                         Gender.place(x=430, y=60, height=25)
                         TrainNumber = Label(window3, justify="center",fg='white',bg='gray16',text=x1, font=('Century Gothic', 10))
                         TrainNumber.place(x=150, y=140, height=25)
                         
                         a=111111
                         b=999999
                         pnr=(random.randint(a, b))
                         Numberpnr=Label(window3, justify="center",fg='white',bg='gray16',text=pnr, font=('Century Gothic', 10))
                         Numberpnr.place(x=430, y=180, height=25) 


                         #global conn, cursor, x2
                         # passenger_data=[("pnr","enn7.get()","enn9.get()", "enn8.get()","x1")]
                        
                         # passenger_data=[(pnr,enn7.get(),enn9.get(), enn8.get(),x1)]
                         # c.execute("CREATE TABLE rail1 (passen_pnr integer, passen_name text, passen_gender text,passen_age integer,train_number integer)")
                         print("Command executed successfully...")
                         #insertion
                         #c.execute("INSERT INTO rail VALUES(pnr, enn7.get(),enn8.get(), str(enn9.get()
                         c.execute("INSERT INTO rail1 VALUES (?,?,?,?,?)",(pnr,enn7.get(),enn9.get(), enn8.get(),x1))
                         print("Command inserted successfully...")
                         # c.execute("SELECT*FROM rail")
                         c.execute("SELECT rowid,* FROM rail1")
                         print("Command selected successfully...")
                         items=c.fetchall()

                         print("S.No." + "\tPNR"+ "\tTrain No." +"   \tGender"+ "  \tAge"+ "\tName")
                         print("-----" + "\t---"+ "\t---------" +"   \t------"+ "  \t---"+ "\t----")
                         for item in items:
                             print(item[0] ,"    ",item[1] ," ",item[5],"   \t",item[3] ,"   ", item[4],"\t", item[2])
                         

                         # for item in items:
                         #     print(item)
                         print("Command fetched successfully...")    
                         
                         #-------------------------------------------------------------------  
                         
                         Label(window3, text="Name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=560, y=60)
                         Label(window3, text="Gender",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=60)
                         Label(window3, text="Depart at",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=560, y=100)
                         Label(window3, text="Age",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=100)
                         Label(window3, text="Class",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=140)
                         Label(window3, text="Train no.",bg='gray16',fg='orange',font=('Century Gothic', 11)).place(x=560, y=140)
                         Label(window3, text="Train name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=560, y=180)
                         Label(window3, text="Source",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=560, y=220)
                         Label(window3, text="Destination",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=220)
                         # Label(window3, text="No. of tickets",bg='white', font=('Slab Serif', 11)).place(x=60, y=290)

                         Label(window3, text="PNR No.",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=180)

                         # Number = Label(window3, justify="center",bg='white',text=count, font=('Slab Serif', 10))
                         # Number.place(x=170, y=290,  height=25)

                         Name = Label(window3, justify="center",fg='white',bg='gray16',text=e12.get(), font=('Century Gothic', 10))
                         Name.place(x=670, y=60, height=25)
                         DepartTime = Label(window3, justify="center",fg='white',bg='gray16',text=xdprtTime, font=('Century Gothic', 10))
                         DepartTime.place(x=670, y=100, height=25)
                         TrainName = Label(window3, justify="center",fg='white',bg='gray16',text=xtrainn, font=('Century Gothic', 10))
                         TrainName.place(x=670, y=180, height=25)
                         Age = Label(window3, justify="center",fg='white',bg='gray16',text=e13.get(), font=('Century Gothic', 10))
                         Age.place(x=950, y=100, height=25)
                         Class = Label(window3, justify="center",fg='white',bg='gray16',text=variable2.get(), font=('Century Gothic', 10))
                         Class.place(x=950, y=140, height=25)
                         Depart = Label(window3, justify="center",fg='white',bg='gray16',text=variable.get(), font=('Century Gothic', 10))
                         Depart.place(x=670, y=220, height=25)
                         Arrive = Label(window3, justify="center",fg='white',bg='gray16',text=variable1.get(), font=('Century Gothic', 10))
                         Arrive.place(x=950, y=220, height=25)
                         Gender = Label(window3, justify="center",fg='white',bg='gray16',text=e14.get(), font=('Century Gothic', 10))
                         Gender.place(x=950, y=60, height=25)
                         TrainNumber = Label(window3, justify="center",fg='white',bg='gray16',text=x1, font=('Century Gothic', 10))
                         TrainNumber.place(x=670, y=140, height=25)
                         
                         a=111111
                         b=999999
                         pnr2=(random.randint(a, b))
                         Numberpnr=Label(window3, justify="center",fg='white',bg='gray16',text=pnr2, font=('Century Gothic', 10))
                         Numberpnr.place(x=950, y=180, height=25) 


                         #global conn, cursor, x2
                         # passenger_data=[("pnr","enn7.get()","enn9.get()", "enn8.get()","x1")]
                        
                         # passenger_data=[(pnr,enn7.get(),enn9.get(), enn8.get(),x1)]
                         # c.execute("CREATE TABLE rail1 (passen_pnr integer, passen_name text, passen_gender text,passen_age integer,train_number integer)")
                         print("Command executed successfully...")
                         #insertion
                         #c.execute("INSERT INTO rail VALUES(pnr, enn7.get(),enn8.get(), str(enn9.get()
                         c.execute("INSERT INTO rail1 VALUES (?,?,?,?,?)",(pnr2,e12.get(),e14.get(), e13.get(),x1))
                         print("Command inserted successfully...")
                         # c.execute("SELECT*FROM rail")
                         c.execute("SELECT rowid,* FROM rail1")
                         print("Command selected successfully...")
                         items=c.fetchall()

                         print("S.No." + "\tPNR"+ "\tTrain No." +"   \tGender"+ "  \tAge"+ "\tName")
                         print("-----" + "\t---"+ "\t---------" +"   \t------"+ "  \t---"+ "\t----")
                         for item in items:
                             print(item[0] ,"    ",item[1] ," ",item[5],"   \t",item[3] ,"   ", item[4],"\t", item[2])
                         

                         # for item in items:
                         #     print(item)
                         print("Command fetched successfully...")     
                        


                         Label(window3, text="Have a nice trip!!",fg='white',bg='gray16', font=('Century Gothic', 17)).place(x=500, y=340)

                         mainloop()
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                        elif e17.get()!="" and e22.get()=="":
                         count=3
                         window3 = Tk()

                         window3.title("Ticket")
                         screen_width = window3.winfo_screenwidth()
                         screen_height = window3.winfo_screenheight()
                         width = 1160
                         height = 800
                         x = (screen_width / 2) - (width / 2)
                         y = (screen_height / 2) - (height / 2)
                         window3.geometry('%dx%d+%d+%d' % (width, height, x, y))
                         window3.resizable(0, 0)
                         window3.config(bg='gray16')

                         w11 = 1160
                         h11 = 800
                         canvas3 = Canvas(window3, width=w11, height=h11)
                         canvas3.config(bg='gray16')
                         canvas3.create_rectangle(0, 0,1160,30, fill= "orange")
                         canvas3.create_line(40, 90, 270, 90, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 130, 270, 130, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 170, 270, 170, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 210, 270, 210, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 250, 270, 250, fill="gray13", width=0.0000001)

                         canvas3.create_line(320, 90, 550, 90, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 130, 550, 130, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 170, 550, 170, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 210, 550, 210, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 250, 550, 250, fill="gray13", width=0.0000001)

                         canvas3.create_line(560, 90, 790, 90, fill="gray13", width=0.0000001)
                         canvas3.create_line(560, 130, 790, 130, fill="gray13", width=0.0000001)
                         canvas3.create_line(560, 170, 790, 170, fill="gray13", width=0.0000001)
                         canvas3.create_line(560, 210, 790, 210, fill="gray13", width=0.0000001)
                         canvas3.create_line(560, 250, 790, 250, fill="gray13", width=0.0000001)

                         canvas3.create_line(840, 90, 1070, 90, fill="gray13", width=0.0000001)
                         canvas3.create_line(840, 130, 1070, 130, fill="gray13", width=0.0000001)
                         canvas3.create_line(840, 170, 1070, 170, fill="gray13", width=0.0000001)
                         canvas3.create_line(840, 210, 1070, 210, fill="gray13", width=0.0000001)
                         canvas3.create_line(840, 250, 1070, 250, fill="gray13", width=0.0000001)

                         canvas3.create_line(40, 390, 270, 390, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 430, 270, 430, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 470, 270, 470, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 510, 270, 510, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 550, 270, 550, fill="gray13", width=0.0000001)

                         canvas3.create_line(320, 390, 550, 390, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 430, 550, 430, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 470, 550, 470, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 510, 550, 510, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 550, 550, 550, fill="gray13", width=0.0000001)
                         canvas3.pack()
                         Label(window3, text="PNR Status Details",bg='orange',fg='gray16', font=('Century Gothic', 11)).place(x=10, y=2)
                         
                         Label(window3, text="Name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=60)
                         Label(window3, text="Gender",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=60)
                         Label(window3, text="Depart at",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=100)
                         Label(window3, text="Age",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=100)
                         Label(window3, text="Class",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=140)
                         Label(window3, text="Train no.",bg='gray16',fg='orange',font=('Century Gothic', 11)).place(x=40, y=140)
                         Label(window3, text="Train name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=180)
                         Label(window3, text="Source",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=220)
                         Label(window3, text="Destination",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=220)
                         # Label(window3, text="No. of tickets",bg='white', font=('Slab Serif', 11)).place(x=60, y=290)

                         Label(window3, text="PNR No.",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=180)

                         # Number = Label(window3, justify="center",bg='white',text=count, font=('Slab Serif', 10))
                         # Number.place(x=170, y=290,  height=25)

                         Name = Label(window3, justify="center",fg='white',bg='gray16',text=enn7.get(), font=('Century Gothic', 10))
                         Name.place(x=150, y=60, height=25)
                         DepartTime = Label(window3, justify="center",fg='white',bg='gray16',text=xdprtTime, font=('Century Gothic', 10))
                         DepartTime.place(x=150, y=100, height=25)
                         TrainName = Label(window3, justify="center",fg='white',bg='gray16',text=xtrainn, font=('Century Gothic', 10))
                         TrainName.place(x=150, y=180, height=25)
                         Age = Label(window3, justify="center",fg='white',bg='gray16',text=enn8.get(), font=('Century Gothic', 10))
                         Age.place(x=430, y=100, height=25)
                         Class = Label(window3, justify="center",fg='white',bg='gray16',text=variable2.get(), font=('Century Gothic', 10))
                         Class.place(x=430, y=140, height=25)
                         Depart = Label(window3, justify="center",fg='white',bg='gray16',text=variable.get(), font=('Century Gothic', 10))
                         Depart.place(x=150, y=220, height=25)
                         Arrive = Label(window3, justify="center",fg='white',bg='gray16',text=variable1.get(), font=('Century Gothic', 10))
                         Arrive.place(x=430, y=220, height=25)
                         Gender = Label(window3, justify="center",fg='white',bg='gray16',text=v2.get(), font=('Century Gothic', 10))
                         Gender.place(x=430, y=60, height=25)
                         TrainNumber = Label(window3, justify="center",fg='white',bg='gray16',text=x1, font=('Century Gothic', 10))
                         TrainNumber.place(x=150, y=140, height=25)
                         
                         a=111111
                         b=999999
                         pnr=(random.randint(a, b))
                         Numberpnr=Label(window3, justify="center",fg='white',bg='gray16',text=pnr, font=('Century Gothic', 10))
                         Numberpnr.place(x=430, y=180, height=25) 


                         #global conn, cursor, x2
                         # passenger_data=[("pnr","enn7.get()","enn9.get()", "enn8.get()","x1")]
                        
                         # passenger_data=[(pnr,enn7.get(),enn9.get(), enn8.get(),x1)]
                         # c.execute("CREATE TABLE rail1 (passen_pnr integer, passen_name text, passen_gender text,passen_age integer,train_number integer)")
                         print("Command executed successfully...")
                         #insertion
                         #c.execute("INSERT INTO rail VALUES(pnr, enn7.get(),enn8.get(), str(enn9.get()
                         c.execute("INSERT INTO rail1 VALUES (?,?,?,?,?)",(pnr,enn7.get(),enn9.get(), enn8.get(),x1))
                         print("Command inserted successfully...")
                         # c.execute("SELECT*FROM rail")
                         c.execute("SELECT rowid,* FROM rail1")
                         print("Command selected successfully...")
                         items=c.fetchall()

                         print("S.No." + "\tPNR"+ "\tTrain No." +"   \tGender"+ "\tAge"+ "    \tName")
                         print("-----" + "\t---"+ "\t---------" +"   \t------"+ "\t---"+ "    \t----")
                         for item in items:
                             print(item[0] ,"    ",item[1] ," ",item[5],"   \t",item[3] ," ", item[4],"    \t", item[2])
                         

                         # for item in items:
                         #     print(item)
                         print("Command fetched successfully...")    
                         
                         #-------------------------------------------------------------------  
                         
                         Label(window3, text="Name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=560, y=60)
                         Label(window3, text="Gender",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=60)
                         Label(window3, text="Depart at",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=560, y=100)
                         Label(window3, text="Age",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=100)
                         Label(window3, text="Class",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=140)
                         Label(window3, text="Train no.",bg='gray16',fg='orange',font=('Century Gothic', 11)).place(x=560, y=140)
                         Label(window3, text="Train name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=560, y=180)
                         Label(window3, text="Source",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=560, y=220)
                         Label(window3, text="Destination",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=220)
                         # Label(window3, text="No. of tickets",bg='white', font=('Slab Serif', 11)).place(x=60, y=290)

                         Label(window3, text="PNR No.",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=180)

                         # Number = Label(window3, justify="center",bg='white',text=count, font=('Slab Serif', 10))
                         # Number.place(x=170, y=290,  height=25)

                         Name = Label(window3, justify="center",fg='white',bg='gray16',text=e12.get(), font=('Century Gothic', 10))
                         Name.place(x=670, y=60, height=25)
                         DepartTime = Label(window3, justify="center",fg='white',bg='gray16',text=xdprtTime, font=('Century Gothic', 10))
                         DepartTime.place(x=670, y=100, height=25)
                         TrainName = Label(window3, justify="center",fg='white',bg='gray16',text=xtrainn, font=('Century Gothic', 10))
                         TrainName.place(x=670, y=180, height=25)
                         Age = Label(window3, justify="center",fg='white',bg='gray16',text=e13.get(), font=('Century Gothic', 10))
                         Age.place(x=950, y=100, height=25)
                         Class = Label(window3, justify="center",fg='white',bg='gray16',text=variable2.get(), font=('Century Gothic', 10))
                         Class.place(x=950, y=140, height=25)
                         Depart = Label(window3, justify="center",fg='white',bg='gray16',text=variable.get(), font=('Century Gothic', 10))
                         Depart.place(x=670, y=220, height=25)
                         Arrive = Label(window3, justify="center",fg='white',bg='gray16',text=variable1.get(), font=('Century Gothic', 10))
                         Arrive.place(x=950, y=220, height=25)
                         Gender = Label(window3, justify="center",fg='white',bg='gray16',text=e14.get(), font=('Century Gothic', 10))
                         Gender.place(x=950, y=60, height=25)
                         TrainNumber = Label(window3, justify="center",fg='white',bg='gray16',text=x1, font=('Century Gothic', 10))
                         TrainNumber.place(x=670, y=140, height=25)
                         
                         a=111111
                         b=999999
                         pnr2=(random.randint(a, b))
                         Numberpnr=Label(window3, justify="center",fg='white',bg='gray16',text=pnr2, font=('Century Gothic', 10))
                         Numberpnr.place(x=950, y=180, height=25) 


                         #global conn, cursor, x2
                         # passenger_data=[("pnr","enn7.get()","enn9.get()", "enn8.get()","x1")]
                        
                         # passenger_data=[(pnr,enn7.get(),enn9.get(), enn8.get(),x1)]
                         # c.execute("CREATE TABLE rail1 (passen_pnr integer, passen_name text, passen_gender text,passen_age integer,train_number integer)")
                         print("Command executed successfully...")
                         #insertion
                         #c.execute("INSERT INTO rail VALUES(pnr, enn7.get(),enn8.get(), str(enn9.get()
                         c.execute("INSERT INTO rail1 VALUES (?,?,?,?,?)",(pnr2,e12.get(),e14.get(), e13.get(),x1))
                         print("Command inserted successfully...")
                         # c.execute("SELECT*FROM rail")
                         c.execute("SELECT rowid,* FROM rail1")
                         print("Command selected successfully...")
                         items=c.fetchall()

                         print("S.No." + "\tPNR"+ "\tTrain No." +"   \tGender"+ "\tAge"+ "    \tName")
                         print("-----" + "\t---"+ "\t---------" +"   \t------"+ "\t---"+ "    \t----")
                         for item in items:
                             print(item[0] ,"    ",item[1] ," ",item[5],"   \t",item[3] ," ", item[4],"    \t", item[2])
                         

                         # for item in items:
                         #     print(item)
                         print("Command fetched successfully...")   

                            #  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                         Label(window3, text="Name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=360)
                         Label(window3, text="Gender",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=360)
                         Label(window3, text="Depart at",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=400)
                         Label(window3, text="Age",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=400)
                         Label(window3, text="Class",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=440)
                         Label(window3, text="Train no.",bg='gray16',fg='orange',font=('Century Gothic', 11)).place(x=40, y=440)
                         Label(window3, text="Train name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=480)
                         Label(window3, text="Source",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=520)
                         Label(window3, text="Destination",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=520)
                         # Label(window3, text="No. of tickets",bg='white', font=('Slab Serif', 11)).place(x=60, y=290)

                         Label(window3, text="PNR No.",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=480)

                         # Number = Label(window3, justify="center",bg='white',text=count, font=('Slab Serif', 10))
                         # Number.place(x=170, y=290,  height=25)

                         Name = Label(window3, justify="center",fg='white',bg='gray16',text=e17.get(), font=('Century Gothic', 10))
                         Name.place(x=150, y=360, height=25)
                         DepartTime = Label(window3, justify="center",fg='white',bg='gray16',text=xdprtTime, font=('Century Gothic', 10))
                         DepartTime.place(x=150, y=400, height=25)
                         TrainName = Label(window3, justify="center",fg='white',bg='gray16',text=xtrainn, font=('Century Gothic', 10))
                         TrainName.place(x=150, y=480, height=25)
                         Age = Label(window3, justify="center",fg='white',bg='gray16',text=e18.get(), font=('Century Gothic', 10))
                         Age.place(x=430, y=400, height=25)
                         Class = Label(window3, justify="center",fg='white',bg='gray16',text=variable2.get(), font=('Century Gothic', 10))
                         Class.place(x=430, y=440, height=25)
                         Depart = Label(window3, justify="center",fg='white',bg='gray16',text=variable.get(), font=('Century Gothic', 10))
                         Depart.place(x=150, y=520, height=25)
                         Arrive = Label(window3, justify="center",fg='white',bg='gray16',text=variable1.get(), font=('Century Gothic', 10))
                         Arrive.place(x=430, y=520, height=25)
                         Gender = Label(window3, justify="center",fg='white',bg='gray16',text=e19.get(), font=('Century Gothic', 10))
                         Gender.place(x=430, y=360, height=25)
                         TrainNumber = Label(window3, justify="center",fg='white',bg='gray16',text=x1, font=('Century Gothic', 10))
                         TrainNumber.place(x=150, y=440, height=25)
                         
                         a=111111
                         b=999999
                         pnr3=(random.randint(a, b))
                         Numberpnr=Label(window3, justify="center",fg='white',bg='gray16',text=pnr3, font=('Century Gothic', 10))
                         Numberpnr.place(x=430, y=480, height=25) 


                         #global conn, cursor, x2
                         # passenger_data=[("pnr","enn7.get()","enn9.get()", "enn8.get()","x1")]
                        
                         # passenger_data=[(pnr,enn7.get(),enn9.get(), enn8.get(),x1)]
                         # c.execute("CREATE TABLE rail1 (passen_pnr integer, passen_name text, passen_gender text,passen_age integer,train_number integer)")
                         print("Command executed successfully...")
                         #insertion
                         #c.execute("INSERT INTO rail VALUES(pnr, enn7.get(),enn8.get(), str(enn9.get()
                         c.execute("INSERT INTO rail1 VALUES (?,?,?,?,?)",(pnr3,e17.get(),e19.get(), e18.get(),x1))
                         print("Command inserted successfully...")
                         # c.execute("SELECT*FROM rail")
                         c.execute("SELECT rowid,* FROM rail1")
                         print("Command selected successfully...")
                         items=c.fetchall()

                         print("S.No." + "\tPNR"+ "\tTrain No." +"   \tGender"+ "\tAge"+ "    \tName")
                         print("-----" + "\t---"+ "\t---------" +"   \t------"+ "\t---"+ "    \t----")
                         for item in items:
                             print(item[0] ,"    ",item[1] ," ",item[5],"   \t",item[3] ," ", item[4],"    \t", item[2])
                         

                         # for item in items:
                         #     print(item)
                         print("Command fetched successfully...")  

                        


                         Label(window3, text="Have a nice trip!!",fg='white',bg='gray16', font=('Century Gothic', 17)).place(x=800, y=340)

                         mainloop()
                        else:
                         count=4
                         window3 = Tk()

                         window3.title("Ticket")
                         screen_width = window3.winfo_screenwidth()
                         screen_height = window3.winfo_screenheight()
                         width = 1160
                         height = 800
                         x = (screen_width / 2) - (width / 2)
                         y = (screen_height / 2) - (height / 2)
                         window3.geometry('%dx%d+%d+%d' % (width, height, x, y))
                         window3.resizable(0, 0)
                         window3.config(bg='gray16')

                         w11 = 1160
                         h11 = 800
                         canvas3 = Canvas(window3, width=w11, height=h11)
                         canvas3.config(bg='gray16')
                         canvas3.create_rectangle(0, 0,1160,30, fill= "orange")
                         canvas3.create_line(40, 90, 270, 90, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 130, 270, 130, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 170, 270, 170, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 210, 270, 210, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 250, 270, 250, fill="gray13", width=0.0000001)

                         canvas3.create_line(320, 90, 550, 90, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 130, 550, 130, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 170, 550, 170, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 210, 550, 210, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 250, 550, 250, fill="gray13", width=0.0000001)

                         canvas3.create_line(560, 90, 790, 90, fill="gray13", width=0.0000001)
                         canvas3.create_line(560, 130, 790, 130, fill="gray13", width=0.0000001)
                         canvas3.create_line(560, 170, 790, 170, fill="gray13", width=0.0000001)
                         canvas3.create_line(560, 210, 790, 210, fill="gray13", width=0.0000001)
                         canvas3.create_line(560, 250, 790, 250, fill="gray13", width=0.0000001)

                         canvas3.create_line(840, 90, 1070, 90, fill="gray13", width=0.0000001)
                         canvas3.create_line(840, 130, 1070, 130, fill="gray13", width=0.0000001)
                         canvas3.create_line(840, 170, 1070, 170, fill="gray13", width=0.0000001)
                         canvas3.create_line(840, 210, 1070, 210, fill="gray13", width=0.0000001)
                         canvas3.create_line(840, 250, 1070, 250, fill="gray13", width=0.0000001)

                         canvas3.create_line(40, 390, 270, 390, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 430, 270, 430, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 470, 270, 470, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 510, 270, 510, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 550, 270, 550, fill="gray13", width=0.0000001)

                         canvas3.create_line(320, 390, 550, 390, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 430, 550, 430, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 470, 550, 470, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 510, 550, 510, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 550, 550, 550, fill="gray13", width=0.0000001)

                         canvas3.create_line(560, 390, 790, 390, fill="gray13", width=0.0000001)
                         canvas3.create_line(560, 430, 790, 430, fill="gray13", width=0.0000001)
                         canvas3.create_line(560, 470, 790, 470, fill="gray13", width=0.0000001)
                         canvas3.create_line(560, 510, 790, 510, fill="gray13", width=0.0000001)
                         canvas3.create_line(560, 550, 790, 550, fill="gray13", width=0.0000001)

                         canvas3.create_line(840, 390, 1070, 390, fill="gray13", width=0.0000001)
                         canvas3.create_line(840, 430, 1070, 430, fill="gray13", width=0.0000001)
                         canvas3.create_line(840, 470, 1070, 470, fill="gray13", width=0.0000001)
                         canvas3.create_line(840, 510, 1070, 510, fill="gray13", width=0.0000001)
                         canvas3.create_line(840, 550, 1070, 550, fill="gray13", width=0.0000001)
                         canvas3.pack()
                         Label(window3, text="PNR Status Details",bg='orange',fg='gray16', font=('Century Gothic', 11)).place(x=10, y=2)
                         
                         Label(window3, text="Name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=60)
                         Label(window3, text="Gender",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=60)
                         Label(window3, text="Depart at",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=100)
                         Label(window3, text="Age",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=100)
                         Label(window3, text="Class",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=140)
                         Label(window3, text="Train no.",bg='gray16',fg='orange',font=('Century Gothic', 11)).place(x=40, y=140)
                         Label(window3, text="Train name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=180)
                         Label(window3, text="Source",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=220)
                         Label(window3, text="Destination",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=220)
                         # Label(window3, text="No. of tickets",bg='white', font=('Slab Serif', 11)).place(x=60, y=290)

                         Label(window3, text="PNR No.",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=180)

                         # Number = Label(window3, justify="center",bg='white',text=count, font=('Slab Serif', 10))
                         # Number.place(x=170, y=290,  height=25)

                         Name = Label(window3, justify="center",fg='white',bg='gray16',text=enn7.get(), font=('Century Gothic', 10))
                         Name.place(x=150, y=60, height=25)
                         DepartTime = Label(window3, justify="center",fg='white',bg='gray16',text=xdprtTime, font=('Century Gothic', 10))
                         DepartTime.place(x=150, y=100, height=25)
                         TrainName = Label(window3, justify="center",fg='white',bg='gray16',text=xtrainn, font=('Century Gothic', 10))
                         TrainName.place(x=150, y=180, height=25)
                         Age = Label(window3, justify="center",fg='white',bg='gray16',text=enn8.get(), font=('Century Gothic', 10))
                         Age.place(x=430, y=100, height=25)
                         Class = Label(window3, justify="center",fg='white',bg='gray16',text=variable2.get(), font=('Century Gothic', 10))
                         Class.place(x=430, y=140, height=25)
                         Depart = Label(window3, justify="center",fg='white',bg='gray16',text=variable.get(), font=('Century Gothic', 10))
                         Depart.place(x=150, y=220, height=25)
                         Arrive = Label(window3, justify="center",fg='white',bg='gray16',text=variable1.get(), font=('Century Gothic', 10))
                         Arrive.place(x=430, y=220, height=25)
                         Gender = Label(window3, justify="center",fg='white',bg='gray16',text=v2.get(), font=('Century Gothic', 10))
                         Gender.place(x=430, y=60, height=25)
                         TrainNumber = Label(window3, justify="center",fg='white',bg='gray16',text=x1, font=('Century Gothic', 10))
                         TrainNumber.place(x=150, y=140, height=25)
                         
                         a=111111
                         b=999999
                         pnr=(random.randint(a, b))
                         Numberpnr=Label(window3, justify="center",fg='white',bg='gray16',text=pnr, font=('Century Gothic', 10))
                         Numberpnr.place(x=430, y=180, height=25) 


                         #global conn, cursor, x2
                         # passenger_data=[("pnr","enn7.get()","enn9.get()", "enn8.get()","x1")]
                        
                         # passenger_data=[(pnr,enn7.get(),enn9.get(), enn8.get(),x1)]
                         # c.execute("CREATE TABLE rail1 (passen_pnr integer, passen_name text, passen_gender text,passen_age integer,train_number integer)")
                         print("Command executed successfully...")
                         #insertion
                         #c.execute("INSERT INTO rail VALUES(pnr, enn7.get(),enn8.get(), str(enn9.get()
                         c.execute("INSERT INTO rail1 VALUES (?,?,?,?,?)",(pnr,enn7.get(),enn9.get(), enn8.get(),x1))
                         print("Command inserted successfully...")
                         # c.execute("SELECT*FROM rail")
                         c.execute("SELECT rowid,* FROM rail1")
                         print("Command selected successfully...")
                         items=c.fetchall()

                        #  print("S.No." + "\tPNR"+ "\tTrain No." +"   \tGender"+ "\tAge"+ "    \tName")
                        #  print("-----" + "\t---"+ "\t---------" +"   \t------"+ "\t---"+ "    \t----")
                        #  for item in items:
                        #      print(item[0] ,"    ",item[1] ," ",item[5],"   \t",item[3] ," ", item[4],"    \t", item[2])
                         

                         # for item in items:
                         #     print(item)
                         print("Command fetched successfully...")    
                         
                         #-------------------------------------------------------------------  
                         
                         Label(window3, text="Name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=560, y=60)
                         Label(window3, text="Gender",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=60)
                         Label(window3, text="Depart at",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=560, y=100)
                         Label(window3, text="Age",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=100)
                         Label(window3, text="Class",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=140)
                         Label(window3, text="Train no.",bg='gray16',fg='orange',font=('Century Gothic', 11)).place(x=560, y=140)
                         Label(window3, text="Train name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=560, y=180)
                         Label(window3, text="Source",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=560, y=220)
                         Label(window3, text="Destination",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=220)
                         # Label(window3, text="No. of tickets",bg='white', font=('Slab Serif', 11)).place(x=60, y=290)

                         Label(window3, text="PNR No.",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=180)

                         # Number = Label(window3, justify="center",bg='white',text=count, font=('Slab Serif', 10))
                         # Number.place(x=170, y=290,  height=25)

                         Name = Label(window3, justify="center",fg='white',bg='gray16',text=e12.get(), font=('Century Gothic', 10))
                         Name.place(x=670, y=60, height=25)
                         DepartTime = Label(window3, justify="center",fg='white',bg='gray16',text=xdprtTime, font=('Century Gothic', 10))
                         DepartTime.place(x=670, y=100, height=25)
                         TrainName = Label(window3, justify="center",fg='white',bg='gray16',text=xtrainn, font=('Century Gothic', 10))
                         TrainName.place(x=670, y=180, height=25)
                         Age = Label(window3, justify="center",fg='white',bg='gray16',text=e13.get(), font=('Century Gothic', 10))
                         Age.place(x=950, y=100, height=25)
                         Class = Label(window3, justify="center",fg='white',bg='gray16',text=variable2.get(), font=('Century Gothic', 10))
                         Class.place(x=950, y=140, height=25)
                         Depart = Label(window3, justify="center",fg='white',bg='gray16',text=variable.get(), font=('Century Gothic', 10))
                         Depart.place(x=670, y=220, height=25)
                         Arrive = Label(window3, justify="center",fg='white',bg='gray16',text=variable1.get(), font=('Century Gothic', 10))
                         Arrive.place(x=950, y=220, height=25)
                         Gender = Label(window3, justify="center",fg='white',bg='gray16',text=e14.get(), font=('Century Gothic', 10))
                         Gender.place(x=950, y=60, height=25)
                         TrainNumber = Label(window3, justify="center",fg='white',bg='gray16',text=x1, font=('Century Gothic', 10))
                         TrainNumber.place(x=670, y=140, height=25)
                         
                         a=111111
                         b=999999
                         pnr2=(random.randint(a, b))
                         Numberpnr=Label(window3, justify="center",fg='white',bg='gray16',text=pnr2, font=('Century Gothic', 10))
                         Numberpnr.place(x=950, y=180, height=25) 


                         #global conn, cursor, x2
                         # passenger_data=[("pnr","enn7.get()","enn9.get()", "enn8.get()","x1")]
                        
                         # passenger_data=[(pnr,enn7.get(),enn9.get(), enn8.get(),x1)]
                         # c.execute("CREATE TABLE rail1 (passen_pnr integer, passen_name text, passen_gender text,passen_age integer,train_number integer)")
                         print("Command executed successfully...")
                         #insertion
                         #c.execute("INSERT INTO rail VALUES(pnr, enn7.get(),enn8.get(), str(enn9.get()
                         c.execute("INSERT INTO rail1 VALUES (?,?,?,?,?)",(pnr2,e12.get(),e14.get(), e13.get(),x1))
                         print("Command inserted successfully...")
                         # c.execute("SELECT*FROM rail")
                         c.execute("SELECT rowid,* FROM rail1")
                         print("Command selected successfully...")
                         items=c.fetchall()

                        #  print("S.No." + "\tPNR"+ "\tTrain No." +"   \tGender"+ "\tAge"+ "    \tName")
                        #  print("-----" + "\t---"+ "\t---------" +"   \t------"+ "\t---"+ "    \t----")
                        #  for item in items:
                        #      print(item[0] ,"    ",item[1] ," ",item[5],"   \t",item[3] ," ", item[4],"    \t", item[2])
                         

                         # for item in items:
                         #     print(item)
                         print("Command fetched successfully...")   

                            #  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                         Label(window3, text="Name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=360)
                         Label(window3, text="Gender",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=360)
                         Label(window3, text="Depart at",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=400)
                         Label(window3, text="Age",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=400)
                         Label(window3, text="Class",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=440)
                         Label(window3, text="Train no.",bg='gray16',fg='orange',font=('Century Gothic', 11)).place(x=40, y=440)
                         Label(window3, text="Train name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=480)
                         Label(window3, text="Source",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=520)
                         Label(window3, text="Destination",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=520)
                         # Label(window3, text="No. of tickets",bg='white', font=('Slab Serif', 11)).place(x=60, y=290)

                         Label(window3, text="PNR No.",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=480)

                         # Number = Label(window3, justify="center",bg='white',text=count, font=('Slab Serif', 10))
                         # Number.place(x=170, y=290,  height=25)

                         Name = Label(window3, justify="center",fg='white',bg='gray16',text=e17.get(), font=('Century Gothic', 10))
                         Name.place(x=150, y=360, height=25)
                         DepartTime = Label(window3, justify="center",fg='white',bg='gray16',text=xdprtTime, font=('Century Gothic', 10))
                         DepartTime.place(x=150, y=400, height=25)
                         TrainName = Label(window3, justify="center",fg='white',bg='gray16',text=xtrainn, font=('Century Gothic', 10))
                         TrainName.place(x=150, y=480, height=25)
                         Age = Label(window3, justify="center",fg='white',bg='gray16',text=e18.get(), font=('Century Gothic', 10))
                         Age.place(x=430, y=400, height=25)
                         Class = Label(window3, justify="center",fg='white',bg='gray16',text=variable2.get(), font=('Century Gothic', 10))
                         Class.place(x=430, y=440, height=25)
                         Depart = Label(window3, justify="center",fg='white',bg='gray16',text=variable.get(), font=('Century Gothic', 10))
                         Depart.place(x=150, y=520, height=25)
                         Arrive = Label(window3, justify="center",fg='white',bg='gray16',text=variable1.get(), font=('Century Gothic', 10))
                         Arrive.place(x=430, y=520, height=25)
                         Gender = Label(window3, justify="center",fg='white',bg='gray16',text=e19.get(), font=('Century Gothic', 10))
                         Gender.place(x=430, y=360, height=25)
                         TrainNumber = Label(window3, justify="center",fg='white',bg='gray16',text=x1, font=('Century Gothic', 10))
                         TrainNumber.place(x=150, y=440, height=25)
                         
                         a=111111
                         b=999999
                         pnr3=(random.randint(a, b))
                         Numberpnr=Label(window3, justify="center",fg='white',bg='gray16',text=pnr3, font=('Century Gothic', 10))
                         Numberpnr.place(x=430, y=480, height=25) 


                         #global conn, cursor, x2
                         # passenger_data=[("pnr","enn7.get()","enn9.get()", "enn8.get()","x1")]
                        
                         # passenger_data=[(pnr,enn7.get(),enn9.get(), enn8.get(),x1)]
                         # c.execute("CREATE TABLE rail1 (passen_pnr integer, passen_name text, passen_gender text,passen_age integer,train_number integer)")
                         print("Command executed successfully...")
                         #insertion
                         #c.execute("INSERT INTO rail VALUES(pnr, enn7.get(),enn8.get(), str(enn9.get()
                         c.execute("INSERT INTO rail1 VALUES (?,?,?,?,?)",(pnr3,e17.get(),e19.get(), e18.get(),x1))
                         print("Command inserted successfully...")
                         # c.execute("SELECT*FROM rail")
                         c.execute("SELECT rowid,* FROM rail1")
                         print("Command selected successfully...")
                         items=c.fetchall()

                        #  print("S.No." + "\tPNR"+ "\tTrain No." +"   \tGender"+ "\tAge"+ "    \tName")
                        #  print("-----" + "\t---"+ "\t---------" +"   \t------"+ "\t---"+ "    \t----")
                        #  for item in items:
                        #      print(item[0] ,"    ",item[1] ," ",item[5],"   \t",item[3] ," ", item[4],"    \t", item[2])
                         

                         # for item in items:
                         #     print(item)
                         print("Command fetched successfully...") 

                         Label(window3, text="Name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=560, y=360)
                         Label(window3, text="Gender",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=360)
                         Label(window3, text="Depart at",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=560, y=400)
                         Label(window3, text="Age",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=400)
                         Label(window3, text="Class",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=440)
                         Label(window3, text="Train no.",bg='gray16',fg='orange',font=('Century Gothic', 11)).place(x=560, y=440)
                         Label(window3, text="Train name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=560, y=480)
                         Label(window3, text="Source",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=560, y=520)
                         Label(window3, text="Destination",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=520)
                         # Label(window3, text="No. of tickets",bg='white', font=('Slab Serif', 11)).place(x=60, y=290)

                         Label(window3, text="PNR No.",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=480)

                         # Number = Label(window3, justify="center",bg='white',text=count, font=('Slab Serif', 10))
                         # Number.place(x=170, y=290,  height=25)

                         Name = Label(window3, justify="center",fg='white',bg='gray16',text=e22.get(), font=('Century Gothic', 10))
                         Name.place(x=670, y=360, height=25)
                         DepartTime = Label(window3, justify="center",fg='white',bg='gray16',text=xdprtTime, font=('Century Gothic', 10))
                         DepartTime.place(x=670, y=400, height=25)
                         TrainName = Label(window3, justify="center",fg='white',bg='gray16',text=xtrainn, font=('Century Gothic', 10))
                         TrainName.place(x=670, y=480, height=25)
                         Age = Label(window3, justify="center",fg='white',bg='gray16',text=e23.get(), font=('Century Gothic', 10))
                         Age.place(x=950, y=400, height=25)
                         Class = Label(window3, justify="center",fg='white',bg='gray16',text=variable2.get(), font=('Century Gothic', 10))
                         Class.place(x=950, y=440, height=25)
                         Depart = Label(window3, justify="center",fg='white',bg='gray16',text=variable.get(), font=('Century Gothic', 10))
                         Depart.place(x=670, y=520, height=25)
                         Arrive = Label(window3, justify="center",fg='white',bg='gray16',text=variable1.get(), font=('Century Gothic', 10))
                         Arrive.place(x=950, y=520, height=25)
                         Gender = Label(window3, justify="center",fg='white',bg='gray16',text=e24.get(), font=('Century Gothic', 10))
                         Gender.place(x=950, y=360, height=25)
                         TrainNumber = Label(window3, justify="center",fg='white',bg='gray16',text=x1, font=('Century Gothic', 10))
                         TrainNumber.place(x=670, y=440, height=25)
                         
                         a=111111
                         b=999999
                         pnr4=(random.randint(a, b))
                         Numberpnr=Label(window3, justify="center",fg='white',bg='gray16',text=pnr4, font=('Century Gothic', 10))
                         Numberpnr.place(x=950, y=480, height=25) 


                         #global conn, cursor, x2
                         # passenger_data=[("pnr","enn7.get()","enn9.get()", "enn8.get()","x1")]
                        
                         # passenger_data=[(pnr,enn7.get(),enn9.get(), enn8.get(),x1)]
                         # c.execute("CREATE TABLE rail1 (passen_pnr integer, passen_name text, passen_gender text,passen_age integer,train_number integer)")
                         print("Command executed successfully...")
                         #insertion
                         #c.execute("INSERT INTO rail VALUES(pnr, enn7.get(),enn8.get(), str(enn9.get()
                         c.execute("INSERT INTO rail1 VALUES (?,?,?,?,?)",(pnr4,e22.get(),e24.get(), e23.get(),x1))
                         print("Command inserted successfully...")
                         # c.execute("SELECT*FROM rail")
                         c.execute("SELECT rowid,* FROM rail1")
                         print("Command selected successfully...")
                         items=c.fetchall()

                         print("S.No." + "\tPNR"+ "\tTrain No." +"\tGender"+ "\t\tAge"+ "\tName")
                         print("-----" + "\t---"+ "\t---------" +"\t------"+ "\t\t---"+ "\t----")
                         for item in items:
                             print(item[0] ,"    ",item[1] ," ",item[5],"\t",item[3] ,"\t\t", item[4],"\t", item[2])
                         

                         # for item in items:
                         #     print(item)
                         print("Command fetched successfully...") 
                         


                         Label(window3, text="Have a nice trip!!",fg='white',bg='gray16', font=('Century Gothic', 17)).place(x=450, y=600)

                         mainloop()




                    




                    global count
                    count=0
                    # a=int(enn8.get())
                    # b=int(e13.get())
                    # c=int(e18.get())
                    # d=int(e23.get())
                    if len(enn7.get()) == 0 or len(enn8.get()) == 0 or len(enn9.get()) == 0 or len(e10.get()) == 0:
                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
                    elif len(e12.get()) != 0 and (len(e13.get()) == 0 or len(e14.get()) == 0 or len(e15.get()) == 0):
                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
                    elif len(e17.get()) != 0 and (len(e18.get()) == 0 or len(e19.get()) == 0 or len(e20.get()) == 0):
                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
                    elif len(e22.get()) != 0 and (len(e23.get()) == 0 or len(e24.get()) == 0 or len(e25.get()) == 0):
                        tkinter.messagebox.showinfo('Error', 'enter all required fields')

                    # elif (int(e13.get())<0):
                            # tkinter.messagebox.showinfo('Error', 'Enter a valid age')
        
                    # elif (b<0):
                    #         tkinter.messagebox.showinfo('Error', 'Enter a valid age')
                        
                    # elif (c<0):
                    #         tkinter.messagebox.showinfo('Error', 'Enter a valid age')
                         
                    # elif (d<0):
                            # tkinter.messagebox.showinfo('Error', 'Enter a valid age') 

                    # elif type(e13.get())==str:
                    #         tkinter.messagebox.showinfo('Error', 'Enter a valid age')
        
                    # elif (b>105):
                    #         tkinter.messagebox.showinfo('Error', 'Enter a valid age')
                        
                    # elif (c>105):
                    #         tkinter.messagebox.showinfo('Error', 'Enter a valid age')
                         
                    # elif (d>105):
                    #         tkinter.messagebox.showinfo('Error', 'Enter a valid age')             

                    elif (len(e12.get()) != 0 or len(e13.get()) != 0 or len(e14.get()) != 0 or len(
                            e15.get()) != 0) and (
                            len(e22.get()) != 0 or len(e23.get()) != 0 or len(e24.get()) != 0 or len(
                        e25.get()) != 0) and (
                            len(e17.get()) == 0 or (len(e18.get()) == 0 or len(e19.get()) == 0 or len(e20.get()) == 0)):
                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
                    elif (len(enn7.get()) != 0 or len(enn8.get()) != 0 or len(enn9.get()) != 0 or len(
                            e10.get()) != 0) and (
                            len(e17.get()) != 0 or len(e18.get()) != 0 or len(e19.get()) != 0 or len(
                        e20.get()) != 0) and (
                            len(e12.get()) == 0 or (len(e13.get()) == 0 or len(e14.get()) == 0 or len(e15.get()) == 0)):
                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
                    elif  enn7.get()!="" and e12.get()=="" and e17.get()=="" and e22.get()=="":
                        count=1
                        Show()
                    elif e12.get()!="" and e17.get()=="":
                        count=2
                        Show()
                        
                    elif e17.get()!="" and e22.get()=="":
                        count=3
                        Show()
                    elif e22.get()!="":
                        count=4
                        Show()
                    else:
                        Show()
                
                def Mainmenu():
                    window2.destroy()
                    createWindow()
                    window()
                m = Button(window2, text="Main Menu",font=('Century Gothic',15),width=60, bg="orange", fg="gray16", command=Mainmenu)
                m.place(x=500,y=640,width=120)    

                b = Button(window2, text='Submit', bg="Orange",fg="gray16", font=('Century Gothic', 15), command=Check1)
                b.place(x=670,y=640,width=100)
                # def Main():
                #              window2.destroy()
                #              createWindow()
                # m = Button(window2, text="Main Menu",font=('Century Gothic',15),width=60, bg="orange", fg="gray16", command=Main())
                # m.place(x=600,y=640,width=100)

                mainloop()

            PassengerDetails()

        def PassengerDetails2():
            global x1, xtrainn, xdprtTime

            if f15.get()=="12303":
                x1=12303
            elif f15.get()=="123031":
                x1=123031
            elif f15.get() == "18237":
                x1 = 18237
            elif f15.get() == "182371":
                x1 = 182371
            elif f15.get() == "13006":
                x1 = 13006
            elif f15.get() == "130061":
                x1 = 130061 
            elif f15.get() == "12616":
                x1 = 12616   
            else:
                x1 = 126161

            if f16.get()=="Poorva Express":
                xtrainn="Poorva Express"
                xdprtTime="16:30"
            elif f16.get()=="Poorva Express":
                xtrainn="Poorva Express"
                xdprtTime="16:30"
            elif f16.get() == "Chattisgarh Express":
                xtrainn = "Chattisgarh Express"
                xdprtTime="16:30"
            elif f16.get() == "Chattisgarh Express":
                xtrainn = "Chattisgarh Express"
                xdprtTime="16:30"
            elif f16.get() == "ASR HWH Mail":
                xtrainn = "ASR HWH Mail"
                xdprtTime="00:45"
            elif f16.get() == "ASR HWH Mail":
                xtrainn = "ASR HWH Mail"
                xdprtTime="00:45"
            elif f16.get() == "Tamil Nadu Express":
                xtrainn = "Tamil Nadu Express"
                xdprtTime="16:30"  
            else:
                xtrainn = "Tamil Nadu Express"
                xdprtTime="16:30"

            def PassengerDetails():
                window1.destroy()
                window2 = Tk()
                window2.title("Passenger Details")
                window2.config(bg="gray16")
                screen_width = window2.winfo_screenwidth()
                screen_height = window2.winfo_screenheight()
                width = 1280
                height = 720
                x = (screen_width / 2) - (width / 2)
                y = (screen_height / 2) - (height / 2)
                window2.geometry('%dx%d+%d+%d' % (width, height, x, y))
                window2.resizable(0, 0)

                Label(window2, text= "Enter your Details",font=('Century Gothic',24), bg="gray16", fg='white').place(x=380,y=30,width=500)

                height = 5
                width = 5
                for i in range(height):  # Rows
                    for j in range(width):  # Columns
                        e1 = Label(window2, text="Passenger 1",justify="center",font=('Century Gothic',15), bg="gray16", fg="Orange")
                        e1.place(x=0,y=100,width=165)
                        e2 = Label(window2, text="Passenger 2",justify="center",font=('Century Gothic',15), bg="gray16", fg="Orange", width="13")
                        e2.place(x=0,y=230,width=165)
                        e3 = Label(window2, text="Passenger 3",justify="center",font=('Century Gothic',15), bg="gray16", fg="Orange", width="13")
                        e3.place(x=0,y=360,width=165)
                        e4 = Label(window2, text="Passenger 4",justify="center",font=('Century Gothic',15), bg="gray16", fg="Orange", width="13")
                        e4.place(x=0,y=490,width=165)

                        name1=Label(window2, text="Name",justify="center",font=('Century Gothic',13), bg="gray16", fg="White", width="13")
                        name1.place(x=130,y=160,width=100)
                        name2=Label(window2, text="Name",justify="center",font=('Century Gothic',13), bg="gray16", fg="White", width="13")
                        name2.place(x=130,y=290,width=100)
                        name3=Label(window2, text="Name",justify="center",font=('Century Gothic',13), bg="gray16", fg="White", width="13")
                        name3.place(x=130,y=420,width=100)
                        name4=Label(window2, text="Name",justify="center",font=('Century Gothic',13), bg="gray16", fg="White", width="13")
                        name4.place(x=130,y=550,width=100)

                        age1=Label(window2, text="Age",justify="center",font=('Century Gothic',13), bg="gray16", fg="White", width="13")
                        age1.place(x=400,y=160,width=70)
                        age2=Label(window2, text="Age",justify="center",font=('Century Gothic',13), bg="gray16", fg="White", width="13")
                        age2.place(x=400,y=290,width=70)
                        age3=Label(window2, text="Age",justify="center",font=('Century Gothic',13), bg="gray16", fg="White", width="13")
                        age3.place(x=400,y=420,width=70)
                        age4=Label(window2, text="Age",justify="center",font=('Century Gothic',13), bg="gray16", fg="White", width="13")
                        age4.place(x=400,y=550,width=70)

                        gender1=Label(window2, text="Gender",justify="center",font=('Century Gothic',13), bg="gray16", fg="White", width="13")
                        gender1.place(x=600,y=160,width=70)
                        gender2=Label(window2, text="Gender",justify="center",font=('Century Gothic',13), bg="gray16", fg="White", width="13")
                        gender2.place(x=600,y=290,width=70)
                        gender3=Label(window2, text="Gender",justify="center",font=('Century Gothic',13), bg="gray16", fg="White", width="13")
                        gender3.place(x=600,y=420,width=70)
                        gender4=Label(window2, text="Gender",justify="center",font=('Century Gothic',13), bg="gray16", fg="White", width="13")
                        gender4.place(x=600,y=550,width=70)

                        idproof1=Label(window2, text="ID Proof",justify="center",font=('Century Gothic',13), bg="gray16", fg="White", width="13")
                        idproof1.place(x=870,y=160,width=70)
                        idproof2=Label(window2, text="ID Proof",justify="center",font=('Century Gothic',13), bg="gray16", fg="White", width="13")
                        idproof2.place(x=870,y=290,width=70)
                        idproof3=Label(window2, text="ID Proof",justify="center",font=('Century Gothic',13), bg="gray16", fg="White", width="13")
                        idproof3.place(x=870,y=420,width=70)
                        idproof4=Label(window2, text="ID Proof",justify="center",font=('Century Gothic',13), bg="gray16", fg="White", width="13")
                        idproof4.place(x=870,y=550,width=70)

                        enn7 = Entry(window2, justify="center", font=('Slab Serif', 13), bg="white",fg="gray16")
                        enn7.place(x=230,y=164,width=120)
                        enn8 = Entry(window2, justify="center", font=('Slab Serif', 13), bg="white",fg="gray16")
                        enn8.place(x=480,y=164,width=50)
                        enn9 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        enn9.place(x=700,y=164,width=10)
                        e10 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        e10.place(x=970,y=164,width=10)

                        e12 = Entry(window2, justify="center", font=('Slab Serif', 13), bg="white",fg="gray16")
                        e12.place(x=230,y=294,width=120)
                        e13 = Entry(window2, justify="center", font=('Slab Serif', 13), bg="white",fg="gray16")
                        e13.place(x=480,y=294,width=50)
                        e14 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        e14.place(x=700,y=294,width=10)
                        e15 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        e15.place(x=970,y=294,width=10)

                        # if 0>e12.get()>105:
                        #     tkinter.messagebox.showinfo('Error', 'Enter a valid age')
        
                        # if 0>e13.get()>105:
                        #     tkinter.messagebox.showinfo('Error', 'Enter a valid age')
                        
                        # if 0>e14.get()>105:
                        #     tkinter.messagebox.showinfo('Error', 'Enter a valid age')
                         
                        # if 0>e15.get()>105:
                        #     tkinter.messagebox.showinfo('Error', 'Enter a valid age')

                        e17 = Entry(window2, justify="center", font=('Slab Serif', 13), bg="white",fg="gray16")
                        e17.place(x=230,y=424,width=120)
                        e18 = Entry(window2, justify="center", font=('Slab Serif', 13), bg="white",fg="gray16")
                        e18.place(x=480,y=424,width=50)
                        e19 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        e19.place(x=700,y=424,width=10)
                        e20 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        e20.place(x=970,y=424,width=10)

                        e22 = Entry(window2, justify="center", font=('Slab Serif', 13), bg="white",fg="gray16")
                        e22.place(x=230,y=554,width=120)
                        e23 = Entry(window2, justify="center", font=('Slab Serif', 13), bg="white",fg="gray16")
                        e23.place(x=480,y=554,width=50)
                        e24 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        e24.place(x=700,y=554,width=10)
                        e25 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        e25.place(x=970,y=554,width=10)

                        def fun(*args):
                            enn9.insert(10, v2.get())

                        def fun1(*args):
                            e14.insert(10, v3.get())

                        def fun2(*args):
                            e19.insert(10, v4.get())

                        def fun3(*args):
                            e24.insert(10, v5.get())

                        def fun4(*args):
                            e10.insert(10, v6.get())

                        def fun5(*args):
                            e15.insert(10, v7.get())

                        def fun6(*args):
                            e20.insert(10, v8.get())

                        def fun7(*args):
                            e25.insert(10, v9.get())

                        v2 = StringVar(window2)
                        genderr = {'Male', 'Female'}
                        v2.set('Select')
                        v2.trace("w", fun)
                        popupMenu1 = OptionMenu(window2, v2, *genderr)
                        popupMenu1.config(font=('Slab Serif', 13), bg="gray16", fg="orange")
                        popupMenu1.place(x=700,y=160,width=100)

                        v3 = StringVar(window2)
                        genderr1 = {'Male', 'Female'}
                        v3.set('Select')
                        v3.trace("w", fun1)
                        popupMenu2 = OptionMenu(window2, v3, *genderr1)
                        popupMenu2.config(font=('Slab Serif', 13), bg="gray16", fg="orange")
                        popupMenu2.place(x=700,y=290,width=100)

                        v4 = StringVar(window2)
                        genderr2 = {'Male', 'Female'}
                        v4.set('Select')
                        v4.trace("w", fun2)
                        popupMenu3 = OptionMenu(window2, v4, *genderr2)
                        popupMenu3.config(font=('Slab Serif', 13), bg="gray16", fg="orange")
                        popupMenu3.place(x=700,y=420,width=100)

                        v5 = StringVar(window2)
                        genderr3 = {'Male', 'Female'}
                        v5.set('Select')
                        v5.trace("w", fun3)
                        popupMenu4 = OptionMenu(window2, v5, *genderr3)
                        popupMenu4.config(font=('Slab Serif', 13), bg="gray16", fg="orange")
                        popupMenu4.place(x=700,y=550,width=100)

                        v6 = StringVar(window2)
                        proof = {'Aadhar card', 'Pan card'}
                        v6.set('Select')
                        v6.trace("w", fun4)
                        popup = OptionMenu(window2, v6, *proof)
                        popup.config(font=('Slab Serif', 13), bg="gray16",fg="orange")
                        popup.place(x=970,y=160,width=150)

                        v7 = StringVar(window2)
                        proof = {'Aadhar card', 'Pan card'}
                        v7.set('Select')
                        v7.trace("w", fun5)
                        popup = OptionMenu(window2, v7, *proof)
                        popup.config(font=('Slab Serif', 13), bg="gray16",fg="orange")
                        popup.place(x=970,y=290,width=150)

                        v8 = StringVar(window2)
                        proof = {'Aadhar card', 'Pan card'}
                        v8.set('Select')
                        v8.trace("w", fun6)
                        popup = OptionMenu(window2, v8, *proof)
                        popup.config(font=('Slab Serif', 13), bg="gray16",fg="orange")
                        popup.place(x=970,y=420,width=150)
                        v9 = StringVar(window2)
                        proof = {'Aadhar card', 'Pan card'}
                        v9.set('Select')
                        v9.trace("w", fun7)
                        popup = OptionMenu(window2, v9, *proof)
                        popup.config(font=('Slab Serif', 13), bg="gray16",fg="orange")

                        popup.place(x=970,y=550,width=150)    
   

                def Check1():

                    def Show():
                        global x1,count
                        if enn7.get()!="" and e12.get()=="" and e17.get()=="" and e22.get()=="":
                         
                         
                         count=1
                         window3 = Tk()

                         window3.title("Ticket")
                         screen_width = window3.winfo_screenwidth()
                         screen_height = window3.winfo_screenheight()
                         width = 580
                         height = 480
                         x = (screen_width / 2) - (width / 2)
                         y = (screen_height / 2) - (height / 2)
                         window3.geometry('%dx%d+%d+%d' % (width, height, x, y))
                         window3.resizable(0, 0)
                         window3.config(bg='gray16')

                         w11 = 580
                         h11 = 480
                         canvas3 = Canvas(window3, width=w11, height=h11)
                         canvas3.config(bg='gray16')
                         canvas3.create_rectangle(0, 0,580,30, fill= "orange")
                         canvas3.create_line(40, 90, 270, 90, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 130, 270, 130, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 170, 270, 170, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 210, 270, 210, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 250, 270, 250, fill="gray13", width=0.0000001)

                         canvas3.create_line(320, 90, 550, 90, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 130, 550, 130, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 170, 550, 170, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 210, 550, 210, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 250, 550, 250, fill="gray13", width=0.0000001)
                         canvas3.pack()
                         Label(window3, text="PNR Status Details",bg='orange',fg='gray16', font=('Century Gothic', 11)).place(x=10, y=2)
                         
                         Label(window3, text="Name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=60)
                         Label(window3, text="Gender",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=60)
                         Label(window3, text="Depart at",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=100)
                         Label(window3, text="Age",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=100)
                         Label(window3, text="Class",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=140)
                         Label(window3, text="Train no.",bg='gray16',fg='orange',font=('Century Gothic', 11)).place(x=40, y=140)
                         Label(window3, text="Train name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=180)
                         Label(window3, text="Source",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=220)
                         Label(window3, text="Destination",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=220)
                         # Label(window3, text="No. of tickets",bg='white', font=('Slab Serif', 11)).place(x=60, y=290)

                         Label(window3, text="PNR No.",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=180)

                         # Number = Label(window3, justify="center",bg='white',text=count, font=('Slab Serif', 10))
                         # Number.place(x=170, y=290,  height=25)

                         Name = Label(window3, justify="center",fg='white',bg='gray16',text=enn7.get(), font=('Century Gothic', 10))
                         Name.place(x=150, y=60, height=25)
                         DepartTime = Label(window3, justify="center",fg='white',bg='gray16',text=xdprtTime, font=('Century Gothic', 10))
                         DepartTime.place(x=150, y=100, height=25)
                         TrainName = Label(window3, justify="center",fg='white',bg='gray16',text=xtrainn, font=('Century Gothic', 10))
                         TrainName.place(x=150, y=180, height=25)
                         Age = Label(window3, justify="center",fg='white',bg='gray16',text=enn8.get(), font=('Century Gothic', 10))
                         Age.place(x=430, y=100, height=25)
                         Class = Label(window3, justify="center",fg='white',bg='gray16',text=variable2.get(), font=('Century Gothic', 10))
                         Class.place(x=430, y=140, height=25)
                         Depart = Label(window3, justify="center",fg='white',bg='gray16',text=variable.get(), font=('Century Gothic', 10))
                         Depart.place(x=150, y=220, height=25)
                         Arrive = Label(window3, justify="center",fg='white',bg='gray16',text=variable1.get(), font=('Century Gothic', 10))
                         Arrive.place(x=430, y=220, height=25)
                         Gender = Label(window3, justify="center",fg='white',bg='gray16',text=v2.get(), font=('Century Gothic', 10))
                         Gender.place(x=430, y=60, height=25)
                         TrainNumber = Label(window3, justify="center",fg='white',bg='gray16',text=x1, font=('Century Gothic', 10))
                         TrainNumber.place(x=150, y=140, height=25)
                         
                         a=111111
                         b=999999
                         pnr=(random.randint(a, b))
                         Numberpnr=Label(window3, justify="center",fg='white',bg='gray16',text=pnr, font=('Century Gothic', 10))
                         Numberpnr.place(x=430, y=180, height=25) 


                         #global conn, cursor, x2
                         # passenger_data=[("pnr","enn7.get()","enn9.get()", "enn8.get()","x1")]
                        
                         # passenger_data=[(pnr,enn7.get(),enn9.get(), enn8.get(),x1)]
                         # c.execute("CREATE TABLE rail1 (passen_pnr integer, passen_name text, passen_gender text,passen_age integer,train_number integer)")
                         print("Command executed successfully...")
                         #insertion
                         #c.execute("INSERT INTO rail VALUES(pnr, enn7.get(),enn8.get(), str(enn9.get()
                         c.execute("INSERT INTO rail1 VALUES (?,?,?,?,?)",(pnr,enn7.get(),enn9.get(), enn8.get(),x1))
                         print("Command inserted successfully...")
                         # c.execute("SELECT*FROM rail")
                         c.execute("SELECT rowid,* FROM rail1")
                         print("Command selected successfully...")
                         items=c.fetchall()

                         print("S.No." + "\tPNR"+ "\tTrain No." +"   \tGender"+ "\tAge"+ "\tName")
                         print("-----" + "\t---"+ "\t---------" +"   \t------"+ "\t---"+ "\t----")
                         for item in items:
                             print(item[0] ,"    ",item[1] ," ",item[5],"   \t",item[3] ," ", item[4],"\t", item[2])
                         

                         # for item in items:
                         #     print(item)
                         print("Command fetched successfully...")    
                        


                         Label(window3, text="Have a nice trip!!",fg='white',bg='gray16', font=('Century Gothic', 17)).place(x=200, y=340)

                         mainloop()

                        elif e12.get()!="" and e17.get()=="":
                         
                         count=1
                         window3 = Tk()

                         window3.title("Ticket")
                         screen_width = window3.winfo_screenwidth()
                         screen_height = window3.winfo_screenheight()
                         width = 1160
                         height = 480
                         x = (screen_width / 2) - (width / 2)
                         y = (screen_height / 2) - (height / 2)
                         window3.geometry('%dx%d+%d+%d' % (width, height, x, y))
                         window3.resizable(0, 0)
                         window3.config(bg='gray16')

                         w11 = 1160
                         h11 = 480
                         canvas3 = Canvas(window3, width=w11, height=h11)
                         canvas3.config(bg='gray16')
                         canvas3.create_rectangle(0, 0,1160,30, fill= "orange")
                         canvas3.create_line(40, 90, 270, 90, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 130, 270, 130, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 170, 270, 170, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 210, 270, 210, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 250, 270, 250, fill="gray13", width=0.0000001)

                         canvas3.create_line(320, 90, 550, 90, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 130, 550, 130, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 170, 550, 170, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 210, 550, 210, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 250, 550, 250, fill="gray13", width=0.0000001)

                         canvas3.create_line(560, 90, 790, 90, fill="gray13", width=0.0000001)
                         canvas3.create_line(560, 130, 790, 130, fill="gray13", width=0.0000001)
                         canvas3.create_line(560, 170, 790, 170, fill="gray13", width=0.0000001)
                         canvas3.create_line(560, 210, 790, 210, fill="gray13", width=0.0000001)
                         canvas3.create_line(560, 250, 790, 250, fill="gray13", width=0.0000001)

                         canvas3.create_line(840, 90, 1070, 90, fill="gray13", width=0.0000001)
                         canvas3.create_line(840, 130, 1070, 130, fill="gray13", width=0.0000001)
                         canvas3.create_line(840, 170, 1070, 170, fill="gray13", width=0.0000001)
                         canvas3.create_line(840, 210, 1070, 210, fill="gray13", width=0.0000001)
                         canvas3.create_line(840, 250, 1070, 250, fill="gray13", width=0.0000001)
                         canvas3.pack()
                         Label(window3, text="PNR Status Details",bg='orange',fg='gray16', font=('Century Gothic', 11)).place(x=10, y=2)
                         
                         Label(window3, text="Name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=60)
                         Label(window3, text="Gender",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=60)
                         Label(window3, text="Depart at",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=100)
                         Label(window3, text="Age",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=100)
                         Label(window3, text="Class",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=140)
                         Label(window3, text="Train no.",bg='gray16',fg='orange',font=('Century Gothic', 11)).place(x=40, y=140)
                         Label(window3, text="Train name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=180)
                         Label(window3, text="Source",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=220)
                         Label(window3, text="Destination",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=220)
                         # Label(window3, text="No. of tickets",bg='white', font=('Slab Serif', 11)).place(x=60, y=290)

                         Label(window3, text="PNR No.",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=180)

                         # Number = Label(window3, justify="center",bg='white',text=count, font=('Slab Serif', 10))
                         # Number.place(x=170, y=290,  height=25)

                         Name = Label(window3, justify="center",fg='white',bg='gray16',text=enn7.get(), font=('Century Gothic', 10))
                         Name.place(x=150, y=60, height=25)
                         DepartTime = Label(window3, justify="center",fg='white',bg='gray16',text=xdprtTime, font=('Century Gothic', 10))
                         DepartTime.place(x=150, y=100, height=25)
                         TrainName = Label(window3, justify="center",fg='white',bg='gray16',text=xtrainn, font=('Century Gothic', 10))
                         TrainName.place(x=150, y=180, height=25)
                         Age = Label(window3, justify="center",fg='white',bg='gray16',text=enn8.get(), font=('Century Gothic', 10))
                         Age.place(x=430, y=100, height=25)
                         Class = Label(window3, justify="center",fg='white',bg='gray16',text=variable2.get(), font=('Century Gothic', 10))
                         Class.place(x=430, y=140, height=25)
                         Depart = Label(window3, justify="center",fg='white',bg='gray16',text=variable.get(), font=('Century Gothic', 10))
                         Depart.place(x=150, y=220, height=25)
                         Arrive = Label(window3, justify="center",fg='white',bg='gray16',text=variable1.get(), font=('Century Gothic', 10))
                         Arrive.place(x=430, y=220, height=25)
                         Gender = Label(window3, justify="center",fg='white',bg='gray16',text=v2.get(), font=('Century Gothic', 10))
                         Gender.place(x=430, y=60, height=25)
                         TrainNumber = Label(window3, justify="center",fg='white',bg='gray16',text=x1, font=('Century Gothic', 10))
                         TrainNumber.place(x=150, y=140, height=25)
                         
                         a=111111
                         b=999999
                         pnr=(random.randint(a, b))
                         Numberpnr=Label(window3, justify="center",fg='white',bg='gray16',text=pnr, font=('Century Gothic', 10))
                         Numberpnr.place(x=430, y=180, height=25) 


                         #global conn, cursor, x2
                         # passenger_data=[("pnr","enn7.get()","enn9.get()", "enn8.get()","x1")]
                        
                         # passenger_data=[(pnr,enn7.get(),enn9.get(), enn8.get(),x1)]
                         # c.execute("CREATE TABLE rail1 (passen_pnr integer, passen_name text, passen_gender text,passen_age integer,train_number integer)")
                         print("Command executed successfully...")
                         #insertion
                         #c.execute("INSERT INTO rail VALUES(pnr, enn7.get(),enn8.get(), str(enn9.get()
                         c.execute("INSERT INTO rail1 VALUES (?,?,?,?,?)",(pnr,enn7.get(),enn9.get(), enn8.get(),x1))
                         print("Command inserted successfully...")
                         # c.execute("SELECT*FROM rail")
                         c.execute("SELECT rowid,* FROM rail1")
                         print("Command selected successfully...")
                         items=c.fetchall()

                         print("S.No." + "\tPNR"+ "\tTrain No." +"   \tGender"+ "  \tAge"+ "\tName")
                         print("-----" + "\t---"+ "\t---------" +"   \t------"+ "  \t---"+ "\t----")
                         for item in items:
                             print(item[0] ,"    ",item[1] ," ",item[5],"   \t",item[3] ,"   ", item[4],"\t", item[2])
                         

                         # for item in items:
                         #     print(item)
                         print("Command fetched successfully...")    
                         
                         #-------------------------------------------------------------------  
                         
                         Label(window3, text="Name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=560, y=60)
                         Label(window3, text="Gender",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=60)
                         Label(window3, text="Depart at",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=560, y=100)
                         Label(window3, text="Age",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=100)
                         Label(window3, text="Class",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=140)
                         Label(window3, text="Train no.",bg='gray16',fg='orange',font=('Century Gothic', 11)).place(x=560, y=140)
                         Label(window3, text="Train name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=560, y=180)
                         Label(window3, text="Source",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=560, y=220)
                         Label(window3, text="Destination",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=220)
                         # Label(window3, text="No. of tickets",bg='white', font=('Slab Serif', 11)).place(x=60, y=290)

                         Label(window3, text="PNR No.",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=180)

                         # Number = Label(window3, justify="center",bg='white',text=count, font=('Slab Serif', 10))
                         # Number.place(x=170, y=290,  height=25)

                         Name = Label(window3, justify="center",fg='white',bg='gray16',text=e12.get(), font=('Century Gothic', 10))
                         Name.place(x=670, y=60, height=25)
                         DepartTime = Label(window3, justify="center",fg='white',bg='gray16',text=xdprtTime, font=('Century Gothic', 10))
                         DepartTime.place(x=670, y=100, height=25)
                         TrainName = Label(window3, justify="center",fg='white',bg='gray16',text=xtrainn, font=('Century Gothic', 10))
                         TrainName.place(x=670, y=180, height=25)
                         Age = Label(window3, justify="center",fg='white',bg='gray16',text=e13.get(), font=('Century Gothic', 10))
                         Age.place(x=950, y=100, height=25)
                         Class = Label(window3, justify="center",fg='white',bg='gray16',text=variable2.get(), font=('Century Gothic', 10))
                         Class.place(x=950, y=140, height=25)
                         Depart = Label(window3, justify="center",fg='white',bg='gray16',text=variable.get(), font=('Century Gothic', 10))
                         Depart.place(x=670, y=220, height=25)
                         Arrive = Label(window3, justify="center",fg='white',bg='gray16',text=variable1.get(), font=('Century Gothic', 10))
                         Arrive.place(x=950, y=220, height=25)
                         Gender = Label(window3, justify="center",fg='white',bg='gray16',text=e14.get(), font=('Century Gothic', 10))
                         Gender.place(x=950, y=60, height=25)
                         TrainNumber = Label(window3, justify="center",fg='white',bg='gray16',text=x1, font=('Century Gothic', 10))
                         TrainNumber.place(x=670, y=140, height=25)
                         
                         a=111111
                         b=999999
                         pnr2=(random.randint(a, b))
                         Numberpnr=Label(window3, justify="center",fg='white',bg='gray16',text=pnr2, font=('Century Gothic', 10))
                         Numberpnr.place(x=950, y=180, height=25) 


                         #global conn, cursor, x2
                         # passenger_data=[("pnr","enn7.get()","enn9.get()", "enn8.get()","x1")]
                        
                         # passenger_data=[(pnr,enn7.get(),enn9.get(), enn8.get(),x1)]
                         # c.execute("CREATE TABLE rail1 (passen_pnr integer, passen_name text, passen_gender text,passen_age integer,train_number integer)")
                         print("Command executed successfully...")
                         #insertion
                         #c.execute("INSERT INTO rail VALUES(pnr, enn7.get(),enn8.get(), str(enn9.get()
                         c.execute("INSERT INTO rail1 VALUES (?,?,?,?,?)",(pnr2,e12.get(),e14.get(), e13.get(),x1))
                         print("Command inserted successfully...")
                         # c.execute("SELECT*FROM rail")
                         c.execute("SELECT rowid,* FROM rail1")
                         print("Command selected successfully...")
                         items=c.fetchall()

                         print("S.No." + "\tPNR"+ "\tTrain No." +"   \tGender"+ "  \tAge"+ "\tName")
                         print("-----" + "\t---"+ "\t---------" +"   \t------"+ "  \t---"+ "\t----")
                         for item in items:
                             print(item[0] ,"    ",item[1] ," ",item[5],"   \t",item[3] ,"   ", item[4],"\t", item[2])
                         

                         # for item in items:
                         #     print(item)
                         print("Command fetched successfully...")     
                        


                         Label(window3, text="Have a nice trip!!",fg='white',bg='gray16', font=('Century Gothic', 17)).place(x=500, y=340)

                         mainloop()
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                        elif e17.get()!="" and e22.get()=="":
                         count=3
                         window3 = Tk()

                         window3.title("Ticket")
                         screen_width = window3.winfo_screenwidth()
                         screen_height = window3.winfo_screenheight()
                         width = 1160
                         height = 800
                         x = (screen_width / 2) - (width / 2)
                         y = (screen_height / 2) - (height / 2)
                         window3.geometry('%dx%d+%d+%d' % (width, height, x, y))
                         window3.resizable(0, 0)
                         window3.config(bg='gray16')

                         w11 = 1160
                         h11 = 800
                         canvas3 = Canvas(window3, width=w11, height=h11)
                         canvas3.config(bg='gray16')
                         canvas3.create_rectangle(0, 0,1160,30, fill= "orange")
                         canvas3.create_line(40, 90, 270, 90, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 130, 270, 130, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 170, 270, 170, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 210, 270, 210, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 250, 270, 250, fill="gray13", width=0.0000001)

                         canvas3.create_line(320, 90, 550, 90, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 130, 550, 130, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 170, 550, 170, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 210, 550, 210, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 250, 550, 250, fill="gray13", width=0.0000001)

                         canvas3.create_line(560, 90, 790, 90, fill="gray13", width=0.0000001)
                         canvas3.create_line(560, 130, 790, 130, fill="gray13", width=0.0000001)
                         canvas3.create_line(560, 170, 790, 170, fill="gray13", width=0.0000001)
                         canvas3.create_line(560, 210, 790, 210, fill="gray13", width=0.0000001)
                         canvas3.create_line(560, 250, 790, 250, fill="gray13", width=0.0000001)

                         canvas3.create_line(840, 90, 1070, 90, fill="gray13", width=0.0000001)
                         canvas3.create_line(840, 130, 1070, 130, fill="gray13", width=0.0000001)
                         canvas3.create_line(840, 170, 1070, 170, fill="gray13", width=0.0000001)
                         canvas3.create_line(840, 210, 1070, 210, fill="gray13", width=0.0000001)
                         canvas3.create_line(840, 250, 1070, 250, fill="gray13", width=0.0000001)

                         canvas3.create_line(40, 390, 270, 390, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 430, 270, 430, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 470, 270, 470, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 510, 270, 510, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 550, 270, 550, fill="gray13", width=0.0000001)

                         canvas3.create_line(320, 390, 550, 390, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 430, 550, 430, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 470, 550, 470, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 510, 550, 510, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 550, 550, 550, fill="gray13", width=0.0000001)
                         canvas3.pack()
                         Label(window3, text="PNR Status Details",bg='orange',fg='gray16', font=('Century Gothic', 11)).place(x=10, y=2)
                         
                         Label(window3, text="Name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=60)
                         Label(window3, text="Gender",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=60)
                         Label(window3, text="Depart at",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=100)
                         Label(window3, text="Age",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=100)
                         Label(window3, text="Class",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=140)
                         Label(window3, text="Train no.",bg='gray16',fg='orange',font=('Century Gothic', 11)).place(x=40, y=140)
                         Label(window3, text="Train name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=180)
                         Label(window3, text="Source",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=220)
                         Label(window3, text="Destination",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=220)
                         # Label(window3, text="No. of tickets",bg='white', font=('Slab Serif', 11)).place(x=60, y=290)

                         Label(window3, text="PNR No.",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=180)

                         # Number = Label(window3, justify="center",bg='white',text=count, font=('Slab Serif', 10))
                         # Number.place(x=170, y=290,  height=25)

                         Name = Label(window3, justify="center",fg='white',bg='gray16',text=enn7.get(), font=('Century Gothic', 10))
                         Name.place(x=150, y=60, height=25)
                         DepartTime = Label(window3, justify="center",fg='white',bg='gray16',text=xdprtTime, font=('Century Gothic', 10))
                         DepartTime.place(x=150, y=100, height=25)
                         TrainName = Label(window3, justify="center",fg='white',bg='gray16',text=xtrainn, font=('Century Gothic', 10))
                         TrainName.place(x=150, y=180, height=25)
                         Age = Label(window3, justify="center",fg='white',bg='gray16',text=enn8.get(), font=('Century Gothic', 10))
                         Age.place(x=430, y=100, height=25)
                         Class = Label(window3, justify="center",fg='white',bg='gray16',text=variable2.get(), font=('Century Gothic', 10))
                         Class.place(x=430, y=140, height=25)
                         Depart = Label(window3, justify="center",fg='white',bg='gray16',text=variable.get(), font=('Century Gothic', 10))
                         Depart.place(x=150, y=220, height=25)
                         Arrive = Label(window3, justify="center",fg='white',bg='gray16',text=variable1.get(), font=('Century Gothic', 10))
                         Arrive.place(x=430, y=220, height=25)
                         Gender = Label(window3, justify="center",fg='white',bg='gray16',text=v2.get(), font=('Century Gothic', 10))
                         Gender.place(x=430, y=60, height=25)
                         TrainNumber = Label(window3, justify="center",fg='white',bg='gray16',text=x1, font=('Century Gothic', 10))
                         TrainNumber.place(x=150, y=140, height=25)
                         
                         a=111111
                         b=999999
                         pnr=(random.randint(a, b))
                         Numberpnr=Label(window3, justify="center",fg='white',bg='gray16',text=pnr, font=('Century Gothic', 10))
                         Numberpnr.place(x=430, y=180, height=25) 


                         #global conn, cursor, x2
                         # passenger_data=[("pnr","enn7.get()","enn9.get()", "enn8.get()","x1")]
                        
                         # passenger_data=[(pnr,enn7.get(),enn9.get(), enn8.get(),x1)]
                         # c.execute("CREATE TABLE rail1 (passen_pnr integer, passen_name text, passen_gender text,passen_age integer,train_number integer)")
                         print("Command executed successfully...")
                         #insertion
                         #c.execute("INSERT INTO rail VALUES(pnr, enn7.get(),enn8.get(), str(enn9.get()
                         c.execute("INSERT INTO rail1 VALUES (?,?,?,?,?)",(pnr,enn7.get(),enn9.get(), enn8.get(),x1))
                         print("Command inserted successfully...")
                         # c.execute("SELECT*FROM rail")
                         c.execute("SELECT rowid,* FROM rail1")
                         print("Command selected successfully...")
                         items=c.fetchall()

                         print("S.No." + "\tPNR"+ "\tTrain No." +"   \tGender"+ "\tAge"+ "    \tName")
                         print("-----" + "\t---"+ "\t---------" +"   \t------"+ "\t---"+ "    \t----")
                         for item in items:
                             print(item[0] ,"    ",item[1] ," ",item[5],"   \t",item[3] ," ", item[4],"    \t", item[2])
                         

                         # for item in items:
                         #     print(item)
                         print("Command fetched successfully...")    
                         
                         #-------------------------------------------------------------------  
                         
                         Label(window3, text="Name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=560, y=60)
                         Label(window3, text="Gender",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=60)
                         Label(window3, text="Depart at",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=560, y=100)
                         Label(window3, text="Age",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=100)
                         Label(window3, text="Class",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=140)
                         Label(window3, text="Train no.",bg='gray16',fg='orange',font=('Century Gothic', 11)).place(x=560, y=140)
                         Label(window3, text="Train name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=560, y=180)
                         Label(window3, text="Source",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=560, y=220)
                         Label(window3, text="Destination",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=220)
                         # Label(window3, text="No. of tickets",bg='white', font=('Slab Serif', 11)).place(x=60, y=290)

                         Label(window3, text="PNR No.",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=180)

                         # Number = Label(window3, justify="center",bg='white',text=count, font=('Slab Serif', 10))
                         # Number.place(x=170, y=290,  height=25)

                         Name = Label(window3, justify="center",fg='white',bg='gray16',text=e12.get(), font=('Century Gothic', 10))
                         Name.place(x=670, y=60, height=25)
                         DepartTime = Label(window3, justify="center",fg='white',bg='gray16',text=xdprtTime, font=('Century Gothic', 10))
                         DepartTime.place(x=670, y=100, height=25)
                         TrainName = Label(window3, justify="center",fg='white',bg='gray16',text=xtrainn, font=('Century Gothic', 10))
                         TrainName.place(x=670, y=180, height=25)
                         Age = Label(window3, justify="center",fg='white',bg='gray16',text=e13.get(), font=('Century Gothic', 10))
                         Age.place(x=950, y=100, height=25)
                         Class = Label(window3, justify="center",fg='white',bg='gray16',text=variable2.get(), font=('Century Gothic', 10))
                         Class.place(x=950, y=140, height=25)
                         Depart = Label(window3, justify="center",fg='white',bg='gray16',text=variable.get(), font=('Century Gothic', 10))
                         Depart.place(x=670, y=220, height=25)
                         Arrive = Label(window3, justify="center",fg='white',bg='gray16',text=variable1.get(), font=('Century Gothic', 10))
                         Arrive.place(x=950, y=220, height=25)
                         Gender = Label(window3, justify="center",fg='white',bg='gray16',text=e14.get(), font=('Century Gothic', 10))
                         Gender.place(x=950, y=60, height=25)
                         TrainNumber = Label(window3, justify="center",fg='white',bg='gray16',text=x1, font=('Century Gothic', 10))
                         TrainNumber.place(x=670, y=140, height=25)
                         
                         a=111111
                         b=999999
                         pnr2=(random.randint(a, b))
                         Numberpnr=Label(window3, justify="center",fg='white',bg='gray16',text=pnr2, font=('Century Gothic', 10))
                         Numberpnr.place(x=950, y=180, height=25) 


                         #global conn, cursor, x2
                         # passenger_data=[("pnr","enn7.get()","enn9.get()", "enn8.get()","x1")]
                        
                         # passenger_data=[(pnr,enn7.get(),enn9.get(), enn8.get(),x1)]
                         # c.execute("CREATE TABLE rail1 (passen_pnr integer, passen_name text, passen_gender text,passen_age integer,train_number integer)")
                         print("Command executed successfully...")
                         #insertion
                         #c.execute("INSERT INTO rail VALUES(pnr, enn7.get(),enn8.get(), str(enn9.get()
                         c.execute("INSERT INTO rail1 VALUES (?,?,?,?,?)",(pnr2,e12.get(),e14.get(), e13.get(),x1))
                         print("Command inserted successfully...")
                         # c.execute("SELECT*FROM rail")
                         c.execute("SELECT rowid,* FROM rail1")
                         print("Command selected successfully...")
                         items=c.fetchall()

                         print("S.No." + "\tPNR"+ "\tTrain No." +"   \tGender"+ "\tAge"+ "    \tName")
                         print("-----" + "\t---"+ "\t---------" +"   \t------"+ "\t---"+ "    \t----")
                         for item in items:
                             print(item[0] ,"    ",item[1] ," ",item[5],"   \t",item[3] ," ", item[4],"    \t", item[2])
                         

                         # for item in items:
                         #     print(item)
                         print("Command fetched successfully...")   

                            #  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                         Label(window3, text="Name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=360)
                         Label(window3, text="Gender",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=360)
                         Label(window3, text="Depart at",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=400)
                         Label(window3, text="Age",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=400)
                         Label(window3, text="Class",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=440)
                         Label(window3, text="Train no.",bg='gray16',fg='orange',font=('Century Gothic', 11)).place(x=40, y=440)
                         Label(window3, text="Train name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=480)
                         Label(window3, text="Source",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=520)
                         Label(window3, text="Destination",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=520)
                         # Label(window3, text="No. of tickets",bg='white', font=('Slab Serif', 11)).place(x=60, y=290)

                         Label(window3, text="PNR No.",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=480)

                         # Number = Label(window3, justify="center",bg='white',text=count, font=('Slab Serif', 10))
                         # Number.place(x=170, y=290,  height=25)

                         Name = Label(window3, justify="center",fg='white',bg='gray16',text=e17.get(), font=('Century Gothic', 10))
                         Name.place(x=150, y=360, height=25)
                         DepartTime = Label(window3, justify="center",fg='white',bg='gray16',text=xdprtTime, font=('Century Gothic', 10))
                         DepartTime.place(x=150, y=400, height=25)
                         TrainName = Label(window3, justify="center",fg='white',bg='gray16',text=xtrainn, font=('Century Gothic', 10))
                         TrainName.place(x=150, y=480, height=25)
                         Age = Label(window3, justify="center",fg='white',bg='gray16',text=e18.get(), font=('Century Gothic', 10))
                         Age.place(x=430, y=400, height=25)
                         Class = Label(window3, justify="center",fg='white',bg='gray16',text=variable2.get(), font=('Century Gothic', 10))
                         Class.place(x=430, y=440, height=25)
                         Depart = Label(window3, justify="center",fg='white',bg='gray16',text=variable.get(), font=('Century Gothic', 10))
                         Depart.place(x=150, y=520, height=25)
                         Arrive = Label(window3, justify="center",fg='white',bg='gray16',text=variable1.get(), font=('Century Gothic', 10))
                         Arrive.place(x=430, y=520, height=25)
                         Gender = Label(window3, justify="center",fg='white',bg='gray16',text=e19.get(), font=('Century Gothic', 10))
                         Gender.place(x=430, y=360, height=25)
                         TrainNumber = Label(window3, justify="center",fg='white',bg='gray16',text=x1, font=('Century Gothic', 10))
                         TrainNumber.place(x=150, y=440, height=25)
                         
                         a=111111
                         b=999999
                         pnr3=(random.randint(a, b))
                         Numberpnr=Label(window3, justify="center",fg='white',bg='gray16',text=pnr3, font=('Century Gothic', 10))
                         Numberpnr.place(x=430, y=480, height=25) 


                         #global conn, cursor, x2
                         # passenger_data=[("pnr","enn7.get()","enn9.get()", "enn8.get()","x1")]
                        
                         # passenger_data=[(pnr,enn7.get(),enn9.get(), enn8.get(),x1)]
                         # c.execute("CREATE TABLE rail1 (passen_pnr integer, passen_name text, passen_gender text,passen_age integer,train_number integer)")
                         print("Command executed successfully...")
                         #insertion
                         #c.execute("INSERT INTO rail VALUES(pnr, enn7.get(),enn8.get(), str(enn9.get()
                         c.execute("INSERT INTO rail1 VALUES (?,?,?,?,?)",(pnr3,e17.get(),e19.get(), e18.get(),x1))
                         print("Command inserted successfully...")
                         # c.execute("SELECT*FROM rail")
                         c.execute("SELECT rowid,* FROM rail1")
                         print("Command selected successfully...")
                         items=c.fetchall()

                         print("S.No." + "\tPNR"+ "\tTrain No." +"   \tGender"+ "\tAge"+ "    \tName")
                         print("-----" + "\t---"+ "\t---------" +"   \t------"+ "\t---"+ "    \t----")
                         for item in items:
                             print(item[0] ,"    ",item[1] ," ",item[5],"   \t",item[3] ," ", item[4],"    \t", item[2])
                         

                         # for item in items:
                         #     print(item)
                         print("Command fetched successfully...")  

                        


                         Label(window3, text="Have a nice trip!!",fg='white',bg='gray16', font=('Century Gothic', 17)).place(x=800, y=340)

                         mainloop()
                        else:
                         count=4
                         window3 = Tk()

                         window3.title("Ticket")
                         screen_width = window3.winfo_screenwidth()
                         screen_height = window3.winfo_screenheight()
                         width = 1160
                         height = 800
                         x = (screen_width / 2) - (width / 2)
                         y = (screen_height / 2) - (height / 2)
                         window3.geometry('%dx%d+%d+%d' % (width, height, x, y))
                         window3.resizable(0, 0)
                         window3.config(bg='gray16')

                         w11 = 1160
                         h11 = 800
                         canvas3 = Canvas(window3, width=w11, height=h11)
                         canvas3.config(bg='gray16')
                         canvas3.create_rectangle(0, 0,1160,30, fill= "orange")
                         canvas3.create_line(40, 90, 270, 90, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 130, 270, 130, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 170, 270, 170, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 210, 270, 210, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 250, 270, 250, fill="gray13", width=0.0000001)

                         canvas3.create_line(320, 90, 550, 90, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 130, 550, 130, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 170, 550, 170, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 210, 550, 210, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 250, 550, 250, fill="gray13", width=0.0000001)

                         canvas3.create_line(560, 90, 790, 90, fill="gray13", width=0.0000001)
                         canvas3.create_line(560, 130, 790, 130, fill="gray13", width=0.0000001)
                         canvas3.create_line(560, 170, 790, 170, fill="gray13", width=0.0000001)
                         canvas3.create_line(560, 210, 790, 210, fill="gray13", width=0.0000001)
                         canvas3.create_line(560, 250, 790, 250, fill="gray13", width=0.0000001)

                         canvas3.create_line(840, 90, 1070, 90, fill="gray13", width=0.0000001)
                         canvas3.create_line(840, 130, 1070, 130, fill="gray13", width=0.0000001)
                         canvas3.create_line(840, 170, 1070, 170, fill="gray13", width=0.0000001)
                         canvas3.create_line(840, 210, 1070, 210, fill="gray13", width=0.0000001)
                         canvas3.create_line(840, 250, 1070, 250, fill="gray13", width=0.0000001)

                         canvas3.create_line(40, 390, 270, 390, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 430, 270, 430, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 470, 270, 470, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 510, 270, 510, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 550, 270, 550, fill="gray13", width=0.0000001)

                         canvas3.create_line(320, 390, 550, 390, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 430, 550, 430, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 470, 550, 470, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 510, 550, 510, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 550, 550, 550, fill="gray13", width=0.0000001)

                         canvas3.create_line(560, 390, 790, 390, fill="gray13", width=0.0000001)
                         canvas3.create_line(560, 430, 790, 430, fill="gray13", width=0.0000001)
                         canvas3.create_line(560, 470, 790, 470, fill="gray13", width=0.0000001)
                         canvas3.create_line(560, 510, 790, 510, fill="gray13", width=0.0000001)
                         canvas3.create_line(560, 550, 790, 550, fill="gray13", width=0.0000001)

                         canvas3.create_line(840, 390, 1070, 390, fill="gray13", width=0.0000001)
                         canvas3.create_line(840, 430, 1070, 430, fill="gray13", width=0.0000001)
                         canvas3.create_line(840, 470, 1070, 470, fill="gray13", width=0.0000001)
                         canvas3.create_line(840, 510, 1070, 510, fill="gray13", width=0.0000001)
                         canvas3.create_line(840, 550, 1070, 550, fill="gray13", width=0.0000001)
                         canvas3.pack()
                         Label(window3, text="PNR Status Details",bg='orange',fg='gray16', font=('Century Gothic', 11)).place(x=10, y=2)
                         
                         Label(window3, text="Name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=60)
                         Label(window3, text="Gender",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=60)
                         Label(window3, text="Depart at",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=100)
                         Label(window3, text="Age",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=100)
                         Label(window3, text="Class",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=140)
                         Label(window3, text="Train no.",bg='gray16',fg='orange',font=('Century Gothic', 11)).place(x=40, y=140)
                         Label(window3, text="Train name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=180)
                         Label(window3, text="Source",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=220)
                         Label(window3, text="Destination",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=220)
                         # Label(window3, text="No. of tickets",bg='white', font=('Slab Serif', 11)).place(x=60, y=290)

                         Label(window3, text="PNR No.",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=180)

                         # Number = Label(window3, justify="center",bg='white',text=count, font=('Slab Serif', 10))
                         # Number.place(x=170, y=290,  height=25)

                         Name = Label(window3, justify="center",fg='white',bg='gray16',text=enn7.get(), font=('Century Gothic', 10))
                         Name.place(x=150, y=60, height=25)
                         DepartTime = Label(window3, justify="center",fg='white',bg='gray16',text=xdprtTime, font=('Century Gothic', 10))
                         DepartTime.place(x=150, y=100, height=25)
                         TrainName = Label(window3, justify="center",fg='white',bg='gray16',text=xtrainn, font=('Century Gothic', 10))
                         TrainName.place(x=150, y=180, height=25)
                         Age = Label(window3, justify="center",fg='white',bg='gray16',text=enn8.get(), font=('Century Gothic', 10))
                         Age.place(x=430, y=100, height=25)
                         Class = Label(window3, justify="center",fg='white',bg='gray16',text=variable2.get(), font=('Century Gothic', 10))
                         Class.place(x=430, y=140, height=25)
                         Depart = Label(window3, justify="center",fg='white',bg='gray16',text=variable.get(), font=('Century Gothic', 10))
                         Depart.place(x=150, y=220, height=25)
                         Arrive = Label(window3, justify="center",fg='white',bg='gray16',text=variable1.get(), font=('Century Gothic', 10))
                         Arrive.place(x=430, y=220, height=25)
                         Gender = Label(window3, justify="center",fg='white',bg='gray16',text=v2.get(), font=('Century Gothic', 10))
                         Gender.place(x=430, y=60, height=25)
                         TrainNumber = Label(window3, justify="center",fg='white',bg='gray16',text=x1, font=('Century Gothic', 10))
                         TrainNumber.place(x=150, y=140, height=25)
                         
                         a=111111
                         b=999999
                         pnr=(random.randint(a, b))
                         Numberpnr=Label(window3, justify="center",fg='white',bg='gray16',text=pnr, font=('Century Gothic', 10))
                         Numberpnr.place(x=430, y=180, height=25) 


                         #global conn, cursor, x2
                         # passenger_data=[("pnr","enn7.get()","enn9.get()", "enn8.get()","x1")]
                        
                         # passenger_data=[(pnr,enn7.get(),enn9.get(), enn8.get(),x1)]
                         # c.execute("CREATE TABLE rail1 (passen_pnr integer, passen_name text, passen_gender text,passen_age integer,train_number integer)")
                         print("Command executed successfully...")
                         #insertion
                         #c.execute("INSERT INTO rail VALUES(pnr, enn7.get(),enn8.get(), str(enn9.get()
                         c.execute("INSERT INTO rail1 VALUES (?,?,?,?,?)",(pnr,enn7.get(),enn9.get(), enn8.get(),x1))
                         print("Command inserted successfully...")
                         # c.execute("SELECT*FROM rail")
                         c.execute("SELECT rowid,* FROM rail1")
                         print("Command selected successfully...")
                         items=c.fetchall()

                        #  print("S.No." + "\tPNR"+ "\tTrain No." +"   \tGender"+ "\tAge"+ "    \tName")
                        #  print("-----" + "\t---"+ "\t---------" +"   \t------"+ "\t---"+ "    \t----")
                        #  for item in items:
                        #      print(item[0] ,"    ",item[1] ," ",item[5],"   \t",item[3] ," ", item[4],"    \t", item[2])
                         

                         # for item in items:
                         #     print(item)
                         print("Command fetched successfully...")    
                         
                         #-------------------------------------------------------------------  
                         
                         Label(window3, text="Name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=560, y=60)
                         Label(window3, text="Gender",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=60)
                         Label(window3, text="Depart at",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=560, y=100)
                         Label(window3, text="Age",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=100)
                         Label(window3, text="Class",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=140)
                         Label(window3, text="Train no.",bg='gray16',fg='orange',font=('Century Gothic', 11)).place(x=560, y=140)
                         Label(window3, text="Train name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=560, y=180)
                         Label(window3, text="Source",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=560, y=220)
                         Label(window3, text="Destination",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=220)
                         # Label(window3, text="No. of tickets",bg='white', font=('Slab Serif', 11)).place(x=60, y=290)

                         Label(window3, text="PNR No.",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=180)

                         # Number = Label(window3, justify="center",bg='white',text=count, font=('Slab Serif', 10))
                         # Number.place(x=170, y=290,  height=25)

                         Name = Label(window3, justify="center",fg='white',bg='gray16',text=e12.get(), font=('Century Gothic', 10))
                         Name.place(x=670, y=60, height=25)
                         DepartTime = Label(window3, justify="center",fg='white',bg='gray16',text=xdprtTime, font=('Century Gothic', 10))
                         DepartTime.place(x=670, y=100, height=25)
                         TrainName = Label(window3, justify="center",fg='white',bg='gray16',text=xtrainn, font=('Century Gothic', 10))
                         TrainName.place(x=670, y=180, height=25)
                         Age = Label(window3, justify="center",fg='white',bg='gray16',text=e13.get(), font=('Century Gothic', 10))
                         Age.place(x=950, y=100, height=25)
                         Class = Label(window3, justify="center",fg='white',bg='gray16',text=variable2.get(), font=('Century Gothic', 10))
                         Class.place(x=950, y=140, height=25)
                         Depart = Label(window3, justify="center",fg='white',bg='gray16',text=variable.get(), font=('Century Gothic', 10))
                         Depart.place(x=670, y=220, height=25)
                         Arrive = Label(window3, justify="center",fg='white',bg='gray16',text=variable1.get(), font=('Century Gothic', 10))
                         Arrive.place(x=950, y=220, height=25)
                         Gender = Label(window3, justify="center",fg='white',bg='gray16',text=e14.get(), font=('Century Gothic', 10))
                         Gender.place(x=950, y=60, height=25)
                         TrainNumber = Label(window3, justify="center",fg='white',bg='gray16',text=x1, font=('Century Gothic', 10))
                         TrainNumber.place(x=670, y=140, height=25)
                         
                         a=111111
                         b=999999
                         pnr2=(random.randint(a, b))
                         Numberpnr=Label(window3, justify="center",fg='white',bg='gray16',text=pnr2, font=('Century Gothic', 10))
                         Numberpnr.place(x=950, y=180, height=25) 


                         #global conn, cursor, x2
                         # passenger_data=[("pnr","enn7.get()","enn9.get()", "enn8.get()","x1")]
                        
                         # passenger_data=[(pnr,enn7.get(),enn9.get(), enn8.get(),x1)]
                         # c.execute("CREATE TABLE rail1 (passen_pnr integer, passen_name text, passen_gender text,passen_age integer,train_number integer)")
                         print("Command executed successfully...")
                         #insertion
                         #c.execute("INSERT INTO rail VALUES(pnr, enn7.get(),enn8.get(), str(enn9.get()
                         c.execute("INSERT INTO rail1 VALUES (?,?,?,?,?)",(pnr2,e12.get(),e14.get(), e13.get(),x1))
                         print("Command inserted successfully...")
                         # c.execute("SELECT*FROM rail")
                         c.execute("SELECT rowid,* FROM rail1")
                         print("Command selected successfully...")
                         items=c.fetchall()

                        #  print("S.No." + "\tPNR"+ "\tTrain No." +"   \tGender"+ "\tAge"+ "    \tName")
                        #  print("-----" + "\t---"+ "\t---------" +"   \t------"+ "\t---"+ "    \t----")
                        #  for item in items:
                        #      print(item[0] ,"    ",item[1] ," ",item[5],"   \t",item[3] ," ", item[4],"    \t", item[2])
                         

                         # for item in items:
                         #     print(item)
                         print("Command fetched successfully...")   

                            #  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                         Label(window3, text="Name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=360)
                         Label(window3, text="Gender",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=360)
                         Label(window3, text="Depart at",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=400)
                         Label(window3, text="Age",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=400)
                         Label(window3, text="Class",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=440)
                         Label(window3, text="Train no.",bg='gray16',fg='orange',font=('Century Gothic', 11)).place(x=40, y=440)
                         Label(window3, text="Train name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=480)
                         Label(window3, text="Source",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=520)
                         Label(window3, text="Destination",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=520)
                         # Label(window3, text="No. of tickets",bg='white', font=('Slab Serif', 11)).place(x=60, y=290)

                         Label(window3, text="PNR No.",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=480)

                         # Number = Label(window3, justify="center",bg='white',text=count, font=('Slab Serif', 10))
                         # Number.place(x=170, y=290,  height=25)

                         Name = Label(window3, justify="center",fg='white',bg='gray16',text=e17.get(), font=('Century Gothic', 10))
                         Name.place(x=150, y=360, height=25)
                         DepartTime = Label(window3, justify="center",fg='white',bg='gray16',text=xdprtTime, font=('Century Gothic', 10))
                         DepartTime.place(x=150, y=400, height=25)
                         TrainName = Label(window3, justify="center",fg='white',bg='gray16',text=xtrainn, font=('Century Gothic', 10))
                         TrainName.place(x=150, y=480, height=25)
                         Age = Label(window3, justify="center",fg='white',bg='gray16',text=e18.get(), font=('Century Gothic', 10))
                         Age.place(x=430, y=400, height=25)
                         Class = Label(window3, justify="center",fg='white',bg='gray16',text=variable2.get(), font=('Century Gothic', 10))
                         Class.place(x=430, y=440, height=25)
                         Depart = Label(window3, justify="center",fg='white',bg='gray16',text=variable.get(), font=('Century Gothic', 10))
                         Depart.place(x=150, y=520, height=25)
                         Arrive = Label(window3, justify="center",fg='white',bg='gray16',text=variable1.get(), font=('Century Gothic', 10))
                         Arrive.place(x=430, y=520, height=25)
                         Gender = Label(window3, justify="center",fg='white',bg='gray16',text=e19.get(), font=('Century Gothic', 10))
                         Gender.place(x=430, y=360, height=25)
                         TrainNumber = Label(window3, justify="center",fg='white',bg='gray16',text=x1, font=('Century Gothic', 10))
                         TrainNumber.place(x=150, y=440, height=25)
                         
                         a=111111
                         b=999999
                         pnr3=(random.randint(a, b))
                         Numberpnr=Label(window3, justify="center",fg='white',bg='gray16',text=pnr3, font=('Century Gothic', 10))
                         Numberpnr.place(x=430, y=480, height=25) 


                         #global conn, cursor, x2
                         # passenger_data=[("pnr","enn7.get()","enn9.get()", "enn8.get()","x1")]
                        
                         # passenger_data=[(pnr,enn7.get(),enn9.get(), enn8.get(),x1)]
                         # c.execute("CREATE TABLE rail1 (passen_pnr integer, passen_name text, passen_gender text,passen_age integer,train_number integer)")
                         print("Command executed successfully...")
                         #insertion
                         #c.execute("INSERT INTO rail VALUES(pnr, enn7.get(),enn8.get(), str(enn9.get()
                         c.execute("INSERT INTO rail1 VALUES (?,?,?,?,?)",(pnr3,e17.get(),e19.get(), e18.get(),x1))
                         print("Command inserted successfully...")
                         # c.execute("SELECT*FROM rail")
                         c.execute("SELECT rowid,* FROM rail1")
                         print("Command selected successfully...")
                         items=c.fetchall()

                        #  print("S.No." + "\tPNR"+ "\tTrain No." +"   \tGender"+ "\tAge"+ "    \tName")
                        #  print("-----" + "\t---"+ "\t---------" +"   \t------"+ "\t---"+ "    \t----")
                        #  for item in items:
                        #      print(item[0] ,"    ",item[1] ," ",item[5],"   \t",item[3] ," ", item[4],"    \t", item[2])
                         

                         # for item in items:
                         #     print(item)
                         print("Command fetched successfully...") 

                         Label(window3, text="Name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=560, y=360)
                         Label(window3, text="Gender",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=360)
                         Label(window3, text="Depart at",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=560, y=400)
                         Label(window3, text="Age",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=400)
                         Label(window3, text="Class",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=440)
                         Label(window3, text="Train no.",bg='gray16',fg='orange',font=('Century Gothic', 11)).place(x=560, y=440)
                         Label(window3, text="Train name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=560, y=480)
                         Label(window3, text="Source",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=560, y=520)
                         Label(window3, text="Destination",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=520)
                         # Label(window3, text="No. of tickets",bg='white', font=('Slab Serif', 11)).place(x=60, y=290)

                         Label(window3, text="PNR No.",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=480)

                         # Number = Label(window3, justify="center",bg='white',text=count, font=('Slab Serif', 10))
                         # Number.place(x=170, y=290,  height=25)

                         Name = Label(window3, justify="center",fg='white',bg='gray16',text=e22.get(), font=('Century Gothic', 10))
                         Name.place(x=670, y=360, height=25)
                         DepartTime = Label(window3, justify="center",fg='white',bg='gray16',text=xdprtTime, font=('Century Gothic', 10))
                         DepartTime.place(x=670, y=400, height=25)
                         TrainName = Label(window3, justify="center",fg='white',bg='gray16',text=xtrainn, font=('Century Gothic', 10))
                         TrainName.place(x=670, y=480, height=25)
                         Age = Label(window3, justify="center",fg='white',bg='gray16',text=e23.get(), font=('Century Gothic', 10))
                         Age.place(x=950, y=400, height=25)
                         Class = Label(window3, justify="center",fg='white',bg='gray16',text=variable2.get(), font=('Century Gothic', 10))
                         Class.place(x=950, y=440, height=25)
                         Depart = Label(window3, justify="center",fg='white',bg='gray16',text=variable.get(), font=('Century Gothic', 10))
                         Depart.place(x=670, y=520, height=25)
                         Arrive = Label(window3, justify="center",fg='white',bg='gray16',text=variable1.get(), font=('Century Gothic', 10))
                         Arrive.place(x=950, y=520, height=25)
                         Gender = Label(window3, justify="center",fg='white',bg='gray16',text=e24.get(), font=('Century Gothic', 10))
                         Gender.place(x=950, y=360, height=25)
                         TrainNumber = Label(window3, justify="center",fg='white',bg='gray16',text=x1, font=('Century Gothic', 10))
                         TrainNumber.place(x=670, y=440, height=25)
                         
                         a=111111
                         b=999999
                         pnr4=(random.randint(a, b))
                         Numberpnr=Label(window3, justify="center",fg='white',bg='gray16',text=pnr4, font=('Century Gothic', 10))
                         Numberpnr.place(x=950, y=480, height=25) 


                         #global conn, cursor, x2
                         # passenger_data=[("pnr","enn7.get()","enn9.get()", "enn8.get()","x1")]
                        
                         # passenger_data=[(pnr,enn7.get(),enn9.get(), enn8.get(),x1)]
                         # c.execute("CREATE TABLE rail1 (passen_pnr integer, passen_name text, passen_gender text,passen_age integer,train_number integer)")
                         print("Command executed successfully...")
                         #insertion
                         #c.execute("INSERT INTO rail VALUES(pnr, enn7.get(),enn8.get(), str(enn9.get()
                         c.execute("INSERT INTO rail1 VALUES (?,?,?,?,?)",(pnr4,e22.get(),e24.get(), e23.get(),x1))
                         print("Command inserted successfully...")
                         # c.execute("SELECT*FROM rail")
                         c.execute("SELECT rowid,* FROM rail1")
                         print("Command selected successfully...")
                         items=c.fetchall()

                         print("S.No." + "\tPNR"+ "\tTrain No." +"\tGender"+ "\tAge"+ "\tName")
                         print("-----" + "\t---"+ "\t---------" +"\t------"+ "\t---"+ "\t----")
                         for item in items:
                             print(item[0] ,"    ",item[1] ," ",item[5],"\t",item[3] ,"", item[4],"\t", item[2])
                         

                         # for item in items:
                         #     print(item)
                         print("Command fetched successfully...") 
                         


                         Label(window3, text="Have a nice trip!!",fg='white',bg='gray16', font=('Century Gothic', 17)).place(x=450, y=600)

                         mainloop()




                    




                    global count
                    count=0
                    if len(enn7.get()) == 0 or len(enn8.get()) == 0 or len(enn9.get()) == 0 or len(e10.get()) == 0:
                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
                    elif len(e12.get()) != 0 and (len(e13.get()) == 0 or len(e14.get()) == 0 or len(e15.get()) == 0):
                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
                    elif len(e17.get()) != 0 and (len(e18.get()) == 0 or len(e19.get()) == 0 or len(e20.get()) == 0):
                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
                    elif len(e22.get()) != 0 and (len(e23.get()) == 0 or len(e24.get()) == 0 or len(e25.get()) == 0):
                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
                    elif (len(e12.get()) != 0 or len(e13.get()) != 0 or len(e14.get()) != 0 or len(
                            e15.get()) != 0) and (
                            len(e22.get()) != 0 or len(e23.get()) != 0 or len(e24.get()) != 0 or len(
                        e25.get()) != 0) and (
                            len(e17.get()) == 0 or (len(e18.get()) == 0 or len(e19.get()) == 0 or len(e20.get()) == 0)):
                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
                    elif (len(enn7.get()) != 0 or len(enn8.get()) != 0 or len(enn9.get()) != 0 or len(
                            e10.get()) != 0) and (
                            len(e17.get()) != 0 or len(e18.get()) != 0 or len(e19.get()) != 0 or len(
                        e20.get()) != 0) and (
                            len(e12.get()) == 0 or (len(e13.get()) == 0 or len(e14.get()) == 0 or len(e15.get()) == 0)):
                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
                    elif  enn7.get()!="" and e12.get()=="" and e17.get()=="" and e22.get()=="":
                        count=1
                        Show()
                    elif e12.get()!="" and e17.get()=="":
                        count=2
                        Show()
                        
                    elif e17.get()!="" and e22.get()=="":
                        count=3
                        Show()
                    elif e22.get()!="":
                        count=4
                        Show()
                    else:
                        Show()
                
                def Mainmenu():
                    window2.destroy()
                    createWindow()
                    window()
                m = Button(window2, text="Main Menu",font=('Century Gothic',15),width=60, bg="orange", fg="gray16", command=Mainmenu)
                m.place(x=500,y=640,width=120)    

                b = Button(window2, text='Submit', bg="Orange",fg="gray16", font=('Century Gothic', 15), command=Check1)
                b.place(x=670,y=640,width=100)
                # def Main():
                #              window2.destroy()
                #              createWindow()
                # m = Button(window2, text="Main Menu",font=('Century Gothic',15),width=60, bg="orange", fg="gray16", command=Main())
                # m.place(x=600,y=640,width=100)

                mainloop() 

            PassengerDetails()

        def PassengerDetails3():
            global x1, xtrainn, xdprtTime

            if f22.get()=="12273":
                x1=12273
            elif f22.get()=="122731":
                x1=122731
            elif f22.get() == "12497":
                x1 = 12497
            elif f22.get() == "124971":
                x1 = 124971
            elif f22.get() == "12380":
                x1 = 12380
            elif f22.get() == "123801":
                x1 = 123801 
            elif f22.get() == "16032":
                x1 = 16032   
            else:
                x1 = 1603201

            if f23.get()=="New Delhi Duronto":
                xtrainn="New Delhi Duronto"
                xdprtTime="8:35"
            elif f23.get()=="New Delhi Duronto":
                xtrainn="New Delhi Duronto"
                xdprtTime="8:35"
            elif f23.get() == "Shane Punjab":
                xtrainn = "Shane Punjab"
                xdprtTime="8:35"
            elif f23.get() == "Shane Punjab":
                xtrainn = "Shane Punjab"
                xdprtTime="8:35"
            elif f23.get() == "Jaliwala B Express":
                xtrainn = "Jaliwala B Express"
                xdprtTime="3:00"
            elif f23.get() == "Jaliwala B Express":
                xtrainn = "Jaliwala B Express"
                xdprtTime="3:00"
            elif f23.get() == "Andaman Express":
                xtrainn = "Andaman Express"
                xdprtTime="8:35"  
            else:
                xtrainn = "Andaman Express"
                xdprtTime="8:35"

            def PassengerDetails():
                window1.destroy()
                window2 = Tk()
                window2.title("Passenger Details")
                window2.config(bg="gray16")
                screen_width = window2.winfo_screenwidth()
                screen_height = window2.winfo_screenheight()
                width = 1280
                height = 720
                x = (screen_width / 2) - (width / 2)
                y = (screen_height / 2) - (height / 2)
                window2.geometry('%dx%d+%d+%d' % (width, height, x, y))
                window2.resizable(0, 0)

                height = 5
                width = 5
                for i in range(height):  # Rows
                    for j in range(width):  # Columns
                        e1 = Label(window2, text="Passenger 1",justify="center",font=('Century Gothic',15), bg="gray16", fg="Orange")
                        e1.place(x=0,y=100,width=165)
                        e2 = Label(window2, text="Passenger 2",justify="center",font=('Century Gothic',15), bg="gray16", fg="Orange", width="13")
                        e2.place(x=0,y=230,width=165)
                        e3 = Label(window2, text="Passenger 3",justify="center",font=('Century Gothic',15), bg="gray16", fg="Orange", width="13")
                        e3.place(x=0,y=360,width=165)
                        e4 = Label(window2, text="Passenger 4",justify="center",font=('Century Gothic',15), bg="gray16", fg="Orange", width="13")
                        e4.place(x=0,y=490,width=165)

                        name1=Label(window2, text="Name",justify="center",font=('Century Gothic',13), bg="gray16", fg="White", width="13")
                        name1.place(x=130,y=160,width=100)
                        name2=Label(window2, text="Name",justify="center",font=('Century Gothic',13), bg="gray16", fg="White", width="13")
                        name2.place(x=130,y=290,width=100)
                        name3=Label(window2, text="Name",justify="center",font=('Century Gothic',13), bg="gray16", fg="White", width="13")
                        name3.place(x=130,y=420,width=100)
                        name4=Label(window2, text="Name",justify="center",font=('Century Gothic',13), bg="gray16", fg="White", width="13")
                        name4.place(x=130,y=550,width=100)

                        age1=Label(window2, text="Age",justify="center",font=('Century Gothic',13), bg="gray16", fg="White", width="13")
                        age1.place(x=400,y=160,width=70)
                        age2=Label(window2, text="Age",justify="center",font=('Century Gothic',13), bg="gray16", fg="White", width="13")
                        age2.place(x=400,y=290,width=70)
                        age3=Label(window2, text="Age",justify="center",font=('Century Gothic',13), bg="gray16", fg="White", width="13")
                        age3.place(x=400,y=420,width=70)
                        age4=Label(window2, text="Age",justify="center",font=('Century Gothic',13), bg="gray16", fg="White", width="13")
                        age4.place(x=400,y=550,width=70)

                        gender1=Label(window2, text="Gender",justify="center",font=('Century Gothic',13), bg="gray16", fg="White", width="13")
                        gender1.place(x=600,y=160,width=70)
                        gender2=Label(window2, text="Gender",justify="center",font=('Century Gothic',13), bg="gray16", fg="White", width="13")
                        gender2.place(x=600,y=290,width=70)
                        gender3=Label(window2, text="Gender",justify="center",font=('Century Gothic',13), bg="gray16", fg="White", width="13")
                        gender3.place(x=600,y=420,width=70)
                        gender4=Label(window2, text="Gender",justify="center",font=('Century Gothic',13), bg="gray16", fg="White", width="13")
                        gender4.place(x=600,y=550,width=70)

                        idproof1=Label(window2, text="ID Proof",justify="center",font=('Century Gothic',13), bg="gray16", fg="White", width="13")
                        idproof1.place(x=870,y=160,width=70)
                        idproof2=Label(window2, text="ID Proof",justify="center",font=('Century Gothic',13), bg="gray16", fg="White", width="13")
                        idproof2.place(x=870,y=290,width=70)
                        idproof3=Label(window2, text="ID Proof",justify="center",font=('Century Gothic',13), bg="gray16", fg="White", width="13")
                        idproof3.place(x=870,y=420,width=70)
                        idproof4=Label(window2, text="ID Proof",justify="center",font=('Century Gothic',13), bg="gray16", fg="White", width="13")
                        idproof4.place(x=870,y=550,width=70)

                        enn7 = Entry(window2, justify="center", font=('Slab Serif', 13), bg="white",fg="gray16")
                        enn7.place(x=230,y=164,width=120)
                        enn8 = Entry(window2, justify="center", font=('Slab Serif', 13), bg="white",fg="gray16")
                        enn8.place(x=480,y=164,width=50)
                        enn9 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        enn9.place(x=700,y=164,width=10)
                        e10 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        e10.place(x=970,y=164,width=10)

                        e12 = Entry(window2, justify="center", font=('Slab Serif', 13), bg="white",fg="gray16")
                        e12.place(x=230,y=294,width=120)
                        e13 = Entry(window2, justify="center", font=('Slab Serif', 13), bg="white",fg="gray16")
                        e13.place(x=480,y=294,width=50)
                        e14 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        e14.place(x=700,y=294,width=10)
                        e15 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        e15.place(x=970,y=294,width=10)

                        # if 0>e12.get()>105:
                        #     tkinter.messagebox.showinfo('Error', 'Enter a valid age')
        
                        # if 0>e13.get()>105:
                        #     tkinter.messagebox.showinfo('Error', 'Enter a valid age')
                        
                        # if 0>e14.get()>105:
                        #     tkinter.messagebox.showinfo('Error', 'Enter a valid age')
                         
                        # if 0>e15.get()>105:
                        #     tkinter.messagebox.showinfo('Error', 'Enter a valid age')

                        e17 = Entry(window2, justify="center", font=('Slab Serif', 13), bg="white",fg="gray16")
                        e17.place(x=230,y=424,width=120)
                        e18 = Entry(window2, justify="center", font=('Slab Serif', 13), bg="white",fg="gray16")
                        e18.place(x=480,y=424,width=50)
                        e19 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        e19.place(x=700,y=424,width=10)
                        e20 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        e20.place(x=970,y=424,width=10)

                        e22 = Entry(window2, justify="center", font=('Slab Serif', 13), bg="white",fg="gray16")
                        e22.place(x=230,y=554,width=120)
                        e23 = Entry(window2, justify="center", font=('Slab Serif', 13), bg="white",fg="gray16")
                        e23.place(x=480,y=554,width=50)
                        e24 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        e24.place(x=700,y=554,width=10)
                        e25 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        e25.place(x=970,y=554,width=10)

                        # e1.insert(10, "S.no")
                        # enn2.insert(10, "Name")
                        # enn3.insert(10, "Age")
                        # enn4.insert(10, "Gender")
                        # e5.insert(10, "IdProof")
                        # e6.insert(10, "1")

                        # e11.insert(10, "2")
                        # e16.insert(10, "3")
                        # e21.insert(10, "4")

                        # e1.grid(row=0, column=0)
                        # enn2.grid(row=0, column=1)
                        # enn3.grid(row=0, column=2)
                        # enn4.grid(row=0, column=3)
                        # e5.grid(row=0, column=4)
                        # e6.grid(row=1, column=0)
                        # enn7.grid(row=1, column=1)
                        # enn8.grid(row=1, column=2)
                        # enn9.grid(row=1, column=3)
                        # e10.grid(row=1, column=4)

                        # e11.grid(row=2, column=0)
                        # e12.grid(row=2, column=1)
                        # e13.grid(row=2, column=2)
                        # e14.grid(row=2, column=3)
                        # e15.grid(row=2, column=4)

                        # e16.grid(row=3, column=0)
                        # e17.grid(row=3, column=1)
                        # e18.grid(row=3, column=2)
                        # e19.grid(row=3, column=3)
                        # e20.grid(row=3, column=4)

                        # e21.grid(row=4, column=0)
                        # e22.grid(row=4, column=1)
                        # e23.grid(row=4, column=2)
                        # e24.grid(row=4, column=3)
                        # e25.grid(row=4, column=4)

                        def fun(*args):
                            enn9.insert(10, v2.get())

                        def fun1(*args):
                            e14.insert(10, v3.get())

                        def fun2(*args):
                            e19.insert(10, v4.get())

                        def fun3(*args):
                            e24.insert(10, v5.get())

                        def fun4(*args):
                            e10.insert(10, v6.get())

                        def fun5(*args):
                            e15.insert(10, v7.get())

                        def fun6(*args):
                            e20.insert(10, v8.get())

                        def fun7(*args):
                            e25.insert(10, v9.get())

                        v2 = StringVar(window2)
                        genderr = {'Male', 'Female'}
                        v2.set('Select')
                        v2.trace("w", fun)
                        popupMenu1 = OptionMenu(window2, v2, *genderr)
                        popupMenu1.config(font=('Slab Serif', 13), bg="gray16", fg="orange")
                        popupMenu1.place(x=700,y=160,width=100)

                        v3 = StringVar(window2)
                        genderr1 = {'Male', 'Female'}
                        v3.set('Select')
                        v3.trace("w", fun1)
                        popupMenu2 = OptionMenu(window2, v3, *genderr1)
                        popupMenu2.config(font=('Slab Serif', 13), bg="gray16", fg="orange")
                        popupMenu2.place(x=700,y=290,width=100)

                        v4 = StringVar(window2)
                        genderr2 = {'Male', 'Female'}
                        v4.set('Select')
                        v4.trace("w", fun2)
                        popupMenu3 = OptionMenu(window2, v4, *genderr2)
                        popupMenu3.config(font=('Slab Serif', 13), bg="gray16", fg="orange")
                        popupMenu3.place(x=700,y=420,width=100)

                        v5 = StringVar(window2)
                        genderr3 = {'Male', 'Female'}
                        v5.set('Select')
                        v5.trace("w", fun3)
                        popupMenu4 = OptionMenu(window2, v5, *genderr3)
                        popupMenu4.config(font=('Slab Serif', 13), bg="gray16", fg="orange")
                        popupMenu4.place(x=700,y=550,width=100)

                        v6 = StringVar(window2)
                        proof = {'Aadhar card', 'Pan card'}
                        v6.set('Select')
                        v6.trace("w", fun4)
                        popup = OptionMenu(window2, v6, *proof)
                        popup.config(font=('Slab Serif', 13), bg="gray16",fg="orange")
                        popup.place(x=970,y=160,width=150)

                        v7 = StringVar(window2)
                        proof = {'Aadhar card', 'Pan card'}
                        v7.set('Select')
                        v7.trace("w", fun5)
                        popup = OptionMenu(window2, v7, *proof)
                        popup.config(font=('Slab Serif', 13), bg="gray16",fg="orange")
                        popup.place(x=970,y=290,width=150)

                        v8 = StringVar(window2)
                        proof = {'Aadhar card', 'Pan card'}
                        v8.set('Select')
                        v8.trace("w", fun6)
                        popup = OptionMenu(window2, v8, *proof)
                        popup.config(font=('Slab Serif', 13), bg="gray16",fg="orange")
                        popup.place(x=970,y=420,width=150)
                        v9 = StringVar(window2)
                        proof = {'Aadhar card', 'Pan card'}
                        v9.set('Select')
                        v9.trace("w", fun7)
                        popup = OptionMenu(window2, v9, *proof)
                        popup.config(font=('Slab Serif', 13), bg="gray16",fg="orange")

                        popup.place(x=970,y=550,width=150)

                def Check1():

                    def Show():
                        global x1,count
                        if enn7.get()!="" and e12.get()=="" and e17.get()=="" and e22.get()=="":
                         
                         
                         count=1
                         window3 = Tk()

                         window3.title("Ticket")
                         screen_width = window3.winfo_screenwidth()
                         screen_height = window3.winfo_screenheight()
                         width = 580
                         height = 480
                         x = (screen_width / 2) - (width / 2)
                         y = (screen_height / 2) - (height / 2)
                         window3.geometry('%dx%d+%d+%d' % (width, height, x, y))
                         window3.resizable(0, 0)
                         window3.config(bg='gray16')

                         w11 = 580
                         h11 = 480
                         canvas3 = Canvas(window3, width=w11, height=h11)
                         canvas3.config(bg='gray16')
                         canvas3.create_rectangle(0, 0,580,30, fill= "orange")
                         canvas3.create_line(40, 90, 270, 90, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 130, 270, 130, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 170, 270, 170, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 210, 270, 210, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 250, 270, 250, fill="gray13", width=0.0000001)

                         canvas3.create_line(320, 90, 550, 90, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 130, 550, 130, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 170, 550, 170, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 210, 550, 210, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 250, 550, 250, fill="gray13", width=0.0000001)
                         canvas3.pack()
                         Label(window3, text="PNR Status Details",bg='orange',fg='gray16', font=('Century Gothic', 11)).place(x=10, y=2)
                         
                         Label(window3, text="Name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=60)
                         Label(window3, text="Gender",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=60)
                         Label(window3, text="Depart at",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=100)
                         Label(window3, text="Age",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=100)
                         Label(window3, text="Class",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=140)
                         Label(window3, text="Train no.",bg='gray16',fg='orange',font=('Century Gothic', 11)).place(x=40, y=140)
                         Label(window3, text="Train name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=180)
                         Label(window3, text="Source",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=220)
                         Label(window3, text="Destination",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=220)
                         # Label(window3, text="No. of tickets",bg='white', font=('Slab Serif', 11)).place(x=60, y=290)

                         Label(window3, text="PNR No.",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=180)

                         # Number = Label(window3, justify="center",bg='white',text=count, font=('Slab Serif', 10))
                         # Number.place(x=170, y=290,  height=25)

                         Name = Label(window3, justify="center",fg='white',bg='gray16',text=enn7.get(), font=('Century Gothic', 10))
                         Name.place(x=150, y=60, height=25)
                         DepartTime = Label(window3, justify="center",fg='white',bg='gray16',text=xdprtTime, font=('Century Gothic', 10))
                         DepartTime.place(x=150, y=100, height=25)
                         TrainName = Label(window3, justify="center",fg='white',bg='gray16',text=xtrainn, font=('Century Gothic', 10))
                         TrainName.place(x=150, y=180, height=25)
                         Age = Label(window3, justify="center",fg='white',bg='gray16',text=enn8.get(), font=('Century Gothic', 10))
                         Age.place(x=430, y=100, height=25)
                         Class = Label(window3, justify="center",fg='white',bg='gray16',text=variable2.get(), font=('Century Gothic', 10))
                         Class.place(x=430, y=140, height=25)
                         Depart = Label(window3, justify="center",fg='white',bg='gray16',text=variable.get(), font=('Century Gothic', 10))
                         Depart.place(x=150, y=220, height=25)
                         Arrive = Label(window3, justify="center",fg='white',bg='gray16',text=variable1.get(), font=('Century Gothic', 10))
                         Arrive.place(x=430, y=220, height=25)
                         Gender = Label(window3, justify="center",fg='white',bg='gray16',text=v2.get(), font=('Century Gothic', 10))
                         Gender.place(x=430, y=60, height=25)
                         TrainNumber = Label(window3, justify="center",fg='white',bg='gray16',text=x1, font=('Century Gothic', 10))
                         TrainNumber.place(x=150, y=140, height=25)
                         
                         a=111111
                         b=999999
                         pnr=(random.randint(a, b))
                         Numberpnr=Label(window3, justify="center",fg='white',bg='gray16',text=pnr, font=('Century Gothic', 10))
                         Numberpnr.place(x=430, y=180, height=25) 


                         #global conn, cursor, x2
                         # passenger_data=[("pnr","enn7.get()","enn9.get()", "enn8.get()","x1")]
                        
                         # passenger_data=[(pnr,enn7.get(),enn9.get(), enn8.get(),x1)]
                         # c.execute("CREATE TABLE rail1 (passen_pnr integer, passen_name text, passen_gender text,passen_age integer,train_number integer)")
                         print("Command executed successfully...")
                         #insertion
                         #c.execute("INSERT INTO rail VALUES(pnr, enn7.get(),enn8.get(), str(enn9.get()
                         c.execute("INSERT INTO rail1 VALUES (?,?,?,?,?)",(pnr,enn7.get(),enn9.get(), enn8.get(),x1))
                         print("Command inserted successfully...")
                         # c.execute("SELECT*FROM rail")
                         c.execute("SELECT rowid,* FROM rail1")
                         print("Command selected successfully...")
                         items=c.fetchall()

                         print("S.No." + "\tPNR"+ "\tTrain No." +"   \tGender"+ "\tAge"+ "\tName")
                         print("-----" + "\t---"+ "\t---------" +"   \t------"+ "\t---"+ "\t----")
                         for item in items:
                             print(item[0] ,"    ",item[1] ," ",item[5],"   \t",item[3] ," ", item[4],"\t", item[2])
                         

                         # for item in items:
                         #     print(item)
                         print("Command fetched successfully...")    
                        


                         Label(window3, text="Have a nice trip!!",fg='white',bg='gray16', font=('Century Gothic', 17)).place(x=200, y=340)

                         mainloop()

                        elif e12.get()!="" and e17.get()=="":
                         
                         count=2
                         window3 = Tk()

                         window3.title("Ticket")
                         screen_width = window3.winfo_screenwidth()
                         screen_height = window3.winfo_screenheight()
                         width = 1160
                         height = 480
                         x = (screen_width / 2) - (width / 2)
                         y = (screen_height / 2) - (height / 2)
                         window3.geometry('%dx%d+%d+%d' % (width, height, x, y))
                         window3.resizable(0, 0)
                         window3.config(bg='gray16')

                         w11 = 1160
                         h11 = 480
                         canvas3 = Canvas(window3, width=w11, height=h11)
                         canvas3.config(bg='gray16')
                         canvas3.create_rectangle(0, 0,1160,30, fill= "orange")
                         canvas3.create_line(40, 90, 270, 90, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 130, 270, 130, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 170, 270, 170, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 210, 270, 210, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 250, 270, 250, fill="gray13", width=0.0000001)

                         canvas3.create_line(320, 90, 550, 90, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 130, 550, 130, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 170, 550, 170, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 210, 550, 210, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 250, 550, 250, fill="gray13", width=0.0000001)

                         canvas3.create_line(560, 90, 790, 90, fill="gray13", width=0.0000001)
                         canvas3.create_line(560, 130, 790, 130, fill="gray13", width=0.0000001)
                         canvas3.create_line(560, 170, 790, 170, fill="gray13", width=0.0000001)
                         canvas3.create_line(560, 210, 790, 210, fill="gray13", width=0.0000001)
                         canvas3.create_line(560, 250, 790, 250, fill="gray13", width=0.0000001)

                         canvas3.create_line(840, 90, 1070, 90, fill="gray13", width=0.0000001)
                         canvas3.create_line(840, 130, 1070, 130, fill="gray13", width=0.0000001)
                         canvas3.create_line(840, 170, 1070, 170, fill="gray13", width=0.0000001)
                         canvas3.create_line(840, 210, 1070, 210, fill="gray13", width=0.0000001)
                         canvas3.create_line(840, 250, 1070, 250, fill="gray13", width=0.0000001)
                         canvas3.pack()
                         Label(window3, text="PNR Status Details",bg='orange',fg='gray16', font=('Century Gothic', 11)).place(x=10, y=2)
                         
                         Label(window3, text="Name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=60)
                         Label(window3, text="Gender",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=60)
                         Label(window3, text="Depart at",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=100)
                         Label(window3, text="Age",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=100)
                         Label(window3, text="Class",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=140)
                         Label(window3, text="Train no.",bg='gray16',fg='orange',font=('Century Gothic', 11)).place(x=40, y=140)
                         Label(window3, text="Train name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=180)
                         Label(window3, text="Source",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=220)
                         Label(window3, text="Destination",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=220)
                         # Label(window3, text="No. of tickets",bg='white', font=('Slab Serif', 11)).place(x=60, y=290)

                         Label(window3, text="PNR No.",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=180)

                         # Number = Label(window3, justify="center",bg='white',text=count, font=('Slab Serif', 10))
                         # Number.place(x=170, y=290,  height=25)

                         Name = Label(window3, justify="center",fg='white',bg='gray16',text=enn7.get(), font=('Century Gothic', 10))
                         Name.place(x=150, y=60, height=25)
                         DepartTime = Label(window3, justify="center",fg='white',bg='gray16',text=xdprtTime, font=('Century Gothic', 10))
                         DepartTime.place(x=150, y=100, height=25)
                         TrainName = Label(window3, justify="center",fg='white',bg='gray16',text=xtrainn, font=('Century Gothic', 10))
                         TrainName.place(x=150, y=180, height=25)
                         Age = Label(window3, justify="center",fg='white',bg='gray16',text=enn8.get(), font=('Century Gothic', 10))
                         Age.place(x=430, y=100, height=25)
                         Class = Label(window3, justify="center",fg='white',bg='gray16',text=variable2.get(), font=('Century Gothic', 10))
                         Class.place(x=430, y=140, height=25)
                         Depart = Label(window3, justify="center",fg='white',bg='gray16',text=variable.get(), font=('Century Gothic', 10))
                         Depart.place(x=150, y=220, height=25)
                         Arrive = Label(window3, justify="center",fg='white',bg='gray16',text=variable1.get(), font=('Century Gothic', 10))
                         Arrive.place(x=430, y=220, height=25)
                         Gender = Label(window3, justify="center",fg='white',bg='gray16',text=v2.get(), font=('Century Gothic', 10))
                         Gender.place(x=430, y=60, height=25)
                         TrainNumber = Label(window3, justify="center",fg='white',bg='gray16',text=x1, font=('Century Gothic', 10))
                         TrainNumber.place(x=150, y=140, height=25)
                         
                         a=111111
                         b=999999
                         pnr=(random.randint(a, b))
                         Numberpnr=Label(window3, justify="center",fg='white',bg='gray16',text=pnr, font=('Century Gothic', 10))
                         Numberpnr.place(x=430, y=180, height=25) 


                         #global conn, cursor, x2
                         # passenger_data=[("pnr","enn7.get()","enn9.get()", "enn8.get()","x1")]
                        
                         # passenger_data=[(pnr,enn7.get(),enn9.get(), enn8.get(),x1)]
                         # c.execute("CREATE TABLE rail1 (passen_pnr integer, passen_name text, passen_gender text,passen_age integer,train_number integer)")
                         print("Command executed successfully...")
                         #insertion
                         #c.execute("INSERT INTO rail VALUES(pnr, enn7.get(),enn8.get(), str(enn9.get()
                         c.execute("INSERT INTO rail1 VALUES (?,?,?,?,?)",(pnr,enn7.get(),enn9.get(), enn8.get(),x1))
                         print("Command inserted successfully...")
                         # c.execute("SELECT*FROM rail")
                         c.execute("SELECT rowid,* FROM rail1")
                         print("Command selected successfully...")
                         items=c.fetchall()

                         print("S.No." + "\tPNR"+ "\tTrain No." +"   \tGender"+ "  \tAge"+ "\tName")
                         print("-----" + "\t---"+ "\t---------" +"   \t------"+ "  \t---"+ "\t----")
                         for item in items:
                             print(item[0] ,"    ",item[1] ," ",item[5],"   \t",item[3] ,"   ", item[4],"\t", item[2])
                         

                         # for item in items:
                         #     print(item)
                         print("Command fetched successfully...")    
                         
                         #-------------------------------------------------------------------  
                         
                         Label(window3, text="Name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=560, y=60)
                         Label(window3, text="Gender",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=60)
                         Label(window3, text="Depart at",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=560, y=100)
                         Label(window3, text="Age",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=100)
                         Label(window3, text="Class",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=140)
                         Label(window3, text="Train no.",bg='gray16',fg='orange',font=('Century Gothic', 11)).place(x=560, y=140)
                         Label(window3, text="Train name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=560, y=180)
                         Label(window3, text="Source",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=560, y=220)
                         Label(window3, text="Destination",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=220)
                         # Label(window3, text="No. of tickets",bg='white', font=('Slab Serif', 11)).place(x=60, y=290)

                         Label(window3, text="PNR No.",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=180)

                         # Number = Label(window3, justify="center",bg='white',text=count, font=('Slab Serif', 10))
                         # Number.place(x=170, y=290,  height=25)

                         Name = Label(window3, justify="center",fg='white',bg='gray16',text=e12.get(), font=('Century Gothic', 10))
                         Name.place(x=670, y=60, height=25)
                         DepartTime = Label(window3, justify="center",fg='white',bg='gray16',text=xdprtTime, font=('Century Gothic', 10))
                         DepartTime.place(x=670, y=100, height=25)
                         TrainName = Label(window3, justify="center",fg='white',bg='gray16',text=xtrainn, font=('Century Gothic', 10))
                         TrainName.place(x=670, y=180, height=25)
                         Age = Label(window3, justify="center",fg='white',bg='gray16',text=e13.get(), font=('Century Gothic', 10))
                         Age.place(x=950, y=100, height=25)
                         Class = Label(window3, justify="center",fg='white',bg='gray16',text=variable2.get(), font=('Century Gothic', 10))
                         Class.place(x=950, y=140, height=25)
                         Depart = Label(window3, justify="center",fg='white',bg='gray16',text=variable.get(), font=('Century Gothic', 10))
                         Depart.place(x=670, y=220, height=25)
                         Arrive = Label(window3, justify="center",fg='white',bg='gray16',text=variable1.get(), font=('Century Gothic', 10))
                         Arrive.place(x=950, y=220, height=25)
                         Gender = Label(window3, justify="center",fg='white',bg='gray16',text=e14.get(), font=('Century Gothic', 10))
                         Gender.place(x=950, y=60, height=25)
                         TrainNumber = Label(window3, justify="center",fg='white',bg='gray16',text=x1, font=('Century Gothic', 10))
                         TrainNumber.place(x=670, y=140, height=25)
                         
                         a=111111
                         b=999999
                         pnr2=(random.randint(a, b))
                         Numberpnr=Label(window3, justify="center",fg='white',bg='gray16',text=pnr2, font=('Century Gothic', 10))
                         Numberpnr.place(x=950, y=180, height=25) 


                         #global conn, cursor, x2
                         # passenger_data=[("pnr","enn7.get()","enn9.get()", "enn8.get()","x1")]
                        
                         # passenger_data=[(pnr,enn7.get(),enn9.get(), enn8.get(),x1)]
                         # c.execute("CREATE TABLE rail1 (passen_pnr integer, passen_name text, passen_gender text,passen_age integer,train_number integer)")
                         print("Command executed successfully...")
                         #insertion
                         #c.execute("INSERT INTO rail VALUES(pnr, enn7.get(),enn8.get(), str(enn9.get()
                         c.execute("INSERT INTO rail1 VALUES (?,?,?,?,?)",(pnr2,e12.get(),e14.get(), e13.get(),x1))
                         print("Command inserted successfully...")
                         # c.execute("SELECT*FROM rail")
                         c.execute("SELECT rowid,* FROM rail1")
                         print("Command selected successfully...")
                         items=c.fetchall()

                         print("S.No." + "\tPNR"+ "\tTrain No." +"   \tGender"+ "  \tAge"+ "\tName")
                         print("-----" + "\t---"+ "\t---------" +"   \t------"+ "  \t---"+ "\t----")
                         for item in items:
                             print(item[0] ,"    ",item[1] ," ",item[5],"   \t",item[3] ,"   ", item[4],"\t", item[2])
                         

                         # for item in items:
                         #     print(item)
                         print("Command fetched successfully...")     
                        


                         Label(window3, text="Have a nice trip!!",fg='white',bg='gray16', font=('Century Gothic', 17)).place(x=500, y=340)

                         mainloop()
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                        elif e17.get()!="" and e22.get()=="":
                         count=3
                         window3 = Tk()

                         window3.title("Ticket")
                         screen_width = window3.winfo_screenwidth()
                         screen_height = window3.winfo_screenheight()
                         width = 1160
                         height = 800
                         x = (screen_width / 2) - (width / 2)
                         y = (screen_height / 2) - (height / 2)
                         window3.geometry('%dx%d+%d+%d' % (width, height, x, y))
                         window3.resizable(0, 0)
                         window3.config(bg='gray16')

                         w11 = 1160
                         h11 = 800
                         canvas3 = Canvas(window3, width=w11, height=h11)
                         canvas3.config(bg='gray16')
                         canvas3.create_rectangle(0, 0,1160,30, fill= "orange")
                         canvas3.create_line(40, 90, 270, 90, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 130, 270, 130, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 170, 270, 170, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 210, 270, 210, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 250, 270, 250, fill="gray13", width=0.0000001)

                         canvas3.create_line(320, 90, 550, 90, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 130, 550, 130, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 170, 550, 170, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 210, 550, 210, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 250, 550, 250, fill="gray13", width=0.0000001)

                         canvas3.create_line(560, 90, 790, 90, fill="gray13", width=0.0000001)
                         canvas3.create_line(560, 130, 790, 130, fill="gray13", width=0.0000001)
                         canvas3.create_line(560, 170, 790, 170, fill="gray13", width=0.0000001)
                         canvas3.create_line(560, 210, 790, 210, fill="gray13", width=0.0000001)
                         canvas3.create_line(560, 250, 790, 250, fill="gray13", width=0.0000001)

                         canvas3.create_line(840, 90, 1070, 90, fill="gray13", width=0.0000001)
                         canvas3.create_line(840, 130, 1070, 130, fill="gray13", width=0.0000001)
                         canvas3.create_line(840, 170, 1070, 170, fill="gray13", width=0.0000001)
                         canvas3.create_line(840, 210, 1070, 210, fill="gray13", width=0.0000001)
                         canvas3.create_line(840, 250, 1070, 250, fill="gray13", width=0.0000001)

                         canvas3.create_line(40, 390, 270, 390, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 430, 270, 430, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 470, 270, 470, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 510, 270, 510, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 550, 270, 550, fill="gray13", width=0.0000001)

                         canvas3.create_line(320, 390, 550, 390, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 430, 550, 430, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 470, 550, 470, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 510, 550, 510, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 550, 550, 550, fill="gray13", width=0.0000001)
                         canvas3.pack()
                         Label(window3, text="PNR Status Details",bg='orange',fg='gray16', font=('Century Gothic', 11)).place(x=10, y=2)
                         
                         Label(window3, text="Name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=60)
                         Label(window3, text="Gender",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=60)
                         Label(window3, text="Depart at",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=100)
                         Label(window3, text="Age",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=100)
                         Label(window3, text="Class",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=140)
                         Label(window3, text="Train no.",bg='gray16',fg='orange',font=('Century Gothic', 11)).place(x=40, y=140)
                         Label(window3, text="Train name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=180)
                         Label(window3, text="Source",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=220)
                         Label(window3, text="Destination",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=220)
                         # Label(window3, text="No. of tickets",bg='white', font=('Slab Serif', 11)).place(x=60, y=290)

                         Label(window3, text="PNR No.",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=180)

                         # Number = Label(window3, justify="center",bg='white',text=count, font=('Slab Serif', 10))
                         # Number.place(x=170, y=290,  height=25)

                         Name = Label(window3, justify="center",fg='white',bg='gray16',text=enn7.get(), font=('Century Gothic', 10))
                         Name.place(x=150, y=60, height=25)
                         DepartTime = Label(window3, justify="center",fg='white',bg='gray16',text=xdprtTime, font=('Century Gothic', 10))
                         DepartTime.place(x=150, y=100, height=25)
                         TrainName = Label(window3, justify="center",fg='white',bg='gray16',text=xtrainn, font=('Century Gothic', 10))
                         TrainName.place(x=150, y=180, height=25)
                         Age = Label(window3, justify="center",fg='white',bg='gray16',text=enn8.get(), font=('Century Gothic', 10))
                         Age.place(x=430, y=100, height=25)
                         Class = Label(window3, justify="center",fg='white',bg='gray16',text=variable2.get(), font=('Century Gothic', 10))
                         Class.place(x=430, y=140, height=25)
                         Depart = Label(window3, justify="center",fg='white',bg='gray16',text=variable.get(), font=('Century Gothic', 10))
                         Depart.place(x=150, y=220, height=25)
                         Arrive = Label(window3, justify="center",fg='white',bg='gray16',text=variable1.get(), font=('Century Gothic', 10))
                         Arrive.place(x=430, y=220, height=25)
                         Gender = Label(window3, justify="center",fg='white',bg='gray16',text=v2.get(), font=('Century Gothic', 10))
                         Gender.place(x=430, y=60, height=25)
                         TrainNumber = Label(window3, justify="center",fg='white',bg='gray16',text=x1, font=('Century Gothic', 10))
                         TrainNumber.place(x=150, y=140, height=25)
                         
                         a=111111
                         b=999999
                         pnr=(random.randint(a, b))
                         Numberpnr=Label(window3, justify="center",fg='white',bg='gray16',text=pnr, font=('Century Gothic', 10))
                         Numberpnr.place(x=430, y=180, height=25) 


                         #global conn, cursor, x2
                         # passenger_data=[("pnr","enn7.get()","enn9.get()", "enn8.get()","x1")]
                        
                         # passenger_data=[(pnr,enn7.get(),enn9.get(), enn8.get(),x1)]
                         # c.execute("CREATE TABLE rail1 (passen_pnr integer, passen_name text, passen_gender text,passen_age integer,train_number integer)")
                         print("Command executed successfully...")
                         #insertion
                         #c.execute("INSERT INTO rail VALUES(pnr, enn7.get(),enn8.get(), str(enn9.get()
                         c.execute("INSERT INTO rail1 VALUES (?,?,?,?,?)",(pnr,enn7.get(),enn9.get(), enn8.get(),x1))
                         print("Command inserted successfully...")
                         # c.execute("SELECT*FROM rail")
                         c.execute("SELECT rowid,* FROM rail1")
                         print("Command selected successfully...")
                         items=c.fetchall()

                         print("S.No." + "\tPNR"+ "\tTrain No." +"   \tGender"+ "\tAge"+ "    \tName")
                         print("-----" + "\t---"+ "\t---------" +"   \t------"+ "\t---"+ "    \t----")
                         for item in items:
                             print(item[0] ,"    ",item[1] ," ",item[5],"   \t",item[3] ," ", item[4],"    \t", item[2])
                         

                         # for item in items:
                         #     print(item)
                         print("Command fetched successfully...")    
                         
                         #-------------------------------------------------------------------  
                         
                         Label(window3, text="Name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=560, y=60)
                         Label(window3, text="Gender",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=60)
                         Label(window3, text="Depart at",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=560, y=100)
                         Label(window3, text="Age",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=100)
                         Label(window3, text="Class",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=140)
                         Label(window3, text="Train no.",bg='gray16',fg='orange',font=('Century Gothic', 11)).place(x=560, y=140)
                         Label(window3, text="Train name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=560, y=180)
                         Label(window3, text="Source",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=560, y=220)
                         Label(window3, text="Destination",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=220)
                         # Label(window3, text="No. of tickets",bg='white', font=('Slab Serif', 11)).place(x=60, y=290)

                         Label(window3, text="PNR No.",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=180)

                         # Number = Label(window3, justify="center",bg='white',text=count, font=('Slab Serif', 10))
                         # Number.place(x=170, y=290,  height=25)

                         Name = Label(window3, justify="center",fg='white',bg='gray16',text=e12.get(), font=('Century Gothic', 10))
                         Name.place(x=670, y=60, height=25)
                         DepartTime = Label(window3, justify="center",fg='white',bg='gray16',text=xdprtTime, font=('Century Gothic', 10))
                         DepartTime.place(x=670, y=100, height=25)
                         TrainName = Label(window3, justify="center",fg='white',bg='gray16',text=xtrainn, font=('Century Gothic', 10))
                         TrainName.place(x=670, y=180, height=25)
                         Age = Label(window3, justify="center",fg='white',bg='gray16',text=e13.get(), font=('Century Gothic', 10))
                         Age.place(x=950, y=100, height=25)
                         Class = Label(window3, justify="center",fg='white',bg='gray16',text=variable2.get(), font=('Century Gothic', 10))
                         Class.place(x=950, y=140, height=25)
                         Depart = Label(window3, justify="center",fg='white',bg='gray16',text=variable.get(), font=('Century Gothic', 10))
                         Depart.place(x=670, y=220, height=25)
                         Arrive = Label(window3, justify="center",fg='white',bg='gray16',text=variable1.get(), font=('Century Gothic', 10))
                         Arrive.place(x=950, y=220, height=25)
                         Gender = Label(window3, justify="center",fg='white',bg='gray16',text=e14.get(), font=('Century Gothic', 10))
                         Gender.place(x=950, y=60, height=25)
                         TrainNumber = Label(window3, justify="center",fg='white',bg='gray16',text=x1, font=('Century Gothic', 10))
                         TrainNumber.place(x=670, y=140, height=25)
                         
                         a=111111
                         b=999999
                         pnr2=(random.randint(a, b))
                         Numberpnr=Label(window3, justify="center",fg='white',bg='gray16',text=pnr2, font=('Century Gothic', 10))
                         Numberpnr.place(x=950, y=180, height=25) 


                         #global conn, cursor, x2
                         # passenger_data=[("pnr","enn7.get()","enn9.get()", "enn8.get()","x1")]
                        
                         # passenger_data=[(pnr,enn7.get(),enn9.get(), enn8.get(),x1)]
                         # c.execute("CREATE TABLE rail1 (passen_pnr integer, passen_name text, passen_gender text,passen_age integer,train_number integer)")
                         print("Command executed successfully...")
                         #insertion
                         #c.execute("INSERT INTO rail VALUES(pnr, enn7.get(),enn8.get(), str(enn9.get()
                         c.execute("INSERT INTO rail1 VALUES (?,?,?,?,?)",(pnr2,e12.get(),e14.get(), e13.get(),x1))
                         print("Command inserted successfully...")
                         # c.execute("SELECT*FROM rail")
                         c.execute("SELECT rowid,* FROM rail1")
                         print("Command selected successfully...")
                         items=c.fetchall()

                         print("S.No." + "\tPNR"+ "\tTrain No." +"   \tGender"+ "\tAge"+ "    \tName")
                         print("-----" + "\t---"+ "\t---------" +"   \t------"+ "\t---"+ "    \t----")
                         for item in items:
                             print(item[0] ,"    ",item[1] ," ",item[5],"   \t",item[3] ," ", item[4],"    \t", item[2])
                         

                         # for item in items:
                         #     print(item)
                         print("Command fetched successfully...")   

                            #  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                         Label(window3, text="Name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=360)
                         Label(window3, text="Gender",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=360)
                         Label(window3, text="Depart at",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=400)
                         Label(window3, text="Age",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=400)
                         Label(window3, text="Class",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=440)
                         Label(window3, text="Train no.",bg='gray16',fg='orange',font=('Century Gothic', 11)).place(x=40, y=440)
                         Label(window3, text="Train name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=480)
                         Label(window3, text="Source",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=520)
                         Label(window3, text="Destination",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=520)
                         # Label(window3, text="No. of tickets",bg='white', font=('Slab Serif', 11)).place(x=60, y=290)

                         Label(window3, text="PNR No.",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=480)

                         # Number = Label(window3, justify="center",bg='white',text=count, font=('Slab Serif', 10))
                         # Number.place(x=170, y=290,  height=25)

                         Name = Label(window3, justify="center",fg='white',bg='gray16',text=e17.get(), font=('Century Gothic', 10))
                         Name.place(x=150, y=360, height=25)
                         DepartTime = Label(window3, justify="center",fg='white',bg='gray16',text=xdprtTime, font=('Century Gothic', 10))
                         DepartTime.place(x=150, y=400, height=25)
                         TrainName = Label(window3, justify="center",fg='white',bg='gray16',text=xtrainn, font=('Century Gothic', 10))
                         TrainName.place(x=150, y=480, height=25)
                         Age = Label(window3, justify="center",fg='white',bg='gray16',text=e18.get(), font=('Century Gothic', 10))
                         Age.place(x=430, y=400, height=25)
                         Class = Label(window3, justify="center",fg='white',bg='gray16',text=variable2.get(), font=('Century Gothic', 10))
                         Class.place(x=430, y=440, height=25)
                         Depart = Label(window3, justify="center",fg='white',bg='gray16',text=variable.get(), font=('Century Gothic', 10))
                         Depart.place(x=150, y=520, height=25)
                         Arrive = Label(window3, justify="center",fg='white',bg='gray16',text=variable1.get(), font=('Century Gothic', 10))
                         Arrive.place(x=430, y=520, height=25)
                         Gender = Label(window3, justify="center",fg='white',bg='gray16',text=e19.get(), font=('Century Gothic', 10))
                         Gender.place(x=430, y=360, height=25)
                         TrainNumber = Label(window3, justify="center",fg='white',bg='gray16',text=x1, font=('Century Gothic', 10))
                         TrainNumber.place(x=150, y=440, height=25)
                         
                         a=111111
                         b=999999
                         pnr3=(random.randint(a, b))
                         Numberpnr=Label(window3, justify="center",fg='white',bg='gray16',text=pnr3, font=('Century Gothic', 10))
                         Numberpnr.place(x=430, y=480, height=25) 


                         #global conn, cursor, x2
                         # passenger_data=[("pnr","enn7.get()","enn9.get()", "enn8.get()","x1")]
                        
                         # passenger_data=[(pnr,enn7.get(),enn9.get(), enn8.get(),x1)]
                         # c.execute("CREATE TABLE rail1 (passen_pnr integer, passen_name text, passen_gender text,passen_age integer,train_number integer)")
                         print("Command executed successfully...")
                         #insertion
                         #c.execute("INSERT INTO rail VALUES(pnr, enn7.get(),enn8.get(), str(enn9.get()
                         c.execute("INSERT INTO rail1 VALUES (?,?,?,?,?)",(pnr3,e17.get(),e19.get(), e18.get(),x1))
                         print("Command inserted successfully...")
                         # c.execute("SELECT*FROM rail")
                         c.execute("SELECT rowid,* FROM rail1")
                         print("Command selected successfully...")
                         items=c.fetchall()

                         print("S.No." + "\tPNR"+ "\tTrain No." +"   \tGender"+ "\tAge"+ "    \tName")
                         print("-----" + "\t---"+ "\t---------" +"   \t------"+ "\t---"+ "    \t----")
                         for item in items:
                             print(item[0] ,"    ",item[1] ," ",item[5],"   \t",item[3] ," ", item[4],"    \t", item[2])
                         

                         # for item in items:
                         #     print(item)
                         print("Command fetched successfully...")  

                        


                         Label(window3, text="Have a nice trip!!",fg='white',bg='gray16', font=('Century Gothic', 17)).place(x=800, y=340)

                         mainloop()
                        else:
                         count=4
                         window3 = Tk()

                         window3.title("Ticket")
                         screen_width = window3.winfo_screenwidth()
                         screen_height = window3.winfo_screenheight()
                         width = 1160
                         height = 800
                         x = (screen_width / 2) - (width / 2)
                         y = (screen_height / 2) - (height / 2)
                         window3.geometry('%dx%d+%d+%d' % (width, height, x, y))
                         window3.resizable(0, 0)
                         window3.config(bg='gray16')

                         w11 = 1160
                         h11 = 800
                         canvas3 = Canvas(window3, width=w11, height=h11)
                         canvas3.config(bg='gray16')
                         canvas3.create_rectangle(0, 0,1160,30, fill= "orange")
                         canvas3.create_line(40, 90, 270, 90, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 130, 270, 130, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 170, 270, 170, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 210, 270, 210, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 250, 270, 250, fill="gray13", width=0.0000001)

                         canvas3.create_line(320, 90, 550, 90, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 130, 550, 130, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 170, 550, 170, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 210, 550, 210, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 250, 550, 250, fill="gray13", width=0.0000001)

                         canvas3.create_line(560, 90, 790, 90, fill="gray13", width=0.0000001)
                         canvas3.create_line(560, 130, 790, 130, fill="gray13", width=0.0000001)
                         canvas3.create_line(560, 170, 790, 170, fill="gray13", width=0.0000001)
                         canvas3.create_line(560, 210, 790, 210, fill="gray13", width=0.0000001)
                         canvas3.create_line(560, 250, 790, 250, fill="gray13", width=0.0000001)

                         canvas3.create_line(840, 90, 1070, 90, fill="gray13", width=0.0000001)
                         canvas3.create_line(840, 130, 1070, 130, fill="gray13", width=0.0000001)
                         canvas3.create_line(840, 170, 1070, 170, fill="gray13", width=0.0000001)
                         canvas3.create_line(840, 210, 1070, 210, fill="gray13", width=0.0000001)
                         canvas3.create_line(840, 250, 1070, 250, fill="gray13", width=0.0000001)

                         canvas3.create_line(40, 390, 270, 390, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 430, 270, 430, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 470, 270, 470, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 510, 270, 510, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 550, 270, 550, fill="gray13", width=0.0000001)

                         canvas3.create_line(320, 390, 550, 390, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 430, 550, 430, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 470, 550, 470, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 510, 550, 510, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 550, 550, 550, fill="gray13", width=0.0000001)

                         canvas3.create_line(560, 390, 790, 390, fill="gray13", width=0.0000001)
                         canvas3.create_line(560, 430, 790, 430, fill="gray13", width=0.0000001)
                         canvas3.create_line(560, 470, 790, 470, fill="gray13", width=0.0000001)
                         canvas3.create_line(560, 510, 790, 510, fill="gray13", width=0.0000001)
                         canvas3.create_line(560, 550, 790, 550, fill="gray13", width=0.0000001)

                         canvas3.create_line(840, 390, 1070, 390, fill="gray13", width=0.0000001)
                         canvas3.create_line(840, 430, 1070, 430, fill="gray13", width=0.0000001)
                         canvas3.create_line(840, 470, 1070, 470, fill="gray13", width=0.0000001)
                         canvas3.create_line(840, 510, 1070, 510, fill="gray13", width=0.0000001)
                         canvas3.create_line(840, 550, 1070, 550, fill="gray13", width=0.0000001)
                         canvas3.pack()
                         Label(window3, text="PNR Status Details",bg='orange',fg='gray16', font=('Century Gothic', 11)).place(x=10, y=2)
                         
                         Label(window3, text="Name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=60)
                         Label(window3, text="Gender",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=60)
                         Label(window3, text="Depart at",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=100)
                         Label(window3, text="Age",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=100)
                         Label(window3, text="Class",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=140)
                         Label(window3, text="Train no.",bg='gray16',fg='orange',font=('Century Gothic', 11)).place(x=40, y=140)
                         Label(window3, text="Train name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=180)
                         Label(window3, text="Source",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=220)
                         Label(window3, text="Destination",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=220)
                         # Label(window3, text="No. of tickets",bg='white', font=('Slab Serif', 11)).place(x=60, y=290)

                         Label(window3, text="PNR No.",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=180)

                         # Number = Label(window3, justify="center",bg='white',text=count, font=('Slab Serif', 10))
                         # Number.place(x=170, y=290,  height=25)

                         Name = Label(window3, justify="center",fg='white',bg='gray16',text=enn7.get(), font=('Century Gothic', 10))
                         Name.place(x=150, y=60, height=25)
                         DepartTime = Label(window3, justify="center",fg='white',bg='gray16',text=xdprtTime, font=('Century Gothic', 10))
                         DepartTime.place(x=150, y=100, height=25)
                         TrainName = Label(window3, justify="center",fg='white',bg='gray16',text=xtrainn, font=('Century Gothic', 10))
                         TrainName.place(x=150, y=180, height=25)
                         Age = Label(window3, justify="center",fg='white',bg='gray16',text=enn8.get(), font=('Century Gothic', 10))
                         Age.place(x=430, y=100, height=25)
                         Class = Label(window3, justify="center",fg='white',bg='gray16',text=variable2.get(), font=('Century Gothic', 10))
                         Class.place(x=430, y=140, height=25)
                         Depart = Label(window3, justify="center",fg='white',bg='gray16',text=variable.get(), font=('Century Gothic', 10))
                         Depart.place(x=150, y=220, height=25)
                         Arrive = Label(window3, justify="center",fg='white',bg='gray16',text=variable1.get(), font=('Century Gothic', 10))
                         Arrive.place(x=430, y=220, height=25)
                         Gender = Label(window3, justify="center",fg='white',bg='gray16',text=v2.get(), font=('Century Gothic', 10))
                         Gender.place(x=430, y=60, height=25)
                         TrainNumber = Label(window3, justify="center",fg='white',bg='gray16',text=x1, font=('Century Gothic', 10))
                         TrainNumber.place(x=150, y=140, height=25)
                         
                         a=111111
                         b=999999
                         pnr=(random.randint(a, b))
                         Numberpnr=Label(window3, justify="center",fg='white',bg='gray16',text=pnr, font=('Century Gothic', 10))
                         Numberpnr.place(x=430, y=180, height=25) 


                         #global conn, cursor, x2
                         # passenger_data=[("pnr","enn7.get()","enn9.get()", "enn8.get()","x1")]
                        
                         # passenger_data=[(pnr,enn7.get(),enn9.get(), enn8.get(),x1)]
                         # c.execute("CREATE TABLE rail1 (passen_pnr integer, passen_name text, passen_gender text,passen_age integer,train_number integer)")
                         print("Command executed successfully...")
                         #insertion
                         #c.execute("INSERT INTO rail VALUES(pnr, enn7.get(),enn8.get(), str(enn9.get()
                         c.execute("INSERT INTO rail1 VALUES (?,?,?,?,?)",(pnr,enn7.get(),enn9.get(), enn8.get(),x1))
                         print("Command inserted successfully...")
                         # c.execute("SELECT*FROM rail")
                         c.execute("SELECT rowid,* FROM rail1")
                         print("Command selected successfully...")
                         items=c.fetchall()

                        #  print("S.No." + "\tPNR"+ "\tTrain No." +"   \tGender"+ "\tAge"+ "    \tName")
                        #  print("-----" + "\t---"+ "\t---------" +"   \t------"+ "\t---"+ "    \t----")
                        #  for item in items:
                        #      print(item[0] ,"    ",item[1] ," ",item[5],"   \t",item[3] ," ", item[4],"    \t", item[2])
                         

                         # for item in items:
                         #     print(item)
                         print("Command fetched successfully...")    
                         
                         #-------------------------------------------------------------------  
                         
                         Label(window3, text="Name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=560, y=60)
                         Label(window3, text="Gender",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=60)
                         Label(window3, text="Depart at",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=560, y=100)
                         Label(window3, text="Age",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=100)
                         Label(window3, text="Class",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=140)
                         Label(window3, text="Train no.",bg='gray16',fg='orange',font=('Century Gothic', 11)).place(x=560, y=140)
                         Label(window3, text="Train name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=560, y=180)
                         Label(window3, text="Source",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=560, y=220)
                         Label(window3, text="Destination",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=220)
                         # Label(window3, text="No. of tickets",bg='white', font=('Slab Serif', 11)).place(x=60, y=290)

                         Label(window3, text="PNR No.",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=180)

                         # Number = Label(window3, justify="center",bg='white',text=count, font=('Slab Serif', 10))
                         # Number.place(x=170, y=290,  height=25)

                         Name = Label(window3, justify="center",fg='white',bg='gray16',text=e12.get(), font=('Century Gothic', 10))
                         Name.place(x=670, y=60, height=25)
                         DepartTime = Label(window3, justify="center",fg='white',bg='gray16',text=xdprtTime, font=('Century Gothic', 10))
                         DepartTime.place(x=670, y=100, height=25)
                         TrainName = Label(window3, justify="center",fg='white',bg='gray16',text=xtrainn, font=('Century Gothic', 10))
                         TrainName.place(x=670, y=180, height=25)
                         Age = Label(window3, justify="center",fg='white',bg='gray16',text=e13.get(), font=('Century Gothic', 10))
                         Age.place(x=950, y=100, height=25)
                         Class = Label(window3, justify="center",fg='white',bg='gray16',text=variable2.get(), font=('Century Gothic', 10))
                         Class.place(x=950, y=140, height=25)
                         Depart = Label(window3, justify="center",fg='white',bg='gray16',text=variable.get(), font=('Century Gothic', 10))
                         Depart.place(x=670, y=220, height=25)
                         Arrive = Label(window3, justify="center",fg='white',bg='gray16',text=variable1.get(), font=('Century Gothic', 10))
                         Arrive.place(x=950, y=220, height=25)
                         Gender = Label(window3, justify="center",fg='white',bg='gray16',text=e14.get(), font=('Century Gothic', 10))
                         Gender.place(x=950, y=60, height=25)
                         TrainNumber = Label(window3, justify="center",fg='white',bg='gray16',text=x1, font=('Century Gothic', 10))
                         TrainNumber.place(x=670, y=140, height=25)
                         
                         a=111111
                         b=999999
                         pnr2=(random.randint(a, b))
                         Numberpnr=Label(window3, justify="center",fg='white',bg='gray16',text=pnr2, font=('Century Gothic', 10))
                         Numberpnr.place(x=950, y=180, height=25) 


                         #global conn, cursor, x2
                         # passenger_data=[("pnr","enn7.get()","enn9.get()", "enn8.get()","x1")]
                        
                         # passenger_data=[(pnr,enn7.get(),enn9.get(), enn8.get(),x1)]
                         # c.execute("CREATE TABLE rail1 (passen_pnr integer, passen_name text, passen_gender text,passen_age integer,train_number integer)")
                         print("Command executed successfully...")
                         #insertion
                         #c.execute("INSERT INTO rail VALUES(pnr, enn7.get(),enn8.get(), str(enn9.get()
                         c.execute("INSERT INTO rail1 VALUES (?,?,?,?,?)",(pnr2,e12.get(),e14.get(), e13.get(),x1))
                         print("Command inserted successfully...")
                         # c.execute("SELECT*FROM rail")
                         c.execute("SELECT rowid,* FROM rail1")
                         print("Command selected successfully...")
                         items=c.fetchall()

                        #  print("S.No." + "\tPNR"+ "\tTrain No." +"   \tGender"+ "\tAge"+ "    \tName")
                        #  print("-----" + "\t---"+ "\t---------" +"   \t------"+ "\t---"+ "    \t----")
                        #  for item in items:
                        #      print(item[0] ,"    ",item[1] ," ",item[5],"   \t",item[3] ," ", item[4],"    \t", item[2])
                         

                         # for item in items:
                         #     print(item)
                         print("Command fetched successfully...")   

                            #  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                         Label(window3, text="Name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=360)
                         Label(window3, text="Gender",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=360)
                         Label(window3, text="Depart at",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=400)
                         Label(window3, text="Age",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=400)
                         Label(window3, text="Class",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=440)
                         Label(window3, text="Train no.",bg='gray16',fg='orange',font=('Century Gothic', 11)).place(x=40, y=440)
                         Label(window3, text="Train name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=480)
                         Label(window3, text="Source",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=520)
                         Label(window3, text="Destination",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=520)
                         # Label(window3, text="No. of tickets",bg='white', font=('Slab Serif', 11)).place(x=60, y=290)

                         Label(window3, text="PNR No.",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=480)

                         # Number = Label(window3, justify="center",bg='white',text=count, font=('Slab Serif', 10))
                         # Number.place(x=170, y=290,  height=25)

                         Name = Label(window3, justify="center",fg='white',bg='gray16',text=e17.get(), font=('Century Gothic', 10))
                         Name.place(x=150, y=360, height=25)
                         DepartTime = Label(window3, justify="center",fg='white',bg='gray16',text=xdprtTime, font=('Century Gothic', 10))
                         DepartTime.place(x=150, y=400, height=25)
                         TrainName = Label(window3, justify="center",fg='white',bg='gray16',text=xtrainn, font=('Century Gothic', 10))
                         TrainName.place(x=150, y=480, height=25)
                         Age = Label(window3, justify="center",fg='white',bg='gray16',text=e18.get(), font=('Century Gothic', 10))
                         Age.place(x=430, y=400, height=25)
                         Class = Label(window3, justify="center",fg='white',bg='gray16',text=variable2.get(), font=('Century Gothic', 10))
                         Class.place(x=430, y=440, height=25)
                         Depart = Label(window3, justify="center",fg='white',bg='gray16',text=variable.get(), font=('Century Gothic', 10))
                         Depart.place(x=150, y=520, height=25)
                         Arrive = Label(window3, justify="center",fg='white',bg='gray16',text=variable1.get(), font=('Century Gothic', 10))
                         Arrive.place(x=430, y=520, height=25)
                         Gender = Label(window3, justify="center",fg='white',bg='gray16',text=e19.get(), font=('Century Gothic', 10))
                         Gender.place(x=430, y=360, height=25)
                         TrainNumber = Label(window3, justify="center",fg='white',bg='gray16',text=x1, font=('Century Gothic', 10))
                         TrainNumber.place(x=150, y=440, height=25)
                         
                         a=111111
                         b=999999
                         pnr3=(random.randint(a, b))
                         Numberpnr=Label(window3, justify="center",fg='white',bg='gray16',text=pnr3, font=('Century Gothic', 10))
                         Numberpnr.place(x=430, y=480, height=25) 


                         #global conn, cursor, x2
                         # passenger_data=[("pnr","enn7.get()","enn9.get()", "enn8.get()","x1")]
                        
                         # passenger_data=[(pnr,enn7.get(),enn9.get(), enn8.get(),x1)]
                         # c.execute("CREATE TABLE rail1 (passen_pnr integer, passen_name text, passen_gender text,passen_age integer,train_number integer)")
                         print("Command executed successfully...")
                         #insertion
                         #c.execute("INSERT INTO rail VALUES(pnr, enn7.get(),enn8.get(), str(enn9.get()
                         c.execute("INSERT INTO rail1 VALUES (?,?,?,?,?)",(pnr3,e17.get(),e19.get(), e18.get(),x1))
                         print("Command inserted successfully...")
                         # c.execute("SELECT*FROM rail")
                         c.execute("SELECT rowid,* FROM rail1")
                         print("Command selected successfully...")
                         items=c.fetchall()

                        #  print("S.No." + "\tPNR"+ "\tTrain No." +"   \tGender"+ "\tAge"+ "    \tName")
                        #  print("-----" + "\t---"+ "\t---------" +"   \t------"+ "\t---"+ "    \t----")
                        #  for item in items:
                        #      print(item[0] ,"    ",item[1] ," ",item[5],"   \t",item[3] ," ", item[4],"    \t", item[2])
                         

                         # for item in items:
                         #     print(item)
                         print("Command fetched successfully...") 

                         Label(window3, text="Name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=560, y=360)
                         Label(window3, text="Gender",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=360)
                         Label(window3, text="Depart at",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=560, y=400)
                         Label(window3, text="Age",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=400)
                         Label(window3, text="Class",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=440)
                         Label(window3, text="Train no.",bg='gray16',fg='orange',font=('Century Gothic', 11)).place(x=560, y=440)
                         Label(window3, text="Train name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=560, y=480)
                         Label(window3, text="Source",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=560, y=520)
                         Label(window3, text="Destination",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=520)
                         # Label(window3, text="No. of tickets",bg='white', font=('Slab Serif', 11)).place(x=60, y=290)

                         Label(window3, text="PNR No.",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=480)

                         # Number = Label(window3, justify="center",bg='white',text=count, font=('Slab Serif', 10))
                         # Number.place(x=170, y=290,  height=25)

                         Name = Label(window3, justify="center",fg='white',bg='gray16',text=e22.get(), font=('Century Gothic', 10))
                         Name.place(x=670, y=360, height=25)
                         DepartTime = Label(window3, justify="center",fg='white',bg='gray16',text=xdprtTime, font=('Century Gothic', 10))
                         DepartTime.place(x=670, y=400, height=25)
                         TrainName = Label(window3, justify="center",fg='white',bg='gray16',text=xtrainn, font=('Century Gothic', 10))
                         TrainName.place(x=670, y=480, height=25)
                         Age = Label(window3, justify="center",fg='white',bg='gray16',text=e23.get(), font=('Century Gothic', 10))
                         Age.place(x=950, y=400, height=25)
                         Class = Label(window3, justify="center",fg='white',bg='gray16',text=variable2.get(), font=('Century Gothic', 10))
                         Class.place(x=950, y=440, height=25)
                         Depart = Label(window3, justify="center",fg='white',bg='gray16',text=variable.get(), font=('Century Gothic', 10))
                         Depart.place(x=670, y=520, height=25)
                         Arrive = Label(window3, justify="center",fg='white',bg='gray16',text=variable1.get(), font=('Century Gothic', 10))
                         Arrive.place(x=950, y=520, height=25)
                         Gender = Label(window3, justify="center",fg='white',bg='gray16',text=e24.get(), font=('Century Gothic', 10))
                         Gender.place(x=950, y=360, height=25)
                         TrainNumber = Label(window3, justify="center",fg='white',bg='gray16',text=x1, font=('Century Gothic', 10))
                         TrainNumber.place(x=670, y=440, height=25)
                         
                         a=111111
                         b=999999
                         pnr4=(random.randint(a, b))
                         Numberpnr=Label(window3, justify="center",fg='white',bg='gray16',text=pnr4, font=('Century Gothic', 10))
                         Numberpnr.place(x=950, y=480, height=25) 


                         #global conn, cursor, x2
                         # passenger_data=[("pnr","enn7.get()","enn9.get()", "enn8.get()","x1")]
                        
                         # passenger_data=[(pnr,enn7.get(),enn9.get(), enn8.get(),x1)]
                         # c.execute("CREATE TABLE rail1 (passen_pnr integer, passen_name text, passen_gender text,passen_age integer,train_number integer)")
                         print("Command executed successfully...")
                         #insertion
                         #c.execute("INSERT INTO rail VALUES(pnr, enn7.get(),enn8.get(), str(enn9.get()
                         c.execute("INSERT INTO rail1 VALUES (?,?,?,?,?)",(pnr4,e22.get(),e24.get(), e23.get(),x1))
                         print("Command inserted successfully...")
                         # c.execute("SELECT*FROM rail")
                         c.execute("SELECT rowid,* FROM rail1")
                         print("Command selected successfully...")
                         items=c.fetchall()

                         print("S.No." + "\tPNR"+ "\tTrain No." +"\tGender"+ "\tAge"+ "\tName")
                         print("-----" + "\t---"+ "\t---------" +"\t------"+ "\t---"+ "\t----")
                         for item in items:
                             print(item[0] ,"    ",item[1] ," ",item[5],"\t",item[3] ,"", item[4],"\t", item[2])
                         

                         # for item in items:
                         #     print(item)
                         print("Command fetched successfully...") 
                         


                         Label(window3, text="Have a nice trip!!",fg='white',bg='gray16', font=('Century Gothic', 17)).place(x=450, y=600)

                         mainloop()




                    




                    global count
                    count=0
                    if len(enn7.get()) == 0 or len(enn8.get()) == 0 or len(enn9.get()) == 0 or len(e10.get()) == 0:
                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
                    elif len(e12.get()) != 0 and (len(e13.get()) == 0 or len(e14.get()) == 0 or len(e15.get()) == 0):
                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
                    elif len(e17.get()) != 0 and (len(e18.get()) == 0 or len(e19.get()) == 0 or len(e20.get()) == 0):
                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
                    elif len(e22.get()) != 0 and (len(e23.get()) == 0 or len(e24.get()) == 0 or len(e25.get()) == 0):
                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
                    elif (len(e12.get()) != 0 or len(e13.get()) != 0 or len(e14.get()) != 0 or len(
                            e15.get()) != 0) and (
                            len(e22.get()) != 0 or len(e23.get()) != 0 or len(e24.get()) != 0 or len(
                        e25.get()) != 0) and (
                            len(e17.get()) == 0 or (len(e18.get()) == 0 or len(e19.get()) == 0 or len(e20.get()) == 0)):
                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
                    elif (len(enn7.get()) != 0 or len(enn8.get()) != 0 or len(enn9.get()) != 0 or len(
                            e10.get()) != 0) and (
                            len(e17.get()) != 0 or len(e18.get()) != 0 or len(e19.get()) != 0 or len(
                        e20.get()) != 0) and (
                            len(e12.get()) == 0 or (len(e13.get()) == 0 or len(e14.get()) == 0 or len(e15.get()) == 0)):
                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
                    elif  enn7.get()!="" and e12.get()=="" and e17.get()=="" and e22.get()=="":
                        count=1
                        Show()
                    elif e12.get()!="" and e17.get()=="":
                        count=2
                        Show()
                        
                    elif e17.get()!="" and e22.get()=="":
                        count=3
                        Show()
                    elif e22.get()!="":
                        count=4
                        Show()
                    else:
                        Show()
                
                def Mainmenu():
                    window2.destroy()
                    createWindow()
                    window()
                m = Button(window2, text="Main Menu",font=('Century Gothic',15),width=60, bg="orange", fg="gray16", command=Mainmenu)
                m.place(x=500,y=640,width=120)    

                b = Button(window2, text='Submit', bg="Orange",fg="gray16", font=('Century Gothic', 15), command=Check1)
                b.place(x=670,y=640,width=100)
                # def Main():
                #              window2.destroy()
                #              createWindow()
                # m = Button(window2, text="Main Menu",font=('Century Gothic',15),width=60, bg="orange", fg="gray16", command=Main())
                # m.place(x=600,y=640,width=100)

                mainloop()

            PassengerDetails()

        def PassengerDetails4():
            global x1, xtrainn, xdprtTime

            if f29.get()=="22857":
                x1=22857
            elif f29.get()=="228571":
                x1=228571
            elif f29.get() == "12029":
                x1 = 12029
            elif f29.get() == "120291":
                x1 = 120291
            elif f29.get() == "12317":
                x1 = 12317
            elif f29.get() == "123171":
                x1 = 123171 
            elif f29.get() == "12270":
                x1 = 12270   
            else:
                x1 = 122701

            if f30.get()=="SRC ANVT SF":
                xtrainn="SRC ANVT SF"
                xdprtTime="12:30"
            elif f30.get()=="SRC ANVT SF":
                xtrainn="SRC ANVT SF"
                xdprtTime="12:30"
            elif f30.get() == "Shatabdi":
                xtrainn = "Shatabdi"
                xdprtTime="12:30"
            elif f30.get() == "Shatabdi":
                xtrainn = "Shatabdi"
                xdprtTime="12:30"
            elif f30.get() == "Akal Takhat Express":
                xtrainn = "Akal Takhat Express"
                xdprtTime="6:45"
            elif f30.get() == "Akal Takhat Express":
                xtrainn = "Akal Takhat Express"
                xdprtTime="6:45"
            elif f30.get() == "MAS Duronto Express":
                xtrainn = "MAS Duronto Express"
                xdprtTime="12:30"  
            else:
                xtrainn = "MAS Duronto Express"
                xdprtTime="12:30"

            def PassengerDetails():
                window1.destroy()
                window2 = Tk()
                window2.title("Passenger Details")
                window2.config(bg="gray16")
                screen_width = window2.winfo_screenwidth()
                screen_height = window2.winfo_screenheight()
                width = 1280
                height = 720
                x = (screen_width / 2) - (width / 2)
                y = (screen_height / 2) - (height / 2)
                window2.geometry('%dx%d+%d+%d' % (width, height, x, y))
                window2.resizable(0, 0)

                height = 5
                width = 5
                for i in range(height):  # Rows
                    for j in range(width):  # Columns
                        e1 = Label(window2, text="Passenger 1",justify="center",font=('Century Gothic',15), bg="gray16", fg="Orange")
                        e1.place(x=0,y=100,width=165)
                        e2 = Label(window2, text="Passenger 2",justify="center",font=('Century Gothic',15), bg="gray16", fg="Orange", width="13")
                        e2.place(x=0,y=230,width=165)
                        e3 = Label(window2, text="Passenger 3",justify="center",font=('Century Gothic',15), bg="gray16", fg="Orange", width="13")
                        e3.place(x=0,y=360,width=165)
                        e4 = Label(window2, text="Passenger 4",justify="center",font=('Century Gothic',15), bg="gray16", fg="Orange", width="13")
                        e4.place(x=0,y=490,width=165)

                        name1=Label(window2, text="Name",justify="center",font=('Century Gothic',13), bg="gray16", fg="White", width="13")
                        name1.place(x=130,y=160,width=100)
                        name2=Label(window2, text="Name",justify="center",font=('Century Gothic',13), bg="gray16", fg="White", width="13")
                        name2.place(x=130,y=290,width=100)
                        name3=Label(window2, text="Name",justify="center",font=('Century Gothic',13), bg="gray16", fg="White", width="13")
                        name3.place(x=130,y=420,width=100)
                        name4=Label(window2, text="Name",justify="center",font=('Century Gothic',13), bg="gray16", fg="White", width="13")
                        name4.place(x=130,y=550,width=100)

                        age1=Label(window2, text="Age",justify="center",font=('Century Gothic',13), bg="gray16", fg="White", width="13")
                        age1.place(x=400,y=160,width=70)
                        age2=Label(window2, text="Age",justify="center",font=('Century Gothic',13), bg="gray16", fg="White", width="13")
                        age2.place(x=400,y=290,width=70)
                        age3=Label(window2, text="Age",justify="center",font=('Century Gothic',13), bg="gray16", fg="White", width="13")
                        age3.place(x=400,y=420,width=70)
                        age4=Label(window2, text="Age",justify="center",font=('Century Gothic',13), bg="gray16", fg="White", width="13")
                        age4.place(x=400,y=550,width=70)

                        gender1=Label(window2, text="Gender",justify="center",font=('Century Gothic',13), bg="gray16", fg="White", width="13")
                        gender1.place(x=600,y=160,width=70)
                        gender2=Label(window2, text="Gender",justify="center",font=('Century Gothic',13), bg="gray16", fg="White", width="13")
                        gender2.place(x=600,y=290,width=70)
                        gender3=Label(window2, text="Gender",justify="center",font=('Century Gothic',13), bg="gray16", fg="White", width="13")
                        gender3.place(x=600,y=420,width=70)
                        gender4=Label(window2, text="Gender",justify="center",font=('Century Gothic',13), bg="gray16", fg="White", width="13")
                        gender4.place(x=600,y=550,width=70)

                        idproof1=Label(window2, text="ID Proof",justify="center",font=('Century Gothic',13), bg="gray16", fg="White", width="13")
                        idproof1.place(x=870,y=160,width=70)
                        idproof2=Label(window2, text="ID Proof",justify="center",font=('Century Gothic',13), bg="gray16", fg="White", width="13")
                        idproof2.place(x=870,y=290,width=70)
                        idproof3=Label(window2, text="ID Proof",justify="center",font=('Century Gothic',13), bg="gray16", fg="White", width="13")
                        idproof3.place(x=870,y=420,width=70)
                        idproof4=Label(window2, text="ID Proof",justify="center",font=('Century Gothic',13), bg="gray16", fg="White", width="13")
                        idproof4.place(x=870,y=550,width=70)

                        enn7 = Entry(window2, justify="center", font=('Slab Serif', 13), bg="white",fg="gray16")
                        enn7.place(x=230,y=164,width=120)
                        enn8 = Entry(window2, justify="center", font=('Slab Serif', 13), bg="white",fg="gray16")
                        enn8.place(x=480,y=164,width=50)
                        enn9 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        enn9.place(x=700,y=164,width=10)
                        e10 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        e10.place(x=970,y=164,width=10)

                        e12 = Entry(window2, justify="center", font=('Slab Serif', 13), bg="white",fg="gray16")
                        e12.place(x=230,y=294,width=120)
                        e13 = Entry(window2, justify="center", font=('Slab Serif', 13), bg="white",fg="gray16")
                        e13.place(x=480,y=294,width=50)
                        e14 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        e14.place(x=700,y=294,width=10)
                        e15 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        e15.place(x=970,y=294,width=10)

                        # if 0>e12.get()>105:
                        #     tkinter.messagebox.showinfo('Error', 'Enter a valid age')
        
                        # if 0>e13.get()>105:
                        #     tkinter.messagebox.showinfo('Error', 'Enter a valid age')
                        
                        # if 0>e14.get()>105:
                        #     tkinter.messagebox.showinfo('Error', 'Enter a valid age')
                         
                        # if 0>e15.get()>105:
                        #     tkinter.messagebox.showinfo('Error', 'Enter a valid age')
                        
                        e17 = Entry(window2, justify="center", font=('Slab Serif', 13), bg="white",fg="gray16")
                        e17.place(x=230,y=424,width=120)
                        e18 = Entry(window2, justify="center", font=('Slab Serif', 13), bg="white",fg="gray16")
                        e18.place(x=480,y=424,width=50)
                        e19 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        e19.place(x=700,y=424,width=10)
                        e20 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        e20.place(x=970,y=424,width=10)

                        e22 = Entry(window2, justify="center", font=('Slab Serif', 13), bg="white",fg="gray16")
                        e22.place(x=230,y=554,width=120)
                        e23 = Entry(window2, justify="center", font=('Slab Serif', 13), bg="white",fg="gray16")
                        e23.place(x=480,y=554,width=50)
                        e24 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        e24.place(x=700,y=554,width=10)
                        e25 = Entry(window2, justify="center", font=('Slab Serif', 3))
                        e25.place(x=970,y=554,width=10)

                        # e1.insert(10, "S.no")
                        # enn2.insert(10, "Name")
                        # enn3.insert(10, "Age")
                        # enn4.insert(10, "Gender")
                        # e5.insert(10, "IdProof")
                        # e6.insert(10, "1")

                        # e11.insert(10, "2")
                        # e16.insert(10, "3")
                        # e21.insert(10, "4")

                        # e1.grid(row=0, column=0)
                        # enn2.grid(row=0, column=1)
                        # enn3.grid(row=0, column=2)
                        # enn4.grid(row=0, column=3)
                        # e5.grid(row=0, column=4)
                        # e6.grid(row=1, column=0)
                        # enn7.grid(row=1, column=1)
                        # enn8.grid(row=1, column=2)
                        # enn9.grid(row=1, column=3)
                        # e10.grid(row=1, column=4)

                        # e11.grid(row=2, column=0)
                        # e12.grid(row=2, column=1)
                        # e13.grid(row=2, column=2)
                        # e14.grid(row=2, column=3)
                        # e15.grid(row=2, column=4)

                        # e16.grid(row=3, column=0)
                        # e17.grid(row=3, column=1)
                        # e18.grid(row=3, column=2)
                        # e19.grid(row=3, column=3)
                        # e20.grid(row=3, column=4)

                        # e21.grid(row=4, column=0)
                        # e22.grid(row=4, column=1)
                        # e23.grid(row=4, column=2)
                        # e24.grid(row=4, column=3)
                        # e25.grid(row=4, column=4)

                        def fun(*args):
                            enn9.insert(10, v2.get())

                        def fun1(*args):
                            e14.insert(10, v3.get())

                        def fun2(*args):
                            e19.insert(10, v4.get())

                        def fun3(*args):
                            e24.insert(10, v5.get())

                        def fun4(*args):
                            e10.insert(10, v6.get())

                        def fun5(*args):
                            e15.insert(10, v7.get())

                        def fun6(*args):
                            e20.insert(10, v8.get())

                        def fun7(*args):
                            e25.insert(10, v9.get())

                        v2 = StringVar(window2)
                        genderr = {'Male', 'Female'}
                        v2.set('Select')
                        v2.trace("w", fun)
                        popupMenu1 = OptionMenu(window2, v2, *genderr)
                        popupMenu1.config(font=('Slab Serif', 13), bg="gray16", fg="orange")
                        popupMenu1.place(x=700,y=160,width=100)

                        v3 = StringVar(window2)
                        genderr1 = {'Male', 'Female'}
                        v3.set('Select')
                        v3.trace("w", fun1)
                        popupMenu2 = OptionMenu(window2, v3, *genderr1)
                        popupMenu2.config(font=('Slab Serif', 13), bg="gray16", fg="orange")
                        popupMenu2.place(x=700,y=290,width=100)

                        v4 = StringVar(window2)
                        genderr2 = {'Male', 'Female'}
                        v4.set('Select')
                        v4.trace("w", fun2)
                        popupMenu3 = OptionMenu(window2, v4, *genderr2)
                        popupMenu3.config(font=('Slab Serif', 13), bg="gray16", fg="orange")
                        popupMenu3.place(x=700,y=420,width=100)

                        v5 = StringVar(window2)
                        genderr3 = {'Male', 'Female'}
                        v5.set('Select')
                        v5.trace("w", fun3)
                        popupMenu4 = OptionMenu(window2, v5, *genderr3)
                        popupMenu4.config(font=('Slab Serif', 13), bg="gray16", fg="orange")
                        popupMenu4.place(x=700,y=550,width=100)

                        v6 = StringVar(window2)
                        proof = {'Aadhar card', 'Pan card'}
                        v6.set('Select')
                        v6.trace("w", fun4)
                        popup = OptionMenu(window2, v6, *proof)
                        popup.config(font=('Slab Serif', 13), bg="gray16",fg="orange")
                        popup.place(x=970,y=160,width=150)

                        v7 = StringVar(window2)
                        proof = {'Aadhar card', 'Pan card'}
                        v7.set('Select')
                        v7.trace("w", fun5)
                        popup = OptionMenu(window2, v7, *proof)
                        popup.config(font=('Slab Serif', 13), bg="gray16",fg="orange")
                        popup.place(x=970,y=290,width=150)

                        v8 = StringVar(window2)
                        proof = {'Aadhar card', 'Pan card'}
                        v8.set('Select')
                        v8.trace("w", fun6)
                        popup = OptionMenu(window2, v8, *proof)
                        popup.config(font=('Slab Serif', 13), bg="gray16",fg="orange")
                        popup.place(x=970,y=420,width=150)
                        v9 = StringVar(window2)
                        proof = {'Aadhar card', 'Pan card'}
                        v9.set('Select')
                        v9.trace("w", fun7)
                        popup = OptionMenu(window2, v9, *proof)
                        popup.config(font=('Slab Serif', 13), bg="gray16",fg="orange")

                        popup.place(x=970,y=550,width=150)

                def Check1():

                    def Show():
                        global x1,count
                        if enn7.get()!="" and e12.get()=="" and e17.get()=="" and e22.get()=="":
                         
                         
                         count=1
                         window3 = Tk()

                         window3.title("Ticket")
                         screen_width = window3.winfo_screenwidth()
                         screen_height = window3.winfo_screenheight()
                         width = 580
                         height = 480
                         x = (screen_width / 2) - (width / 2)
                         y = (screen_height / 2) - (height / 2)
                         window3.geometry('%dx%d+%d+%d' % (width, height, x, y))
                         window3.resizable(0, 0)
                         window3.config(bg='gray16')

                         w11 = 580
                         h11 = 480
                         canvas3 = Canvas(window3, width=w11, height=h11)
                         canvas3.config(bg='gray16')
                         canvas3.create_rectangle(0, 0,580,30, fill= "orange")
                         canvas3.create_line(40, 90, 270, 90, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 130, 270, 130, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 170, 270, 170, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 210, 270, 210, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 250, 270, 250, fill="gray13", width=0.0000001)

                         canvas3.create_line(320, 90, 550, 90, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 130, 550, 130, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 170, 550, 170, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 210, 550, 210, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 250, 550, 250, fill="gray13", width=0.0000001)
                         canvas3.pack()
                         Label(window3, text="PNR Status Details",bg='orange',fg='gray16', font=('Century Gothic', 11)).place(x=10, y=2)
                         
                         Label(window3, text="Name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=60)
                         Label(window3, text="Gender",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=60)
                         Label(window3, text="Depart at",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=100)
                         Label(window3, text="Age",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=100)
                         Label(window3, text="Class",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=140)
                         Label(window3, text="Train no.",bg='gray16',fg='orange',font=('Century Gothic', 11)).place(x=40, y=140)
                         Label(window3, text="Train name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=180)
                         Label(window3, text="Source",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=220)
                         Label(window3, text="Destination",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=220)
                         # Label(window3, text="No. of tickets",bg='white', font=('Slab Serif', 11)).place(x=60, y=290)

                         Label(window3, text="PNR No.",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=180)

                         # Number = Label(window3, justify="center",bg='white',text=count, font=('Slab Serif', 10))
                         # Number.place(x=170, y=290,  height=25)

                         Name = Label(window3, justify="center",fg='white',bg='gray16',text=enn7.get(), font=('Century Gothic', 10))
                         Name.place(x=150, y=60, height=25)
                         DepartTime = Label(window3, justify="center",fg='white',bg='gray16',text=xdprtTime, font=('Century Gothic', 10))
                         DepartTime.place(x=150, y=100, height=25)
                         TrainName = Label(window3, justify="center",fg='white',bg='gray16',text=xtrainn, font=('Century Gothic', 10))
                         TrainName.place(x=150, y=180, height=25)
                         Age = Label(window3, justify="center",fg='white',bg='gray16',text=enn8.get(), font=('Century Gothic', 10))
                         Age.place(x=430, y=100, height=25)
                         Class = Label(window3, justify="center",fg='white',bg='gray16',text=variable2.get(), font=('Century Gothic', 10))
                         Class.place(x=430, y=140, height=25)
                         Depart = Label(window3, justify="center",fg='white',bg='gray16',text=variable.get(), font=('Century Gothic', 10))
                         Depart.place(x=150, y=220, height=25)
                         Arrive = Label(window3, justify="center",fg='white',bg='gray16',text=variable1.get(), font=('Century Gothic', 10))
                         Arrive.place(x=430, y=220, height=25)
                         Gender = Label(window3, justify="center",fg='white',bg='gray16',text=v2.get(), font=('Century Gothic', 10))
                         Gender.place(x=430, y=60, height=25)
                         TrainNumber = Label(window3, justify="center",fg='white',bg='gray16',text=x1, font=('Century Gothic', 10))
                         TrainNumber.place(x=150, y=140, height=25)
                         
                         a=111111
                         b=999999
                         pnr=(random.randint(a, b))
                         Numberpnr=Label(window3, justify="center",fg='white',bg='gray16',text=pnr, font=('Century Gothic', 10))
                         Numberpnr.place(x=430, y=180, height=25) 


                         #global conn, cursor, x2
                         # passenger_data=[("pnr","enn7.get()","enn9.get()", "enn8.get()","x1")]
                        
                         # passenger_data=[(pnr,enn7.get(),enn9.get(), enn8.get(),x1)]
                         # c.execute("CREATE TABLE rail1 (passen_pnr integer, passen_name text, passen_gender text,passen_age integer,train_number integer)")
                         print("Command executed successfully...")
                         #insertion
                         #c.execute("INSERT INTO rail VALUES(pnr, enn7.get(),enn8.get(), str(enn9.get()
                         c.execute("INSERT INTO rail1 VALUES (?,?,?,?,?)",(pnr,enn7.get(),enn9.get(), enn8.get(),x1))
                         print("Command inserted successfully...")
                         # c.execute("SELECT*FROM rail")
                         c.execute("SELECT rowid,* FROM rail1")
                         print("Command selected successfully...")
                         items=c.fetchall()

                         print("S.No." + "\tPNR"+ "\tTrain No." +"   \tGender"+ "\tAge"+ "\tName")
                         print("-----" + "\t---"+ "\t---------" +"   \t------"+ "\t---"+ "\t----")
                         for item in items:
                             print(item[0] ,"    ",item[1] ," ",item[5],"   \t",item[3] ," ", item[4],"\t", item[2])
                         

                         # for item in items:
                         #     print(item)
                         print("Command fetched successfully...")    
                        


                         Label(window3, text="Have a nice trip!!",fg='white',bg='gray16', font=('Century Gothic', 17)).place(x=200, y=340)

                         mainloop()

                        elif e12.get()!="" and e17.get()=="":
                         
                         count=2
                         window3 = Tk()

                         window3.title("Ticket")
                         screen_width = window3.winfo_screenwidth()
                         screen_height = window3.winfo_screenheight()
                         width = 1160
                         height = 480
                         x = (screen_width / 2) - (width / 2)
                         y = (screen_height / 2) - (height / 2)
                         window3.geometry('%dx%d+%d+%d' % (width, height, x, y))
                         window3.resizable(0, 0)
                         window3.config(bg='gray16')

                         w11 = 1160
                         h11 = 480
                         canvas3 = Canvas(window3, width=w11, height=h11)
                         canvas3.config(bg='gray16')
                         canvas3.create_rectangle(0, 0,1160,30, fill= "orange")
                         canvas3.create_line(40, 90, 270, 90, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 130, 270, 130, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 170, 270, 170, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 210, 270, 210, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 250, 270, 250, fill="gray13", width=0.0000001)

                         canvas3.create_line(320, 90, 550, 90, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 130, 550, 130, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 170, 550, 170, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 210, 550, 210, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 250, 550, 250, fill="gray13", width=0.0000001)

                         canvas3.create_line(560, 90, 790, 90, fill="gray13", width=0.0000001)
                         canvas3.create_line(560, 130, 790, 130, fill="gray13", width=0.0000001)
                         canvas3.create_line(560, 170, 790, 170, fill="gray13", width=0.0000001)
                         canvas3.create_line(560, 210, 790, 210, fill="gray13", width=0.0000001)
                         canvas3.create_line(560, 250, 790, 250, fill="gray13", width=0.0000001)

                         canvas3.create_line(840, 90, 1070, 90, fill="gray13", width=0.0000001)
                         canvas3.create_line(840, 130, 1070, 130, fill="gray13", width=0.0000001)
                         canvas3.create_line(840, 170, 1070, 170, fill="gray13", width=0.0000001)
                         canvas3.create_line(840, 210, 1070, 210, fill="gray13", width=0.0000001)
                         canvas3.create_line(840, 250, 1070, 250, fill="gray13", width=0.0000001)
                         canvas3.pack()
                         Label(window3, text="PNR Status Details",bg='orange',fg='gray16', font=('Century Gothic', 11)).place(x=10, y=2)
                         
                         Label(window3, text="Name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=60)
                         Label(window3, text="Gender",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=60)
                         Label(window3, text="Depart at",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=100)
                         Label(window3, text="Age",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=100)
                         Label(window3, text="Class",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=140)
                         Label(window3, text="Train no.",bg='gray16',fg='orange',font=('Century Gothic', 11)).place(x=40, y=140)
                         Label(window3, text="Train name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=180)
                         Label(window3, text="Source",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=220)
                         Label(window3, text="Destination",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=220)
                         # Label(window3, text="No. of tickets",bg='white', font=('Slab Serif', 11)).place(x=60, y=290)

                         Label(window3, text="PNR No.",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=180)

                         # Number = Label(window3, justify="center",bg='white',text=count, font=('Slab Serif', 10))
                         # Number.place(x=170, y=290,  height=25)

                         Name = Label(window3, justify="center",fg='white',bg='gray16',text=enn7.get(), font=('Century Gothic', 10))
                         Name.place(x=150, y=60, height=25)
                         DepartTime = Label(window3, justify="center",fg='white',bg='gray16',text=xdprtTime, font=('Century Gothic', 10))
                         DepartTime.place(x=150, y=100, height=25)
                         TrainName = Label(window3, justify="center",fg='white',bg='gray16',text=xtrainn, font=('Century Gothic', 10))
                         TrainName.place(x=150, y=180, height=25)
                         Age = Label(window3, justify="center",fg='white',bg='gray16',text=enn8.get(), font=('Century Gothic', 10))
                         Age.place(x=430, y=100, height=25)
                         Class = Label(window3, justify="center",fg='white',bg='gray16',text=variable2.get(), font=('Century Gothic', 10))
                         Class.place(x=430, y=140, height=25)
                         Depart = Label(window3, justify="center",fg='white',bg='gray16',text=variable.get(), font=('Century Gothic', 10))
                         Depart.place(x=150, y=220, height=25)
                         Arrive = Label(window3, justify="center",fg='white',bg='gray16',text=variable1.get(), font=('Century Gothic', 10))
                         Arrive.place(x=430, y=220, height=25)
                         Gender = Label(window3, justify="center",fg='white',bg='gray16',text=v2.get(), font=('Century Gothic', 10))
                         Gender.place(x=430, y=60, height=25)
                         TrainNumber = Label(window3, justify="center",fg='white',bg='gray16',text=x1, font=('Century Gothic', 10))
                         TrainNumber.place(x=150, y=140, height=25)
                         
                         a=111111
                         b=999999
                         pnr=(random.randint(a, b))
                         Numberpnr=Label(window3, justify="center",fg='white',bg='gray16',text=pnr, font=('Century Gothic', 10))
                         Numberpnr.place(x=430, y=180, height=25) 


                         #global conn, cursor, x2
                         # passenger_data=[("pnr","enn7.get()","enn9.get()", "enn8.get()","x1")]
                        
                         # passenger_data=[(pnr,enn7.get(),enn9.get(), enn8.get(),x1)]
                         # c.execute("CREATE TABLE rail1 (passen_pnr integer, passen_name text, passen_gender text,passen_age integer,train_number integer)")
                         print("Command executed successfully...")
                         #insertion
                         #c.execute("INSERT INTO rail VALUES(pnr, enn7.get(),enn8.get(), str(enn9.get()
                         c.execute("INSERT INTO rail1 VALUES (?,?,?,?,?)",(pnr,enn7.get(),enn9.get(), enn8.get(),x1))
                         print("Command inserted successfully...")
                         # c.execute("SELECT*FROM rail")
                         c.execute("SELECT rowid,* FROM rail1")
                         print("Command selected successfully...")
                         items=c.fetchall()

                         print("S.No." + "\tPNR"+ "\tTrain No." +"   \tGender"+ "  \tAge"+ "\tName")
                         print("-----" + "\t---"+ "\t---------" +"   \t------"+ "  \t---"+ "\t----")
                         for item in items:
                             print(item[0] ,"    ",item[1] ," ",item[5],"   \t",item[3] ,"   ", item[4],"\t", item[2])
                         

                         # for item in items:
                         #     print(item)
                         print("Command fetched successfully...")    
                         
                         #-------------------------------------------------------------------  
                         
                         Label(window3, text="Name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=560, y=60)
                         Label(window3, text="Gender",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=60)
                         Label(window3, text="Depart at",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=560, y=100)
                         Label(window3, text="Age",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=100)
                         Label(window3, text="Class",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=140)
                         Label(window3, text="Train no.",bg='gray16',fg='orange',font=('Century Gothic', 11)).place(x=560, y=140)
                         Label(window3, text="Train name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=560, y=180)
                         Label(window3, text="Source",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=560, y=220)
                         Label(window3, text="Destination",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=220)
                         # Label(window3, text="No. of tickets",bg='white', font=('Slab Serif', 11)).place(x=60, y=290)

                         Label(window3, text="PNR No.",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=180)

                         # Number = Label(window3, justify="center",bg='white',text=count, font=('Slab Serif', 10))
                         # Number.place(x=170, y=290,  height=25)

                         Name = Label(window3, justify="center",fg='white',bg='gray16',text=e12.get(), font=('Century Gothic', 10))
                         Name.place(x=670, y=60, height=25)
                         DepartTime = Label(window3, justify="center",fg='white',bg='gray16',text=xdprtTime, font=('Century Gothic', 10))
                         DepartTime.place(x=670, y=100, height=25)
                         TrainName = Label(window3, justify="center",fg='white',bg='gray16',text=xtrainn, font=('Century Gothic', 10))
                         TrainName.place(x=670, y=180, height=25)
                         Age = Label(window3, justify="center",fg='white',bg='gray16',text=e13.get(), font=('Century Gothic', 10))
                         Age.place(x=950, y=100, height=25)
                         Class = Label(window3, justify="center",fg='white',bg='gray16',text=variable2.get(), font=('Century Gothic', 10))
                         Class.place(x=950, y=140, height=25)
                         Depart = Label(window3, justify="center",fg='white',bg='gray16',text=variable.get(), font=('Century Gothic', 10))
                         Depart.place(x=670, y=220, height=25)
                         Arrive = Label(window3, justify="center",fg='white',bg='gray16',text=variable1.get(), font=('Century Gothic', 10))
                         Arrive.place(x=950, y=220, height=25)
                         Gender = Label(window3, justify="center",fg='white',bg='gray16',text=e14.get(), font=('Century Gothic', 10))
                         Gender.place(x=950, y=60, height=25)
                         TrainNumber = Label(window3, justify="center",fg='white',bg='gray16',text=x1, font=('Century Gothic', 10))
                         TrainNumber.place(x=670, y=140, height=25)
                         
                         a=111111
                         b=999999
                         pnr2=(random.randint(a, b))
                         Numberpnr=Label(window3, justify="center",fg='white',bg='gray16',text=pnr2, font=('Century Gothic', 10))
                         Numberpnr.place(x=950, y=180, height=25) 


                         #global conn, cursor, x2
                         # passenger_data=[("pnr","enn7.get()","enn9.get()", "enn8.get()","x1")]
                        
                         # passenger_data=[(pnr,enn7.get(),enn9.get(), enn8.get(),x1)]
                         # c.execute("CREATE TABLE rail1 (passen_pnr integer, passen_name text, passen_gender text,passen_age integer,train_number integer)")
                         print("Command executed successfully...")
                         #insertion
                         #c.execute("INSERT INTO rail VALUES(pnr, enn7.get(),enn8.get(), str(enn9.get()
                         c.execute("INSERT INTO rail1 VALUES (?,?,?,?,?)",(pnr2,e12.get(),e14.get(), e13.get(),x1))
                         print("Command inserted successfully...")
                         # c.execute("SELECT*FROM rail")
                         c.execute("SELECT rowid,* FROM rail1")
                         print("Command selected successfully...")
                         items=c.fetchall()

                         print("S.No." + "\tPNR"+ "\tTrain No." +"   \tGender"+ "  \tAge"+ "\tName")
                         print("-----" + "\t---"+ "\t---------" +"   \t------"+ "  \t---"+ "\t----")
                         for item in items:
                             print(item[0] ,"    ",item[1] ," ",item[5],"   \t",item[3] ,"   ", item[4],"\t", item[2])
                         

                         # for item in items:
                         #     print(item)
                         print("Command fetched successfully...")     
                        


                         Label(window3, text="Have a nice trip!!",fg='white',bg='gray16', font=('Century Gothic', 17)).place(x=500, y=340)

                         mainloop()
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                        elif e17.get()!="" and e22.get()=="":
                         count=3
                         window3 = Tk()

                         window3.title("Ticket")
                         screen_width = window3.winfo_screenwidth()
                         screen_height = window3.winfo_screenheight()
                         width = 1160
                         height = 800
                         x = (screen_width / 2) - (width / 2)
                         y = (screen_height / 2) - (height / 2)
                         window3.geometry('%dx%d+%d+%d' % (width, height, x, y))
                         window3.resizable(0, 0)
                         window3.config(bg='gray16')

                         w11 = 1160
                         h11 = 800
                         canvas3 = Canvas(window3, width=w11, height=h11)
                         canvas3.config(bg='gray16')
                         canvas3.create_rectangle(0, 0,1160,30, fill= "orange")
                         canvas3.create_line(40, 90, 270, 90, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 130, 270, 130, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 170, 270, 170, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 210, 270, 210, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 250, 270, 250, fill="gray13", width=0.0000001)

                         canvas3.create_line(320, 90, 550, 90, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 130, 550, 130, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 170, 550, 170, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 210, 550, 210, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 250, 550, 250, fill="gray13", width=0.0000001)

                         canvas3.create_line(560, 90, 790, 90, fill="gray13", width=0.0000001)
                         canvas3.create_line(560, 130, 790, 130, fill="gray13", width=0.0000001)
                         canvas3.create_line(560, 170, 790, 170, fill="gray13", width=0.0000001)
                         canvas3.create_line(560, 210, 790, 210, fill="gray13", width=0.0000001)
                         canvas3.create_line(560, 250, 790, 250, fill="gray13", width=0.0000001)

                         canvas3.create_line(840, 90, 1070, 90, fill="gray13", width=0.0000001)
                         canvas3.create_line(840, 130, 1070, 130, fill="gray13", width=0.0000001)
                         canvas3.create_line(840, 170, 1070, 170, fill="gray13", width=0.0000001)
                         canvas3.create_line(840, 210, 1070, 210, fill="gray13", width=0.0000001)
                         canvas3.create_line(840, 250, 1070, 250, fill="gray13", width=0.0000001)

                         canvas3.create_line(40, 390, 270, 390, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 430, 270, 430, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 470, 270, 470, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 510, 270, 510, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 550, 270, 550, fill="gray13", width=0.0000001)

                         canvas3.create_line(320, 390, 550, 390, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 430, 550, 430, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 470, 550, 470, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 510, 550, 510, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 550, 550, 550, fill="gray13", width=0.0000001)
                         canvas3.pack()
                         Label(window3, text="PNR Status Details",bg='orange',fg='gray16', font=('Century Gothic', 11)).place(x=10, y=2)
                         
                         Label(window3, text="Name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=60)
                         Label(window3, text="Gender",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=60)
                         Label(window3, text="Depart at",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=100)
                         Label(window3, text="Age",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=100)
                         Label(window3, text="Class",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=140)
                         Label(window3, text="Train no.",bg='gray16',fg='orange',font=('Century Gothic', 11)).place(x=40, y=140)
                         Label(window3, text="Train name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=180)
                         Label(window3, text="Source",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=220)
                         Label(window3, text="Destination",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=220)
                         # Label(window3, text="No. of tickets",bg='white', font=('Slab Serif', 11)).place(x=60, y=290)

                         Label(window3, text="PNR No.",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=180)

                         # Number = Label(window3, justify="center",bg='white',text=count, font=('Slab Serif', 10))
                         # Number.place(x=170, y=290,  height=25)

                         Name = Label(window3, justify="center",fg='white',bg='gray16',text=enn7.get(), font=('Century Gothic', 10))
                         Name.place(x=150, y=60, height=25)
                         DepartTime = Label(window3, justify="center",fg='white',bg='gray16',text=xdprtTime, font=('Century Gothic', 10))
                         DepartTime.place(x=150, y=100, height=25)
                         TrainName = Label(window3, justify="center",fg='white',bg='gray16',text=xtrainn, font=('Century Gothic', 10))
                         TrainName.place(x=150, y=180, height=25)
                         Age = Label(window3, justify="center",fg='white',bg='gray16',text=enn8.get(), font=('Century Gothic', 10))
                         Age.place(x=430, y=100, height=25)
                         Class = Label(window3, justify="center",fg='white',bg='gray16',text=variable2.get(), font=('Century Gothic', 10))
                         Class.place(x=430, y=140, height=25)
                         Depart = Label(window3, justify="center",fg='white',bg='gray16',text=variable.get(), font=('Century Gothic', 10))
                         Depart.place(x=150, y=220, height=25)
                         Arrive = Label(window3, justify="center",fg='white',bg='gray16',text=variable1.get(), font=('Century Gothic', 10))
                         Arrive.place(x=430, y=220, height=25)
                         Gender = Label(window3, justify="center",fg='white',bg='gray16',text=v2.get(), font=('Century Gothic', 10))
                         Gender.place(x=430, y=60, height=25)
                         TrainNumber = Label(window3, justify="center",fg='white',bg='gray16',text=x1, font=('Century Gothic', 10))
                         TrainNumber.place(x=150, y=140, height=25)
                         
                         a=111111
                         b=999999
                         pnr=(random.randint(a, b))
                         Numberpnr=Label(window3, justify="center",fg='white',bg='gray16',text=pnr, font=('Century Gothic', 10))
                         Numberpnr.place(x=430, y=180, height=25) 


                         #global conn, cursor, x2
                         # passenger_data=[("pnr","enn7.get()","enn9.get()", "enn8.get()","x1")]
                        
                         # passenger_data=[(pnr,enn7.get(),enn9.get(), enn8.get(),x1)]
                         # c.execute("CREATE TABLE rail1 (passen_pnr integer, passen_name text, passen_gender text,passen_age integer,train_number integer)")
                         print("Command executed successfully...")
                         #insertion
                         #c.execute("INSERT INTO rail VALUES(pnr, enn7.get(),enn8.get(), str(enn9.get()
                         c.execute("INSERT INTO rail1 VALUES (?,?,?,?,?)",(pnr,enn7.get(),enn9.get(), enn8.get(),x1))
                         print("Command inserted successfully...")
                         # c.execute("SELECT*FROM rail")
                         c.execute("SELECT rowid,* FROM rail1")
                         print("Command selected successfully...")
                         items=c.fetchall()

                         print("S.No." + "\tPNR"+ "\tTrain No." +"   \tGender"+ "\tAge"+ "    \tName")
                         print("-----" + "\t---"+ "\t---------" +"   \t------"+ "\t---"+ "    \t----")
                         for item in items:
                             print(item[0] ,"    ",item[1] ," ",item[5],"   \t",item[3] ," ", item[4],"    \t", item[2])
                         

                         # for item in items:
                         #     print(item)
                         print("Command fetched successfully...")    
                         
                         #-------------------------------------------------------------------  
                         
                         Label(window3, text="Name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=560, y=60)
                         Label(window3, text="Gender",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=60)
                         Label(window3, text="Depart at",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=560, y=100)
                         Label(window3, text="Age",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=100)
                         Label(window3, text="Class",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=140)
                         Label(window3, text="Train no.",bg='gray16',fg='orange',font=('Century Gothic', 11)).place(x=560, y=140)
                         Label(window3, text="Train name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=560, y=180)
                         Label(window3, text="Source",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=560, y=220)
                         Label(window3, text="Destination",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=220)
                         # Label(window3, text="No. of tickets",bg='white', font=('Slab Serif', 11)).place(x=60, y=290)

                         Label(window3, text="PNR No.",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=180)

                         # Number = Label(window3, justify="center",bg='white',text=count, font=('Slab Serif', 10))
                         # Number.place(x=170, y=290,  height=25)

                         Name = Label(window3, justify="center",fg='white',bg='gray16',text=e12.get(), font=('Century Gothic', 10))
                         Name.place(x=670, y=60, height=25)
                         DepartTime = Label(window3, justify="center",fg='white',bg='gray16',text=xdprtTime, font=('Century Gothic', 10))
                         DepartTime.place(x=670, y=100, height=25)
                         TrainName = Label(window3, justify="center",fg='white',bg='gray16',text=xtrainn, font=('Century Gothic', 10))
                         TrainName.place(x=670, y=180, height=25)
                         Age = Label(window3, justify="center",fg='white',bg='gray16',text=e13.get(), font=('Century Gothic', 10))
                         Age.place(x=950, y=100, height=25)
                         Class = Label(window3, justify="center",fg='white',bg='gray16',text=variable2.get(), font=('Century Gothic', 10))
                         Class.place(x=950, y=140, height=25)
                         Depart = Label(window3, justify="center",fg='white',bg='gray16',text=variable.get(), font=('Century Gothic', 10))
                         Depart.place(x=670, y=220, height=25)
                         Arrive = Label(window3, justify="center",fg='white',bg='gray16',text=variable1.get(), font=('Century Gothic', 10))
                         Arrive.place(x=950, y=220, height=25)
                         Gender = Label(window3, justify="center",fg='white',bg='gray16',text=e14.get(), font=('Century Gothic', 10))
                         Gender.place(x=950, y=60, height=25)
                         TrainNumber = Label(window3, justify="center",fg='white',bg='gray16',text=x1, font=('Century Gothic', 10))
                         TrainNumber.place(x=670, y=140, height=25)
                         
                         a=111111
                         b=999999
                         pnr2=(random.randint(a, b))
                         Numberpnr=Label(window3, justify="center",fg='white',bg='gray16',text=pnr2, font=('Century Gothic', 10))
                         Numberpnr.place(x=950, y=180, height=25) 


                         #global conn, cursor, x2
                         # passenger_data=[("pnr","enn7.get()","enn9.get()", "enn8.get()","x1")]
                        
                         # passenger_data=[(pnr,enn7.get(),enn9.get(), enn8.get(),x1)]
                         # c.execute("CREATE TABLE rail1 (passen_pnr integer, passen_name text, passen_gender text,passen_age integer,train_number integer)")
                         print("Command executed successfully...")
                         #insertion
                         #c.execute("INSERT INTO rail VALUES(pnr, enn7.get(),enn8.get(), str(enn9.get()
                         c.execute("INSERT INTO rail1 VALUES (?,?,?,?,?)",(pnr2,e12.get(),e14.get(), e13.get(),x1))
                         print("Command inserted successfully...")
                         # c.execute("SELECT*FROM rail")
                         c.execute("SELECT rowid,* FROM rail1")
                         print("Command selected successfully...")
                         items=c.fetchall()

                         print("S.No." + "\tPNR"+ "\tTrain No." +"   \tGender"+ "\tAge"+ "    \tName")
                         print("-----" + "\t---"+ "\t---------" +"   \t------"+ "\t---"+ "    \t----")
                         for item in items:
                             print(item[0] ,"    ",item[1] ," ",item[5],"   \t",item[3] ," ", item[4],"    \t", item[2])
                         

                         # for item in items:
                         #     print(item)
                         print("Command fetched successfully...")   

                            #  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                         Label(window3, text="Name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=360)
                         Label(window3, text="Gender",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=360)
                         Label(window3, text="Depart at",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=400)
                         Label(window3, text="Age",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=400)
                         Label(window3, text="Class",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=440)
                         Label(window3, text="Train no.",bg='gray16',fg='orange',font=('Century Gothic', 11)).place(x=40, y=440)
                         Label(window3, text="Train name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=480)
                         Label(window3, text="Source",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=520)
                         Label(window3, text="Destination",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=520)
                         # Label(window3, text="No. of tickets",bg='white', font=('Slab Serif', 11)).place(x=60, y=290)

                         Label(window3, text="PNR No.",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=480)

                         # Number = Label(window3, justify="center",bg='white',text=count, font=('Slab Serif', 10))
                         # Number.place(x=170, y=290,  height=25)

                         Name = Label(window3, justify="center",fg='white',bg='gray16',text=e17.get(), font=('Century Gothic', 10))
                         Name.place(x=150, y=360, height=25)
                         DepartTime = Label(window3, justify="center",fg='white',bg='gray16',text=xdprtTime, font=('Century Gothic', 10))
                         DepartTime.place(x=150, y=400, height=25)
                         TrainName = Label(window3, justify="center",fg='white',bg='gray16',text=xtrainn, font=('Century Gothic', 10))
                         TrainName.place(x=150, y=480, height=25)
                         Age = Label(window3, justify="center",fg='white',bg='gray16',text=e18.get(), font=('Century Gothic', 10))
                         Age.place(x=430, y=400, height=25)
                         Class = Label(window3, justify="center",fg='white',bg='gray16',text=variable2.get(), font=('Century Gothic', 10))
                         Class.place(x=430, y=440, height=25)
                         Depart = Label(window3, justify="center",fg='white',bg='gray16',text=variable.get(), font=('Century Gothic', 10))
                         Depart.place(x=150, y=520, height=25)
                         Arrive = Label(window3, justify="center",fg='white',bg='gray16',text=variable1.get(), font=('Century Gothic', 10))
                         Arrive.place(x=430, y=520, height=25)
                         Gender = Label(window3, justify="center",fg='white',bg='gray16',text=e19.get(), font=('Century Gothic', 10))
                         Gender.place(x=430, y=360, height=25)
                         TrainNumber = Label(window3, justify="center",fg='white',bg='gray16',text=x1, font=('Century Gothic', 10))
                         TrainNumber.place(x=150, y=440, height=25)
                         
                         a=111111
                         b=999999
                         pnr3=(random.randint(a, b))
                         Numberpnr=Label(window3, justify="center",fg='white',bg='gray16',text=pnr3, font=('Century Gothic', 10))
                         Numberpnr.place(x=430, y=480, height=25) 


                         #global conn, cursor, x2
                         # passenger_data=[("pnr","enn7.get()","enn9.get()", "enn8.get()","x1")]
                        
                         # passenger_data=[(pnr,enn7.get(),enn9.get(), enn8.get(),x1)]
                         # c.execute("CREATE TABLE rail1 (passen_pnr integer, passen_name text, passen_gender text,passen_age integer,train_number integer)")
                         print("Command executed successfully...")
                         #insertion
                         #c.execute("INSERT INTO rail VALUES(pnr, enn7.get(),enn8.get(), str(enn9.get()
                         c.execute("INSERT INTO rail1 VALUES (?,?,?,?,?)",(pnr3,e17.get(),e19.get(), e18.get(),x1))
                         print("Command inserted successfully...")
                         # c.execute("SELECT*FROM rail")
                         c.execute("SELECT rowid,* FROM rail1")
                         print("Command selected successfully...")
                         items=c.fetchall()

                         print("S.No." + "\tPNR"+ "\tTrain No." +"   \tGender"+ "\tAge"+ "    \tName")
                         print("-----" + "\t---"+ "\t---------" +"   \t------"+ "\t---"+ "    \t----")
                         for item in items:
                             print(item[0] ,"    ",item[1] ," ",item[5],"   \t",item[3] ," ", item[4],"    \t", item[2])
                         

                         # for item in items:
                         #     print(item)
                         print("Command fetched successfully...")  

                        


                         Label(window3, text="Have a nice trip!!",fg='white',bg='gray16', font=('Century Gothic', 17)).place(x=800, y=340)

                         mainloop()
                        else:
                         count=4
                         window3 = Tk()

                         window3.title("Ticket")
                         screen_width = window3.winfo_screenwidth()
                         screen_height = window3.winfo_screenheight()
                         width = 1160
                         height = 800
                         x = (screen_width / 2) - (width / 2)
                         y = (screen_height / 2) - (height / 2)
                         window3.geometry('%dx%d+%d+%d' % (width, height, x, y))
                         window3.resizable(0, 0)
                         window3.config(bg='gray16')

                         w11 = 1160
                         h11 = 800
                         canvas3 = Canvas(window3, width=w11, height=h11)
                         canvas3.config(bg='gray16')
                         canvas3.create_rectangle(0, 0,1160,30, fill= "orange")
                         canvas3.create_line(40, 90, 270, 90, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 130, 270, 130, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 170, 270, 170, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 210, 270, 210, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 250, 270, 250, fill="gray13", width=0.0000001)

                         canvas3.create_line(320, 90, 550, 90, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 130, 550, 130, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 170, 550, 170, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 210, 550, 210, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 250, 550, 250, fill="gray13", width=0.0000001)

                         canvas3.create_line(560, 90, 790, 90, fill="gray13", width=0.0000001)
                         canvas3.create_line(560, 130, 790, 130, fill="gray13", width=0.0000001)
                         canvas3.create_line(560, 170, 790, 170, fill="gray13", width=0.0000001)
                         canvas3.create_line(560, 210, 790, 210, fill="gray13", width=0.0000001)
                         canvas3.create_line(560, 250, 790, 250, fill="gray13", width=0.0000001)

                         canvas3.create_line(840, 90, 1070, 90, fill="gray13", width=0.0000001)
                         canvas3.create_line(840, 130, 1070, 130, fill="gray13", width=0.0000001)
                         canvas3.create_line(840, 170, 1070, 170, fill="gray13", width=0.0000001)
                         canvas3.create_line(840, 210, 1070, 210, fill="gray13", width=0.0000001)
                         canvas3.create_line(840, 250, 1070, 250, fill="gray13", width=0.0000001)

                         canvas3.create_line(40, 390, 270, 390, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 430, 270, 430, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 470, 270, 470, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 510, 270, 510, fill="gray13", width=0.0000001)
                         canvas3.create_line(40, 550, 270, 550, fill="gray13", width=0.0000001)

                         canvas3.create_line(320, 390, 550, 390, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 430, 550, 430, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 470, 550, 470, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 510, 550, 510, fill="gray13", width=0.0000001)
                         canvas3.create_line(320, 550, 550, 550, fill="gray13", width=0.0000001)

                         canvas3.create_line(560, 390, 790, 390, fill="gray13", width=0.0000001)
                         canvas3.create_line(560, 430, 790, 430, fill="gray13", width=0.0000001)
                         canvas3.create_line(560, 470, 790, 470, fill="gray13", width=0.0000001)
                         canvas3.create_line(560, 510, 790, 510, fill="gray13", width=0.0000001)
                         canvas3.create_line(560, 550, 790, 550, fill="gray13", width=0.0000001)

                         canvas3.create_line(840, 390, 1070, 390, fill="gray13", width=0.0000001)
                         canvas3.create_line(840, 430, 1070, 430, fill="gray13", width=0.0000001)
                         canvas3.create_line(840, 470, 1070, 470, fill="gray13", width=0.0000001)
                         canvas3.create_line(840, 510, 1070, 510, fill="gray13", width=0.0000001)
                         canvas3.create_line(840, 550, 1070, 550, fill="gray13", width=0.0000001)
                         canvas3.pack()
                         Label(window3, text="PNR Status Details",bg='orange',fg='gray16', font=('Century Gothic', 11)).place(x=10, y=2)
                         
                         Label(window3, text="Name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=60)
                         Label(window3, text="Gender",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=60)
                         Label(window3, text="Depart at",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=100)
                         Label(window3, text="Age",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=100)
                         Label(window3, text="Class",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=140)
                         Label(window3, text="Train no.",bg='gray16',fg='orange',font=('Century Gothic', 11)).place(x=40, y=140)
                         Label(window3, text="Train name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=180)
                         Label(window3, text="Source",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=220)
                         Label(window3, text="Destination",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=220)
                         # Label(window3, text="No. of tickets",bg='white', font=('Slab Serif', 11)).place(x=60, y=290)

                         Label(window3, text="PNR No.",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=180)

                         # Number = Label(window3, justify="center",bg='white',text=count, font=('Slab Serif', 10))
                         # Number.place(x=170, y=290,  height=25)

                         Name = Label(window3, justify="center",fg='white',bg='gray16',text=enn7.get(), font=('Century Gothic', 10))
                         Name.place(x=150, y=60, height=25)
                         DepartTime = Label(window3, justify="center",fg='white',bg='gray16',text=xdprtTime, font=('Century Gothic', 10))
                         DepartTime.place(x=150, y=100, height=25)
                         TrainName = Label(window3, justify="center",fg='white',bg='gray16',text=xtrainn, font=('Century Gothic', 10))
                         TrainName.place(x=150, y=180, height=25)
                         Age = Label(window3, justify="center",fg='white',bg='gray16',text=enn8.get(), font=('Century Gothic', 10))
                         Age.place(x=430, y=100, height=25)
                         Class = Label(window3, justify="center",fg='white',bg='gray16',text=variable2.get(), font=('Century Gothic', 10))
                         Class.place(x=430, y=140, height=25)
                         Depart = Label(window3, justify="center",fg='white',bg='gray16',text=variable.get(), font=('Century Gothic', 10))
                         Depart.place(x=150, y=220, height=25)
                         Arrive = Label(window3, justify="center",fg='white',bg='gray16',text=variable1.get(), font=('Century Gothic', 10))
                         Arrive.place(x=430, y=220, height=25)
                         Gender = Label(window3, justify="center",fg='white',bg='gray16',text=v2.get(), font=('Century Gothic', 10))
                         Gender.place(x=430, y=60, height=25)
                         TrainNumber = Label(window3, justify="center",fg='white',bg='gray16',text=x1, font=('Century Gothic', 10))
                         TrainNumber.place(x=150, y=140, height=25)
                         
                         a=111111
                         b=999999
                         pnr=(random.randint(a, b))
                         Numberpnr=Label(window3, justify="center",fg='white',bg='gray16',text=pnr, font=('Century Gothic', 10))
                         Numberpnr.place(x=430, y=180, height=25) 


                         #global conn, cursor, x2
                         # passenger_data=[("pnr","enn7.get()","enn9.get()", "enn8.get()","x1")]
                        
                         # passenger_data=[(pnr,enn7.get(),enn9.get(), enn8.get(),x1)]
                         # c.execute("CREATE TABLE rail1 (passen_pnr integer, passen_name text, passen_gender text,passen_age integer,train_number integer)")
                         print("Command executed successfully...")
                         #insertion
                         #c.execute("INSERT INTO rail VALUES(pnr, enn7.get(),enn8.get(), str(enn9.get()
                         c.execute("INSERT INTO rail1 VALUES (?,?,?,?,?)",(pnr,enn7.get(),enn9.get(), enn8.get(),x1))
                         print("Command inserted successfully...")
                         # c.execute("SELECT*FROM rail")
                         c.execute("SELECT rowid,* FROM rail1")
                         print("Command selected successfully...")
                         items=c.fetchall()

                        #  print("S.No." + "\tPNR"+ "\tTrain No." +"   \tGender"+ "\tAge"+ "    \tName")
                        #  print("-----" + "\t---"+ "\t---------" +"   \t------"+ "\t---"+ "    \t----")
                        #  for item in items:
                        #      print(item[0] ,"    ",item[1] ," ",item[5],"   \t",item[3] ," ", item[4],"    \t", item[2])
                         

                         # for item in items:
                         #     print(item)
                         print("Command fetched successfully...")    
                         
                         #-------------------------------------------------------------------  
                         
                         Label(window3, text="Name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=560, y=60)
                         Label(window3, text="Gender",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=60)
                         Label(window3, text="Depart at",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=560, y=100)
                         Label(window3, text="Age",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=100)
                         Label(window3, text="Class",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=140)
                         Label(window3, text="Train no.",bg='gray16',fg='orange',font=('Century Gothic', 11)).place(x=560, y=140)
                         Label(window3, text="Train name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=560, y=180)
                         Label(window3, text="Source",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=560, y=220)
                         Label(window3, text="Destination",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=220)
                         # Label(window3, text="No. of tickets",bg='white', font=('Slab Serif', 11)).place(x=60, y=290)

                         Label(window3, text="PNR No.",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=180)

                         # Number = Label(window3, justify="center",bg='white',text=count, font=('Slab Serif', 10))
                         # Number.place(x=170, y=290,  height=25)

                         Name = Label(window3, justify="center",fg='white',bg='gray16',text=e12.get(), font=('Century Gothic', 10))
                         Name.place(x=670, y=60, height=25)
                         DepartTime = Label(window3, justify="center",fg='white',bg='gray16',text=xdprtTime, font=('Century Gothic', 10))
                         DepartTime.place(x=670, y=100, height=25)
                         TrainName = Label(window3, justify="center",fg='white',bg='gray16',text=xtrainn, font=('Century Gothic', 10))
                         TrainName.place(x=670, y=180, height=25)
                         Age = Label(window3, justify="center",fg='white',bg='gray16',text=e13.get(), font=('Century Gothic', 10))
                         Age.place(x=950, y=100, height=25)
                         Class = Label(window3, justify="center",fg='white',bg='gray16',text=variable2.get(), font=('Century Gothic', 10))
                         Class.place(x=950, y=140, height=25)
                         Depart = Label(window3, justify="center",fg='white',bg='gray16',text=variable.get(), font=('Century Gothic', 10))
                         Depart.place(x=670, y=220, height=25)
                         Arrive = Label(window3, justify="center",fg='white',bg='gray16',text=variable1.get(), font=('Century Gothic', 10))
                         Arrive.place(x=950, y=220, height=25)
                         Gender = Label(window3, justify="center",fg='white',bg='gray16',text=e14.get(), font=('Century Gothic', 10))
                         Gender.place(x=950, y=60, height=25)
                         TrainNumber = Label(window3, justify="center",fg='white',bg='gray16',text=x1, font=('Century Gothic', 10))
                         TrainNumber.place(x=670, y=140, height=25)
                         
                         a=111111
                         b=999999
                         pnr2=(random.randint(a, b))
                         Numberpnr=Label(window3, justify="center",fg='white',bg='gray16',text=pnr2, font=('Century Gothic', 10))
                         Numberpnr.place(x=950, y=180, height=25) 


                         #global conn, cursor, x2
                         # passenger_data=[("pnr","enn7.get()","enn9.get()", "enn8.get()","x1")]
                        
                         # passenger_data=[(pnr,enn7.get(),enn9.get(), enn8.get(),x1)]
                         # c.execute("CREATE TABLE rail1 (passen_pnr integer, passen_name text, passen_gender text,passen_age integer,train_number integer)")
                         print("Command executed successfully...")
                         #insertion
                         #c.execute("INSERT INTO rail VALUES(pnr, enn7.get(),enn8.get(), str(enn9.get()
                         c.execute("INSERT INTO rail1 VALUES (?,?,?,?,?)",(pnr2,e12.get(),e14.get(), e13.get(),x1))
                         print("Command inserted successfully...")
                         # c.execute("SELECT*FROM rail")
                         c.execute("SELECT rowid,* FROM rail1")
                         print("Command selected successfully...")
                         items=c.fetchall()

                        #  print("S.No." + "\tPNR"+ "\tTrain No." +"   \tGender"+ "\tAge"+ "    \tName")
                        #  print("-----" + "\t---"+ "\t---------" +"   \t------"+ "\t---"+ "    \t----")
                        #  for item in items:
                        #      print(item[0] ,"    ",item[1] ," ",item[5],"   \t",item[3] ," ", item[4],"    \t", item[2])
                         

                         # for item in items:
                         #     print(item)
                         print("Command fetched successfully...")   

                            #  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                         Label(window3, text="Name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=360)
                         Label(window3, text="Gender",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=360)
                         Label(window3, text="Depart at",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=400)
                         Label(window3, text="Age",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=400)
                         Label(window3, text="Class",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=440)
                         Label(window3, text="Train no.",bg='gray16',fg='orange',font=('Century Gothic', 11)).place(x=40, y=440)
                         Label(window3, text="Train name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=480)
                         Label(window3, text="Source",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=40, y=520)
                         Label(window3, text="Destination",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=520)
                         # Label(window3, text="No. of tickets",bg='white', font=('Slab Serif', 11)).place(x=60, y=290)

                         Label(window3, text="PNR No.",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=320, y=480)

                         # Number = Label(window3, justify="center",bg='white',text=count, font=('Slab Serif', 10))
                         # Number.place(x=170, y=290,  height=25)

                         Name = Label(window3, justify="center",fg='white',bg='gray16',text=e17.get(), font=('Century Gothic', 10))
                         Name.place(x=150, y=360, height=25)
                         DepartTime = Label(window3, justify="center",fg='white',bg='gray16',text=xdprtTime, font=('Century Gothic', 10))
                         DepartTime.place(x=150, y=400, height=25)
                         TrainName = Label(window3, justify="center",fg='white',bg='gray16',text=xtrainn, font=('Century Gothic', 10))
                         TrainName.place(x=150, y=480, height=25)
                         Age = Label(window3, justify="center",fg='white',bg='gray16',text=e18.get(), font=('Century Gothic', 10))
                         Age.place(x=430, y=400, height=25)
                         Class = Label(window3, justify="center",fg='white',bg='gray16',text=variable2.get(), font=('Century Gothic', 10))
                         Class.place(x=430, y=440, height=25)
                         Depart = Label(window3, justify="center",fg='white',bg='gray16',text=variable.get(), font=('Century Gothic', 10))
                         Depart.place(x=150, y=520, height=25)
                         Arrive = Label(window3, justify="center",fg='white',bg='gray16',text=variable1.get(), font=('Century Gothic', 10))
                         Arrive.place(x=430, y=520, height=25)
                         Gender = Label(window3, justify="center",fg='white',bg='gray16',text=e19.get(), font=('Century Gothic', 10))
                         Gender.place(x=430, y=360, height=25)
                         TrainNumber = Label(window3, justify="center",fg='white',bg='gray16',text=x1, font=('Century Gothic', 10))
                         TrainNumber.place(x=150, y=440, height=25)
                         
                         a=111111
                         b=999999
                         pnr3=(random.randint(a, b))
                         Numberpnr=Label(window3, justify="center",fg='white',bg='gray16',text=pnr3, font=('Century Gothic', 10))
                         Numberpnr.place(x=430, y=480, height=25) 


                         #global conn, cursor, x2
                         # passenger_data=[("pnr","enn7.get()","enn9.get()", "enn8.get()","x1")]
                        
                         # passenger_data=[(pnr,enn7.get(),enn9.get(), enn8.get(),x1)]
                         # c.execute("CREATE TABLE rail1 (passen_pnr integer, passen_name text, passen_gender text,passen_age integer,train_number integer)")
                         print("Command executed successfully...")
                         #insertion
                         #c.execute("INSERT INTO rail VALUES(pnr, enn7.get(),enn8.get(), str(enn9.get()
                         c.execute("INSERT INTO rail1 VALUES (?,?,?,?,?)",(pnr3,e17.get(),e19.get(), e18.get(),x1))
                         print("Command inserted successfully...")
                         # c.execute("SELECT*FROM rail")
                         c.execute("SELECT rowid,* FROM rail1")
                         print("Command selected successfully...")
                         items=c.fetchall()

                        #  print("S.No." + "\tPNR"+ "\tTrain No." +"   \tGender"+ "\tAge"+ "    \tName")
                        #  print("-----" + "\t---"+ "\t---------" +"   \t------"+ "\t---"+ "    \t----")
                        #  for item in items:
                        #      print(item[0] ,"    ",item[1] ," ",item[5],"   \t",item[3] ," ", item[4],"    \t", item[2])
                         

                         # for item in items:
                         #     print(item)
                         print("Command fetched successfully...") 

                         Label(window3, text="Name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=560, y=360)
                         Label(window3, text="Gender",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=360)
                         Label(window3, text="Depart at",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=560, y=400)
                         Label(window3, text="Age",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=400)
                         Label(window3, text="Class",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=440)
                         Label(window3, text="Train no.",bg='gray16',fg='orange',font=('Century Gothic', 11)).place(x=560, y=440)
                         Label(window3, text="Train name",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=560, y=480)
                         Label(window3, text="Source",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=560, y=520)
                         Label(window3, text="Destination",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=520)
                         # Label(window3, text="No. of tickets",bg='white', font=('Slab Serif', 11)).place(x=60, y=290)

                         Label(window3, text="PNR No.",bg='gray16',fg='orange', font=('Century Gothic', 11)).place(x=840, y=480)

                         # Number = Label(window3, justify="center",bg='white',text=count, font=('Slab Serif', 10))
                         # Number.place(x=170, y=290,  height=25)

                         Name = Label(window3, justify="center",fg='white',bg='gray16',text=e22.get(), font=('Century Gothic', 10))
                         Name.place(x=670, y=360, height=25)
                         DepartTime = Label(window3, justify="center",fg='white',bg='gray16',text=xdprtTime, font=('Century Gothic', 10))
                         DepartTime.place(x=670, y=400, height=25)
                         TrainName = Label(window3, justify="center",fg='white',bg='gray16',text=xtrainn, font=('Century Gothic', 10))
                         TrainName.place(x=670, y=480, height=25)
                         Age = Label(window3, justify="center",fg='white',bg='gray16',text=e23.get(), font=('Century Gothic', 10))
                         Age.place(x=950, y=400, height=25)
                         Class = Label(window3, justify="center",fg='white',bg='gray16',text=variable2.get(), font=('Century Gothic', 10))
                         Class.place(x=950, y=440, height=25)
                         Depart = Label(window3, justify="center",fg='white',bg='gray16',text=variable.get(), font=('Century Gothic', 10))
                         Depart.place(x=670, y=520, height=25)
                         Arrive = Label(window3, justify="center",fg='white',bg='gray16',text=variable1.get(), font=('Century Gothic', 10))
                         Arrive.place(x=950, y=520, height=25)
                         Gender = Label(window3, justify="center",fg='white',bg='gray16',text=e24.get(), font=('Century Gothic', 10))
                         Gender.place(x=950, y=360, height=25)
                         TrainNumber = Label(window3, justify="center",fg='white',bg='gray16',text=x1, font=('Century Gothic', 10))
                         TrainNumber.place(x=670, y=440, height=25)
                         
                         a=111111
                         b=999999
                         pnr4=(random.randint(a, b))
                         Numberpnr=Label(window3, justify="center",fg='white',bg='gray16',text=pnr4, font=('Century Gothic', 10))
                         Numberpnr.place(x=950, y=480, height=25) 


                         #global conn, cursor, x2
                         # passenger_data=[("pnr","enn7.get()","enn9.get()", "enn8.get()","x1")]
                        
                         # passenger_data=[(pnr,enn7.get(),enn9.get(), enn8.get(),x1)]
                         # c.execute("CREATE TABLE rail1 (passen_pnr integer, passen_name text, passen_gender text,passen_age integer,train_number integer)")
                         print("Command executed successfully...")
                         #insertion
                         #c.execute("INSERT INTO rail VALUES(pnr, enn7.get(),enn8.get(), str(enn9.get()
                         c.execute("INSERT INTO rail1 VALUES (?,?,?,?,?)",(pnr4,e22.get(),e24.get(), e23.get(),x1))
                         print("Command inserted successfully...")
                         # c.execute("SELECT*FROM rail")
                         c.execute("SELECT rowid,* FROM rail1")
                         print("Command selected successfully...")
                         items=c.fetchall()

                         print("S.No." + "\tPNR"+ "\tTrain No." +"\tGender"+ "\tAge"+ "\tName")
                         print("-----" + "\t---"+ "\t---------" +"\t------"+ "\t---"+ "\t----")
                         for item in items:
                             print(item[0] ,"\t",item[1] ,"\t",item[5],"\t",item[3] ,"\t", item[4],"\t", item[2])
                         

                         # for item in items:
                         #     print(item)
                         print("Command fetched successfully...") 
                         


                         Label(window3, text="Have a nice trip!!",fg='white',bg='gray16', font=('Century Gothic', 17)).place(x=450, y=600)

                         mainloop()




                    




                    global count
                    count=0
                    if len(enn7.get()) == 0 or len(enn8.get()) == 0 or len(enn9.get()) == 0 or len(e10.get()) == 0:
                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
                    elif len(e12.get()) != 0 and (len(e13.get()) == 0 or len(e14.get()) == 0 or len(e15.get()) == 0):
                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
                    elif len(e17.get()) != 0 and (len(e18.get()) == 0 or len(e19.get()) == 0 or len(e20.get()) == 0):
                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
                    elif len(e22.get()) != 0 and (len(e23.get()) == 0 or len(e24.get()) == 0 or len(e25.get()) == 0):
                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
                    elif (len(e12.get()) != 0 or len(e13.get()) != 0 or len(e14.get()) != 0 or len(
                            e15.get()) != 0) and (
                            len(e22.get()) != 0 or len(e23.get()) != 0 or len(e24.get()) != 0 or len(
                        e25.get()) != 0) and (
                            len(e17.get()) == 0 or (len(e18.get()) == 0 or len(e19.get()) == 0 or len(e20.get()) == 0)):
                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
                    elif (len(enn7.get()) != 0 or len(enn8.get()) != 0 or len(enn9.get()) != 0 or len(
                            e10.get()) != 0) and (
                            len(e17.get()) != 0 or len(e18.get()) != 0 or len(e19.get()) != 0 or len(
                        e20.get()) != 0) and (
                            len(e12.get()) == 0 or (len(e13.get()) == 0 or len(e14.get()) == 0 or len(e15.get()) == 0)):
                        tkinter.messagebox.showinfo('Error', 'enter all required fields')
                    elif  enn7.get()!="" and e12.get()=="" and e17.get()=="" and e22.get()=="":
                        count=1
                        Show()
                    elif e12.get()!="" and e17.get()=="":
                        count=2
                        Show()
                        
                    elif e17.get()!="" and e22.get()=="":
                        count=3
                        Show()
                    elif e22.get()!="":
                        count=4
                        Show()
                    else:
                        Show()
                
                def Mainmenu():
                    window2.destroy()
                    createWindow()
                    window()
                m = Button(window2, text="Main Menu",font=('Century Gothic',15),width=60, bg="orange", fg="gray16", command=Mainmenu)
                m.place(x=500,y=640,width=120)    

                b = Button(window2, text='Submit', bg="Orange",fg="gray16", font=('Century Gothic', 15), command=Check1)
                b.place(x=670,y=640,width=100)
                # def Main():
                #              window2.destroy()
                #              createWindow()
                # m = Button(window2, text="Main Menu",font=('Century Gothic',15),width=60, bg="orange", fg="gray16", command=Main())
                # m.place(x=600,y=640,width=100)

                mainloop()


            PassengerDetails()


        
        def Back1():
            window1.destroy()
            createWindow()
            window()
            

        button1=Button(window1,text="Book",font=('Century Gothic',9),width=10,bg="gray16",fg="orange",command=PassengerDetails1)
        button1.place(x=1190,y=201,height=40,width=80)
        button2 = Button(window1, text="Book",font=('Century Gothic',9),width=10, bg="gray16",fg="orange",command=PassengerDetails2)
        button2.place(x=1190,y=271,height=40,width=80)
        button3 = Button(window1, text="Book",font=('Century Gothic',9),width=10, bg="gray16",fg="orange", command=PassengerDetails3)
        button3.place(x=1190,y=341,height=40,width=80)
        button4 = Button(window1, text="Book",font=('Century Gothic',9),width=10,bg="gray16",fg="orange", command=PassengerDetails4)
        button4.place(x=1190,y=411,height=40,width=80)

        button5 = Button(window1, text="Back",font=('Century Gothic',15),width=60, bg="orange", fg="gray16", command=Back1)
        button5.place(x=600,y=640,width=100)

        mainloop()


    def Cancellation():
        # window.destroy()
        window4 = Tk()
        window4.title("Cancel Ticket")

        screen_width = window4.winfo_screenwidth()
        screen_height = window4.winfo_screenheight()
        width = 410
        height = 400
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        window4.geometry('%dx%d+%d+%d' % (width, height, x, y))
        window4.resizable(0, 0)

        window4.config(bg='gray16')
        cancel = Label(window4, text="PNR NO", font=('Century Gothic', 15), bg="gray16", fg="white")
        cancel.place(x=100, y=150, width=90)
        e=Entry(window4,justify="center", font=('Slab Serif', 15), bg="white")
        e.place(x=210, y=150, width=100)
        

        def Delete1():
            result = tkinter.messagebox.askquestion('Ask', 'Are you sure you want to delete your booked ticket?',
                                              icon="warning")
            if result == 'yes':
                c.execute("SELECT rowid,*FROM rail1")
                items0=c.fetchall()
                length0=len(items0)
                print(length0)
                
                # cursor = conn.cursor()
                # c.execute("SELECT *FROM rail1 WHERE passen_pnr='e.get()'")
                c.execute("DELETE FROM rail1 WHERE passen_pnr=(?)",(e.get(),))
                
                print("S.No." + "\tPNR"+ "\tTrain No." +"\tGender"+ "\tAge"+ "\tName")
                print("-----" + "\t---"+ "\t---------" +"\t------"+ "\t---"+ "\t----")
                c.execute("SELECT rowid,*FROM rail1")
                items1=c.fetchall()
                for item1 in items1:
                    print(item1[0] ,"\t",item1[1] ,"\t",item1[5],"\t",item1[3] ,"\t", item1[4],"\t", item1[2])
                
                c.execute("SELECT rowid,*FROM rail1")
                items2=c.fetchall()
                length2=len(items2)
                print(length2)
                if length2<length0:
                   tkinter.messagebox.showinfo('Success', 'Ticket Deleted Successfully')
                   window4.destroy()
                else:
                   tkinter.messagebox.showinfo('Error', 'Ticket Not Found!')          
                

                # at=str(d)
                # d1=at.replace('(','')
                # d2 = d1.replace(')', '')
                # d3 = d2.replace(',', '')
                # d4=d3.replace('[','')
                # d5 = d4.replace(']', '')
                # d6=d5.split(' ')


                # q=0
                # for i in range(1,len(d6)):
                #     if e.get()==d6[i]:
                #         x123=e.get()
                #         q=1
                # if q==1
                #     c.execute("DELETE FROM rail1 WHERE passen_pnr=?",(x123))
                #     tkinter.messagebox.showinfo('Success', 'Ticket Deleted Successfully')
                #     window4.destroy()
                # else:
                #     tkinter.messagebox.showinfo('Error', 'Ticket Not Found!')
                
                conn.commit()
                # conn.close()


        def Delete():
            if (len(e.get())==""):
                tkinter.messagebox.showinfo('Error', 'Enter the required PNR No.')
            else:

                Delete1()
        def Back():
            window4.destroy()
            createWindow()
            window()
           


        Button(window4, text="Back", font=('Century Gothic', 15), bg="gray13", fg="white",command=Back).place(x=80,y=250, width=120)

        Button(window4, text="Delete", font=('Century Gothic', 15), bg="orange", fg="gray16",command=Delete
               ).place(x=220, y=250, width=120)
        mainloop()
    e1.config(bg="gray16",fg="orange")

    e1.place(x=850,y=300,height=30,width=115)
    Button(window,text="Search Trains",font=('Century Gothic',15), bg="orange",fg="gray16",command=Check).place(x=630,y=500,width=140)

    Button(window, text="Change Password",font=('Century Gothic',12), bg="gray16",fg="orange",command=Cancellation).place(x=20,y=260,width=160)

    Button(window, text="Cancellation",font=('Century Gothic',12), bg="gray16",fg="orange",command=Cancellation).place(x=20,y=210,width=160)

   # Button(window, text= "Select the Date",font=('Slab Serif',13), bg="gray16",fg="orange", command= get_date).place(x=200,y=260,width=160)
    
    
    mainloop()


button_1 = Button(root, text="Login",font=('Comic Sans',15),bg='orange',fg='white', command=printMsg).place(x=120,y=440)
button_2 = Button(root, text="Quit",font=('Slab Serif',15),bg='orange',fg='white', command=root.destroy).place(x=220,y=440)



root.mainloop()




root.mainloop()