# Secure_Password_Storage_System

# Overview
This project is a simple Secure Password Storage System built using Python, Flask, SQLite, and bcrypt.
It allows users to:
Register and login securely (passwords hashed with bcrypt).
Store multiple credentials (site, username, password) in a personal vault.
View saved credentials via a web dashboard.

# Tech Stack
Backend: Flask (Python)
Database: SQLite
Security: bcrypt hashing for user passwords
Frontend: HTML templates (Optional)

# Install dependencies:
pip install -r requirements.txt

# Run the application:
python app.py

# Usage
Register a new account.

Login with your credentials.

Add new site credentials (site, username, password).

View all saved credentials in your dashboard.
# Security Notes
User passwords are stored using bcrypt hashing.

Credentials stored in the vault are not encrypted in this basic version (for demo purposes).

For production use, consider encrypting stored credentials with a master key.
# Future Improvements
Encrypt stored credentials with AES.

Add password strength validation.

Implement role-based access control.

Deploy on cloud (Heroku/AWS).
