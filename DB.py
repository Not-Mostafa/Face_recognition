import pyodbc
import Config
from datetime import datetime

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
    connection  = connect_to_database()
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

def Cdb_query(connection,query, params=None):
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
        return result
    except pyodbc.Error as ex:
        print(f'Failed to make the query: {ex}')
        return None

def insert_students(ID, name, email,department_name):
    q0 = "SELECT department_id FROM Departments WHERE dep_name = ?"
    department_result = db_query(q0, (department_name,))
    if not department_result:
        print(f"Department '{department_name}' not found. Cannot insert student: {name}")
        return
    department = db_query(q0, (department_name,))[0][0]
    print(department)
    q = "INSERT INTO students (student_ID, st_name, Email,major_department_id) VALUES (?, ?, ?,?)"
    result = db_query(q, (ID, name, email,department))
    if result is None:
        print(f'Failed to insert student: {name}, {email}')


def insert_instructor(ID, name, hiredate, departments, salary, email, password): #updated to be used for the add to instructor
    g0 = "SELECT department_id FROM Departments WHERE dep_name = ?"
    department_result = db_query(g0, (departments,))
    if not department_result:
        print(f"Department '{departments}' not found")
        return

    department = department_result[0][0]
    g = """SET IDENTITY_INSERT Instructors ON;
           INSERT INTO Instructors 
           (instructor_id, in_name, hire_date, department_id, salary, email, password) 
           VALUES (?, ?, ?, ?, ?, ?, ?);
           SET IDENTITY_INSERT Instructors OFF;"""
    result = db_query(g, (ID, name, hiredate, department, salary, email, password))

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

def auth(Mail,Password):
    q = "SELECT name FROM instructors WHERE email = ? and password = ?"
    result = db_query(q, (Mail,Password))
    return result


def mark_attendance(student_id, course_name):
    c = connect_to_database()
    if not c:
        print("Database connection failed.")
        return

    # Step 1: Get the course_id for the given course_name
    q1 = "SELECT course_id FROM Courses WHERE course_name = ?"
    course_id_result = Cdb_query(c, q1, (course_name,))
    if not course_id_result:
        print("Course not found.")
        return

    course_id = course_id_result[0][0]
    print("Course ID: ", course_id)

    # Step 2: Get all students enrolled in the course
    q2 = "SELECT E.student_id FROM Enrollments E WHERE E.course_id = ?"
    enrolled_students = Cdb_query(c, q2, (course_id,))

    if not enrolled_students:
        print("No students are enrolled in this course.")
        return

    today_date = datetime.now().strftime('%Y-%m-%d')
    for student in enrolled_students:
        q3 = "INSERT INTO Attendance (student_id, course_id, attendance_date, status) VALUES (?, ?, ?, 'Absent')"
        Cdb_query(c, q3, (student[0], course_id, today_date))
    # Step 4: Set the status to 'Present' for the specified student_id
    for student in student_id:
        q4 = "UPDATE Attendance SET status = 'Present' WHERE student_id = ? AND course_id = ? AND attendance_date = ?"
        Cdb_query(c, q4, (student, course_id, today_date))  # Correct parameters here as well

    print("Attendance Taken")



if __name__ == '__main__':
    students = (1,9)
    # mark_attendance(students, "Introduction to Programming")
    insert_students(1,"mos","mail","CS")


