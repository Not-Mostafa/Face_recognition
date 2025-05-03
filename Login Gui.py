from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import pyodbc
import Config
import DB_Connection as DB
import customtkinter as ctk

def show_login_failed_window():
    error_window = ctk.CTk()
    error_window.title("Login Failed")
    error_window.geometry("300x150")

    label = ctk.CTkLabel(error_window, text="Incorrect email or password.", text_color="red")
    label.pack(pady=20)

    close_button = ctk.CTkButton(error_window, text="Close", command=error_window.destroy)
    close_button.pack(pady=10)

    error_window.mainloop()

def authenticate(email, password):
    """
    Checks if the email and password are correct by querying the Users table.
    Returns the user's name if authentication is successful, otherwise shows an error window.
    """
    connection = DB.connect_to_database()
    if connection is None:
        print("Database connection failed.")
        show_login_failed_window()
        return None

    try:
        cursor = connection.cursor()
        query = "SELECT Name FROM Users WHERE Email = ? AND Password = ?"
        cursor.execute(query, (email, password))
        result = cursor.fetchone()

        cursor.close()
        connection.close()

        if result:
            return result[0]
        else:
            print("Incorrect email or password.")
            show_login_failed_window()
            return None

    except pyodbc.Error as e:
        print("Error retrieving user:", e)
        show_login_failed_window()
        return None


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)



window = Tk()

window.geometry("1920x1080")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

def DB_authentication():
    email = entry_1.get()
    password = entry_2.get()

    user_name = authenticate(email, password)
    if user_name:
        print(f"Welcome, {user_name}!")
        # TODO: Open dashboard window here
    else:
        show_login_failed_window()

canvas.place(x = 0, y = 0)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command= DB_authentication,
    relief="flat"
)

button_1.place(
    x=772.0,
    y=640.0,
    width=400.0,
    height=40.0
)

canvas.create_text(
    824.0,
    424.0,
    anchor="nw",
    text="Enter your Username and Password ",
    fill="#000000",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    921.0,
    388.0,
    anchor="nw",
    text="Sign in ",
    fill="#000000",
    font=("Inter SemiBold", 24 * -1)
)

canvas.create_text(
    836.0,
    154.0,
    anchor="nw",
    text="Attendance Taker",
    fill="#000000",
    font=("Inter SemiBold", 32 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    972.0,
    526.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=781.0,
    y=506.0,
    width=382.0,
    height=38.0
)

canvas.create_text(
    772.0,
    470.0,
    anchor="nw",
    text="Username",
    fill="#828282",
    font=("Inter", 20 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    972.0,
    597.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=781.0,
    y=577.0,
    width=382.0,
    height=38.0
)

canvas.create_text(
    772.0,
    547.0,
    anchor="nw",
    text="Password",
    fill="#828282",
    font=("Inter", 20 * -1)
)
window.resizable(False, False)
window.mainloop()
