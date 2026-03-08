# 🏦 Bank Account System (Python OOP Project)

A simple **Command Line Bank Account System** built using **Python and Object-Oriented Programming (OOP)**.  
This project allows users to deposit money, withdraw money, and check their account balance.

---

## 🚀 Features

- Create a bank account with an **initial balance**
- **Deposit money** into the account
- **Withdraw money** with balance validation
- **Check current balance**
- **Input validation** to prevent invalid data
- **Encapsulation using private variables**
- Simple **menu-driven CLI interface**

---

## 🧠 Concepts Used

This project demonstrates the following Python concepts:

- Classes and Objects
- Constructors (`__init__`)
- Encapsulation
- Private Variables (`__balance`)
- Conditional Statements
- Loops (`while`)
- Exception Handling (`try-except`)
- User Input Handling

---

## 📂 Project Structure

```
Day06_Bank-System
│
├── main.py
└── README.md
```

---

## 💻 How to Run

1. Install Python (if not installed)

2. Clone the repository

```bash
git clone https://github.com/thevishaal/projects.git
```

3. Navigate to the project folder

```bash
cd Day06_Bank_System
```

4. Run the program

```bash
python main.py
```

---

## 🖥 Example Output

```
Enter Name: Vishal
Enter your Initial Balance: 1000

1 Deposit
2 Withdraw
3 Check Balance
4 Exit

Enter choice: 1
Enter Amount: 500
Rs. 500 is deposited.
Current Balance: Rs. 1500
```

---

## ⚠️ Validations Implemented

✔ Deposit amount must be **positive**  
✔ Withdraw amount must be **greater than 0**  
✔ Withdraw cannot exceed **available balance**  
✔ Initial balance must be **positive**  
✔ Handles **invalid number input**

---

## 📚 Learning Purpose

This project was created to practice **Python OOP concepts and basic banking logic** using a **menu-driven command line interface**.

---