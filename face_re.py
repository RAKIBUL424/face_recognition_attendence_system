

from time import strftime
from datetime import datetime    
import cv2
import mysql.connector
from tkinter import *
from PIL import Image, ImageTk

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x720+0+0")
        self.root.title("Face Recognition System")

        title = Label(self.root, text="Face Recognition ", font=('times new roman', 35, 'bold'), bg='#070ed5', fg='#bfc9ca')
        title.place(x=0, y=0, width=1480, height=45)

        img_top = Image.open(r"c:\Users\User\Downloads\2464735.jpg")
        img_top = img_top.resize((650, 700), Image.LANCZOS)
        self.photoimg_tp = ImageTk.PhotoImage(img_top)
        f_lbl = Label(self.root, image=self.photoimg_tp)
        f_lbl.place(x=0, y=55, width=650, height=700)

        img_top_r = Image.open(r"c:\Users\User\Downloads\852.jpg")
        img_top_r = img_top_r.resize((650, 700), Image.LANCZOS)
        self.photoimg_tpp = ImageTk.PhotoImage(img_top_r)
        f_lbl_l = Label(self.root, image=self.photoimg_tpp)
        f_lbl_l.place(x=650, y=55, width=950, height=700)

        b1_1 = Button(f_lbl_l, text='Face Recognition', cursor='hand2', command=self.face_recognition, 
                      font=('times new roman', 18, 'bold'), bg='blue', fg='white')
        b1_1.place(x=50, y=510, width=200, height=40)
    #==================mark attendance======================
    def mark_attendance(self, i, r, d, n):
        with open("attendance.csv", "+r", newline="\n") as file:
            myDataList = file.readlines()
            nameList = []
            for line in myDataList:
                entry = line.split((","))
                nameList.append(entry[0])
            if ((i not in nameList) and (r not in nameList) and (d not in nameList) and (n not in nameList)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                file.writelines(f"\n{i},{r},{d},{n},{dtString},{d1},Present")

    def draw_boundary(self, img, classifier, scaleFactor, minNeighbors, color, text, clf):
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
        coord = []

        for (x, y, w, h) in features:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
            id, predict = clf.predict(gray_image[y:y+h, x:x+w])
            confidence = int((100 * (1 - predict / 300)))

            conn = mysql.connector.connect(host="localhost", username="root", password='1234', database="face_recognizer")
            my_cursor = conn.cursor()

            my_cursor.execute("SELECT Name FROM student WHERE StudentID=%s", (id,))
            i = my_cursor.fetchone()
            i = "+".join(i) if i else "Unknown"

            my_cursor.execute("SELECT Roll FROM student WHERE StudentID=%s", (id,))
            r = my_cursor.fetchone()
            r = "+".join(r) if r else "Unknown"

            my_cursor.execute("SELECT Department FROM student WHERE StudentID=%s", (id,))
            d = my_cursor.fetchone()
            d = "+".join(d) if d else "Unknown"

            my_cursor.execute("SELECT StudentID FROM student WHERE StudentID=%s", (id,))
            n = my_cursor.fetchone()
            n = "+".join(n) if d else "Unknown"

            if confidence > 77:
                cv2.putText(img, f"ID: {n}", (x, y-95), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1, cv2.LINE_AA)
                cv2.putText(img, f"Name: {i}", (x, y-75), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1, cv2.LINE_AA)
                cv2.putText(img, f"Roll: {r}", (x, y-55), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1, cv2.LINE_AA)
                cv2.putText(img, f"Department: {d}", (x, y-30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1, cv2.LINE_AA)
                self.mark_attendance(i, r, d, n)
            else:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                cv2.putText(img, "Unknown Face", (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 1, cv2.LINE_AA)

            coord = [x, y, w, h]

        return coord

    def recognize(self, img, clf, faceCascade):
        self.draw_boundary(img, faceCascade, 1.2, 5, (255, 25, 255), "Face", clf)
        return img

    def face_recognition(self):
        faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = self.recognize(img, clf, faceCascade)  # Now recognize is a method of the class
            cv2.imshow("Welcome to Face Recognition", img)

            if cv2.waitKey(1) == 13:  # Press Enter to exit
                break

        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()



