import pyautogui as ato
from tkinter import *
import datetime
import time
import pywhatkit


class autosender:

    def __init__(self):
        self.wn = Tk()
        self.write_str = StringVar()
        self.num_tm = StringVar()
        self.ph_nm = StringVar()
        self.component()

    def write_auto(self):
        str = self.write_str.get()
        int_loop = self.num_tm.get()
        number = self.ph_nm.get()
        i = 1

        cur_hour = datetime.datetime.now().strftime('%H')
        cur_min = datetime.datetime.now().strftime('%M')

        pywhatkit.sendwhatmsg(number, str,
                              int(cur_hour), int(cur_min) + 1, 10)

        while i < int(int_loop):
            ato.write(str)
            ato.press('enter')
            i = i + 1

    def component(self):
        self.wn.title('Message Sender by POG PKS')

        self.wn.maxsize(500, 500)
        self.wn.minsize(500, 500)

        label1 = Label(self.wn, text="Write here : ", fg='blue')
        label1.place(x=40, y=20)

        inp = Entry(self.wn, textvariable=self.write_str, width=50)
        inp.place(x=40, y=50)

        label2 = Label(self.wn, text='Number of Time Send : ', fg='blue')
        label2.place(x=40, y=80)

        inp_loop = Entry(self.wn, textvariable=self.num_tm, width=20)
        inp_loop.place(x=40, y=110)

        label3 = Label(
            self.wn, text='Enter Phone Number With Country Code +__ : ', fg='blue')
        label3.place(x=40, y=140)

        inp_num = Entry(self.wn, textvariable=self.ph_nm, width=20)
        inp_num.place(x=40, y=170)

        self.wait_lb = Label(
            self.wn, text='Wait for open whatsapp on browser', fg='blue', font=('none', 10, 'bold'))
        self.wait_lb.place(x=105, y=300)

        send = Button(self.wn, text="Start", bg='yellow',
                      fg='black', width=7, height=1, command=self.write_auto)
        send.place(x=220, y=420)
        self.wn.mainloop()


A = autosender()
