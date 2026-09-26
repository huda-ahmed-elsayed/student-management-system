```markdown
# 🎓 Student Management System

A Python CLI application for managing student records using JSON file storage, built with clean separation of concerns and robust error handling.

---

## 📁 Project Structure

```
student-management-system/
│
├── main.py          # CLI interface & menu logic
├── students.py      # Core functions & business logic
├── students.json    # Data storage
├── logs.txt         # Activity log with timestamps
└── .gitignore
```

## ⚙️ Features

- ➕ Add new students
- 👁️ View all students
- 🔍 Search for a student by ID
- ✏️ Update student information
- 🗑️ Delete a student
- 📋 Activity logging with timestamps
- ⚠️ Full error handling for invalid input & missing files

---

## 🚀 How to Run

**Requirements:** Python 3.x

```bash
git clone https://github.com/huda-ahmed-elsayed/student-management-system.git
cd student-management-system
python main.py
```

---

## 🗂️ Data Format

Student records are stored in `students.json`:

```json
{
    "students": [
        {
            "id": 1,
            "name": "Huda Ahmed",
            "age": 24,
            "track": "AI Engineering"
        }
    ]
}
```

---

## 📋 Activity Log Sample

```
[26-09-2026 22:14:01] Added student 1
[26-09-2026 22:15:30] Searched for student 1, result successfully
[26-09-2026 22:16:45] Updated student 1
[26-09-2026 22:17:10] Deleted student 1
```

---

## 🛠️ Technologies

- Python 3
- JSON — data persistence
- datetime — timestamp logging
- os — cross-platform terminal handling

---

## 👩‍💻 Author

**Huda Ahmed**  
[GitHub](https://github.com/huda-ahmed-elsayed) · [LinkedIn](https://linkedin.com/in/huda-ahmed-elsayed)
```
