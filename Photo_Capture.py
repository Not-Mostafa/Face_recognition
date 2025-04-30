import cv2
import tkinter as tk
import Image_Encoder
from tkinter import messagebox
from PIL import Image, ImageTk

# Flag to know if the capture button was pressed
button_pressed = False

# Function to capture and save the image
def capture_image():
    global button_pressed
    button_pressed = True  # Set the flag to True
    ret, frame = cap.read()
    if ret:
        cv2.imwrite("captured_image.jpg", frame)
        messagebox.showinfo("Success", "Image captured and saved successfully!")
        window.destroy()
        Image_Encoder.EncodeImage()
    else:
        messagebox.showerror("Error", "Failed to capture image.")

# Function to update the video feed in the GUI window
def update_frame():
    if not button_pressed:  # Only update if the button hasn't been pressed
        ret, frame = cap.read()
        if ret:
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame_rgb)
            imgtk = ImageTk.PhotoImage(image=img)
            video_label.imgtk = imgtk
            video_label.config(image=imgtk)
    window.after(10, update_frame)  # Schedule next frame update

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
