from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata = []
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x720+0+0")
        self.root.title("Face Recognition System")

        title = Label(self.root, text="Student Attendance Management System", font=('times new roman', 35, 'bold'), bg='#070ed5', fg='#bfc9ca')
        title.place(x=0, y=0, width=1480, height=45)

        #============variables===========
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()


        # img1 = Image.open(r"c:\Users\User\OneDrive\Desktop\image_of_face\images (3).jpeg")
        # img1 = img1.resize((500, 130), Image.LANCZOS)
        # self.photoimg1 = ImageTk.PhotoImage(img1)
        # first_label1 = Label(self.root, image=self.photoimg1)
        # first_label1.place(x=0, y=0, width=500, height=130)

        # img2 = Image.open(r"c:\Users\User\OneDrive\Desktop\image_of_face\download.jpeg")
        # img2 = img2.resize((500, 130), Image.LANCZOS)
        # self.photoimg2 = ImageTk.PhotoImage(img2)
        # first_label2 = Label(self.root, image=self.photoimg2)
        # first_label2.place(x=500, y=0, width=500, height=130)
        main_frame = Frame( bd=2)
        main_frame.place(x=10, y=55, width=1330, height=626)

        #left frame
        left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details", font=('times new roman', 12, "bold"))
        left_frame.place(x=5, y=5, width=665, height=510)

        left_inside_frame = Frame(left_frame, bd=2, relief=RIDGE)
        left_inside_frame.place(x=5, y=10, width=650, height=470)

         #studentID
        student_label = Label(left_frame, text='StudentID :',font=('times new roman', 12,'bold'))
        student_label.grid(row=1, column=0, padx=8, pady=15, sticky=W)
        studentID_entry = ttk.Entry(left_frame, width=20,textvariable=self.var_atten_id, font=('times new roman', 12,'bold'))
        studentID_entry.grid(row=1, column=2, padx=8,pady=10, sticky=W)

        #roll
        roll_label = Label(left_frame, text='Roll :',font=('times new roman', 12,'bold'))
        roll_label.grid(row=2, column=0, padx=8,pady=8, sticky=W)
        roll_entry = ttk.Entry(left_frame, width=20,textvariable=self.var_atten_roll, font=('times new roman', 12,'bold'))
        roll_entry.grid(row=2, column=2, padx=8, pady=8, sticky=W)

        #student name
        student_label = Label(left_frame, text='Student Name :',font=('times new roman', 12,'bold'))
        student_label.grid(row=2, column=0, padx=8,pady=8, sticky=W)
        student_entry = ttk.Entry(left_frame, width=20,textvariable=self.var_atten_name, font=('times new roman', 12,'bold'))
        student_entry.grid(row=2, column=2, padx=8, pady=8, sticky=W)

        #date
        date_label = Label(left_frame, text='Date :',font=('times new roman', 12,'bold'))
        date_label.grid(row=3, column=0, padx=8,pady=8, sticky=W)
        date_entry = ttk.Entry(left_frame, width=20,textvariable=self.var_atten_date, font=('times new roman', 12,'bold'))
        date_entry.grid(row=3, column=2, padx=8, pady=8, sticky=W)

        #department
        department_label = Label(left_frame, text='Department :',font=('times new roman', 12,'bold'))
        department_label.grid(row=4, column=0, padx=8,pady=8, sticky=W)
        department_entry = ttk.Entry(left_frame, width=20,textvariable=self.var_atten_dep, font=('times new roman', 12,'bold'))
        department_entry.grid(row=4, column=2, padx=8, pady=8, sticky=W)

        #time
        time_label = Label(left_frame, text='Time :',font=('times new roman', 12,'bold'))
        time_label.grid(row=5, column=0, padx=8,pady=8, sticky=W)
        time_entry = ttk.Entry(left_frame, width=20,textvariable=self.var_atten_time, font=('times new roman', 12,'bold'))
        time_entry.grid(row=5, column=2, padx=8, pady=8, sticky=W)

        #attendance
        attendance_label = Label(left_frame, text='Attendance Status :',font=('times new roman', 12,'bold'))
        attendance_label.grid(row=6, column=0, padx=8,pady=8, sticky=W)
        self.attendance_status = ttk.Combobox(left_frame, font=('times new roman', 12,'bold'), width=18,textvariable=self.var_atten_attendance, state='readonly')
        self.attendance_status['values'] = ("Select Status", "Present", "Absent")
        self.attendance_status.current(0)
        self.attendance_status.grid(row=6, column=2, padx=8, pady=8, sticky=W)

        #button frame
        #buttons frame
        button_frame = Frame(left_frame, bd=2, relief=RIDGE, bg='white')
        button_frame.place(x=0, y=384, width=645, height=50)
        #save button
        save_button = Button(button_frame, width=18, height=2, command=self.importCSV, text="Import CSV", font=('times new roman', 12, 'bold'), bg='#2e86c1')
        save_button.grid(row=0, column=0)
        #update
        update_button = Button(button_frame, width=15, height=2, command=self.exportCSV, text="Export CSV", font=('times new roman', 12, 'bold'), bg='#229954')
        update_button.grid(row=0, column=1)
        #reset
        reset_button = Button(button_frame, width=15, height=2, text="Update", font=('times new roman', 12, 'bold'), bg='#f1c40f')
        reset_button.grid(row=0, column=2)
        #delete
        delete_button = Button(button_frame, width=20,command=self.reset_data, height=2, text="Reset", font=('times new roman', 12, 'bold'), bg='#ba4a00')
        delete_button.grid(row=0, column=3)



        #right frame
        right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details", font=('times new roman', 12, "bold"))
        right_frame.place(x=672, y=5, width=650, height=510)
        img_right = Image.open

        #========table frame=========
        table_frame = Frame(right_frame, bd=2, relief=RIDGE)
        table_frame.place(x=0, y=70, width=645, height=250)
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame, column=('studentID', 'roll', 'name', 'department', 'date', 'time', 'attendance'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading('studentID', text='Student ID')
        self.AttendanceReportTable.heading('roll', text='Roll')
        self.AttendanceReportTable.heading('name', text='Name')
        self.AttendanceReportTable.heading('department', text='Department')
        self.AttendanceReportTable.heading('date', text='Date')
        self.AttendanceReportTable.heading('time', text='Time')
        self.AttendanceReportTable.heading('attendance', text='Attendance')
        self.AttendanceReportTable['show'] = 'headings'

        self.AttendanceReportTable.column('studentID', width=100)
        self.AttendanceReportTable.column('roll', width=100)
        self.AttendanceReportTable.column('name', width=100)
        self.AttendanceReportTable.column('department', width=100)
        self.AttendanceReportTable.column('date', width=100)
        self.AttendanceReportTable.column('time', width=100)
        self.AttendanceReportTable.column('attendance', width=100)


        self.AttendanceReportTable.pack(fill=BOTH, expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease-1>", self.get_cursor)
    
    #==================fetch data=================
    def fetchData(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert('', END, values=i)

    #==================import data=================
    def importCSV(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")))
        with open(fln) as myfile:
            csvread = csv.reader(myfile)
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    #==================export data=================
    def exportCSV(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data", "No Data Found to Export", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")))
            with open(fln, mode='w', newline='') as myfile:
                exp_write = csv.writer(myfile)
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export", "Your Data Exported to " + os.path.basename(fln) + " successfully")
        except Exception as es:
            messagebox.showerror("Error", f"Due to : {str(es)}", parent=self.root)
    
    #==================get cursor=================
    def get_cursor(self, event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        row = content['values']
        self.var_atten_id.set(row[0])
        self.var_atten_roll.set(row[1])
        self.var_atten_name.set(row[2])
        self.var_atten_dep.set(row[3])
        self.var_atten_date.set(row[4])
        self.var_atten_time.set(row[5])
        self.var_atten_attendance.set(row[6])
    
    #==================reset data=================
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_date.set("")
        self.var_atten_time.set("")
        self.var_atten_attendance.set("")
    
    #==================update data=================
    # def update_data(self):
    #     if self.var_atten_id.get() == "":
    #         messagebox.showerror("Error", "Student ID must be required", parent=self.root)
    #     else:
    #         try:
    #             conn = mysql.connector.connect(host="localhost", username="root", password='1234', database="face_recognizer")
    #             my_cursor = conn.cursor()
    #             my_cursor.execute("UPDATE student SET Name=%s, Roll=%s, Department=%s WHERE StudentID=%s", (
    #                 self.var_atten_name.get(),
    #                 self.var_atten_roll.get(),
    #                 self.var_atten_dep.get(),
    #                 self.var_atten_id.get()
    #             ))
    #             conn.commit()
    #             self.fetch_data()
    #             conn.close()
    #             messagebox.showinfo("Success", "Student details successfully updated", parent=self.root)
    #         except Exception as es:
    #             messagebox.showerror("Error", f"Due to : {str(es)}", parent=self.root)





if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()