from fastapi import FastAPI, HTTPException, Depends, status, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime
import pyodbc
from fastapi.templating import Jinja2Templates

app = FastAPI()

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Database connection
def get_db_connection():
    server = 'Zeyad-legion'
    database = 'face_attendance'
    try:
        conn = pyodbc.connect(
            f'DRIVER={{ODBC Driver 17 for SQL Server}};'
            f'SERVER={server};'
            f'DATABASE={database};'
            'Trusted_Connection=yes;'
        )
        return conn
    except Exception as e:
        print(f"Database connection error: {e}")
        raise HTTPException(status_code=500, detail="Database connection failed")

# Pydantic models
class LoginRequest(BaseModel):
    username: str
    password: str

class StudentUpdate(BaseModel):
    st_name: Optional[str] = None
    email: Optional[str] = None
    major_department_id: Optional[int] = None

class InstructorUpdate(BaseModel):
    in_name: Optional[str] = None
    email: Optional[str] = None
    hire_date: Optional[date] = None
    salary: Optional[float] = None
    department_id: Optional[int] = None

class EnrollmentUpdate(BaseModel):
    course_id: Optional[int] = None





@app.get("/dashboard")
async def get_dashboard():
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        # Fetch students
        cursor.execute("""
            SELECT s.student_id, s.st_name as name, s.email, 
                   d.dep_name as department_name
            FROM Students s
            LEFT JOIN Departments d ON s.major_department_id = d.department_id
        """)
        student_columns = [column[0] for column in cursor.description]
        students = [dict(zip(student_columns, row)) for row in cursor.fetchall()]

        # Fetch instructors
        cursor.execute("""
            SELECT i.instructor_id, i.in_name as name, i.email,
                   i.hire_date, i.salary, d.dep_name as department_name
            FROM Instructors i
            LEFT JOIN Departments d ON i.department_id = d.department_id
        """)
        instructor_columns = [column[0] for column in cursor.description]
        instructors = [dict(zip(instructor_columns, row)) for row in cursor.fetchall()]

        # Fetch enrollments
        cursor.execute("""
            SELECT e.enrollment_id, e.student_id, s.st_name as student_name, 
                   e.course_id, c.course_name, e.enrollment_date
            FROM Enrollments e
            JOIN Students s ON e.student_id = s.student_id
            JOIN Courses c ON e.course_id = c.course_id
        """)
        enrollment_columns = [column[0] for column in cursor.description]
        enrollments = [dict(zip(enrollment_columns, row)) for row in cursor.fetchall()]

        # Fetch attendance
        cursor.execute("""
            SELECT a.attendance_id, a.student_id, s.st_name as student_name,
                   a.course_id, c.course_name, a.attendance_date,
                   a.timestamp_in, a.status
            FROM Attendance a
            JOIN Students s ON a.student_id = s.student_id
            JOIN Courses c ON a.course_id = c.course_id
        """)
        attendance_columns = [column[0] for column in cursor.description]
        attendance = [dict(zip(attendance_columns, row)) for row in cursor.fetchall()]

        # Fetch courses
        cursor.execute("""
            SELECT c.course_id, c.course_name
            FROM Courses c
        """)
        course_columns = [column[0] for column in cursor.description]
        courses = [dict(zip(course_columns, row)) for row in cursor.fetchall()]

        return templates.TemplateResponse(
            "index.html",
            {

                "students": students,
                "instructors": instructors,
                "enrollments": enrollments,
                "attendance": attendance,
                "courses": courses,
                "message": None
            }
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

# Student Endpoints
@app.get("/students")
async def get_students():
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT s.student_id, s.st_name as name, s.email, 
                   d.dep_name as department_name
            FROM Students s
            LEFT JOIN Departments d ON s.major_department_id = d.department_id
        """)
        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return {"data": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

@app.put("/students/{student_id}")
async def update_student(student_id: int, student: StudentUpdate):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT 1 FROM Students WHERE student_id = ?", student_id)
        if not cursor.fetchone():
            raise HTTPException(status_code=404, detail="Student not found")

        updates = []
        params = []
        if student.st_name is not None:
            updates.append("st_name = ?")
            params.append(student.st_name)
        if student.email is not None:
            updates.append("email = ?")
            params.append(student.email)
        if student.major_department_id is not None:
            updates.append("major_department_id = ?")
            params.append(student.major_department_id)

        if not updates:
            raise HTTPException(status_code=400, detail="No fields to update")

        params.append(student_id)
        query = f"UPDATE Students SET {', '.join(updates)} WHERE student_id = ?"
        cursor.execute(query, params)
        conn.commit()
        return {"message": "Student updated successfully"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

@app.delete("/students/{student_id}")
async def delete_student(student_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM Enrollments WHERE student_id = ?", (student_id,))
        cursor.execute("DELETE FROM Attendance WHERE student_id = ?", (student_id,))
        cursor.execute("DELETE FROM Students WHERE student_id = ?", (student_id,))
        conn.commit()
        return {"message": "Student deleted successfully"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

# Instructor Endpoints
@app.get("/instructors")
async def get_instructors():
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT i.instructor_id, i.in_name as name, i.email,
                   i.hire_date, i.salary, d.dep_name as department_name,
                   i.department_id
            FROM Instructors i
            LEFT JOIN Departments d ON i.department_id = d.department_id
        """)
        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return {"data": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

@app.put("/instructors/{instructor_id}")
async def update_instructor(instructor_id: int, instructor: InstructorUpdate):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT 1 FROM Instructors WHERE instructor_id = ?", instructor_id)
        if not cursor.fetchone():
            raise HTTPException(status_code=404, detail="Instructor not found")

        updates = []
        params = []
        if instructor.in_name is not None:
            updates.append("in_name = ?")
            params.append(instructor.in_name)
        if instructor.email is not None:
            updates.append("email = ?")
            params.append(instructor.email)
        if instructor.hire_date is not None:
            updates.append("hire_date = ?")
            params.append(instructor.hire_date)
        if instructor.salary is not None:
            updates.append("salary = ?")
            params.append(instructor.salary)
        if instructor.department_id is not None:
            updates.append("department_id = ?")
            params.append(instructor.department_id)

        if not updates:
            raise HTTPException(status_code=400, detail="No fields to update")

        params.append(instructor_id)
        query = f"UPDATE Instructors SET {', '.join(updates)} WHERE instructor_id = ?"
        cursor.execute(query, params)
        conn.commit()
        return {"message": "Instructor updated successfully"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

@app.delete("/instructors/{instructor_id}")
async def delete_instructor(instructor_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM Instructors WHERE instructor_id = ?", (instructor_id,))
        conn.commit()
        return {"message": "Instructor deleted successfully"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

# Add these Pydantic models at the top with your other models
class DepartmentCreate(BaseModel):
    name: str


class CourseCreate(BaseModel):
    code: str
    name: str
    credits: int
    department_id: int


# Add these endpoints with your other department endpoints
# Update the DepartmentCreate model (add to your existing models)
class DepartmentCreate(BaseModel):
    name: str
    location: Optional[str] = None
    budget: Optional[float] = None

class DepartmentUpdate(BaseModel):
    name: Optional[str] = None
    location: Optional[str] = None
    budget: Optional[float] = None

# Update the GET endpoint to include new fields
@app.get("/departments")
async def get_departments():
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT department_id, dep_name as name, location, budget FROM Departments")
        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return {"data": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

# Update the POST endpoint
@app.post("/departments")
async def create_department(department: DepartmentCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO Departments (dep_name, location, budget) VALUES (?, ?, ?)",
            (department.name, department.location, department.budget)
        )
        conn.commit()
        cursor.execute("SELECT SCOPE_IDENTITY()")
        new_id = cursor.fetchone()[0]
        return {
            "message": "Department created successfully",
            "department_id": new_id
        }
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

# Add PUT endpoint for updates
@app.put("/departments/{department_id}")
async def update_department(department_id: int, department: DepartmentUpdate):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        updates = []
        params = []
        if department.name is not None:
            updates.append("dep_name = ?")
            params.append(department.name)
        if department.location is not None:
            updates.append("location = ?")
            params.append(department.location)
        if department.budget is not None:
            updates.append("budget = ?")
            params.append(department.budget)

        if not updates:
            raise HTTPException(status_code=400, detail="No fields to update")

        params.append(department_id)
        query = f"UPDATE Departments SET {', '.join(updates)} WHERE department_id = ?"
        cursor.execute(query, params)
        conn.commit()
        return {"message": "Department updated successfully"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()


@app.delete("/departments/{department_id}")
async def delete_department(department_id: int):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # First check if department exists
        cursor.execute("SELECT dep_name FROM Departments WHERE department_id = ?", department_id)
        dept = cursor.fetchone()
        if not dept:
            raise HTTPException(status_code=404, detail=f"Department {department_id} not found")

        # Check for dependencies
        cursor.execute("""
            SELECT 
                (SELECT COUNT(*) FROM Courses WHERE department_id = ?) as course_count,
                (SELECT COUNT(*) FROM Instructors WHERE department_id = ?) as instructor_count,
                (SELECT COUNT(*) FROM Students WHERE major_department_id = ?) as student_count
        """, (department_id, department_id, department_id))

        counts = cursor.fetchone()
        if counts.course_count > 0 or counts.instructor_count > 0 or counts.student_count > 0:
            error_msg = f"Cannot delete department {dept.dep_name} - it has: "
            messages = []
            if counts.course_count > 0:
                messages.append(f"{counts.course_count} courses")
            if counts.instructor_count > 0:
                messages.append(f"{counts.instructor_count} instructors")
            if counts.student_count > 0:
                messages.append(f"{counts.student_count} students")

            raise HTTPException(
                status_code=409,
                detail=error_msg + ", ".join(messages)
            )

        # Perform deletion
        cursor.execute("DELETE FROM Departments WHERE department_id = ?", department_id)
        conn.commit()
        return {"message": f"Department {dept.dep_name} deleted successfully"}

    except pyodbc.Error as e:
        print(f"Database error: {str(e)}")
        if conn:
            conn.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"Database operation failed: {str(e)}"
        )
    except HTTPException:
        raise
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
    finally:
        if conn:
            conn.close()

@app.get("/courses")
async def get_courses():
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT c.course_id, c.code, c.course_name as name, c.credits,
                   c.department_id, d.dep_name as department_name
            FROM Courses c
            LEFT JOIN Departments d ON c.department_id = d.department_id
        """)
        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return {"data": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

@app.post("/courses")
async def create_course(course: CourseCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO Courses (code, course_name, credits, department_id) VALUES (?, ?, ?, ?)",
            (course.code, course.name, course.credits, course.department_id)
        )
        conn.commit()
        cursor.execute("SELECT SCOPE_IDENTITY()")
        new_id = cursor.fetchone()[0]
        return {
            "message": "Course created successfully",
            "course_id": new_id
        }
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

@app.put("/courses/{course_id}")
async def update_course(course_id: int, course: CourseCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """UPDATE Courses SET 
                code = ?, 
                course_name = ?, 
                credits = ?, 
                department_id = ?
            WHERE course_id = ?""",
            (course.code, course.name, course.credits, course.department_id, course_id)
        )
        conn.commit()
        return {"message": "Course updated successfully"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

@app.delete("/courses/{course_id}")
async def delete_course(course_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        # First delete related records
        cursor.execute("DELETE FROM Enrollments WHERE course_id = ?", (course_id,))
        cursor.execute("DELETE FROM Attendance WHERE course_id = ?", (course_id,))
        # Then delete the course
        cursor.execute("DELETE FROM Courses WHERE course_id = ?", (course_id,))
        conn.commit()
        return {"message": "Course deleted successfully"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()
# Enrollment Endpoints
@app.get("/enrollments")
async def get_enrollments():
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT e.enrollment_id, e.student_id, s.st_name as student_name, 
                   e.course_id, c.course_name, e.enrollment_date
            FROM Enrollments e
            JOIN Students s ON e.student_id = s.student_id
            JOIN Courses c ON e.course_id = c.course_id
        """)
        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return {"data": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

@app.put("/enrollments/{enrollment_id}")
async def update_enrollment(enrollment_id: int, enrollment: EnrollmentUpdate):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT 1 FROM Enrollments WHERE enrollment_id = ?", enrollment_id)
        if not cursor.fetchone():
            raise HTTPException(status_code=404, detail="Enrollment not found")

        updates = []
        params = []
        if enrollment.course_id is not None:
            updates.append("course_id = ?")
            params.append(enrollment.course_id)

        if not updates:
            raise HTTPException(status_code=400, detail="No fields to update")

        params.append(enrollment_id)
        query = f"UPDATE Enrollments SET {', '.join(updates)} WHERE enrollment_id = ?"
        cursor.execute(query, params)
        conn.commit()
        return {"message": "Enrollment updated successfully"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

# Attendance Endpoints
@app.get("/attendance")
async def get_attendance():
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT a.attendance_id, a.student_id, s.st_name as student_name,
                   a.course_id, c.course_name, a.attendance_date,
                   a.timestamp_in, a.status
            FROM Attendance a
            JOIN Students s ON a.student_id = s.student_id
            JOIN Courses c ON a.course_id = c.course_id
        """)
        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return {"data": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)