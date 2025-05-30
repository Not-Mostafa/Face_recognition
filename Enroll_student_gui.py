import subprocess
import sys
from pathlib import Path

from tkcalendar import DateEntry

import DB
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
from datetime import datetime

from DB import db_query


def open_gui(script_name):
    global window
    subprocess.Popen([sys.executable, script_name])
    window.destroy()


def enroll_student():
    student_id = entry_1.get()
    course_id = entry_2.get()
    enrollment_date = entry_3.get_date().strftime('%Y-%m-%d')  # Get date from DateEntry

    if not student_id or not course_id:
        messagebox.showerror("Error", "Please fill all fields")
        return

    # Call DB function to enroll student
    result = DB.enroll_student_db(student_id, course_id, enrollment_date)


venv_python = sys.executable

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "build" / "assets" / "frame0"


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "build" / "assets" / "frame5"
# At the top of your file






def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)




window = Tk()

window.geometry("1440x960")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 960,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    240.0,
    960.0,
    fill="#F1F2F7",
    outline="")

canvas.create_text(
    78.0,
    310.0,
    anchor="nw",
    text="Enroll Student",
    fill="#5969CF",
    font=("Poppins Regular", 12 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=64.0,
    y=226.0,
    width=96.0,
    height=12.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_gui("Add_student_gui.py"),
    relief="flat"
)
button_2.place(
    x=65.0,
    y=268.0,
    width=99.0,
    height=12.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_gui("Add_student_gui.py"),
    relief="flat"
)
button_3.place(
    x=58.0,
    y=184.0,
    width=109.0,
    height=12.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_gui("dashboard_gui.py"),
    relief="flat"
)
button_4.place(
    x=70.0,
    y=142.0,
    width=72.0,
    height=12.0
)

canvas.create_text(
    40.0,
    104.0,
    anchor="nw",
    text="Pages\n",
    fill="#082431",
    font=("Poppins Regular", 11 * -1)
)

canvas.create_rectangle(
    40.0,
    20.0,
    64.0,
    44.0,
    fill="#5A67BA",
    outline="")


canvas.create_text(
    47.0,
    27.0,
    anchor="nw",
    text="M",
    fill="#FFFFFF",
    font=("Poppins Bold", 11 * -1)
)

canvas.create_text(
    72.0,
    26.0,
    anchor="nw",
    text="Smart Attendance",
    fill="#5A67BA",
    font=("Poppins Bold", 11 * -1)
)

canvas.create_rectangle(
    -0.4999999403953552,
    67.50000005960464,
    1440.0,
    68.0,
    fill="#C7CAD8",
    outline="")

canvas.create_rectangle(
    1307.0,
    15.0,
    1339.0,
    47.0,
    fill="#FFE6CC",
    outline="")

canvas.create_text(
    1318.0,
    25.0,
    anchor="nw",
    text="U",
    fill="#000000",
    font=("Poppins Regular", 12 * -1)
)

canvas.create_text(
    1349.0,
    23.0,
    anchor="nw",
    text="User Name",
    fill="#1F384C",
    font=("Poppins Regular", 12 * -1)
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print('button_5'),
    relief="flat"
)
button_5.place(
    x=1223.0,
    y=900.0,
    width=200.0,
    height=42.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    486.0,
    170.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#F1F2F7",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=312.0,
    y=151.0,
    width=348.0,
    height=36.0
)

canvas.create_text(
    305.0,
    124.0,
    anchor="nw",
    text="Student_id",
    fill="#000000",
    font=("Poppins Regular", 12 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    486.0,
    335.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#F1F2F7",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=312.0,
    y=316.0,
    width=348.0,
    height=36.0
)

canvas.create_text(
    305.0,
    289.0,
    anchor="nw",
    text="Course_id",
    fill="#000000",
    font=("Poppins Regular", 12 * -1)
)

canvas.create_text(
    283.0,
200.0,
anchor="nw",
text="Enrollment Date",
 fill="#000000",
 font=("Poppins Regular", 12 * -1))

entry_3 = DateEntry(
    window,
    date_pattern='yyyy-mm-dd',
    background='white',
    foreground='black',
    borderwidth=0
)
entry_3.place(
x=312.0,
y=230.0,
 width=230.0,
height=36.0)


button_image_6 = PhotoImage(file="./build/assets/frame0/button_5.png")
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:enroll_student(),
    relief="flat"
)
button_6.place(
    x=305.0,
    y=402.0,
    width=362.0,
    height=56.629215240478516
)
window.resizable(False, False)
window.mainloop()
