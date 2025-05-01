import face_recognition
import Image_Comparasion
import numpy as np
import os
import Config as C
import DB_Connection as db



def EncodeImage(image,id):
    C.check()
    match = Image_Comparasion.compare_jpg_with_all(image)
    if  match is not None:
        print("User Already Encoded, User ID is " ,id)
        return None

    encoded_img = face_recognition.face_encodings(image)
    if encoded_img:  # Check if at least one face was found
        encoding = encoded_img[0]
        filename = f"Encodes/{id}.npy"
        np.save(filename, encoding)# Save as .npy
        print("Face encoding saved successfully.")
        db.launch_insert(id)
    else:
        print("No face found in the image.")
    return None
