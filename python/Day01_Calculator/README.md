## 📌 Description

This project is a **Python-based CLI Calculator** that allows users to perform basic and advanced mathematical operations through the terminal.  
The calculator runs continuously until the user chooses to exit and handles invalid inputs and errors gracefully.

It is built to practice **Python fundamentals**, user input handling, and exception handling in a real-world style mini project.

---

## ⚙️ Features

- ➕ Addition
- ➖ Subtraction
- ✖️ Multiplication
- ➗ Division (with division-by-zero handling)
- 📐 Modulus operation (`%`)
- 🔢 Power operation (`**`)
- 🔁 Continuous execution using a loop
- ❌ Exit option (`q`)
- ⚠️ Proper error handling for invalid input and operators

---

## 🛠 Concepts Used

- Python Functions
- Conditional Statements (`if-elif-else`)
- While Loop
- Exception Handling (`try-except`)
- User Input Validation
- String Methods (`strip()`, `lower()`)
- CLI (Command Line Interface) Programming

---

## ▶️ How to Run

1. Make sure **Python 3** is installed on your system.
2. Save the code in a file, for example:  
    *(copy main.py)*
    ```python
    def calculator(operator, num1, num2):
    if operator == "+":
        return num1 + num2
    ......
    ......
        print("Error: Invalid input or operator!")
    ```
3. python main.py