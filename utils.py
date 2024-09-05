import base64
import os

def encrypt_file(file_path, encryption_key):
    # Encrypt file using base64
    with open(file_path, "rb") as file:
        file_data = file.read()
    encrypted_data = base64.b64encode(file_data)
    return encrypted_data

def create_log_directory(log_directory):
    # Create logs directory if it doesn't exist
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)