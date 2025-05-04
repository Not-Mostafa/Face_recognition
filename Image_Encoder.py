import face_recognition
import Image_Comparasion
import numpy as np
import os
import Config as C
import DB as db



def EncodeImage(image,id):
    C.check()
    match = Image_Comparasion.compare_jpg_with_all(image)
    if  match is not None:
        print("User Already Encoded")
        return False

    encoded_img = face_recognition.face_encodings(image)
    if encoded_img:  # Check if at least one face was found
        encoding = encoded_img[0]
        filename = f"Encodes/{id}.npy"
        np.save(filename, encoding)# Save as .npy
        print("Face encoding saved successfully.")
        return True
    else:
        print("No face found in the image.")
    return False

def EncodeImages(images):
    """
    Encodes a list of face images and compares them against a known set of encodings to identify users.

    Parameters:
        images (list): A list of images (numpy arrays) to process.

    Returns:
        list: A list of user IDs for matched faces, or None for unmatched or unrecognized faces.

    Notes:
        - Only one face per image is assumed; if no face is found, None is added to the result.
        - Uses face_recognition to encode faces and a helper function to compare against saved encodings.
        - Requires 'Encodes' directory to contain pre-stored encodings accessible by load_all_encodings.
        - Prints status messages for debugging (found/not found).
    """
    C.check()
    ans = []
    encodings_dict = Image_Comparasion.load_all_encodings("Encodes")

    for image in images:
        encoded_imgs = face_recognition.face_encodings(image)

        if not encoded_imgs:
            print("No face found in the image.")
            ans.append(None)
            continue

        encoded_img = encoded_imgs[0]  # Assuming one face per image
        match = Image_Comparasion.compare_all_with_all(encoded_img, encodings_dict)

        if match is None:
            print("User Not Found")
            ans.append(None)
        else:
            print("User Found, ID:", match)
            ans.append(match)

    return ans