# 🚀 Face Recognition Attendance System

An integrated face recognition system built with Python and MySQL that automatically marks attendance by recognizing faces in real-time. Perfect for academic institutions, offices, and events.

## ✨ Key Features

- **Real-time face detection** using OpenCV
- **Face encoding & recognition** with `face_recognition` library
- **Database integration** for user management
- **Simple GUI** for user registration
- **Attendance tracking** with timestamps
- **Configurable recognition threshold**

## 🛠 System Requirements

- Windows 10/11 (64-bit recommended)
- Python 3.9 (for dlib compatibility)
- Webcam (or USB camera)
- MySQL Server 8.0+

## 📦 Installation Guide

### 1. Prerequisites


# Install Python 3.9 from Microsoft Store
https://apps.microsoft.com/detail/python-39/9P7QFQMJRFP7

### 2. Set Up Virtual Environment (Recommended)
```bash

python -m venv venv
venv\Scripts\activate
```
### 3. Install Dependencies
Run these commands in the Terminal
```bash

pip install --upgrade pip
pip install cmake wheel
pip install dlib==19.24.0
pip install face-recognition==1.3.0
pip install opencv-python==4.8.0.76
pip install numpy==1.26.4
pip install pyodbc==5.0.1
pip install pillow==10.0.1
```
### 4. Database Setup

    Install MySQL Server

    Create a new database (or use existing one)

    Update database credentials in DB_Connection.py

# 🖥 Usage
  Need to improve by making one single GUI for full options
  Run Photo_Capture.py and capture users
  Image_Encoder.py Encodes and Saves automaticly files in Encodes dirictory while Image_Comparasion.py makes sure no duplicates
  
# ⚙️ Configuration

  Still need to make this file later
  Edit config.py to customize:
  python

# Database Configuration
DB_SERVER = "localhost"
DB_NAME = "face_attendance"
DB_USER = "root"
DB_PASSWORD = ""
