CREATE DATABASE UniversityDB;
USE UniversityDB;

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
