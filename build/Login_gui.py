import subprocess
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

def open_gui(script_name):
    global window
    subprocess.Popen(["python", script_name])  # or "python3" on mac/linux
    window.destroy()


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\mosta\Desktop\build\assets\frame0")

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\mosta\Desktop\build\assets\frame4")


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
    x=652.0,
    y=668.0,
    width=115.0,
    height=24.0
)

canvas.create_rectangle(
    493.0,
    154.0,
    948.0,
    747.0,
    fill="#F1F2F7",
    outline="")

canvas.create_text(
    532.0,
    356.0,
    anchor="nw",
    text="Username",
    fill="#082431",
    font=("Poppins Bold", 11 * -1)
)

canvas.create_text(
    532.0,
    474.0,
    anchor="nw",
    text="Password",
    fill="#082431",
    font=("Poppins Bold", 11 * -1)
)

canvas.create_rectangle(
    40.0,
    20.0,
    64.0,
    44.0,
    fill="#5A67BA",
    outline="")

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=620.0,
    y=659.0,
    width=200.0,
    height=42.0
)

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

canvas.create_text(
    624.0,
    206.0,
    anchor="nw",
    text="Welcome!",
    fill="#5969CF",
    font=("Poppins Regular", 36 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    720.0,
    410.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=539.0,
    y=394.0,
    width=362.0,
    height=30.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    720.0,
    522.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=539.0,
    y=506.0,
    width=362.0,
    height=30.0
)

canvas.create_text(
    528.0,
    292.0,
    anchor="nw",
    text="Kindly enter your username and password...",
    fill="#000000",
    font=("Poppins Bold", 11 * -1)
)
window.resizable(False, False)
window.mainloop()
