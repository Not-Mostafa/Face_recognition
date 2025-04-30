# Face Recognition
An integrated system built with Python and MySQL that uses face recognition to mark attendance. This project combines computer vision, database management, and real-time image processing, and is ideal for academic or small-scale organizational use.
# 🧠 Face Recognition Project — Installation Guide (Windows)

This guide helps you set up a stable environment for face recognition using Python, OpenCV, and the `face_recognition` library on **Windows**.

---

## 📦 Required Libraries

- `opencv-python` — For webcam video capture and displaying frames.
- `face_recognition` — For face detection and recognition.
- `dlib` — Dependency used by `face_recognition`.
- `numpy`, `cmake` — Additional required dependencies.

---

## ⚙️ Installation Steps (Recommended)

> 🐍 Use **Python 3.9** — Most stable version for `dlib`. Install from the [Microsoft Store](https://apps.microsoft.com/detail/python-39/9P7QFQMJRFP7).

### 1. Set Up Python 3.9
Make sure it's added to your PATH during installation.

### 2. Open your terminal (Command Prompt, PowerShell, or VS Code) and run the following:

```bash
# Upgrade pip
python -m pip install --upgrade pip

# Install CMake (required for dlib)
pip install cmake

# Install dlib (used by face_recognition)
pip install dlib

# Install face_recognition
pip install face_recognition

# Install OpenCV
pip install opencv-python

# Install compatible version of NumPy
pip install numpy==1.26.4
