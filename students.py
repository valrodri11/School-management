def create_student():
    from db import execute_query 
    from classrooms import read_classroom
    from classrooms import print_classroom
    name = input("\nName of student: ")
    email = input("Email of student : ")
    
    classrooms = read_classroom()
    if not classrooms:
        print("No classrooms registered.")
        return

    print_classroom()

    try:
        id_classroom = int(input("\nEnter the classroom ID: "))
    except ValueError:
        print("\nInvalid input. Please enter a number.")
        return

    classroom_ids = [c[0] for c in classrooms]
    if id_classroom not in classroom_ids:
        print("\nThe classroom ID does not exist.")
        return

    sql = "INSERT INTO students (name, email, id_classroom) VALUES (%s, %s, %s)"
    values = (name, email, id_classroom)
    execute_query(sql, values)
    print("\n---Student created successfully.---")

def read_student():
    from db import execute_query
    
    sql = "SELECT * FROM students"
    results = execute_query(sql)
    if not results:
        print("No students registered.")
        return []
    return results

def print_students():
    students = read_student()
    if not students:
        print("No students registered.")
        return

    print("\nStudents:")
    for s in students:
        print(f"ID: {s[0]} | Name: {s[1]} | Email: {s[2]} | Classroom: {s[3]}")


def update_student():
    from db import execute_query
    from classrooms import read_classroom
    from classrooms import print_classroom
    
    students = read_student()
    if not students:
        print("No students registered.")
        return

    print_students()

    try:
        id_student = int(input("\nEnter the student ID you want to update: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    student_ids = [s[0] for s in students]
    if id_student not in student_ids:
        print("The student ID does not exist.")
        return
    
    print("\nWhat do you want to update?")
    print("1. Name")
    print("2. Email")
    print("3. Classroom ID")
    
    option = input("\nEnter your option (1-3): ")
    
    if option == "1":
        name = input("\nNew name of student: ")
        sql = "UPDATE students SET name = %s WHERE id_student = %s"
        values = (name, id_student)
    elif option == "2":
        email = input("\nNew email of student: ")
        sql = "UPDATE students SET email = %s WHERE id_student = %s"
        values = (email, id_student)
    elif option == "3":
       classrooms = read_classroom()
       if not classrooms:
            print("\nNo classrooms registered.")
            return
       print_classroom()
        
       try:
        id_classroom = int(input("\nNew ID of classroom: "))
       except ValueError:
        print("\nInvalid input. Please enter a number.")
        return
       
       classroom_ids = [c[0] for c in classrooms]
       if id_classroom not in classroom_ids:
        print("\nThe classroom ID does not exist.")
        return
       sql = "UPDATE students SET id_classroom = %s WHERE id_student = %s"
       values = (id_classroom, id_student)

    else:
        print("\nInvalid option.")
        return
    execute_query(sql, values)
    print("\n---Student updated successfully.---")

def delete_student():
    from db import execute_query

    students = read_student()
    if not students:
        return
    print_students()
    try:
        id_student = int(input("\nID of student you want to delete: "))
    except ValueError:
        print("\nInvalid input. Please enter a number.")
        return
    ids_existentes = [fila[0] for fila in students]
    if id_student not in ids_existentes:
        print("\nThat ID student does not exists.")
        return
    
    sql = "DELETE FROM students WHERE id_student = %s"
    values = (id_student,)
    execute_query(sql, values)
    print("\n---Student deleted successfully---")

def list_students_by_classroom():
    from db import execute_query
    from classrooms import read_classroom
    from classrooms import print_classroom
    classrooms = read_classroom()
    if not classrooms:
        print("\nNo classrooms registered.")
        return

    print_classroom()

    try:
        id_classroom = int(input("\nEnter the classroom ID: "))
    except ValueError:
        print("\nInvalid input. Please enter a number.")
        return

    classroom_ids = [c[0] for c in classrooms]
    if id_classroom not in classroom_ids:
        print("\nThe classroom ID does not exist.")
        return

    sql = "SELECT id_student, name, email FROM students WHERE id_classroom = %s"
    values = (id_classroom,)
    results = execute_query(sql, values)
    if not results:
        print("\nThere are no students in this classroom.")
    else:
        print("\nStudents in this classroom:")
        for r in results:
            print(f"ID: {r[0]} - Name: {r[1]} - Email: {r[2]}")
