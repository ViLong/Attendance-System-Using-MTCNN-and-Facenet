from tkinter import *
from PIL import Image, ImageTk

from time import strftime
from datetime import datetime

import smtplib, email, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from tkinter import messagebox

import csv
from tkinter import ttk
import pandas as pd


mydata = []
class View_Attendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry('1280x720+0+0')
        self.root.title('View Attendance')
        self.root.configure(bg='#f5f5f5')

        # Logo image
        img = Image.open(r'D:\DemoPython\AttendanceSystem\image_system\logo_2.jpg')
        img = img.resize((450, 250), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=450, height=250)

        # Title Homepage
        title_lbl = Label(self.root, text="VIEW ATTENDANCE STUDENT", font=("montserrat", 32, 'bold'), bg='#f5f5f5',
                          fg='black')
        title_lbl.place(x=515, y=75, width=700, height=100)

        # Main Frame
        main_frame = Frame(self.root, bd='2', bg='white')
        main_frame.place(x=5, y=260, width=1270, height=460)

        # Student Left Frame
        left_frame = LabelFrame(main_frame, bg='white', bd='2', relief='ridge', text='Search Student Attendance',
                                font=("montserrat", 13, 'bold'))
        left_frame.place(x=10, y=10, width=600, height=440)

        # Left Inside frame
        left_inside_frame = Frame(left_frame, bg='white')
        left_inside_frame.place(x=5, y=5, width=585, height=400)

        # Label Entry

        name_lbl = Label(left_inside_frame, text='Student Name', font=("montserrat", 13, 'bold'), bg='white')
        name_lbl.place(x=50, y=80, width=150, height=30)

        self.name_data = StringVar()
        name_entry = ttk.Entry(left_inside_frame,textvariable=self.name_data, width=27, font=("montserrat", 12, 'bold'))
        name_entry.place(x=250, y=80, width=270, height=30)


        # Button Frame
        btn_frame = Frame(left_inside_frame, bg='white')
        btn_frame.place(x=5, y=180, width=571, height=800)

        # Search button
        search_btn = Button(btn_frame,command = self.search ,text='Search', cursor='hand2', font=("montserrat", 12, 'bold'), bg='#5E95E7', fg='white', activebackground='#5E95E7', relief='ridge')
        search_btn.place(x=10, y=25, width=250, height=50)

        # Show All button
        showAll_btn = Button(btn_frame,command = self.fetch_data, text='Show All', cursor='hand2', font=("montserrat", 12, 'bold'), bg='#5E95E7', fg='white', activebackground='#5E95E7', relief='ridge')
        showAll_btn.place(x=310, y=25, width=250, height=50)

        # Send CSV button
        sendcsv_btn = Button(btn_frame, text='Send CSV file to Email',command = self.sendemail, cursor='hand2',
                             font=("montserrat", 12, 'bold'), bg='#5E95E7', fg='white', activebackground='#5E95E7',
                             relief='ridge')
        sendcsv_btn.place(x=10, y=85, width=250, height=50)

        # Reset Data button
        reset_btn = Button(btn_frame, text='Reset Data',command = self.resetdata, cursor='hand2',
                             font=("montserrat", 12, 'bold'), bg='#5E95E7', fg='white', activebackground='#5E95E7',
                             relief='ridge')
        reset_btn.place(x=310, y=85, width=250, height=50)

        # Student Right Frame
        right_frame = LabelFrame(main_frame, bg='white', bd='2', relief='ridge', text='Student Attendance Details',
                                 font=("montserrat", 13, 'bold'))
        right_frame.place(x=620, y=10, width=630, height=440)

        table_frame = Frame(right_frame, bd=2, bg='white', relief='ridge')
        table_frame.place(x=5, y=5, width=615, height=400)

        # Scroll Bar Table
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.attendance_table = ttk.Treeview(table_frame,xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.attendance_table.xview)
        scroll_y.config(command=self.attendance_table.yview)


        self.attendance_table.pack(fill=BOTH,expand=1)
        self.fetch_data()

    # ======================= Fetch Data ==========================
    def fetch_data(self):
        with open('attendance.csv') as file:
            df = pd.read_csv('attendance.csv')

        self.attendance_table['column'] = list(df.columns)
        self.attendance_table["show"] = 'headings'
        for column in self.attendance_table['columns']:
            self.attendance_table.heading(column,text=column)

        self.attendance_table.delete(*self.attendance_table.get_children())
        df_rows= df.to_numpy().tolist()
        for row in df_rows:
            self.attendance_table.insert("",END,values = row)


    def search(self):
        with open('attendance.csv','r') as file:
            filereader = csv.reader(file)
            filereader_list = list(filereader)

        self.attendance_table.delete(*self.attendance_table.get_children())
        word = self.name_data.get().title()
        if self.name_data.get():
            for i in filereader_list:
                if word in i:
                    self.attendance_table.insert("", END, values=i)



    def sendemail(self):
        curr = datetime.now()
        dt = curr.strftime("%d/%m/%Y")

        subject = "Data Attendance"
        body = "Here are the data attendance"
        sender_email = "universitygreenwichattendance@gmail.com"
        receiver_email = "vilong242@gmail.com"
        password = 'mkbwaznnpkxulxiy'

        # Create a multipart message and set headers
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        message["Bcc"] = receiver_email  # Recommended for mass emails

        # Add body to email
        message.attach(MIMEText(body, "plain"))

        filename = "attendance.csv"  # In same directory as script

        # Open PDF file in binary mode
        with open(filename, "rb") as attachment:
            # Add file as application/octet-stream
            # Email client can usually download this automatically as attachment
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        # Encode file in ASCII characters to send by email
        encoders.encode_base64(part)

        # Add header as key/value pair to attachment part
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )

        # Add attachment to message and convert message to string
        message.attach(part)
        text = message.as_string()

        # Log in to server using secure context and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text)
            messagebox.showinfo('Successfull', f'Attendance data on %s has been sent'%dt)





    def resetdata(self):
        df = pd.read_csv('attendance.csv')
        f = df.drop(df.index)
        f.to_csv('attendance.csv',index=None)
        messagebox.showinfo('Success','Attendance data has been cleared')


if __name__ == '__main__':
    root = Tk()
    obj = View_Attendance(root)
    root.mainloop()

