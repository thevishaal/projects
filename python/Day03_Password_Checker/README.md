# 🔐 Password Strength Validator (Python)

## 📌 Description
A simple and effective **password strength validation script** written in Python.
It validates user passwords against common security rules to ensure strong and safe passwords.

---

## ⚙️ Features
- ✔️ Minimum password length check
- ✔️ At least **one number (0–9)**
- ✔️ At least **one lowercase letter (a–z)**
- ✔️ Password must **start with an uppercase letter**
- ✔️ At least **one special character**
- ✔️ Prevents usage of **username inside password**
- ✔️ Clear and user-friendly error messages

---

## 🛠 Concepts Used
- Uses Python built-in methods like:
    - **isdigit()**
    - **islower()**
    - **isupper()**
- Uses **any()** for fast validation
- Collects all validation errors in a **list**
- Returns all issues at once

---

## ▶️ How to Run
1. Make sure **Python 3.x** is installed on your system
2. Clone the repository or download the source file
3. Open terminal / command prompt and run:

```bash
python main.py
