#creating data structure --> lists 
#intialize empty list
students = []
print("===== Student Management System =====")
print("1. Add Student")
print("2. View Students")
print("3. Search Student")
print("4. Update Student")
print("5. Delete Student")
print("6. Save & Exit")

while True:
    choice = input("Enter your choice: ")
    if choice not in ['1','2','3','4','5','6']:
        print("Invalid choice. Please try again.")
        break
    elif choice == '1':
        # Add Student
        row=[]
        id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        age = input("Enter Student Age: ")
        course = input("Enter Student Course: ")
        marks = input("Enter Student Marks: ")

        row.append(id)
        row.append(name)
        row.append(age)
        row.append(course)
        row.append(marks)

        students.append(row)

        print("Student added successfully!")

    elif choice == '2':
        # View Students
        print("ID\tName\tAge\tCourse\tMarks")

        for student in students:
            print(f"{student[0]}\t{student[1]}\t{student[2]}\t{student[3]}\t{student[4]}")
            #student[0] --> ID
            #student[1] --> Name
            #student[2] --> Age
            #student[3] --> Course
            #student[4] --> Marks

    elif choice == '3':
        #Searching based on name
        search_name= input("Enter the name of the student to search:")
        searched_user=[] 
        is_found= False
        for student in students:
            if student[1]==search_name:
                searched_user.append(student)
                is_found= True
        if not is_found:
            print("Student not found.")
        else:
            print("ID\tName\tAge\tCourse\tMarks")
            for student in searched_user:
                print(f"{student[0]}\t{student[1]}\t{student[2]}\t{student[3]}\t{student[4]}")

    elif choice == '4':
        # Update Student
        update_det = input("Enter the column for which you want to update the details:") #input of column name.
        #NAME --> name, name = name , Name --> name
        update_id = input("Enter Student ID  to update the details: ")
        is_found= False
        for student in students:
            if student[0] == update_id:
                is_found= True
                if update_det.lower() == 'name':
                    new_name = input("Enter new name: ")
                    student[1] = new_name
                elif update_det.lower() == 'age':
                    new_age = input("Enter new age: ")
                    student[2] = new_age
                elif update_det.lower() == 'course':
                    new_course = input("Enter new course: ")
                    student[3] = new_course
                elif update_det.lower() == 'marks':
                    new_marks = input("Enter new marks: ")
                    student[4] = new_marks
                else:
                    print("Invalid detail type.")
                    break
                print("Student details updated successfully!")
                break
        if not is_found:
            print("Inavlid Student ID.")    
        
    elif choice == '5':
        # Delete Student
        delete_id = input("Enter Student ID to delete: ")
        is_found= False
        for student in students:
            if student[0]==delete_id:
                students.remove(student)   
                is_found =True 
                print("Student deleted successfully!")
                break 
        if not is_found:
            print("Invalid Student ID.")

    elif choice == '6':
        # Save & Exit
        print("Saving data and exiting...")
        break

