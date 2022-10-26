import tkinter as t
from tkinter import *
from tkinter import messagebox
import os, time, random





def createWid():

    l1 = Label(root, text="Enter the time in hh:mm format.")
    l1.grid(row=0, column=0, padx=5, pady=5)

    global box1
    box1 = Entry(root, width=20)
    box1.grid(row=0, column=1)

    l2 = Label(root, text="Enter the message of the alarm.")
    l2.grid(row=1, column=0, padx=5, pady=5)

    global box2
    box2 = Entry(root, width=20)
    box2.grid(row=1, column=1)


    b1 = Button(root, text="Set", width=15, command=submit)
    b1.grid(row=3, column=1)

    global l3
    l3 = Label(root, text="")
    l3.grid(row=3,column=0)

    global l4
    l4 = Label(root, text="Path of the music file.")
    l4.grid(row=2,column=0)

    global box3
    box3 = Entry(root, width=20)
    box3.grid(row=2,column=1)

def message1():

    global box1, l3
    Alarmtimelabel = box1.get()
    l3.config(text="The alarm is set and is counting....")
    messagebox.showinfo("Alarm clock", f"The alarm time is set to {Alarmtimelabel}")



def rndring():
    global l4, box3
    directory = box3.get()
    song = os.listdir(directory)
    print(song)
    n = random.randint(0,len(song))
    print(n)
    os.startfile(os.path.join(directory, song[n]))


def submit():
    global box1, box2, l3
    Alarmtime = box1.get()
    message1()
    currenttime = time.strftime("%H:%M")
    alarmmessage = box2.get()
    print(f"The alarm time is set to {Alarmtime}")
    while Alarmtime != currenttime:
        currenttime = time.strftime("%H:%M")
        time.sleep(1)
    if Alarmtime == currenttime:
        # import ringtone as r 
        print("The alarm is ringing!!!")
        l3.config(text="Alarm is ringing>>>>>>") 
        rndring() 
        messagebox.showinfo("Alarm Message", f"The message is: {alarmmessage}")  
        
        

        

root = t.Tk()
root.title("Alarm!!")
root.geometry("400x200")
createWid()




root.mainloop()