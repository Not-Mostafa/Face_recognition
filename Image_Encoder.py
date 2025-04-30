import face_recognition
import Image_Comparasion
import numpy as np
import os

def Test():
    image = face_recognition.load_image_file("v.jpg")
    EncodeImage(image,1)
    print("Test Pass")

def EncodeImage(image,id):
    match = Image_Comparasion.compare_jpg_with_all(image)
    if  match is not None:
        print("User Already Encoded, User ID is " ,id)
        return None

    encoded_img = face_recognition.face_encodings(image)
    if encoded_img:  # Check if at least one face was found
        encoding = encoded_img[0]
        os.makedirs("Encodes", exist_ok=True)
        filename = f"Encodes/{id}.npy"
        np.save(filename, encoding)# Save as .npy
        print("Face encoding saved successfully.")
    else:
        print("No face found in the image.")
    return None
