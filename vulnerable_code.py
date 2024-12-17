import os

# 1. Command Injection
def execute_command(user_input):
    os.system(f"echo {user_input}")

user_input = input("Enter a command: ")
execute_command(user_input)

# 2. SQL Injection
import sqlite3

def find_user(username):
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}';"
    cursor.execute(query)  # Vulnerable to SQL injection
    print(cursor.fetchall())
    conn.close()

username = input("Enter username to search: ")
find_user(username)

# 3. Hardcoded Sensitive Information
API_KEY = "12345-SECRET-KEY"  # Avoid hardcoding sensitive data

# 4. Unvalidated File Uploads
def save_uploaded_file(filename, content):
    with open(f"/tmp/{filename}", "w") as file:
        file.write(content)

uploaded_file_name = input("Enter the name of the file to upload: ")
uploaded_file_content = input("Enter file content: ")
save_uploaded_file(uploaded_file_name, uploaded_file_content)
