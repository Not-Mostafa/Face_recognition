import cv2
import tkinter as tk
from PIL import Image, ImageTk
import Image_Encoder
import First_avalaible_id as fid
import Config as C
import DB
from pathlib import Path
from tkinter import Canvas, Entry, Button, PhotoImage, messagebox
import sys
import subprocess

def capture_user(course):
    C.check()
    button_pressed = False
    captured_frame = [None]

    def capture_image():
        nonlocal button_pressed
        if button_pressed:
            return
        ret, frame = cap.read()
        if ret:
            button_pressed = True
            captured_frame[0] = frame
            messagebox.showinfo("Success", "Image captured successfully!")
            Image_Encoder.EncodeImage_attendance(frame, course)
            window2.destroy()
        else:
            messagebox.showerror("Error", "Failed to capture image.")

    def update_frame():
        if not button_pressed:
            ret, frame = cap.read()
            if ret:
                frame = cv2.flip(frame, 1)
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, 1.1, 5)
                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(rgb_frame)
                imgtk = ImageTk.PhotoImage(image=img)
                video_label.imgtk = imgtk
                video_label.config(image=imgtk)

        if window2.winfo_exists():
            window2.after(10, update_frame)

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        messagebox.showerror("Error", "Could not access the camera.")
        return

    window2 = tk.Toplevel()
    window2.title("Live Camera Feed")

    video_label = tk.Label(window2)
    video_label.pack()

    capture_btn = tk.Button(window2, text="Capture Image", command=capture_image)
    capture_btn.pack(pady=20)

    def on_closing():
        cap.release()
        cv2.destroyAllWindows()
        window2.destroy()

    window2.protocol("WM_DELETE_WINDOW", on_closing)
    update_frame()
    window2.mainloop()

def open_gui(script_name):
    global window
    subprocess.Popen([sys.executable, script_name])
    window.destroy()

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "build" / "assets" / "frame3"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = tk.Tk()
window.geometry("1440x960")
window.configure(bg="#FFFFFF")

canvas = Canvas(window, bg="#FFFFFF", height=960, width=1440, bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)

# Course Entry
entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
canvas.create_image(457.0, 200.0, image=entry_image_1)
entry_1 = Entry(bd=0, bg="#F1F2F7", fg="#000716", highlightthickness=0)
entry_1.place(x=283.0, y=181.0, width=348.0, height=36.0)

# Sidebar and Branding
canvas.create_rectangle(0.0, 0.0, 240.0, 960.0, fill="#F1F2F7", outline="")

def add_button(x, y, image_file, command):
    img = PhotoImage(file=relative_to_assets(image_file))
    btn = Button(image=img, borderwidth=0, highlightthickness=0, command=command, relief="flat")
    btn.image = img
    btn.place(x=x, y=y)
    return btn

add_button(78.0, 310.0, "button_1.png", lambda: open_gui("Add_student_gui.py"))
add_button(64.0, 226.0, "button_2.png", lambda: open_gui("Enroll_student_gui.py"))
add_button(65.0, 268.0, "button_3.png", lambda: open_gui("Add_instructor_gui.py"))
add_button(70.0, 142.0, "button_4.png", lambda: open_gui("Dashboard_gui.py"))
add_button(1223.0, 900.0, "button_5.png", lambda: open_gui("Login_gui.py"))  # Logout

canvas.create_text(58.0, 184.0, anchor="nw", text="Take Attendance", fill="#5969CF", font=("Poppins Regular", 12 * -1))
canvas.create_text(40.0, 104.0, anchor="nw", text="Pages\n", fill="#082431", font=("Poppins Regular", 11 * -1))
canvas.create_rectangle(40.0, 20.0, 64.0, 44.0, fill="#5A67BA", outline="")
canvas.create_text(47.0, 27.0, anchor="nw", text="M", fill="#FFFFFF", font=("Poppins Bold", 11 * -1))
canvas.create_text(72.0, 26.0, anchor="nw", text="Smart Attendance", fill="#5A67BA", font=("Poppins Bold", 11 * -1))
canvas.create_rectangle(-0.5, 63.5, 1440.0, 64.0, fill="#C7CAD8", outline="")
canvas.create_rectangle(1307.0, 15.0, 1339.0, 47.0, fill="#FFE6CC", outline="")
canvas.create_text(1318.0, 25.0, anchor="nw", text="U", fill="#000000", font=("Poppins Regular", 12 * -1))
canvas.create_text(1349.0, 23.0, anchor="nw", text="User Name", fill="#1F384C", font=("Poppins Regular", 12 * -1))
canvas.create_text(276.0, 154.0, anchor="nw", text="Select course...", fill="#000000", font=("Poppins Regular", 12 * -1))

# Date Entry (optional)
entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
canvas.create_image(457.0, 278.0, image=entry_image_2)
entry_2 = Entry(bd=0, bg="#F1F2F7", fg="#000716", highlightthickness=0)
entry_2.place(x=283.0, y=259.0, width=348.0, height=36.0)
canvas.create_text(276.0, 232.0, anchor="nw", text="Select date...", fill="#000000", font=("Poppins Regular", 12 * -1))

# Take Attendance
def start_attendance():
    course = entry_1.get().strip()
    if not course:
        messagebox.showerror("Error", "Please enter a course name.")
        return
    capture_user(course)

add_button(276.0, 337.0, "button_6.png", start_attendance)

window.resizable(False, False)
window.mainloop()
