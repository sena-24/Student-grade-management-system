# Student Marks Management System

students = []

def add_student():
    name = input("Enter student name: ")
    marks = list(map(int, input("Enter marks (3 subjects): ").split()))
    
    total = sum(marks)
    average = total / len(marks)
    
    if average >= 90:
        grade = 'A'
    elif average >= 75:
        grade = 'B'
    elif average >= 50:
        grade = 'C'
    else:
        grade = 'F'
    
    student = {
        "name": name,
        "marks": marks,
        "total": total,
        "average": average,
        "grade": grade
    }
    
    students.append(student)
    print("✅ Student added successfully!\n")


def display_students():
    if not students:
        print("No records found.\n")
        return
    
    for s in students:
        print(f"Name: {s['name']}")
        print(f"Marks: {s['marks']}")
        print(f"Total: {s['total']}")
        print(f"Average: {s['average']:.2f}")
        print(f"Grade: {s['grade']}")
        print("------------------------")


def menu():
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            display_students()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

menu()