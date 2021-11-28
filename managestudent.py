from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
from mtcnn_cv2 import MTCNN

class Manage_Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry('1280x720+0+0')
        self.root.title('Student Management')
        self.root.configure(bg='#f5f5f5')

        # ================ Variables ==================
        self.var_fac = StringVar()
        self.var_cou = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_class = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()


        # Logo image
        img = Image.open(r'D:\DemoPython\AttendanceSystem\image_system\logo_2.jpg')
        img = img.resize((450, 250), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=450, height=250)

        # Title Homepage
        title_lbl = Label(self.root, text="STUDENT MANAGEMENT", font=("montserrat", 40, 'bold'), bg='#f5f5f5',
                          fg='black')
        title_lbl.place(x=515, y=75, width=700, height=100)

        # Main Frame
        main_frame = Frame(self.root, bd='2', bg='white')
        main_frame.place(x=5, y=260, width=1270, height=460)

        # Student Left Frame
        left_frame = LabelFrame(main_frame, bg='white', bd='2', relief='ridge', text='Add Student Information',
                                font=("montserrat", 10, 'bold'))
        left_frame.place(x=10, y=10, width=600, height=440)

        # Current Course Frame
        current_course_frame = LabelFrame(left_frame, bg='white', bd='2', relief='ridge',
                                          text='Current Course Information', font=("montserrat", 10, 'bold'))
        current_course_frame.place(x=5, y=5, width=585, height=100)

        # Faculty
        fac_label = Label(current_course_frame, text='Faculty', font=("montserrat", 10, 'bold'), bg='white')
        fac_label.grid(row=0, column=0, padx=8, sticky=W)

        fac_combobox = ttk.Combobox(current_course_frame,textvariable=self.var_fac, font=("montserrat", 10, 'bold'),
                                    state='readonly', width=18)
        fac_combobox['values'] = ('Select Faculty', 'Information Technology', 'Business Management', 'Graphic Design')
        fac_combobox.current(0)
        fac_combobox.grid(row=0, column=1, padx=8, pady=5, sticky=W)

        # Course
        cou_label = Label(current_course_frame, text='Course', font=("montserrat", 10, 'bold'), bg='white')
        cou_label.grid(row=0, column=2, padx=8, sticky=W)

        cou_combobox = ttk.Combobox(current_course_frame,textvariable=self.var_cou, font=("montserrat", 10, 'bold'),
                                    state='readonly', width=18)
        cou_combobox['values'] = ('Select Course', 'Top-Up', 'BTEC', 'English')
        cou_combobox.current(0)
        cou_combobox.grid(row=0, column=3, padx=8, pady=5, sticky=W)

        # Year
        year_label = Label(current_course_frame, text='Year', font=("montserrat", 10, 'bold'), bg='white')
        year_label.grid(row=1, column=0, padx=8, sticky=W)

        year_combobox = ttk.Combobox(current_course_frame,textvariable=self.var_year, font=("montserrat", 10, 'bold'),
                                     state='readonly', width=18)
        year_combobox['values'] = ('Select Year', '2018', '2019', '2020', '2021')
        year_combobox.current(0)
        year_combobox.grid(row=1, column=1, padx=8, pady=5, sticky=W)

        # Semester
        sem_label = Label(current_course_frame, text='Semester', font=("montserrat", 10, 'bold'), bg='white')
        sem_label.grid(row=1, column=2, padx=8, sticky=W)

        sem_combobox = ttk.Combobox(current_course_frame,textvariable=self.var_sem, font=("montserrat", 10, 'bold'),
                                    state='readonly', width=18)
        sem_combobox['values'] = ('Select Semester', 'Spring', 'Summer', 'Autumn')
        sem_combobox.current(0)
        sem_combobox.grid(row=1, column=3, padx=8, pady=5, sticky=W)

        # Class Student Frame
        class_student_frame = LabelFrame(left_frame, bg='white', bd='2', relief='ridge', text='Student Information',
                                         font=("montserrat", 10, 'bold'))
        class_student_frame.place(x=5, y=110, width=585, height=305)

        # Student ID
        studentID_lbl = Label(class_student_frame, text='Student ID', font=("montserrat", 10, 'bold'), bg='white')
        studentID_lbl.grid(row=0, column=0, padx=8, pady=8, sticky=W)

        studentID_entry = ttk.Entry(class_student_frame,textvariable=self.var_std_id, width=18,
                                    font=("montserrat", 10, 'bold'))
        studentID_entry.grid(row=0, column=1, padx=8, pady=8, sticky=W)

        # Student Name
        studentName_lbl = Label(class_student_frame, text='Student Name', font=("montserrat", 10, 'bold'), bg='white')
        studentName_lbl.grid(row=0, column=2, padx=8, pady=8, sticky=W)

        studentName_entry = ttk.Entry(class_student_frame,textvariable=self.var_std_name, width=18,
                                      font=("montserrat", 10, 'bold'))
        studentName_entry.grid(row=0, column=3, padx=8, pady=8, sticky=W)

        # Student Class
        studentClass_lbl = Label(class_student_frame, text='Class', font=("montserrat", 10, 'bold'), bg='white')
        studentClass_lbl.grid(row=1, column=0, padx=8, pady=8, sticky=W)

        studentClass_entry = ttk.Entry(class_student_frame,textvariable=self.var_class, width=18,
                                       font=("montserrat", 10, 'bold'))
        studentClass_entry.grid(row=1, column=1, padx=8, pady=8, sticky=W)

        # Student Gender
        studentGender_lbl = Label(class_student_frame, text='Gender', font=("montserrat", 10, 'bold'), bg='white')
        studentGender_lbl.grid(row=1, column=2, padx=8, pady=8, sticky=W)

        studentGender_combobox = ttk.Combobox(class_student_frame,textvariable=self.var_gender,
                                              font=("montserrat", 10, 'bold'), state='readonly', width=16)
        studentGender_combobox['values'] = ('Male', 'Female')
        studentGender_combobox.current(0)
        studentGender_combobox.grid(row=1, column=3, padx=8, pady=5, sticky=W)

        # Student DOB
        studentDob_lbl = Label(class_student_frame, text='Birthday', font=("montserrat", 10, 'bold'), bg='white')
        studentDob_lbl.grid(row=2, column=0, padx=8, pady=8, sticky=W)

        studentDob_entry = ttk.Entry(class_student_frame,textvariable=self.var_dob, width=18,
                                     font=("montserrat", 10, 'bold'))
        studentDob_entry.grid(row=2, column=1, padx=8, pady=8, sticky=W)

        # Student Email
        studentEmail_lbl = Label(class_student_frame, text='Email', font=("montserrat", 10, 'bold'), bg='white')
        studentEmail_lbl.grid(row=2, column=2, padx=8, pady=8, sticky=W)

        studentEmail_entry = ttk.Entry(class_student_frame,textvariable=self.var_email, width=18,
                                       font=("montserrat", 10, 'bold'))
        studentEmail_entry.grid(row=2, column=3, padx=8, pady=8, sticky=W)

        # Student Phone
        studentPhone_lbl = Label(class_student_frame, text='Phone', font=("montserrat", 10, 'bold'), bg='white')
        studentPhone_lbl.grid(row=3, column=0, padx=8, pady=8, sticky=W)

        studentPhone_entry = ttk.Entry(class_student_frame,textvariable=self.var_phone, width=18,
                                       font=("montserrat", 10, 'bold'))
        studentPhone_entry.grid(row=3, column=1, padx=8, pady=8, sticky=W)

        # Student Address
        studentAddress_lbl = Label(class_student_frame, text='Address', font=("montserrat", 10, 'bold'), bg='white')
        studentAddress_lbl.grid(row=3, column=2, padx=8, pady=8, sticky=W)

        studentAddress_entry = ttk.Entry(class_student_frame,textvariable=self.var_address, width=18,
                                         font=("montserrat", 10, 'bold'))
        studentAddress_entry.grid(row=3, column=3, padx=8, pady=8, sticky=W)

        # Take Photo Sample Button
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1,text='Take Photo Sample',value='Yes')
        radiobtn1.grid(row=4, column=1)

        # No Photo Sample Button
        radiobtn2 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text='No Photo Sample', value='No')
        radiobtn2.grid(row=4, column=2)

        # Button Frame
        btn_frame = Frame(class_student_frame, bg='white')
        btn_frame.place(x=5, y=230, width=570, height=52)

        # Save button
        save_btn = Button(btn_frame, text='Save', command=self.add_data, cursor='hand2',
                          font=("montserrat", 11, 'bold'), bg='#5E95E7', fg='white', activebackground='#5E95E7',
                          relief='ridge')
        save_btn.place(x=5, y=5, width=100, height=40)

        # Update button
        update_btn = Button(btn_frame, text='Update', command=self.update_data, cursor='hand2',
                            font=("montserrat", 11, 'bold'), bg='#5E95E7', fg='white', activebackground='#5E95E7',
                            relief='ridge')
        update_btn.place(x=158, y=5, width=100, height=40)

        # Delete button
        delete_btn = Button(btn_frame, text='Delete', command=self.delete_data, cursor='hand2',
                            font=("montserrat", 11, 'bold'), bg='#5E95E7', fg='white', activebackground='#5E95E7',
                            relief='ridge')
        delete_btn.place(x=311, y=5, width=100, height=40)

        # Reset button
        reset_btn = Button(btn_frame, text='Reset', command=self.reset_data, cursor='hand2',
                           font=("montserrat", 11, 'bold'), bg='#5E95E7', fg='white', activebackground='#5E95E7',
                           relief='ridge')
        reset_btn.place(x=464, y=5, width=100, height=40)

        # Button Frame 1
        btn_frame1 = Frame(class_student_frame, bg='white')
        btn_frame1.place(x=5, y=185, width=570, height=47)

        # Take Photo button
        take_photo_btn = Button(btn_frame1, text='Take Photo',command=self.generate_dataset, cursor='hand2',
                                font=("montserrat", 11, 'bold'), bg='#3e3e3e', fg='white', activebackground='#3e3e3e',
                                relief='ridge')
        take_photo_btn.place(x=50, y=3, width=180, height=38)

        # Update Photo button
        update_photo_btn = Button(btn_frame1, text='Update Photo',command=self.generate_dataset, cursor='hand2', font=("montserrat", 11, 'bold'),
                                  bg='#3e3e3e', fg='white', activebackground='#3e3e3e', relief='ridge')
        update_photo_btn.place(x=335, y=3, width=180, height=38)

        # Student Right Frame
        right_frame = LabelFrame(main_frame, bg='white', bd='2', relief='ridge', text='Student Details',
                                 font=("montserrat", 10, 'bold'))
        right_frame.place(x=620, y=10, width=630, height=440)

        # ============= Search System ===============
        # Search Frame
        search_frame = LabelFrame(right_frame, bg='white', bd='2', relief='ridge', text='Search Tools',
                                  font=("montserrat", 10, 'bold'))
        search_frame.place(x=5, y=5, width=615, height=70)

        # Search label
        search_lbl = Label(search_frame, text='Search By :', font=("montserrat", 10, 'bold'), bg='#FC473C', fg='white')
        search_lbl.grid(row=0, column=0, padx=8, pady=8, sticky=W)

        self.search_by = StringVar()
        search_combobox = ttk.Combobox(search_frame,textvariable=self.search_by, font=("montserrat", 10, 'bold'),
                                       state='readonly', width=15)
        search_combobox['values'] = ('Select', 'Student_ID', 'Name', 'Phone')
        search_combobox.current(0)
        search_combobox.grid(row=0, column=1, padx=8, pady=5, sticky=W)

        self.search_data = StringVar()
        search_entry = ttk.Entry(search_frame,textvariable=self.search_data, width=15, font=("montserrat", 10, 'bold'))
        search_entry.grid(row=0, column=2, padx=8, pady=8, sticky=W)

        # Search button
        search_btn = Button(search_frame, text='Search',command=self.search_student, cursor='hand2',
                            font=("montserrat", 10, 'bold'), bg='#5E95E7', fg='white', activebackground='#5E95E7',
                            relief='ridge')
        search_btn.grid(row=0, column=3, padx=8, pady=5, sticky=W)

        # Show All button
        showAll_btn = Button(search_frame, text='Show All',command=self.fetch_data, cursor='hand2',
                             font=("montserrat", 10, 'bold'), bg='#5E95E7', fg='white', activebackground='#5E95E7',
                             relief='ridge')
        showAll_btn.grid(row=0, column=4, padx=8, pady=5, sticky=W)

        # =========== Table Frame =============
        table_frame = Frame(right_frame, bd=2, bg='white', relief='ridge')
        table_frame.place(x=5, y=80, width=615, height=335)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, column=(
        'fac', 'cou', 'year', 'sem', 'id', 'name', 'class', 'gender', 'dob', 'email', 'phone', 'address','photo'),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table['show'] = 'headings'

        self.student_table.heading('fac', text='Faculty')
        self.student_table.heading('cou', text='Course')
        self.student_table.heading('year', text='Year')
        self.student_table.heading('sem', text='Semester')
        self.student_table.heading('id', text='Student ID')
        self.student_table.heading('name', text='Student Name')
        self.student_table.heading('class', text='Class')
        self.student_table.heading('gender', text='Gender')
        self.student_table.heading('dob', text='Birthday')
        self.student_table.heading('email', text='Email')
        self.student_table.heading('phone', text='Phone')
        self.student_table.heading('address', text='Address')
        self.student_table.heading('photo', text='Photo Sample Status')


        self.student_table.column('fac', width=150)
        self.student_table.column('cou', width=100)
        self.student_table.column('year', width=100)
        self.student_table.column('sem', width=100)
        self.student_table.column('id', width=100)
        self.student_table.column('name', width=100)
        self.student_table.column('class', width=100)
        self.student_table.column('gender', width=100)
        self.student_table.column('dob', width=100)
        self.student_table.column('email', width=100)
        self.student_table.column('phone', width=100)
        self.student_table.column('address', width=100)
        self.student_table.column('photo', width=150)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind('<ButtonRelease>',self.get_cur)
        self.fetch_data()


    # ================== Function Decration ======================
    def add_data(self):
        if self.var_fac.get()=='Select Faculty' or self.var_std_name.get()=='' or self.var_std_id.get()=='':
            messagebox.showerror('Error','All field are required',parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host='localhost',user="root",password='Vilong242',db='face_recognition')
                cur=conn.cursor()
                cur.execute('insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                    self.var_fac.get(),
                    self.var_cou.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_class.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_radio1.get()
                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success', 'Student Information has been added successfully',parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Due to: {str(es)}',parent=self.root)


    # ======================= Fetch Data ==========================
    def fetch_data(self):
        conn = mysql.connector.connect(host='localhost', user="root", password='Vilong242', db='face_recognition')
        cur = conn.cursor()
        cur.execute('select * from student')
        data = cur.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert('',END,values=i)
            conn.commit()
        conn.close()



    # ======================= Get Cursor ==========================
    def get_cur(self,event=""):
        cur_focus = self.student_table.focus()
        content = self.student_table.item(cur_focus)
        data = content['values']

        self.var_fac.set(data[0]),
        self.var_cou.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_class.set(data[6]),
        self.var_gender.set(data[7]),
        self.var_dob.set(data[8]),
        self.var_email.set(data[9]),
        self.var_phone.set(data[10]),
        self.var_address.set(data[11]),
        self.var_radio1.set(data[12])



    # ======================= Update Data ==========================
    def update_data(self):
        if self.var_fac.get()=='Select Faculty' or self.var_std_name.get()=='' or self.var_std_id.get()=='':
            messagebox.showerror('Error','All field are required',parent=self.root)
        else:
            try:
                update = messagebox.askyesno('Update','Do you want to update this student ?',parent = self.root)
                if update>0:
                    conn = mysql.connector.connect(host='localhost', user="root", password='Vilong242', db='face_recognition')
                    cur = conn.cursor()
                    cur.execute('update student set Faculty=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Class=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,PhotoSample=%s where Student_ID=%s',(
                        self.var_fac.get(),
                        self.var_cou.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_std_name.get(),
                        self.var_class.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()
                    ))
                else :
                    if not update:
                        return
                messagebox.showinfo('Success','Student Information has been updated successfully',parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror('Error', f'Due to: {str(es)}', parent=self.root)



    # ===================== Delete Function =======================
    def delete_data(self):
        if self.var_std_id.get()=='':
            messagebox.showerror('Error','Student ID must be required',parent=self.root)
        else:
            try:
                delete = messagebox.askyesno('Delete','Do you want delete this student ?',parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host='localhost', user="root", password='Vilong242',db='face_recognition')
                    cur = conn.cursor()
                    sql = 'delete from student where Student_ID=%s'
                    value = (self.var_std_id.get(),)
                    cur.execute(sql,value)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Delete','Student has been deleted successfully',parent=self.root)
            except Exception as es:
                messagebox.showerror('Error', f'Due to: {str(es)}', parent=self.root)


    # ===================== Reset Data =======================
    def reset_data(self):
        self.var_fac.set('Select Faculty')
        self.var_cou.set('Select Course')
        self.var_year.set('Select Year')
        self.var_sem.set('Select Semester')
        self.var_std_id.set('')
        self.var_std_name.set('')
        self.var_class.set('')
        self.var_gender.set('Male')
        self.var_dob.set('')
        self.var_email.set('')
        self.var_phone.set('')
        self.var_address.set('')
        self.var_radio1.set('')




    # ===================== Generate Dataset or Take Photo button ============================
    def generate_dataset(self):
        if self.var_fac.get()=='Select Faculty' or self.var_std_name.get()=='' or self.var_std_id.get()=='':
            messagebox.showerror('Error','All field are required',parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host='localhost', user="root", password='Vilong242', db='face_recognition')
                cur = conn.cursor()
                cur.execute('select * from student')
                result = cur.fetchall()
                id = 0
                for x in result:
                    id += 1
                cur.execute(
                'update student set Faculty=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Class=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,PhotoSample=%s where Student_ID=%s',
                    (
                        self.var_fac.get(),
                        self.var_cou.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_std_name.get(),
                        self.var_class.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get() == id+1
                    ))

                conn.commit()
                name = str(self.var_std_name.get())
                os.makedirs('dataSet/' +name+ '-' +str(id)+'')
                self.fetch_data()
                self.reset_data()
                conn.close()


                # ============== Load Predifined data ==============
                detector = MTCNN()
                camera = cv2.VideoCapture(0)
                sampleNum = 0

                while True:
                    ret, my_frame = camera.read()

                    my_frame = cv2.flip(my_frame, 1)
                    faces = detector.detect_faces(my_frame)

                    if faces != [] :
                        for person in faces:
                            bounding_box = person['box']
                            keypoints = person['keypoints']

                            cv2.rectangle(my_frame,
                                          (bounding_box[0], bounding_box[1]),
                                          (bounding_box[0] + bounding_box[2], bounding_box[1] + bounding_box[3]),
                                          (0, 155, 255),
                                          2)

                            cv2.circle(my_frame, (keypoints['left_eye']), 2, (0, 155, 255), 2)
                            cv2.circle(my_frame, (keypoints['right_eye']), 2, (0, 155, 255), 2)
                            cv2.circle(my_frame, (keypoints['nose']), 2, (0, 155, 255), 2)
                            cv2.circle(my_frame, (keypoints['mouth_left']), 2, (0, 155, 255), 2)
                            cv2.circle(my_frame, (keypoints['mouth_right']), 2, (0, 155, 255), 2)

                            sampleNum += 1

                            file_path = "dataSet/" +str(name)+ '-' +str(id)+'' "/" +str(name)+ "-" +str(id)+ "." + str(sampleNum) + ".jpg"
                            cv2.imwrite(file_path,my_frame)

                        cv2.putText(my_frame, str(sampleNum), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (100, 200, 200), 2)
                        cv2.imshow('Take Photo', my_frame)

                    if cv2.waitKey(100) & 0xFF == ord('q'):
                        break
                    elif sampleNum > 100:
                        break

                camera.release()
                cv2.destroyAllWindows()
                messagebox.showinfo('Result', 'Taking photo completed !!!')

            except Exception as es:
                messagebox.showerror('Error', f'Due to: {str(es)}', parent=self.root)


    #================== Search ==================
    def search_student(self):
        conn = mysql.connector.connect(host='localhost', user="root", password='Vilong242', db='face_recognition')
        cur = conn.cursor()
        cur.execute('select * from student where '+str(self.search_by.get())+" LIKE '%"+str(self.search_data.get())+"%'")
        result = cur.fetchall()

        if len(result)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in result:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

if __name__ == '__main__':
    root = Tk()
    obj = Manage_Student(root)
    root.mainloop()