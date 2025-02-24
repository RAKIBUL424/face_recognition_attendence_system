# from tkinter import *
# from tkinter import ttk
# from PIL import Image, ImageTk
# from tkinter import messagebox
# import mysql.connector
# import cv2
# import os
# import numpy as np


# class Train:
#     def __init__(self, root):
#         self.root = root
#         self.root.geometry("1280x720+0+0")
#         self.root.title("Face Recognition System")
#         self.train_classifier()

#     def train_classifier(self):
#         data_dir = "data"
#         if not os.path.exists(data_dir):
#             messagebox.showerror("Error", f"Data directory '{data_dir}' does not exist")
#             return

#         # Gather image paths
#         path = [os.path.join(data_dir, f) for f in os.listdir(data_dir)]
#         if len(path) == 0:
#             messagebox.showerror("Error", "No images found in data directory")
#             return

#         faces = []
#         ids = []
#         for image in path:
#             img = Image.open(image).convert('L')
#             imageNp = np.array(img, 'uint8')
#             id = int(os.path.split(image)[1].split('.')[1])
#             faces.append(imageNp)
#             ids.append(id)
#             cv2.imshow("Training", imageNp)
#             cv2.waitKey(1)
#         ids = np.array(ids)

#         # Train the classifier and save
#         try:
#             clf = cv2.face.LBPHFaceRecognizer_create()
#             clf.train(faces, ids)
#             save_path = "classifier.xml"
#             clf.write(save_path)
#             if os.path.exists(save_path):
#                 print(f"Classifier saved successfully at {save_path}")
#             else:
#                 print(f"Failed to save the classifier at {save_path}")
#             cv2.destroyAllWindows()
#             messagebox.showinfo("Result", "Training dataset completed!!!")
#         except AttributeError as e:
#             messagebox.showerror("Error", f"Attribute error: {e}")
#         except Exception as e:
#             messagebox.showerror("Error", f"An error occurred: {e}")

# if __name__ == "__main__":
#     root = Tk()
#     obj = Train(root)
#     root.mainloop()
import cv2
import os
import numpy as np
from PIL import Image
from tkinter import messagebox

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x720+0+0")
        self.root.title("Face Recognition System")
        self.train_classifier()

    def train_classifier(self):
        data_dir = "data"
        if not os.path.exists(data_dir):
            messagebox.showerror("Error", f"Data directory '{data_dir}' does not exist")
            return

        # Load OpenCV face detector
        detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

        # Gather image paths
        image_paths = [os.path.join(data_dir, f) for f in os.listdir(data_dir) if f.endswith(".jpg")]
        if len(image_paths) == 0:
            messagebox.showerror("Error", "No images found in data directory")
            return

        faces = []
        ids = []

        for image_path in image_paths:
            img = Image.open(image_path).convert('L')  # Convert to grayscale
            img_numpy = np.array(img, 'uint8')

            try:
                id = int(os.path.split(image_path)[1].split('.')[1])  # Extract ID
            except ValueError:
                print(f"Skipping invalid filename: {image_path}")
                continue

            # Detect faces
            faces_detected = detector.detectMultiScale(img_numpy, scaleFactor=1.1, minNeighbors=5)

            for (x, y, w, h) in faces_detected:
                faces.append(img_numpy[y:y+h, x:x+w])
                ids.append(id)

        if len(faces) == 0:
            messagebox.showerror("Error", "No faces detected in dataset")
            return

        ids = np.array(ids, dtype=np.int32)  # Ensure correct NumPy format

        # Train the classifier
        try:
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.train(faces, ids)
            clf.write("classifier.xml")

            if os.path.exists("classifier.xml"):
                print(" Classifier saved successfully!")
            else:
                print(" Failed to save the classifier.")
                
            messagebox.showinfo("Result", "Training dataset completed successfully!")

        except AttributeError as e:
            messagebox.showerror("Error", f"Attribute error: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    from tkinter import Tk
    root = Tk()
    obj = Train(root)
    root.mainloop()
