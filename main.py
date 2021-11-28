import cv2
import numpy as np
import os
from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
from time import strftime
from datetime import datetime
from managestudent import Manage_Student
from attendance import View_Attendance
from tkinter import messagebox
import tkinter
import mysql.connector

class Face_Recognition_Attendance_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1280x720+0+0')
        self.root.title('Face Recognition Attendance System')
        self.root.configure(bg='#f5f5f5')


        # First image
        img = Image.open(r'D:\DemoPython\AttendanceSystemDemo\image_system\Greenwich.jpg')
        img = img.resize((700, 720), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=700, height=720)

        # Second image
        img2 = Image.open(r'D:\DemoPython\AttendanceSystemDemo\image_system\logo.png')
        img2 = img2.resize((480, 230), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=750, y=20, width=480, height=230)

        # Title Homepage
        title_lbl = Label(text="FACE RECOGNITION ATTENDANCE SYSTEM", font=("montserrat", 15, 'bold'), bg='#f5f5f5',
                          fg='black')
        title_lbl.place(x=750, y=270, width=480, height=50)

        # Manage Student Button
        button1 = Button(text='Manage Student', command = self.student, cursor='hand2',
                         font=("montserrat", 10, 'bold'), bg='#5E95E7', fg='white', activebackground='#5E95E7',
                         relief='ridge')
        button1.place(x=825, y=380, width=330, height=40)

        # Train Data Button
        button2 = Button(text='Train Data', cursor='hand2',command = self.train,
                         font=("montserrat", 10, 'bold'), bg='#5E95E7', fg='white',
                         activebackground='#5E95E7', relief='ridge')
        button2.place(x=825, y=440, width=330, height=40)

        # Check Attendance Button
        button3 = Button(text='Check Attendance',command = self.detect, cursor='hand2',
                         font=("montserrat", 10, 'bold'), bg='#5E95E7',
                         fg='white', activebackground='#5E95E7', relief='ridge')
        button3.place(x=825, y=500, width=330, height=40)

        # View Attendance Button
        button4 = Button(text='View Attendance',command = self.viewattendance, cursor='hand2',
                         font=("montserrat", 10, 'bold'), bg='#5E95E7',
                         fg='white', activebackground='#5E95E7', relief='ridge')
        button4.place(x=825, y=560, width=330, height=40)


        # Exit Button
        button5 = Button(text='Exit', cursor='hand2',command = self.iExit, font=("montserrat", 10, 'bold'), bg='#5E95E7',
                         fg='white',
                         activebackground='#5E95E7', relief='ridge')
        button5.place(x=825, y=620, width=330, height=40)

        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)

        lbl = Label(self.root, font=("montserrat", 10, 'bold'), bg='#f5f5f5', fg='blue')
        lbl.place(x=937, y=310, width=110, height=50)
        time()

    # ================== Function button =====================
    def student(self):
        self.new_window = Toplevel(self.root)
        self.app = Manage_Student(self.new_window)

    # ================== Function button =====================
    def train(self):
        os.system('python train.py')

    # ================== Face Recognition =====================
    def detect(self):
        os.system('python detection.py')

    # ================== Exit ============================
    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno('Face Recognition System','Are you sure to want exit',parent = self.root)
        if self.iExit > 0:
            self.root.destroy()
        else:
            return

    # ========== View Attendance ==============
    def viewattendance(self):
        self.new_window = Toplevel(self.root)
        self.app = View_Attendance(self.new_window)

if __name__ == '__main__':
    root = Tk()
    obj = Face_Recognition_Attendance_System(root)
    root.mainloop()