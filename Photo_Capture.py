import cv2
import tkinter as tk
import Image_Encoder
from tkinter import messagebox
from PIL import Image, ImageTk
import First_avalaible_id as fid
import Config as C




def capture_new_user():
    C.check()

    # Function to capture and save the image
    def capture_image():
        global button_pressed
        button_pressed = True  # Set the flag to True
        ret, frame = cap.read()
        if ret:
            messagebox.showinfo("Success", "Image captured successfully!")
            window.destroy()
            Image_Encoder.EncodeImage(frame, fid.find_available_id())
        else:
            messagebox.showerror("Error", "Failed to capture image.")

    # Function to update the video feed in the GUI window
    def update_frame():
        if not button_pressed:  # Only update if the button hasn't been pressed
            ret, frame = cap.read()
            frame = cv2.flip(frame,1)
            if ret:
                # Convert to grayscale for face detection
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                # Detect faces
                faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

                # Draw green box around faces
                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Green box with thickness 2

                # Convert frame to RGB for displaying in tkinter window
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(frame_rgb)
                imgtk = ImageTk.PhotoImage(image=img)
                video_label.imgtk = imgtk
                video_label.config(image=imgtk)

        window.after(10, update_frame)  # Schedule next frame update
    button_pressed = False

    # Initialize face cascade (you can change this to other classifiers for different objects)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    # Setup camera capture
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not access the camera.")
    else:
        window = tk.Tk()
        window.title("Live Camera Feed")

        video_label = tk.Label(window)
        video_label.pack()

        capture_button = tk.Button(window, text="Capture Image", command=capture_image)
        capture_button.pack(pady=20)

        update_frame()  # Start updating frames

        window.mainloop()

        cap.release()
        cv2.destroyAllWindows()

        # Function to capture and save the image
        def capture_image():
            ret, frame = cap.read()
            if ret:
                messagebox.showinfo("Success", "Image captured successfully!")
                window.destroy()
                Image_Encoder.EncodeImage(frame, fid.find_available_id())
            else:
                messagebox.showerror("Error", "Failed to capture image.")

        # Function to update the video feed in the GUI window
        def update_frame():
            if not button_pressed:  # Only update if the button hasn't been pressed
                ret, frame = cap.read()
                if ret:
                    # Convert to grayscale for face detection
                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                    # Detect faces
                    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

                    # Draw green box around faces
                    for (x, y, w, h) in faces:
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Green box with thickness 2

                    # Convert frame to RGB for displaying in tkinter window
                    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    img = Image.fromarray(frame_rgb)
                    imgtk = ImageTk.PhotoImage(image=img)
                    video_label.imgtk = imgtk
                    video_label.config(image=imgtk)

                window.after(10, update_frame)  # Schedule next frame update

if __name__ == '__main__':
    capture_new_user()
