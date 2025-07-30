def create_subject():
    from db import execute_query
    name = input("\nName of subject: ")
    
    sql = "INSERT INTO subjects (name) VALUES (%s)"
    values = (name,)
    execute_query(sql, values)
    print("\n---Subject created successfully.---")

def read_subject():
    from db import execute_query
    sql = "SELECT * FROM subjects"
    return execute_query(sql)

def print_subjects():
    subjects = read_subject()
    if not subjects:
        return

    print("\nSubjects:")
    for s in subjects:
        print(f"ID: {s[0]} | Name: {s[1]}")
