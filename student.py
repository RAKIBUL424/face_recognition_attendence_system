from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x720+0+0")
        self.root.title("Face Recognition System")

        #==========variable for data==========
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = IntVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()



        # Top banners
        img1 = Image.open(r"c:\Users\User\OneDrive\Desktop\image_of_face\images (3).jpeg")
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        first_label1 = Label(self.root, image=self.photoimg1)
        first_label1.place(x=0, y=0, width=500, height=130)

        img2 = Image.open(r"c:\Users\User\OneDrive\Desktop\image_of_face\download.jpeg")
        img2 = img2.resize((500, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        first_label2 = Label(self.root, image=self.photoimg2)
        first_label2.place(x=500, y=0, width=500, height=130)

        img3 = Image.open(r"c:\Users\User\OneDrive\Desktop\image_of_face\images (2).jpeg")
        img3 = img3.resize((500, 130), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        first_label3 = Label(self.root, image=self.photoimg3)
        first_label3.place(x=1000, y=0, width=500, height=130)

        # Background
        img_bg = Image.open(r"c:\Users\User\OneDrive\Desktop\image_of_face\istockphoto-1470617656-612x612.jpg")
        img_bg = img_bg.resize((1480, 780), Image.LANCZOS)
        self.photoimg_bg = ImageTk.PhotoImage(img_bg)
        bg_image = Label(self.root, image=self.photoimg_bg)
        bg_image.place(x=0, y=130, width=1480, height=720)

        # Title
        title = Label(bg_image, text="STUDENT MANAGEMENT SYSTEM",
                      font=('times new roman', 35, 'bold'), bg='#070ed5', fg='#bfc9ca')
        title.place(x=0, y=0, width=1480, height=45)

        main_frame = Frame(bg_image, bd=2)
        main_frame.place(x=10, y=55, width=1330, height=526)

        #left frame
        left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details", font=('times new roman', 12, "bold"))
        left_frame.place(x=5, y=5, width=665, height=510)

        img_left = Image.open(r"c:\Users\User\OneDrive\Desktop\image_of_face\images (5).jpeg")
        img_left = img_left.resize((720, 130), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        left_img = Label(left_frame, image=self.photoimg_left)
        left_img.place(x=5, y=0, width=650, height=100)

        #current course frame
        current_course_frame = LabelFrame(left_frame, bd=2, relief=RIDGE, text="Current course Information", font=('times new roman', 12, "bold"))
        current_course_frame.place(x=5, y=100, width=650, height=120)

        dep_label = Label(current_course_frame, text='Department', font=('times new roman', 12,'bold'))
        dep_label.grid(row=0, column=0)
        dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_dep, font=('times new roman', 12,'bold'), state="read only")
        dep_combo['values'] = ("Select Department","CSE","IT","ECE","CIVIL")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10)
        #semester label
        semester_label = Label(current_course_frame, text='Semester', font=('times new roman', 12,'bold'))
        semester_label.grid(row=0, column=2, padx=2, sticky=W)
        semester_combo = ttk.Combobox(current_course_frame,textvariable=self.var_semester, font=('times new roman', 12,'bold'), state="read only")
        semester_combo['values'] = ("Select Semester","Semester-1","Semester-2")
        semester_combo.current(0)
        semester_combo.grid(row=0, column=3, padx=2, pady=10)

        #year label
        year_label = Label(current_course_frame, text='Year', font=('times new roman', 12,'bold'))
        year_label.grid(row=1, column=0, padx=2, sticky=W)
        year_combo = ttk.Combobox(current_course_frame,textvariable=self.var_year, font=('times new roman', 12,'bold'), state="read only")
        year_combo['values'] = ("Select Year","2020","2021","2022","2023","2024")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10)
        #Course
        course_label = Label(current_course_frame, text='Course', font=('times new roman', 12,'bold'))
        course_label.grid(row=1, column=2, padx=2, sticky=W)
        course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_course, font=('times new roman', 12,'bold'), state="read only")
        course_combo['values'] = ("Select course","FE","SE","BE","TE")
        course_combo.current(0)
        course_combo.grid(row=1, column=3, padx=2, pady=10)

        #class student frame
        class_student_frame = LabelFrame(left_frame, bd=2, relief=RIDGE, text="Class Student Information", font=('times new roman', 12, "bold"))
        class_student_frame.place(x=5, y=135+90, width=650, height=260)
        #studentID
        student_label = Label(class_student_frame, text='StudentID',font=('times new roman', 12,'bold'))
        student_label.grid(row=0, column=0, padx=2, sticky=W)
        studentID_entry = ttk.Entry(class_student_frame,textvariable=self.var_std_id, width=20, font=('times new roman', 12,'bold'))
        studentID_entry.grid(row=0, column=1, padx=2, sticky=W)
        #student name
        student_name_label = Label(class_student_frame, text='Student Name:',font=('times new roman', 12,'bold'))
        student_name_label.grid(row=0, column=2, padx=5, sticky=W)
        student_name_entry = ttk.Entry(class_student_frame,textvariable=self.var_std_name, width=20, font=('times new roman', 12,'bold'))
        student_name_entry.grid(row=0, column=3, padx=2, sticky=W)
        #class division
        division_label = Label(class_student_frame, text='Division:',font=('times new roman', 12,'bold'))
        division_label.grid(row=1, column=0, padx=2, pady=5, sticky=W)
        division_entry = ttk.Entry(class_student_frame,textvariable=self.var_div, width=20, font=('times new roman', 12,'bold'))
        division_entry.grid(row=1, column=1, padx=2, pady=5, sticky=W)
        #roll no
        roll_no_label = Label(class_student_frame, text='Roll No:',font=('times new roman', 12,'bold'))
        roll_no_label.grid(row=1, column=2, padx=2, pady=5, sticky=W)
        roll_no_entry = ttk.Entry(class_student_frame,textvariable=self.var_roll, width=20, font=('times new roman', 12,'bold'))
        roll_no_entry.grid(row=1, column=3, padx=2, pady=5, sticky=W)
        #gender
        gender_label = Label(class_student_frame, text='Gender:',font=('times new roman', 12,'bold'))
        gender_label.grid(row=2, column=0, padx=2, pady=5, sticky=W)
        gender_entry = ttk.Entry(class_student_frame,textvariable=self.var_gender, width=20, font=('times new roman', 12,'bold'))
        gender_entry.grid(row=2, column=1, padx=2, pady=5, sticky=W)
        #dob
        dob_label = Label(class_student_frame, text='DOB:',font=('times new roman', 12,'bold'))
        dob_label.grid(row=2, column=2, padx=2, pady=5, sticky=W)
        dob_entry = ttk.Entry(class_student_frame,textvariable=self.var_dob, width=20, font=('times new roman', 12,'bold'))
        dob_entry.grid(row=2, column=3, padx=2, pady=5, sticky=W)
        #email
        email_label = Label(class_student_frame, text='E-mail:',font=('times new roman', 12,'bold'))
        email_label.grid(row=3, column=0, padx=2, pady=5, sticky=W)
        email_entry = ttk.Entry(class_student_frame,textvariable=self.var_email, width=20, font=('times new roman', 12,'bold'))
        email_entry.grid(row=3, column=1, padx=2, pady=5, sticky=W)
        #phone no
        phone_no_label = Label(class_student_frame, text='Phone No',font=('times new roman', 12,'bold'))
        phone_no_label.grid(row=3, column=2, padx=2, pady=5, sticky=W)
        phone_no_entry = ttk.Entry(class_student_frame,textvariable=self.var_phone, width=20, font=('times new roman', 12,'bold'))
        phone_no_entry.grid(row=3, column=3, padx=2, pady=5, sticky=W)
        #address
        address_label = Label(class_student_frame, text='Address',font=('times new roman', 12,'bold'))
        address_label.grid(row=4, column=0, padx=2, pady=5, sticky=W)
        address_entry = ttk.Entry(class_student_frame,textvariable=self.var_address, width=20, font=('times new roman', 12,'bold'))
        address_entry.grid(row=4, column=1, padx=2, pady=5, sticky=W)
        #teacher name
        teacher_name_label = Label(class_student_frame, text='Teacher Name',font=('times new roman', 12,'bold'))
        teacher_name_label.grid(row=4, column=2, padx=2, pady=5, sticky=W)
        teacher_name_entry = ttk.Entry(class_student_frame,textvariable=self.var_teacher, width=20, font=('times new roman', 12,'bold'))
        teacher_name_entry.grid(row=4, column=3, padx=2, pady=5, sticky=W)
        #buttons
        self.var_radio1 = StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1, text='Take Photo Sample', value='Yes')
        radiobtn1.grid(row=5, column=0, padx=2, sticky=W)
        
        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1, text='No Photo Sample', value='No')
        radiobtn2.grid(row=5, column=3, padx=2, sticky=W)
        #buttons frame
        button_frame = Frame(class_student_frame, bd=2, relief=RIDGE, bg='white')
        button_frame.place(x=0, y=184, width=645, height=50)
        #save button
        save_button = Button(button_frame,command=self.add_data, width=11, height=2, text="Save", font=('times new roman', 12, 'bold'), bg='#2e86c1')
        save_button.grid(row=0, column=0)
        #update
        update_button = Button(button_frame, width=11, height=2, text="Update", font=('times new roman', 12, 'bold'), bg='#229954')
        update_button.grid(row=0, column=1)
        #reset
        reset_button = Button(button_frame, width=11, height=2, text="Reset", font=('times new roman', 12, 'bold'), bg='#f1c40f')
        reset_button.grid(row=0, column=2)
        #delete
        delete_button = Button(button_frame, width=11, height=2, text="Delete", font=('times new roman', 12, 'bold'), bg='#ba4a00')
        delete_button.grid(row=0, column=3)
        #take photo sample
        take_photo_button = Button(button_frame, width=11, height=2, text="TPS", font=('times new roman', 12, 'bold'), bg='#a569bd')
        take_photo_button.grid(row=0, column=4)
        #update photo sample
        update_photo_button = Button(button_frame, width=11, height=2, text="UPS", font=('times new roman', 12, 'bold'), bg='#34495e')
        update_photo_button.grid(row=0, column=5)




        #right frame
        right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details", font=('times new roman', 12, "bold"))
        right_frame.place(x=672, y=5, width=650, height=510)
        img_right = Image.open(r"c:\Users\User\OneDrive\Desktop\image_of_face\istockphoto-1164612248-612x612.jpg")
        img_right = img_right.resize((720, 130), Image.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        right_img = Label(right_frame, image=self.photoimg_right)
        right_img.place(x=5, y=0, width=645, height=100)
        #==========Search system============
        search_frame = LabelFrame(right_frame, bd=2, relief=RIDGE, text="Search System", font=('times new roman', 12, "bold"))
        search_frame.place(x=5, y=102, width=642, height=65)
        #search buttons
        search_by_label = Label(search_frame, text='Search By :', font=('times new roman', 12, 'bold'), bg='#7f8c8d')
        search_by_label.grid(row=0, column=0, padx=3, pady=2)
        search_combo = ttk.Combobox(search_frame, font=('times new roman', 12,'bold'), state="read only")
        search_combo['values'] = ("Select","Roll_no","SE","BE","TE")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=2)
        #entry fill
        entry_fill = ttk.Entry(search_frame, width=20, font=('times new roman', 12,'bold'))
        entry_fill.grid(row=0, column=2, padx=2, pady=2)
        #search button
        search_button = Button(search_frame, width=8, height=1, text="Search", font=('times new roman', 12, 'bold'), bg='#7d3c98')
        search_button.grid(row=0, column=3, padx=2, pady=2)
        #search all
        search_all_button = Button(search_frame, width=8, height=1, text="Search All", font=('times new roman', 12, 'bold'), bg='#1abc9c')
        search_all_button.grid(row=0, column=4, padx=2, pady=2)
        #========table frame=========
        table_frame = Frame(right_frame, bd=2, relief=RIDGE)
        table_frame.place(x=0, y=170, width=645, height=150)
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, columns=("dep", "course", "year","sem", "id", "name","div",'roll', "gender", "dob", "email", "phone", "address", "teacher", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll")
        self.student_table.heading('gender', text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="E-mail")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="Photo")
        self.student_table['show']='headings'
        
        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=100)
        

        self.student_table.pack(fill=BOTH, expand=1)
        self.fetch_data()
    #==========function declaration=============
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get()=="":
            messagebox.showerror('Error', 'All Fields are required!', parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='root', password='1234', database='face_recognizer')
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                 self.var_dep.get(),
                 self.var_course.get(),
                 self.var_year.get(),
                 self.var_semester.get(),
                 self.var_std_id.get(),
                 self.var_std_name.get(),
                 self.var_div.get(),
                 self.var_roll.get(),
                 self.var_gender.get(),
                 self.var_dob.get(),
                 self.var_email.get(),
                 self.var_phone.get(),
                 self.var_address.get(),
                 self.var_teacher.get(),
                 self.var_radio1.get(),  # Assuming this is for the 'photo' column.
))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('success',"Student Details Has been Added successfully!!", parent= self.root) 
            except Exception as es:
                messagebox.showerror('Error',f"Due to :{str(es)}", parent= self.root)
    #==========fetch data=========
    def fetch_data(self):
        conn = mysql.connector.connect(host='localhost', username='root', password='1234', database='face_recognizer')
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM student")
        data = my_cursor.fetchall()
        if len(data) != 0 :
            self.student_table.delete(*student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
            conn.close()





if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()