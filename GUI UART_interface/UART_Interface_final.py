#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#

#    Jan 19, 2024 07:04:08 PM IST  platform: Windows 11

import sys
import time
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path
import threading
import serial

global ser, connected

ser = ''
connected = 0

_script = sys.argv[0]
_location = os.path.dirname(_script)

import UART_Interface_support

_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = 'gray40' # X11 color: #666666
_ana1color = '#c3c3c3' # Closest X11 color: 'gray76'
_ana2color = 'beige' # X11 color: #f5f5dc
_tabfg1 = 'black' 
_tabfg2 = 'black' 
_tabbg1 = 'grey75' 
_tabbg2 = 'grey89' 
_bgmode = 'light' 

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("497x423+383+106")
        top.minsize(120, 1)
        top.maxsize(2736, 749)
        top.resizable(1,  1)
        top.title("Toplevel 0")
        top.configure(background="#d9d9d9")

        self.top = top
        self.che50 = tk.IntVar()
        self.che51 = tk.IntVar()
        self.che52 = tk.IntVar()
        self.che53 = tk.IntVar()

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.0, rely=0.0, height=21, width=494)
        self.Label1.configure(background="#00ff80")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 14")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''UART Interface''')

        self.Labelframe1 = tk.LabelFrame(self.top)
        self.Labelframe1.place(relx=0.02, rely=0.071, relheight=0.248
                , relwidth=0.966)
        self.Labelframe1.configure(relief='groove')
        self.Labelframe1.configure(foreground="#000000")
        self.Labelframe1.configure(text='''COMP Port Setting''')
        self.Labelframe1.configure(background="#d9d9d9")
        self.Labelframe1.configure(cursor="fleur")


        self.Button1 = tk.Button(self.Labelframe1)
        self.Button1.place(relx=0.063, rely=0.381, height=34, width=87
                , bordermode='ignore')
        self.Button1.configure(activebackground="beige")
        self.Button1.configure(activeforeground="black")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(compound='left')
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Segoe UI} -size 11")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Connect''')
        self.Button1.configure(command = connect_to_serial)

        self.Listbox1 = tk.Listbox(self.Labelframe1)
        self.Listbox1.place(relx=0.292, rely=0.19, relheight=0.686
                , relwidth=0.279, bordermode='ignore')
        self.Listbox1.configure(background="white")
        self.Listbox1.configure(disabledforeground="#a3a3a3")
        self.Listbox1.configure(font="TkFixedFont")
        self.Listbox1.configure(foreground="#000000")
        self.Listbox1.insert(END,"COM1")
        self.Listbox1.insert(END,"COM2")
        self.Listbox1.insert(END,"COM3")
        self.Listbox1.insert(END,"COM7")

        self.Checkbutton1 = tk.Checkbutton(self.Labelframe1)
        self.Checkbutton1.place(relx=0.625, rely=0.381, relheight=0.238
                , relwidth=0.127, bordermode='ignore')
        self.Checkbutton1.configure(activebackground="beige")
        self.Checkbutton1.configure(activeforeground="black")
        self.Checkbutton1.configure(anchor='w')
        self.Checkbutton1.configure(background="#d9d9d9")
        self.Checkbutton1.configure(compound='left')
        self.Checkbutton1.configure(disabledforeground="#a3a3a3")
        self.Checkbutton1.configure(font="-family {Segoe UI} -size 11")
        self.Checkbutton1.configure(foreground="#000000")
        self.Checkbutton1.configure(highlightbackground="#d9d9d9")
        self.Checkbutton1.configure(highlightcolor="black")
        self.Checkbutton1.configure(justify='left')
        self.Checkbutton1.configure(selectcolor="#d9d9d9")
        self.Checkbutton1.configure(text='''4800''')
        self.Checkbutton1.configure(command=select_4800)
        self.Checkbutton1.configure(variable=self.che50)

        self.Checkbutton2 = tk.Checkbutton(self.Labelframe1)
        self.Checkbutton2.place(relx=0.625, rely=0.667, relheight=0.238
                , relwidth=0.148, bordermode='ignore')
        self.Checkbutton2.configure(activebackground="beige")
        self.Checkbutton2.configure(activeforeground="black")
        self.Checkbutton2.configure(anchor='w')
        self.Checkbutton2.configure(background="#d9d9d9")
        self.Checkbutton2.configure(compound='left')
        self.Checkbutton2.configure(disabledforeground="#a3a3a3")
        self.Checkbutton2.configure(font="-family {Segoe UI} -size 11")
        self.Checkbutton2.configure(foreground="#000000")
        self.Checkbutton2.configure(highlightbackground="#d9d9d9")
        self.Checkbutton2.configure(highlightcolor="black")
        self.Checkbutton2.configure(justify='left')
        self.Checkbutton2.configure(selectcolor="#d9d9d9")
        self.Checkbutton2.configure(text='''115200''')
        self.Checkbutton2.configure(command=select_115200)
        self.Checkbutton2.configure(variable=self.che51)

        self.Checkbutton3 = tk.Checkbutton(self.Labelframe1)
        self.Checkbutton3.place(relx=0.792, rely=0.381, relheight=0.238
                , relwidth=0.127, bordermode='ignore')
        self.Checkbutton3.configure(activebackground="beige")
        self.Checkbutton3.configure(activeforeground="black")
        self.Checkbutton3.configure(anchor='w')
        self.Checkbutton3.configure(background="#d9d9d9")
        self.Checkbutton3.configure(compound='left')
        self.Checkbutton3.configure(disabledforeground="#a3a3a3")
        self.Checkbutton3.configure(font="-family {Segoe UI} -size 11")
        self.Checkbutton3.configure(foreground="#000000")
        self.Checkbutton3.configure(highlightbackground="#d9d9d9")
        self.Checkbutton3.configure(highlightcolor="black")
        self.Checkbutton3.configure(justify='left')
        self.Checkbutton3.configure(selectcolor="#d9d9d9")
        self.Checkbutton3.configure(text='''9600''')
        self.Checkbutton3.configure(command=select_9600)
        self.Checkbutton3.configure(variable=self.che52)

        self.Checkbutton4 = tk.Checkbutton(self.Labelframe1)
        self.Checkbutton4.place(relx=0.792, rely=0.667, relheight=0.238
                , relwidth=0.148, bordermode='ignore')
        self.Checkbutton4.configure(activebackground="beige")
        self.Checkbutton4.configure(activeforeground="black")
        self.Checkbutton4.configure(anchor='w')
        self.Checkbutton4.configure(background="#d9d9d9")
        self.Checkbutton4.configure(compound='left')
        self.Checkbutton4.configure(cursor="fleur")
        self.Checkbutton4.configure(disabledforeground="#a3a3a3")
        self.Checkbutton4.configure(font="-family {Segoe UI} -size 11")
        self.Checkbutton4.configure(foreground="#000000")
        self.Checkbutton4.configure(highlightbackground="#d9d9d9")
        self.Checkbutton4.configure(highlightcolor="black")
        self.Checkbutton4.configure(justify='left')
        self.Checkbutton4.configure(selectcolor="#d9d9d9")
        self.Checkbutton4.configure(text='''19200''')
        self.Checkbutton4.configure(command=select_19200)
        self.Checkbutton4.configure(variable=self.che53)

        self.Label2 = tk.Label(self.Labelframe1)
        self.Label2.place(relx=0.667, rely=0.095, height=31, width=124
                , bordermode='ignore')
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(compound='left')
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Segoe UI} -size 11")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Select BAUD Rate''')

        self.Labelframe2 = tk.LabelFrame(self.top)
        self.Labelframe2.place(relx=0.02, rely=0.355, relheight=0.272
                , relwidth=0.966)
        self.Labelframe2.configure(relief='groove')
        self.Labelframe2.configure(foreground="#000000")
        self.Labelframe2.configure(text='''Receive''')
        self.Labelframe2.configure(background="#d9d9d9")

        self.Text1 = tk.Text(self.Labelframe2)
        self.Text1.place(relx=0.029, rely=0.174, relheight=0.73, relwidth=0.946
                , bordermode='ignore')
        self.Text1.configure(background="white")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(wrap="word")

        self.Labelframe3 = tk.LabelFrame(self.top)
        self.Labelframe3.place(relx=0.02, rely=0.662, relheight=0.296
                , relwidth=0.966)
        self.Labelframe3.configure(relief='groove')
        self.Labelframe3.configure(foreground="#000000")
        self.Labelframe3.configure(text='''Labelframe''')
        self.Labelframe3.configure(background="#d9d9d9")

        self.Entry1 = tk.Entry(self.Labelframe3)
        self.Entry1.place(relx=0.042, rely=0.24, height=30, relwidth=0.258
                , bordermode='ignore')
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Entry2 = tk.Entry(self.Labelframe3)
        self.Entry2.place(relx=0.042, rely=0.56, height=30, relwidth=0.633
                , bordermode='ignore')
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")

        self.Label3 = tk.Label(self.Labelframe3)
        self.Label3.place(relx=0.313, rely=0.32, height=21, width=84
                , bordermode='ignore')
        self.Label3.configure(anchor='w')
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(compound='left')
        self.Label3.configure(cursor="fleur")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font="-family {Segoe UI} -size 11")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Send Char''')

        self.Button2 = tk.Button(self.Labelframe3)
        self.Button2.place(relx=0.708, rely=0.56, height=34, width=107
                , bordermode='ignore')
        self.Button2.configure(activebackground="beige")
        self.Button2.configure(activeforeground="black")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(compound='left')
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font="-family {Segoe UI} -size 11")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Send String''')
        self.Button2.configure(command=send_string)

# def start_up():
#     UART_Interface_support.main()
def connect_to_serial():
    global ser, connected
    comp_selected = gui.Listbox1.get(ANCHOR)
    print(comp_selected)

    if gui.che50.get():
        baudrate_selected = 4800
    elif gui.che51.get():
        baudrate_selected = 115200
    elif gui.che52.get():
        baudrate_selected = 9600
    else:
        baudrate_selected = 19200

    print(baudrate_selected)

    ser = serial.Serial(port=comp_selected, baudrate=baudrate_selected, timeout = 2, bytesize= 8, stopbits=serial.STOPBITS_ONE)
    connected = 1

def select_4800():
    if gui.che50.get():
        gui.che51.set(0)
        gui.che52.set(0)
        gui.che53.set(0)


def select_9600():
    if gui.che52.get():
        gui.che50.set(0)
        gui.che51.set(0)
        gui.che53.set(0)

def select_115200():
    if gui.che51.get():
        gui.che50.set(0)
        gui.che52.set(0)
        gui.che53.set(0)

def select_19200():
    if gui.che53.get():
        gui.che50.set(0)
        gui.che51.set(0)
        gui.che52.set(0)

def send_string():
    if gui.Entry2.get():
        value = gui.Entry2.get()
        for mychar in value:
            ser.write(mychar.encode())
            time.sleep(0.1)

        gui.Entry2.delete(0, END)


def send_char():
    while True:
        if gui.Entry1.get():
            value = gui.Entry1.get()
            ser.write(value.encode())
            time.sleep(0.5)
            gui.Entry1.delete(0,END)

def read_char():
    global ser
    while True:
        if connected == 1:
            mychar = ser.read()
            gui.Text1.insert(END,mychar.decode())


if __name__ == '__main__':
    global root, gui, t1, t2

    root = tk.Tk()
    gui = Toplevel1(root)
    gui.che52.set(1)

    t1 = threading.Thread(target = send_char)
    t1.daemon = True
    t1.start()

    t2 = threading.Thread(target = read_char)
    t2.daemon = True
    t2.start()

    root.mainloop()


    # UART_Interface_support.main()




