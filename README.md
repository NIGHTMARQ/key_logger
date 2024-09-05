# Keylogger with Anti-Debugging Techniques

## Project Overview
This is an advanced keylogger designed for educational purposes. It incorporates several anti-debugging techniques to make reverse engineering more difficult. Note: This project should only be used in legal and ethical contexts, such as educational learning or pen-testing with permission.

The keylogger captures and logs keystrokes in a secure manner while implementing defensive mechanisms to prevent tampering, debugging, or analysis. 
Features include:

- **Anti-memory Patch**: Code integrity is monitored, preventing runtime patching of key sections.
- **Thread hiding**: Critical threads used for logging and anti-debugging checks are hidden from standard debuggers.
- **Code obfuscation**: The keylogger employs techniques like self-modifying code and control flow obfuscation to make analysis and decompilation more challenging.
- **Timing check with anti-timing**: Detects delays or changes in program execution that occur when debugging tools are used.

## Key Features
### 1. Keystroke Logging
The keylogger logs all keystrokes, including:

- Alphanumeric keys
- Special characters
- Modifier keys (Ctrl, Alt, Shift)
### 2. Anti-Memory Patch Protection
The program uses periodic integrity checks to ensure that no external memory patching has been performed. If a memory patch is detected, the program terminates or obfuscates its output.

### 3. Thread Hiding
Threads responsible for key logging and anti-debugging checks are hidden from typical process enumeration tools and debuggers, making it harder to track the program’s actions.

### 4. Code Obfuscation
Self-Modifying Code: The program dynamically changes parts of its own code during runtime, making static analysis difficult.
Control Flow Obfuscation: The keylogger’s execution path is intentionally convoluted, employing indirect jumps and complex control structures to confuse debuggers.

### 5. Timing Check with Anti-Timing Techniques
The program measures time between certain points in execution. If debugging slows down execution (e.g., breakpoints, step-throughs), the keylogger detects it and takes appropriate countermeasures like altering behavior or terminating.

## Installation
Clone this repository:

```bash
git clone https://github.com/NIGHTMARQ/key_logger.git
cd key_logger
```
## Requirements
1. Python 3.x (or adapt code to your preferred language)
2. Libraries:
- ctypes for Windows API access
- time for timing checks
- hashlib for integrity checks
Install necessary libraries using pip:

```bash

pip install ctypes
pip install time
pip install hashlib
```
## Usage:
Run the keylogger with:

```bash
python key_logger.py
```
The keystroke logs will be saved to a file named key_log.txt in the working directory which can be manually changed too. You can modify the file path or logging format in the code as needed.

# Ethical Use Only
Ensure this keylogger is only used in controlled environments where you have permission to capture keystrokes (e.g., pen-testing labs, personal systems). Unauthorized use of keyloggers can violate privacy laws and ethical guidelines.

## Code Explanation
### Memory Patch Detection
The program hashes critical sections of the code and periodically verifies that no alterations have been made. This prevents memory patching techniques often used by reverse engineers to bypass protections.

### Thread Hiding
The program uses Windows API functions to hide threads from typical process enumeration, preventing debuggers from identifying and interfering with key logging operations.

### Code Obfuscation
- **Self-Modifying Code**: Key parts of the code mutate during runtime, making it difficult for debuggers to understand or predict the behavior of the keylogger.
- **Control Flow Obfuscation**: Complex control structures and indirect jumps are introduced to mislead debuggers and static analysis tools.
### Timing Anti-Debugging
The program tracks time between executions using high-resolution timers. If the time exceeds a certain threshold (indicating slowdowns from debugging), the program alters its behavior or terminates.

# Legal Disclaimer
This tool is designed for educational purposes and ethical hacking only. The developer is not responsible for any misuse of this tool in illegal or unethical activities. Always obtain proper authorization before using tools that intercept or log private data.

## Contributions
Feel free to submit pull requests or open issues for bug fixes or feature enhancements.
