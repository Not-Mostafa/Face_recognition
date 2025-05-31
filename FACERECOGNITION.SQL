CREATE DATABASE face_attendance;
USE face_attendance;

-- Create Departments table
CREATE TABLE Departments (
    department_id INT PRIMARY KEY IDENTITY(1,1),
    dep_name VARCHAR(100) NOT NULL,
    location VARCHAR(100),
    budget DECIMAL(15,2)
);

-- Create Instructors table
CREATE TABLE Instructors (
    instructor_id INT PRIMARY KEY IDENTITY(1,1),
    in_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    hire_date DATE NOT NULL,
    department_id INT,
    salary DECIMAL(12,2),
    password VARCHAR(100) NOT NULL DEFAULT 'default123',
    FOREIGN KEY (department_id) REFERENCES Departments(department_id)
);

-- Create Courses table
CREATE TABLE Courses (
    course_id INT PRIMARY KEY IDENTITY(1,1),
    code VARCHAR(20) UNIQUE NOT NULL,
    course_name VARCHAR(100) NOT NULL,
    credits INT NOT NULL,
    department_id INT NOT NULL,
    FOREIGN KEY (department_id) REFERENCES Departments(department_id)
);

-- Create Students table
CREATE TABLE Students (
    student_id INT PRIMARY KEY,
    st_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    major_department_id INT,
    FOREIGN KEY (major_department_id) REFERENCES Departments(department_id)
);

-- Create Enrollments table (no sections, just direct course enrollments)
CREATE TABLE Enrollments (
    enrollment_id INT PRIMARY KEY IDENTITY(1,1),
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    enrollment_date DATE NOT NULL,
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);

-- Create Attendance table (no sections, directly related to courses)
CREATE TABLE Attendance (
    attendance_id INT PRIMARY KEY IDENTITY(1,1),
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    attendance_date DATE NOT NULL,
    timestamp_in DATETIME,
    status VARCHAR(10) DEFAULT 'Absent',
    CHECK (status IN ('Present', 'Absent')),
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);
-- Add to your existing face_attendance database
USE face_attendance;

-- Create Admin table (separate from your existing tables)
CREATE TABLE Admins (
    admin_id INT PRIMARY KEY IDENTITY(1,1),
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at DATETIME DEFAULT GETDATE(),
    last_login DATETIME
);

-- Create AdminLogs table for tracking admin activities
CREATE TABLE AdminLogs (
    log_id INT PRIMARY KEY IDENTITY(1,1),
    admin_id INT NOT NULL,
    action VARCHAR(255) NOT NULL,
    table_affected VARCHAR(50),
    record_id INT,
    action_time DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (admin_id) REFERENCES Admins(admin_id)
);

-- Insert initial admin account (password: admin123)
INSERT INTO Admins (username, password, full_name, email)
VALUES (
    'admin',
    '$2y$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi',
    'System Administrator',
    'admin@university.edu'
);