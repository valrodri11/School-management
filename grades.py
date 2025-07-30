def register_grade():
    from db import execute_query
    from students import read_student
    from students import print_students
    from subjects import read_subject
    from subjects import print_subjects
    print_students()
    students = read_student()
    if not students:
        print("\nNo students registered.")
        return
    try:
        id_student = int(input("\nEnter the student ID: "))
    except ValueError:
        print("\nInvalid input. Please enter a number.")
        return

    student_ids = [s[0] for s in students]
    if id_student not in student_ids:
        print("\nThe student ID does not exist.")
        return    
    
    subjects = read_subject()
    if not subjects:
        print("\nNo classrooms registered.")
        return
    print_subjects()
    
    try:
        id_subjects = int(input("\nID of subject: "))
    except ValueError:
        print("\nInvalid input. Please enter a number.")
        return
    subjects_ids = [s[0] for s in subjects]
    if id_subjects not in subjects_ids:
        print("\nThe subject ID does not exist.")
        return
    
    grade = float(input("\nEnter the grade you want to register: "))
    if grade < 0 or grade > 5:
        print("\nInvalid grade. Must be between 0 and 5.")
        return
    sql = "INSERT INTO grades (id_student, id_subjects, grade) VALUES (%s, %s, %s)"
    values = (id_student, id_subjects, grade)
    execute_query(sql, values)
    print("\n---Grade registered successfully---")

def read_grades():
    from db import execute_query
    from students import read_student
    from students import print_students
    students = read_student()
    if not students:
        print("\nNo students registered.")
        return
    print_students()
    try:
       id_student = int(input("\nEnter the student ID: "))
    except ValueError:
       print("\nInvalid input. Please enter a number.")
       return

    student_ids = [s[0] for s in students]
    if id_student not in student_ids:
       print("\nThe student ID does not exist.")
       return
    
    sql = "SELECT s.name, g.grade FROM grades g JOIN subjects s ON g.id_subjects = s.id_subjects WHERE g.id_student = %s"
    values = (id_student,)
    results = execute_query(sql, values)
    if not results:
        print("\nThis student has no grades yet.")
    else: 
        for fila in results:
            subject_name = fila[0]
            grade = fila[1]    
            print(f"\nSubject name: {subject_name}")
            print(f"Grade: {grade}")
            print("-------------")



