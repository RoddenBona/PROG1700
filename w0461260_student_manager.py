students = ["Abby","Brandon","Carly","Damien","Eddie"]
student_id = [1,2,3,4,5]
student_grades = [80,90,79,70,85]

database = list(zip(students,student_id,student_grades))

while True:
    choice = input("""Please select an option:
                1)Create a new record
                2)See all current records
                3)update a current record
                4)Delete a current record
                5)Exit
                Enter option here: """)
    if choice.isdigit():
        choice = int(choice)
        if choice == 1:
            new_name = input("Enter new student name: ")
            new_id = input("Enter new student id: ")
            if new_id.isdigit():
                new_id = int(new_id)
                new_grade = input("Enter new student grade: ")
                if new_grade.isdigit():
                    new_grade = int(new_grade)
                    students.append(new_name)
                    student_id.append(new_id)
                    student_grades.append(new_grade)
                    print("Student has been added to the list")
                else:
                    print("Please enter grade as a number")
            else:
                print("Please enter id as a number")
            
        else:
            if choice == 2:
                for names,ID,grades in database:
                    print(f"Name:{names} ID:{ID} Grade:{grades}")
            else:
                if choice == 3:
                    update_option = input("Enter a student name to update: ")
                    if update_option in students:
                        student_index = students.index(update_option)
                        updated = input("Enter new student grade")
                        if updated.isdigit():
                            updated = int(updated)
                        else:
                            print("Invalid input")
                else:
                    if  choice == 4:
                        deletion_option = input("Enter a student name to remove: ")
                        if deletion_option in students:
                            deletion_index = int(students.index(deletion_option))
                            final_option = input("""Do you really wish to delete this entry?
                                                 1)Yes
                                                 2)No
                                                 Enter option: """)
                            if final_option.isdigit():
                                final_option = int(final_option)
                                if final_option == 1:
                                    students.remove(deletion_index)
                                    student_id.remove(deletion_index)
                                    student_grades.remove(deletion_index)
                                else:
                                    if final_option == 2:
                                        print("Deletion program aborted")
                            else:
                                print("nvalid entry")
                    else:
                        if choice == 5:
                            print("Exiting program. Thank you for your time")
                            break