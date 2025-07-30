# School Management System - CRUD project in Python

This is a console-based Python project to manage students, teachers, classrooms, subjects and grades.

## How to run
1. Make sure Python and MySQL are installed 
2. Open a terminal in this folder:
```bash
cd "school management"
```

3. Run the project with: 
```bash
python main.py
```


## Requirements
- Python 3.x
- MySQL running 
- mysql-connector-python (install with: `pip install mysql-connector-python`)

## Database Setup
Use the provided database.sql script to create all tables and insert sample data.

You can run the script using MySQL Workbench:

- Open MySQL Workbench
- Go to File > Open SQL Script
- Select database.sql
- Click the Execute icon (⚡) or press Cmd + Shift + Enter to run it

This will create the database structure and populate it with example data.



## Modules
- `db.py`: Handles the database connection and queries 
- `main.py`: Main menu and program flow
- `students.py`, `classrooms.py`, `teachers.py`, `subjects.py`, `grades.py`, `assignments.py`: Each contains CRUD functions for that entity
 
## Author 
Valentina Rodriguez 
