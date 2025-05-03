import pyodbc
import Config
import customtkinter as ctk

def connect_to_database():
    database_name = Config.db_name()
    try:
        connection = pyodbc.connect(
            'DRIVER={SQL Server};'
            f'SERVER={Config.server_name()};'
            f'DATABASE={database_name};'
            'Trusted_Connection=yes;'
        )
        print(f'Successfully connected to database "{database_name}" on server "{Config.server_name()}"')
        return connection
    except pyodbc.Error as ex:
        print(f'Failed to connect to database: {ex}')
        return None

def create_database(database_name):
    try:
        connection = connect_to_database(Config.db_name())
        if connection is None:
            return False

        connection.autocommit = True
        cursor = connection.cursor()
        cursor.execute(f'CREATE DATABASE {database_name}')
        print(f'Database "{database_name}" created successfully on server "{Config.server_name()}"')
        cursor.close()
        connection.close()
        return True
    except pyodbc.Error as ex:
        print(f'Failed to create database: {ex}')
        return False

def drop_database(database_name):
    try:
        connection = connect_to_database('master')
        if connection is None:
            return False

        connection.autocommit = True
        cursor = connection.cursor()
        cursor.execute(f'DROP DATABASE {database_name}')
        print(f'Database "{database_name}" dropped successfully from server "{Config.server_name()}"')
        cursor.close()
        connection.close()
        return True
    except pyodbc.Error as ex:
        print(f'Failed to drop database: {ex}')
        return False

def insert_user(ID,name, email):
    connection = connect_to_database()
    if connection is None:
        return False
    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Users (ID,Name, Email) VALUES (?,?, ?)", (ID,name, email))
        connection.commit()
        cursor.close()
        connection.close()
        return True
    except pyodbc.Error as e:
        print("Insert failed:", e)
        return False

def launch_insert(ID):
    """
        Inserts a new user into the Users table.
        Parameters:
            ID
    """
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.title("Add User to SQL Server")
    app.geometry("400x600")

    # --- Widgets ---
    label_name = ctk.CTkLabel(app, text="Name")
    label_name.pack(pady=10)

    entry_name = ctk.CTkEntry(app, width=300)
    entry_name.pack()

    label_email = ctk.CTkLabel(app, text="Email")
    label_email.pack(pady=10)

    entry_email = ctk.CTkEntry(app, width=300)
    entry_email.pack()

    status_label = ctk.CTkLabel(app, text="")
    status_label.pack(pady=10)

    def on_submit():
        name = entry_name.get()
        email = entry_email.get()
        if name and email and ID:
            if insert_user(ID,name, email):
                status_label.configure(text="User inserted successfully!", text_color="green")
            else:
                status_label.configure(text="Failed to insert user", text_color="red")
        else:
            status_label.configure(text="Please fill in all fields", text_color="orange")

    submit_btn = ctk.CTkButton(app, text="Insert", command=on_submit)
    submit_btn.pack(pady=20)

    app.mainloop()
def delete_user_by_id(user_id):
    """
    Deletes a user from the Users table based on the ID.

    Parameters:
        user_id (int): The ID of the user to delete.

    Returns:
        bool: True if deletion was successful, False otherwise.
    """
    connection = connect_to_database(Config.db_name())
    if connection is None:
        return False
    try:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM Users WHERE ID = ?", (user_id,))
        connection.commit()
        print(f"User with ID {user_id} deleted successfully.")
        cursor.close()
        connection.close()
        return True
    except pyodbc.Error as e:
        print("Delete failed:", e)
        return False


def get_user_by_id(ID):
    """
    Retrieves a user from the Users table based on the ID.

    Parameters:
        user_id (int): The ID of the user to retrieve.

    Returns:
        tuple: A tuple containing user data (ID, Name, Email) or None if not found.
    """
    connection = connect_to_database(Config.db_name())
    if connection is None:
        return None

    try:
        cursor = connection.cursor()
        # SQL query to get user data by ID
        cursor.execute("SELECT ID, Name, Email FROM Users WHERE ID = ?", (ID,))
        result = cursor.fetchone()  # Fetch one row

        cursor.close()
        connection.close()

        if result:
            # Return a tuple (ID, Name, Email)
            return result
        else:
            print(f"No user found with ID {user_id}")
            return None
    except pyodbc.Error as e:
        print("Error retrieving user:", e)
        return None

if __name__ == "__main__":
    ID = 1
#     Config.check()  # Ensure folder exists
#
#     db_name = Config.db_name()
#     if drop_database(db_name):
#         create_database(db_name)
