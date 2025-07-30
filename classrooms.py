def create_classroom():
    from db import execute_query
    name = input("\nName of classroom: ")
    sql = "INSERT INTO classrooms (name) VALUES (%s)"
    values = (name,)
    execute_query(sql, values)
    print("\n---Classroom created successfully---")

def read_classroom():
    from db import execute_query
    sql = "SELECT * FROM classrooms"
    results = execute_query(sql)
    if not results:
        print("\nNo classrooms registered.")
        return []
    return results

def print_classroom():
    classrooms = read_classroom()
    if not classrooms:
        return
    print("\nclassrooms:")
    for c in classrooms:
        print(f"ID: {c[0]} | Name: {c[1]}")   

def update_students_to_classrooms():
    from db import execute_query
    from students import read_student
    from students import print_students
    students = read_student()
    print_students()
    if not students:
        return

    try:
        id_student = int(input("\nEnter the ID of the student to reassign: "))
    except ValueError:
        print("\nInvalid input.")
        return

    if id_student not in [s[0] for s in students]:
        print("\nStudent ID does not exist.")
        return

    classrooms = read_classroom()
    if not classrooms:
        return

    try:
        id_classroom = int(input("\nEnter the new classroom ID: "))
    except ValueError:
        print("\nInvalid input.")
        return

    if id_classroom not in [c[0] for c in classrooms]:
        print("\nClassroom ID does not exist.")
        return

    execute_query(
        "UPDATE students SET id_classroom = %s WHERE id_student = %s",
        (id_classroom, id_student))
    print("\n---Student reassigned successfully.---")


    


   

    
