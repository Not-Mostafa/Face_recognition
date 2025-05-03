import cv2
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import Image_Encoder
import First_avalaible_id as fid
import Config as C
import DB

def capture_new_user(name, department, email):
    C.check()

    button_pressed = False  # Track if capture has been made
    captured_frame = [None]  # Store captured image

    def capture_image():
        nonlocal button_pressed
        if button_pressed:
            return

        ret, frame = cap.read()
        if ret:
            button_pressed = True
            captured_frame[0] = frame
            messagebox.showinfo("Success", "Image captured successfully!")

            ID = fid.find_available_id()
            encoded = Image_Encoder.EncodeImage(frame, ID)
            if encoded:
                print("trying to insert "+ID+" "+name+" "+email+" "+department)
                DB.insert_students(ID, name, email, department)

            # Delay window closing to avoid PhotoImage errors
            window.after(500, window.destroy)
        else:
            messagebox.showerror("Error", "Failed to capture image.")

    def update_frame():
        if not button_pressed:
            ret, frame = cap.read()
            frame = cv2.flip(frame, 1)
            if ret:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(frame_rgb)
                imgtk = ImageTk.PhotoImage(image=img)
                video_label.imgtk = imgtk  # Keep reference
                video_label.config(image=imgtk)

        if window.winfo_exists():
            window.after(10, update_frame)

    # Load face detector
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not access the camera.")
        return

    window = tk.Tk()
    window.title("Live Camera Feed")

    video_label = tk.Label(window)
    video_label.pack()

    capture_button = tk.Button(window, text="Capture Image", command=capture_image)
    capture_button.pack(pady=20)

    update_frame()
    window.mainloop()

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    capture_new_user("TestName", "TestDepartment", "test@example.com")
