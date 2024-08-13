# Input data

def get_input():
    faculties = []
    num_faculties = int(input("Enter number of faculties: "))
    for i in range(num_faculties):
        faculty_name = input(f"Enter faculty {i+1} name: ")
        faculty_subject = input(f"Enter faculty {i+1} subject: ")
        faculties.append((faculty_name, faculty_subject))

    num_working_days = int(input("Enter number of working days in a week: "))

    classes = []
    num_classes = int(input("Enter number of classes: "))
    for i in range(num_classes):
        class_name = input(f"Enter class {i+1} name (Branch + Year + Section): ")
        num_students = int(input(f"Enter number of students in class {i+1}: "))
        subjects = []
        num_subjects = int(input(f"Enter number of subjects in class {i+1}: "))
        for j in range(num_subjects):
            subject_name = input(f"Enter subject {j+1} name: ")
            subjects.append(subject_name)
        labs = []
        num_labs = int(input(f"Enter number of labs in class {i+1}: "))
        for j in range(num_labs):
            lab_name = input(f"Enter lab {j+1} name: ")
            labs.append(lab_name)
        batches = []
        num_batches = int(input(f"Enter number of batches for lab subjects in class {i+1}: "))
        for j in range(num_batches):
            batch_num = int(input(f"Enter batch {j+1} number: "))
            batches.append(batch_num)
        classes.append((class_name, num_students, subjects, labs, batches))

    labs = []
    num_labs = int(input("Enter number of labs: "))
    for i in range(num_labs):
        lab_name = input(f"Enter lab {i+1} name: ")
        labs.append(lab_name)

    classrooms = []
    num_classrooms = int(input("Enter number of classrooms: "))
    for i in range(num_classrooms):
        room_num = input(f"Enter classroom {i + 1} room number: ")
        capacity = int(input(f"Enter classroom {i + 1} capacity: "))
        classrooms.append((room_num, capacity))

    return faculties, num_working_days, classes, labs, classrooms