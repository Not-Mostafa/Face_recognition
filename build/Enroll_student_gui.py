import subprocess
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

def open_gui(script_name):
    global window
    subprocess.Popen(["python", script_name])  # or "python3" on mac/linux
    window.destroy()


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\mosta\Desktop\build\assets\frame0")


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

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_gui("Enroll_student_gui.py"),
    relief="flat"
)
button_1.place(
    x=78.0,
    y=310.0,
    width=86.0,
    height=12.0
)

canvas.create_text(
    64.0,
    226.0,
    anchor="nw",
    text="Enroll Students",
    fill="#5969CF",
    font=("Poppins Regular", 12 * -1)
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_gui("Add_instructor_gui.py"),
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
    command=lambda: open_gui("Take_attendance_gui.py"),
    relief="flat"
)
button_3.place(
    x=58.0,
    y=184.0,
    width=109.0,
    height=12.0
)

canvas.create_text(
    70.0,
    142.0,
    anchor="nw",
    text="Dashboard",
    fill="#273240",
    font=("Poppins Medium", 12 * -1)
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
    63.500000059604645,
    1440.0,
    64.0,
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

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_gui("Login_gui.py"),
    relief="flat"
)
button_4.place(
    x=1223.0,
    y=900.0,
    width=200.0,
    height=42.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    464.0,
    172.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#F1F2F7",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=290.0,
    y=153.0,
    width=348.0,
    height=36.0
)

canvas.create_text(
    283.0,
    126.0,
    anchor="nw",
    text="ID",
    fill="#000000",
    font=("Poppins Regular", 12 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    464.0,
    250.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#F1F2F7",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=290.0,
    y=231.0,
    width=348.0,
    height=36.0
)

canvas.create_text(
    283.0,
    204.0,
    anchor="nw",
    text="Course",
    fill="#000000",
    font=("Poppins Regular", 12 * -1)
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"), #---------------------------------------------------- the file setting enroll student
    relief="flat"
)
button_5.place(
    x=283.0,
    y=331.0,
    width=362.0,
    height=56.629215240478516
)
window.resizable(False, False)
window.mainloop()
