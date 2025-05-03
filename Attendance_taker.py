import cv2
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import Image_Encoder
import First_avalaible_id as fid
import Config as C

def capture_users():
    C.check()

    # List to store captured frames (use a list instead of tuple)
    captured_frames = []
    button_pressed = False

    # Function to capture and save the image
    def capture_image():
        nonlocal button_pressed
        if button_pressed and len(captured_frames) >= 5:  # Limit number of captures to 5 (you can adjust this)
            messagebox.showinfo("Max Captures", "Maximum number of captures reached!")
            return

        # Capture the frame from the camera
        ret, frame = cap.read()
        if ret:
            captured_frames.append(frame)  # Add the frame to the list
            messagebox.showinfo("Success", "Image captured successfully!")
        else:
            messagebox.showerror("Error", "Failed to capture image.")

    # Function to update the video feed in the GUI window
    def update_frame():
        if not button_pressed:  # Only update if the button hasn't been pressed
            ret, frame = cap.read()
            frame = cv2.flip(frame, 1)
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

    # Function to save the captured images
    def save_images():
        if len(captured_frames) == 0:
            messagebox.showerror("No Captures", "No images captured.")
        else:
            for i, frame in enumerate(captured_frames):
                Image_Encoder.EncodeImage(frame, fid.find_available_id() + i)  # Assign unique ID for each capture
            messagebox.showinfo("Saved", "Captured images saved successfully!")

    # Function to close the window
    def close_window():
        window.quit()

    # Initialize face cascade (you can change this to other classifiers for different objects)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    # Setup camera capture
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

    save_button = tk.Button(window, text="Save Images", command=save_images)
    save_button.pack(pady=10)

    close_button = tk.Button(window, text="Close", command=close_window)
    close_button.pack(pady=10)

    update_frame()  # Start updating frames

    window.mainloop()

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    capture_users()
