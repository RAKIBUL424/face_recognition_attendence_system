from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
from train import Train
import os
from face_re import Face_Recognition
from attendance import Attendance

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x720+0+0")
        self.root.title("Face Recognition System")
        
        # Top banners
        img1 = Image.open(r"c:\Users\User\OneDrive\Desktop\image_of_face\images (1).jpeg")
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        first_label1 = Label(self.root, image=self.photoimg1)
        first_label1.place(x=0, y=0, width=500, height=130)

        img2 = Image.open(r"c:\Users\User\OneDrive\Desktop\image_of_face\Learn-How-to-Implement-Face-Recognition-using-OpenCV-with-Python-80.jpg")
        img2 = img2.resize((500, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        first_label2 = Label(self.root, image=self.photoimg2)
        first_label2.place(x=500, y=0, width=500, height=130)

        img3 = Image.open(r"c:\Users\User\OneDrive\Desktop\image_of_face\istockphoto-1124560262-612x612.jpg")
        img3 = img3.resize((500, 130), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        first_label3 = Label(self.root, image=self.photoimg3)
        first_label3.place(x=1000, y=0, width=500, height=130)

        # Background
        img_bg = Image.open(r"c:\Users\User\OneDrive\Desktop\image_of_face\ai-pictures-1600-x-900-sf6dlq7y9q16055s.jpg")
        img_bg = img_bg.resize((1480, 780), Image.LANCZOS)
        self.photoimg_bg = ImageTk.PhotoImage(img_bg)
        bg_image = Label(self.root, image=self.photoimg_bg)
        bg_image.place(x=0, y=130, width=1480, height=720)

        # Title
        title = Label(bg_image, text="Face Recognition Attendance System Software",
                      font=('times new roman', 35, 'bold'), bg='#070ed5', fg='#bfc9ca')
        title.place(x=0, y=0, width=1480, height=45)

        # Buttons
        img_b1 = Image.open(r"c:\Users\User\OneDrive\Desktop\wallpaper\donut-08.jpg")
        img_b1 = img_b1.resize((220, 220), Image.LANCZOS)
        self.photoimg_b1 = ImageTk.PhotoImage(img_b1)
        b1 = Button(bg_image, image=self.photoimg_b1, command=self.student_details, cursor='hand2')
        b1.place(x=100, y=100, width=120, height=120)
        b1_1 = Button(bg_image, text='Student Details', command=self.student_details, cursor='hand2')
        b1_1.place(x=100, y=120+60, width=120, height=40)

        img_b1_1 = Image.open(r"c:\Users\User\OneDrive\Desktop\wallpaper\anime-scenery-17.jpg")
        img_b1_1 = img_b1_1.resize((220, 220), Image.LANCZOS)
        self.photoimg_b1_1 = ImageTk.PhotoImage(img_b1_1)
        b2 = Button(bg_image, image=self.photoimg_b1_1, cursor='hand2', command=self.face_data)
        b2.place(x=400, y=100, width=120, height=120)
        b2_2 = Button(bg_image, text='Face Detection', cursor='hand2', command=self.face_data)
        b2_2.place(x=400, y=120+60, width=120, height=40)

        img_b1_2 = Image.open(r"c:\Users\User\OneDrive\Desktop\wallpaper\books-08.jpg")
        img_b1_2 = img_b1_2.resize((220, 220), Image.LANCZOS)
        self.photoimg_b1_2 = ImageTk.PhotoImage(img_b1_2)
        b3 = Button(bg_image, image=self.photoimg_b1_2, cursor='hand2', command=self.attendance_data)
        b3.place(x=700, y=100, width=120, height=120)
        b3_3 = Button(bg_image, text='Attendance', cursor='hand2', command=self.attendance_data)
        b3_3.place(x=700, y=120+60, width=120, height=40)

        img_b1_3 = Image.open(r"c:\Users\User\OneDrive\Desktop\wallpaper\books-01.jpg")
        img_b1_3 = img_b1_3.resize((220, 220), Image.LANCZOS)
        self.photoimg_b1_3 = ImageTk.PhotoImage(img_b1_3)
        b4 = Button(bg_image, image=self.photoimg_b1_3, cursor='hand2')
        b4.place(x=1000, y=100, width=120, height=120)
        b4_4 = Button(bg_image, text='Help Desk', cursor='hand2')
        b4_4.place(x=1000, y=120+60, width=120, height=40)


        img_b2_1 = Image.open(r"c:\Users\User\OneDrive\Desktop\wallpaper\donut-08.jpg")
        img_b2_1 = img_b2_1.resize((220, 220), Image.LANCZOS)
        self.photoimg_b2_1 = ImageTk.PhotoImage(img_b2_1)
        b5 = Button(bg_image, image=self.photoimg_b2_1, cursor='hand2',command=self.train_data)
        b5.place(x=100, y=300+50, width=120, height=120)
        b5_5 = Button(bg_image, text='Train Data', cursor='hand2',command=self.train_data)
        b5_5.place(x=100, y=370+60, width=120, height=40)

        img_b2_2 = Image.open(r"c:\Users\User\OneDrive\Desktop\wallpaper\anime-scenery-17.jpg")
        img_b2_2 = img_b2_2.resize((220, 220), Image.LANCZOS)
        self.photoimg_b2_2 = ImageTk.PhotoImage(img_b2_2)
        b6 = Button(bg_image, image=self.photoimg_b2_2, cursor='hand2',command=self.open_img)
        b6.place(x=400, y=300+50, width=120, height=120)
        b6_6 = Button(bg_image, text='Photos', cursor='hand2',command=self.open_img)
        b6_6.place(x=400, y=370+60, width=120, height=40)

        img_b2_3 = Image.open(r"c:\Users\User\OneDrive\Desktop\wallpaper\books-08.jpg")
        img_b2_3 = img_b2_3.resize((220, 220), Image.LANCZOS)
        self.photoimg_b2_3 = ImageTk.PhotoImage(img_b2_3)
        b7 = Button(bg_image, image=self.photoimg_b2_3, cursor='hand2')
        b7.place(x=700, y=300+50, width=120, height=120)
        b7_7 = Button(bg_image, text='Deploper', cursor='hand2')
        b7_7.place(x=700, y=370+60, width=120, height=40)

        img_b2_4 = Image.open(r"c:\Users\User\OneDrive\Desktop\wallpaper\books-01.jpg")
        img_b2_4 = img_b2_4.resize((220, 220), Image.LANCZOS)
        self.photoimg_b2_4 = ImageTk.PhotoImage(img_b2_4)
        b8 = Button(bg_image, image=self.photoimg_b2_4, cursor='hand2')
        b8.place(x=1000, y=300+50, width=120, height=120)
        b8_8 = Button(bg_image, text='Exit', cursor='hand2')
        b8_8.place(x=1000, y=370+60, width=120, height=40)

     #==========buttons function=========
    #student details
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)
    #==========functions buttons=========
    def open_img(self):
        os.startfile("data")
    
    #=================train data=======
    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)
    
    #=================open face recognition=======
    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)
    
    #=================open attendance=======
    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)



if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
