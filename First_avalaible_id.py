import os

def find_available_id():
    encodes_dir = "Encodes"
    existing_files = os.listdir(encodes_dir)

    existing_ids = []
    for file in existing_files:
        if file.endswith('.npy'):
            file_id = file.split('.npy')[0]
            existing_ids.append(int(file_id))
    current_id = 1
    while current_id in existing_ids:
        current_id += 1
    return current_id

