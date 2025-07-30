def create_teacher():
    from db import execute_query
    name = input("\nName of teacher: ")
    email = input("Email of student: ")
    sql = "INSERT INTO teachers (name, email) VALUES (%s,%s)"
    values = (name, email)
    execute_query(sql,values)
    print("\n---Teacher created successfully---")

def read_teacher():
    from db import execute_query
    sql = "SELECT * FROM teachers"
    return execute_query(sql)

def print_teacher():
    teachers = read_teacher()
    if not teachers:
        print("\nNo teachers registered.")
    
    print("\nTeachers:")
    for s in teachers:
        print(f"ID: {s[0]} | Name: {s[1]} | Email: {s[2]}")

 
    
def update_teacher():
    from db import execute_query
    teachers = read_teacher()
    if not teachers:
        print("\nNo teachers registered.")
        return
    print_teacher()
    try:
        teacher_id = int(input("\nID of teacher you want to update: "))
    except ValueError:
        print("\nInvalid input. Please enter a number.")
        return
    teachers_ids = [t[0] for t in teachers]
    if teacher_id not in teachers_ids:
        print("\nThe teacher ID does not exist.")
        return
    
    print("\nWhat do you want to update?")
    print("1. Name")
    print("2. Email")
    option = input("\nEnter your option (1-2): ")
    if option == "1":
        name = input("\nNew name of teacher: ")
        sql = "UPDATE teachers SET name = %s WHERE teacher_id = %s"
        values = (name, teacher_id)
    elif option == "2":
        email = input("\nNew email of teacher: ")
        sql = "UPDATE teachers SET email = %s WHERE teacher_id = %s"
        values = (email, teacher_id)
    else:
        print("\nInvalid option.")
        return
    execute_query(sql,values)
    print("\n---Teacher updated successfully.---")

def delete_teacher():
    from db import execute_query
    teachers = read_teacher()
    print_teacher()
    try: 
        teacher_id = int(input("\nID of teacher you want to delete: "))
    except ValueError:
        print("\nInvalid input. Please enter a number.")
        return
    teachers_ids = [t[0] for t in teachers]
    if teacher_id not in teachers_ids:
        print("\nThe teacher ID does not exist.")
        return
    sql = "DELETE FROM teachers WHERE teacher_id = %s"
    values = (teacher_id,)
    execute_query(sql, values)
    print("\n---Teacher deleted successfully---")

def get_teacher_by_subject():
    from db import execute_query
    from subjects import read_subject
    from subjects import print_subjects
    subjects = read_subject()
    if not subjects:
        print("\nNo subjects registered.")

    print_subjects()
    
    try:
        subject_id = int(input("\nEnter the ID of the subject: "))
    except ValueError:
        print("\nInvalid input. Please enter a number.")
    
    subjects_ids = [s[0] for s in subjects]
    if subject_id not in subjects_ids:
        print("\nThe subject ID does not exist.")
        return

    sql = "SELECT t.name, t.email, s.name FROM assignments a JOIN teachers t ON a.teacher_id = t.teacher_id JOIN subjects s ON a.id_subjects = s.id_subjects WHERE s.id_subjects = %s"
    values = (subject_id,)
    results = execute_query(sql, values)

    if not results:
        print("\nNo teacher is assigned to this subject.")
    else:
        print("\nTeacher assigned to this subject:")
        for row in results:
            teacher_name = row[0]
            teacher_email = row[1]
            subject_name = row[2]
            print(f"\nSubject: {subject_name}")
            print(f"Teacher: {teacher_name}")
            print(f"Email: {teacher_email}")
            
