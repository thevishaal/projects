# 🎓 Student Management System (Python OOP)

A simple **Command Line Interface (CLI) based Student Management System** built using **Python Object-Oriented Programming (OOP)**.

This project allows users to **add, view, and delete students** using a menu-driven CLI program.

---

# 📌 Features

- ➕ Add a new student
- 📋 View all students
- ❌ Delete a student
- 🖥 CLI-based interactive menu
- 🧠 Built using Python OOP concepts

---

# 🧠 Concepts Used

This project demonstrates the following **Python OOP concepts**:

- Classes and Objects
- Constructors (`__init__`)
- Instance Variables
- Methods
- List of Objects
- Object Interaction
- Control Flow (`while`, `if`, `break`)
- CLI Application Structure

---

# 🏗 Project Structure

```
Day05_Student_Management/
│
├── main.py
└── README.md
```

---

# ⚙️ How It Works

The program consists of two main classes.

## 1️⃣ Student Class

Represents an individual student.

Attributes:
- `name`
- `age`
- `course`

Method:
- `show()` → Displays student details.

Example:

```python
student = Student("Vishal", 21, "BCA")
student.show()
```

---

## 2️⃣ StudentManager Class

Handles all student management operations.

Attributes:
- `students_list` → Stores all student objects.

Methods:
- `add_student(student)`
- `delete_student(name)`
- `show_students()`

---

# 🖥 CLI Menu

The system runs in a loop and shows this menu:

```
1 Add Student
2 Show Students
3 Delete Student
4 Exit
```

Example interaction:

```
1 Add Student
Enter Student Name: Vishal
Enter Student Age: 21
Enter Student Course: BCA

Student added!
```

---

# 🚀 How to Run the Project

### 1️⃣ Clone the repository

```bash
git clone https://github.com/thevishaal/projects.git
```

### 2️⃣ Navigate to the project folder

```bash
cd python
cd Day05_Student-Management
```

### 3️⃣ Run the program

```bash
python main.py
```

---

# 💡 Example Output

```
1 Add Student
2 Show Students
3 Delete Student
4 Exit

Enter Choice: 2

Name: Vishal
Age: 21
Course: BCA
```

---

# 🔮 Future Improvements

Possible enhancements:

- Search student by name
- Update student details
- Store data in a file (JSON / database)
- Add unique student IDs
- Convert CLI program to Web App (Django / Flask)

---