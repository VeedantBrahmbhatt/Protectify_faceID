import cv2
import tkinter as tk
from tkinter import Button, Label, messagebox
from PIL import Image, ImageTk
import os
import tensorflow as tf
import cv2 as cv
import numpy as np

class CameraCaptureApp:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)

        self.video_source = 0  # Use the default camera (change if necessary)
        self.vid = cv2.VideoCapture(self.video_source)

        self.canvas = tk.Canvas(window, width=self.vid.get(3), height=self.vid.get(4))
        self.canvas.pack()

        self.btn_capture = Button(window, text="Capture", width=10, command=self.capture)
        self.btn_capture.pack(padx=10, pady=10)

        self.capture_count = 0
        self.capture_limit = 1
        self.output_folder = os.path.dirname(os.path.abspath(__file__))
        self.image_path = os.path.join(self.output_folder, "captured_image.jpg")  # Image path

        self.update()
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.window.mainloop()

    def capture(self):
        if self.capture_count < self.capture_limit:
            ret, frame = self.vid.read()
            if ret:
                self.capture_count += 1
                # Delete the old image if it exists
                if os.path.exists(self.image_path):
                    os.remove(self.image_path)
                cv2.imwrite(self.image_path, frame)
                self.show_capture_message()
            else:
                self.show_error_message("Capture Error", "Failed to capture image.")
        else:
            self.show_info_message("Capture Complete", "Image captured. The application will now exit.")
            self.window.quit()

    def update(self):
        ret, frame = self.vid.read()
        if ret:
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
        self.window.after(10, self.update)

    def on_closing(self):
        if self.vid.isOpened():
            self.vid.release()
        self.window.destroy()

    def show_capture_message(self):
        self.show_info_message("Capture Successful", f"Image saved as captured_image.jpg")

    def show_info_message(self, title, message):
        messagebox.showinfo(title, message)

    def show_error_message(self, title, message):
        messagebox.showerror(title, message)

# Create a window and pass it to the CameraCaptureApp class
root = tk.Tk()
app = CameraCaptureApp(root, "Camera Capture App")
def preprocess(path):
    img = cv.imread(path)
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    img = cv.resize(img, (128, 128))
    img = tf.expand_dims(img, axis=0)  # Add a batch dimension
    return img


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def predict_similarity(img1, img2):
    similarity_score = loaded_model.predict([img1, img2])
    similarity_score = sigmoid(similarity_score)
    threshold = 0.998  # Set a threshold for similarity (adjust as needed)

    # Use np.all() to check if all elements in similarity_score are less than threshold
    if np.all(similarity_score < threshold):
        return 'Images are dissimilar', similarity_score
    else:
        return 'Images are similar', similarity_score

def checker(result):
    if result=='Images are similar':
        return 1
    else:
        return 0
if __name__ == '__main__':
    # Load the Siamese model
    loaded_model = tf.keras.models.load_model("FaceIDFinal.keras", compile=False, safe_mode=False)
    # print("Model loaded successfully.")

    # Preprocess the two images you want to compare
    img1 = preprocess('21BCP118 photo.jpg')
    img2 = preprocess('captured_image.jpg')
    # x=loaded_model.predict([img1, img2])
    # print(x)
    # result, score = predict_similarity(img1, img2)
    # print(result)
    # print(f'Similarity Score: {score}')
    result, score = predict_similarity(img1, img2)
    # print(result)
    x=checker(result)
    if x == 1:
        print(1, flush=True)

    else:
        print(0, flush=True)

    # print(f'Similarity Score: {score}')
