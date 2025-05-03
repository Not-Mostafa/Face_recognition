-- Create the database
CREATE DATABASE UniversityDB;
USE UniversityDB;

-- Departments table (primary entity)
CREATE TABLE Departments (
    department_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    location VARCHAR(100),
    budget DECIMAL(15,2)
);

-- Instructors table (connected to Departments)
CREATE TABLE Instructors (
    instructor_id INT PRIMARY KEY AUTO_INCREMENT,
    in_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    hire_date DATE NOT NULL,
    department_id INT,
    salary DECIMAL(12,2),
    FOREIGN KEY (department_id) REFERENCES Departments(department_id)
);

-- Courses table (connected to Departments)
CREATE TABLE Courses (
    course_id INT PRIMARY KEY AUTO_INCREMENT,
    code VARCHAR(20) UNIQUE NOT NULL,
    course_name VARCHAR(100) NOT NULL,
    credits INT NOT NULL,
    department_id INT NOT NULL,
    FOREIGN KEY (department_id) REFERENCES Departments(department_id)
);

-- Students table (connected to Departments for major)
CREATE TABLE Students (
    student_id INT PRIMARY KEY,
    st_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    major_department_id INT,
    FOREIGN KEY (major_department_id) REFERENCES Departments(department_id)
);

-- CourseSections table (connected to Courses and Instructors)
CREATE TABLE CourseSections (
    section_id INT PRIMARY KEY AUTO_INCREMENT,
    course_id INT NOT NULL,
    number VARCHAR(10) NOT NULL,
    semester VARCHAR(20) NOT NULL,
    year INT NOT NULL,
    instructor_id INT,
    FOREIGN KEY (course_id) REFERENCES Courses(course_id),
    FOREIGN KEY (instructor_id) REFERENCES Instructors(instructor_id)
);

-- Enrollments table (connecting Students to CourseSections)
CREATE TABLE Enrollments (
    enrollment_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT NOT NULL,
    section_id INT NOT NULL,
    enrollment_date DATE NOT NULL,
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (section_id) REFERENCES CourseSections(section_id)
);
-- Attendance table (linked to Students and CourseSections)
CREATE TABLE Attendance (
    attendance_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT NOT NULL,
    section_id INT NOT NULL,
    attendance_date DATE NOT NULL,
    timestamp_in DATETIME,
    status ENUM('Present', 'Absent', 'Late') DEFAULT 'Present',
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (section_id) REFERENCES CourseSections(section_id)
);
