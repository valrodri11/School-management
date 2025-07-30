def assign_teacher_to_subject():
    from db import execute_query
    from teachers import read_teacher
    from teachers import print_teacher
    from subjects import read_subject
    from subjects import print_subjects
    
    teachers = read_teacher()
    if not teachers:
        print("\nNo teachers registered.")
        return 
    
    print_teacher()
    
    try:
        teacher_id = int(input("\nID of teacher: "))
    except ValueError:
        print("\nInvalid input. Please enter a number.")
        return
    teachers_ids = [t[0] for t in teachers]
    if teacher_id not in teachers_ids:
        print("\nThe teacher ID does not exist.")
        return
    print_subjects()
    subjects = read_subject()
    if not subjects:
        print("\nNo classrooms registered.")
        return
    print_subjects
    
    try:
        id_subjects = int(input("\nID of the subject you want to assign to the teacher: "))
    except ValueError:
        print("\nInvalid input. Please enter a number.")
        return
    subjects_ids = [s[0] for s in subjects]
    if id_subjects not in subjects_ids:
        print("\nThe subject ID does not exist.")
        return
    
    sql = "INSERT into assignments (teacher_id, id_subjects) VALUES (%s, %s)"
    values = (teacher_id, id_subjects)
    execute_query(sql, values)
    print("\n---Teacher assigned to subject successfully.---")