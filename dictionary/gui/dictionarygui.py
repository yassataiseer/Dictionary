
import tkinter
import os
from tkinter import *
import math
import random
import time
from tkinter import messagebox
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename
import csv
import json
import requests
from tkinter.ttk import Frame, Label, Button, Style
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

screen=tkinter.Tk()

screen.geometry('1000x500')
screen.option_add( "*font", "lucida 12 bold italic" )


screen.title('')
frame=Frame(screen)

frame.grid(row=0,column=0)



#labels
l1=tkinter.Label(frame,text="Word Dictionary",font=("Fixed",18),fg="blue")
l1.grid(row=0,column=1)


##
text_Input = StringVar()
operator =""

l3=tkinter.Label(frame,text="Enter the Word:",font=("Fixed",14),fg="black")
l3.grid(row=3,column=0)

e2=Text(frame,height=1,width=15)
e2.grid(row=3,column=1)

l4=tkinter.Label(frame,text="Meaning will be here:",font=("Fixed",14),fg="black")
l4.grid(row=3,column=0)
e3=Text(frame,height=3,width=35)
e3.grid(row=4,column=1)


photo = PhotoImage(file = r"C:\Users\Admin\Desktop\dictionary\gui\button.png") 
photo1 = PhotoImage(file = r"C:\Users\Admin\Desktop\dictionary\gui\exit.png") 
def save():
    try:
        word = e2.get('1.0',END)
        print(word)
        url = f"""https://googledictionaryapi.eu-gb.mybluemix.net/?define={word}"""
        rawData = requests.get(url).json()
        data = rawData[0]['meaning']['noun'][0]['definition']
        mean =  f"""The definition for that word is: {data}"""
        e3.insert(END, mean)

    except:
        pass
def ext():
    screen.destroy()

b1=tkinter.Label(frame,text="",font=("Fixed",14),fg="black")
b1.grid(row=5,column=1)
b1=tkinter.Button(frame,image = photo,command=save)
b1.grid(row=6,column=1)

b2=tkinter.Button(frame,image = photo1,command=ext)
b2.grid(row=3,column=5)

screen.mainloop()
