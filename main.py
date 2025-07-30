from students import create_student, print_students, read_student, update_student, delete_student, list_students_by_classroom
from classrooms import create_classroom, read_classroom, update_students_to_classrooms, print_classroom
from assignments import assign_teacher_to_subject
from grades import register_grade, read_grades
from teachers import create_teacher, read_teacher, get_teacher_by_subject, print_teacher, delete_teacher, update_teacher
from subjects import create_subject, read_subject, print_subjects
def main():
    while True:
        print("\nSCHOOL MANAGEMENT SYSTEM")

        print("\nSTUDENTS")
        print(" 1. Create student")
        print(" 2. View students")
        print(" 3. Update student")
        print(" 4. Delete student")
        print(" 5. Assign student to classroom")
        print(" 6. View students by classroom")

        print("\nTEACHERS")
        print(" 7. Create teacher")
        print(" 8. View teachers")
        print(" 9. Update teacher")
        print("10. Delete teacher")
        print("11. Assign teacher to subject")
        print("12. View teacher by subject")

        print("\nCLASSROOMS")
        print("13. Create classroom")
        print("14. View classrooms")

        print("\nSUBJECTS")
        print("15. Create subject")
        print("16. View subjects")

        print("\nGRADES")
        print("17. Register grade")
        print("18. View grades of student")

        print("\n0. Exit")

        option = input("\nEnter your option: ")

        # STUDENTS
        if option == "1":
            create_student()
        elif option == "2":
            print_students()
        elif option == "3":
            update_student()
        elif option == "4":
            delete_student()
        elif option == "5":
            update_students_to_classrooms()
        elif option == "6":
            list_students_by_classroom()

        # TEACHERS
        elif option == "7":
            create_teacher()
        elif option == "8":
            print_teacher()
        elif option == "9":
            update_teacher()
        elif option == "10":
            delete_teacher()
        elif option == "11":
            assign_teacher_to_subject()
        elif option == "12":
            get_teacher_by_subject()

        # CLASSROOMS
        elif option == "13":
            create_classroom()
        elif option == "14":
            print_classroom()

        # SUBJECTS
        elif option == "15":
            create_subject()
        elif option == "16":
            print_subjects()

        # GRADES
        elif option == "17":
            register_grade()
        elif option == "18":
            read_grades()

        elif option == "0":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid option. Please try again.")
if __name__ == "__main__":
    main()
