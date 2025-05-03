import pyodbc
import Config

def connect_to_database():
    database_name = Config.db_name()
    try:
        connection = pyodbc.connect(
            'DRIVER={SQL Server};'
            f'SERVER={Config.server_name()};'
            f'DATABASE={database_name};'
            'Trusted_Connection=yes;'
        )
        print(f'Successfully connected to database \"{database_name}\" on server \"{Config.server_name()}\"')
        return connection
    except pyodbc.Error as ex:
        print(f'Failed to connect to database: {ex}')
        return None



def db_query(query, params=None):
    global connection
    if connection is None:
        connection = connect_to_database()
        if connection is None:
            return None
    try:
        connection.autocommit = True
        cursor = connection.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        if query.strip().upper().startswith("SELECT"):
            result = cursor.fetchall()
        else:
            result = True
        cursor.close()
        connection.close()
        return result
    except pyodbc.Error as ex:
        print(f'Failed to make the query: {ex}')
        return None

def insert_students(ID, name, email,department):
    q = "INSERT INTO students (ID, Name, Email,department) VALUES (?, ?, ?,?)"
    result = db_query(q, (ID, name, email))
    if result is None:
        print(f'Failed to insert student: {name}, {email}')


def insert_instructor(name, hiredate , department,salary, email,password):
    q = "INSERT INTO instructor (Name,hiredate,deparatment,salary,Email,password) VALUES (?, ?, ?,?,?,?)"
    result = db_query(q, (ID, name, email))
    if result is None:
        print(f'Failed to insert instructor: {name}, {email}')

def get_user_by_id(ID):
    q = "SELECT * FROM Users WHERE ID = ?"
    result = db_query(q, (ID,))
    return result

def get_user_by_email(email):
    q = "SELECT * FROM Users WHERE Email = ?"
    result = db_query(q, (email,))
    return result

def get_courses(ID):
    q = "SELECT * FROM Courses WHERE UserID = ?"
    result = db_query(q, (ID,))
    return result

if __name__ == '__main__':
    connect_to_database()
