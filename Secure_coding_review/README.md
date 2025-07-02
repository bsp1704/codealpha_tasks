# Secure Login System

This is a simple, secure user login system implemented in Python. It demonstrates secure coding practices such as password hashing, input validation, and safe file handling.



## 📄 Features

- Create new user accounts with hashed passwords using `bcrypt`
- Login functionality with secure password verification
- Input validation to prevent malicious input
- User data stored in a JSON file (for demo purposes — use a database in production)



## ⚙️ Requirements

- Python 3.x
- `bcrypt` library



## 🚀 Installation

1. **Clone this repository**
   ```bash
   git clone <your-repo-url>
   cd <your-repo-directory>

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **run the script**
   ```bash
   python pass.py
   ```
 Choose an option

 1: Create a new user

 2: Login with existing credentials

## 🔐 Security Practices Demonstrated
✅ Passwords hashed using bcrypt with salt
✅ No plaintext passwords stored anywhere
✅ Input validation to prevent injection and path traversal
✅ Proper error handling with generic messages
✅ Secure file operations





