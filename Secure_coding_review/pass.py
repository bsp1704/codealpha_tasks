import bcrypt
import json
import os

USERS_FILE = "users.json"

def read_user_data(username):
   
    if not os.path.exists(USERS_FILE):
        print("User database not found.")
        return None

    with open(USERS_FILE, "r") as f:
        users = json.load(f)

    return users.get(username)


def login():
   
    username = input("Enter username: ").strip()

    # Validate that username contains only allowed characters
    if not username.isalnum():
        print("Invalid username format.")
        return

    password = input("Enter password: ").encode('utf-8')

    user = read_user_data(username)
    if not user:
        print("Invalid credentials.")
        return

    stored_hash = user['password'].encode('utf-8')

    if bcrypt.checkpw(password, stored_hash):
        print("Login successful!")
    else:
        print("Invalid credentials.")


def create_user(username, password):
   
    if not username.isalnum():
        print("Invalid username format.")
        return

    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as f:
            users = json.load(f)
    else:
        users = {}

    if username in users:
        print("User already exists.")
        return

    users[username] = {'password': hashed.decode('utf-8')}

    with open(USERS_FILE, "w") as f:
        json.dump(users, f)

    print("User created successfully.")


if __name__ == "__main__":
    print("1. Create User")
    print("2. Login")
    choice = input("Choose an option (1/2): ")

    if choice == "1":
        username = input("Enter new username: ").strip()
        password = input("Enter new password: ").strip()
        create_user(username, password)
    elif choice == "2":
        login()
    else:
        print("Invalid option.")
