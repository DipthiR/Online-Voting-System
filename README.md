# Online-Voting-System
# 🗳️ Online Voting System (Terminal-Based)

This is a terminal-based **Online Voting System** written in Python. It supports user registration, login, voting, and result viewing with persistent data storage using JSON files.

---

## 🚀 Features

- ✅ User Registration & Authentication
- 🗳️ One-Vote-Per-User Enforcement
- 👨‍💼 Admin Panel to View Results
- 💾 Persistent Data Storage (`users.json`, `candidates.json`)
- 🔐 Secure Password Input using `getpass`
- 🔄 Extensible and Modular Design

---

## 📁 Project Structure

📦 voting-system/
├── users.json # Stores registered users and their vote status
├── candidates.json # Stores candidates and vote counts
├── voting_system.py # Main application file
└── README.md # This file

---

## 🛠️ Requirements

- Python 3.6+
- No external libraries required

---

## ⚙️ How to Run

1. **Clone the repository** or copy the code into a directory:

    ```bash
    git clone <your-repo-url>
    cd voting-system
    ```

2. **Run the Python script:**

    ```bash
    python voting_system.py
    ```

3. **Use the menu:**
    - Register as a new user
    - Login and vote
    - Admin can view results (default admin password: `admin123`)

---

## 🔐 Admin Access

- Admin password is **`admin123`** by default.
- You can change it in the `admin_panel()` function in `voting_system.py`.

---

## ✏️ Sample Users (Optional Setup)

You can prepopulate `users.json` manually like this:

```json
{
  "user1": {"password": "pass1", "voted": false},
  "user2": {"password": "pass2", "voted": false}
}
```
## ✅ Sample Candidates
Candidates are auto-created if candidates.json doesn’t exist:

{
  "Alice": 0,
  "Bob": 0,
  "Charlie": 0
}
## 📌 To-Do & Future Improvements
Web-based version using Flask or Django

OTP or email verification

Role-based admin system

Encrypted passwords

GUI version using Tkinter or PyQt
