import os
import shutil

# Change this to the folder you want to organize
FOLDER_PATH = "files"

FILE_TYPES = {
    "Images": [".png", ".jpg", ".jpeg", ".gif"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Archives": [".zip", ".tar", ".gz"]
}

def get_folder_name(extension):
    for folder, extensions in FILE_TYPES.items():
        if extension in extensions:
            return folder
    return "Others"


def organize_files():
    if not os.path.exists(FOLDER_PATH):
        print("Folder not found!")
        return

    for file in os.listdir(FOLDER_PATH):
        file_path = os.path.join(FOLDER_PATH, file)

        if os.path.isfile(file_path):
            _, ext = os.path.splitext(file)

            folder_name = get_folder_name(ext.lower())
            target_folder = os.path.join(FOLDER_PATH, folder_name)

            os.makedirs(target_folder, exist_ok=True)

            shutil.move(file_path, os.path.join(target_folder, file))

    print("Files organized successfully!")

organize_files()
