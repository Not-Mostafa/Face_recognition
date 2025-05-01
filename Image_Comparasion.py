import face_recognition
import numpy as np
import os
import Config as C

tolerance = 0.55 # tolerance Recommended values 0.55

def Test():
    print("Test Pass")


def load_all_encodings(folder):
    C.check()
    encodings = {}
    for filename in os.listdir(folder):
        if filename.endswith(".npy"):
            user_id = filename.replace(".npy", "")  # Extract ID from filename
            encoding = np.load(os.path.join(folder, filename))
            encodings[user_id] = encoding
    return encodings

def compare_jpg_with_all(image):
    C.check()
    global tolerance
    encodings_dict = load_all_encodings("Encodes")
    new_encodings = face_recognition.face_encodings(image)

    if not new_encodings:
        print("No face found in the new image.")
        return None

    unknown_encoding = new_encodings[0]

    for user_id, known_encoding in encodings_dict.items():
        result = face_recognition.compare_faces([known_encoding], unknown_encoding, tolerance=tolerance)[0]
        distance = face_recognition.face_distance([known_encoding], unknown_encoding)[0]
        print(f"Comparing with ID {user_id} => Match: {result}, Distance: {distance:.4f}")
        if result:
            print(f"✅ Match found with ID: ",user_id) # need to fix old user id not new one
            return user_id

    print("❌ No match found.")
    return None

