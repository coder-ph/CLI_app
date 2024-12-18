from models import Student, Teacher, Subject, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys

engine = create_engine('sqlite:///students.db')
Session = sessionmaker(bind=engine)
session = Session()

def initialize_db():
    Base.metadata.create_all(engine)
    print('Initializing Database ...!')

def create_teacher():
    name = str(input('Enter the name of the teacher: '))  
    email = input('Enter a valid email ')
    teacher = Teacher(name= name, email=email)
    session.add(teacher)
    session.commit()
    
def update_teacher():
    id = int(input("Enter the teacher's ID to be updated: "))
    teacher = session.get(Teacher, id)
    
    if not teacher:
        print(f'No record for the teacher with id {id}')
        return
    else:
        teacher.name = str(input("Enter new teacher's name (current name is {teacher.name})")) or teacher.name
        teacher.email = input("Enter new teacher's email adress. (current email is {teacher.mail})") or teacher.email
        session.commit()
        print(f'Teacher with id {teacher.id} has been updated successfully')
        
def delete_teacher():
    id = int(input("Enter the teacher ID to be deleted: "))
    teacher = session.get(Teacher, id)
    if not teacher:
        print(f'Teacher with ID {id} does not exist. Enter the correct ID: ')
        return
    session.delete(teacher)
    session.commit()
    print(f"Teacher with ID {id} has been deleted successfully: ")
        
def create_student():
    first_name = str(input("Enter the student's first name: "))
    last_name = str(input("Enter the student's lasst name: "))
    teacher_id = int(input("Enter the teacher ID: "))
    subject_id = int(input("Enter the student's subject id: "))
    teacher = session.get(Teacher, teacher_id)
    subject = session.get(Subject, subject_id)
    
    if not teacher or subject:
        print(f"Either the teacher id ({teacher_id} or subject id {subject_id} does not exist: )")
        return
    student =Student(first_name=first_name, last_name= last_name, teacher_id= teacher_id, subject_id = subject_id)
    session.add(student)
    session.commit()
    print(f'The student with the name {first_name} {last_name} has been created with id {student.id}')
    
def update_student():
    student_id = int(input('Enter the student ID to be updated: '))
    student = session.get(Student, student_id)
    if not student:
        print(f'THe student with the ID {student_id} doess not exist. Enter correct id')
        return
    
    student.first_name = str(input("Enter student's first name: ")) or student.first_name
    student.last_name = str(input("Enter student's last name: ")) or student.last_name
    updated_teacher_id = int(input('Enter the teacher ID: ')) or student.teacher_id
    teacher = session.get(Teacher, updated_teacher_id)
    
    if not teacher:
        print(f'Teacher with ID {updated_teacher_id} does not exist')
        return
    else:
        student.teacher_id = updated_teacher_id
    updated_subject = int(input("Enter the updated subject ID: ")) or student.subject_id
    subject = session.get(Subject, updated_subject)
    if not subject:
        print("Enter the correct subject ID")
        return
    student.subject_id = updated_subject
    session.commit()
    
def delete_student():
    id = int(input("Enter the student ID to be deleted: "))  
    student = session.get(Student, id)
    if not student:
        print(f'The student ID {id} does not exist, enter the correct ID')
        return
    session.delete(student)
    session.commit()  
    
def create_subject():
    subject_name =str(input("Enter the subject name: "))
    teacher_id = int(input("Enter the teacher ID for the subject: "))
    teacher = session.get(Teacher, teacher_id)
    if not teacher:
        print(f'The teacher with ID {teacher} is invalid')
        return
    subject = Subject(subject_name=subject_name, teacher_id=teacher_id)
    session.add(subject)
    session.commit()
    
def update_subject():
    id = int(input("Enter the subject ID to be updated: "))
    subject = session.get(Subject, id)
    if not subject:
        print(f'The subject ID {id} is invalid!')
        return
    subject.subject_name = str(input(f"Enter a valid subject name (current subject name- {subject.students})")) or subject.subject_name
    teacher_id = int(input(f"Enter a valid teacher id. Current id is {subject.teacher_id}: "))
    teacher = session.get(Teacher, teacher_id)
    if not teacher:
        print("The teacher ID entered is invalid teacher ID: ")
        return
    else:
        subject.teacher_id = teacher_id
    session.commit()
    print("The subject has been updated successfully!")
    
def delete_subject():
    id = int(input("Enter a valid subject ID"))
    subject = session.get(Subject, id)
    if not subject:
        print("The subject ID entered is invalid")
        return
    session.delete(subject)
    session.commit()

def assign_student():
    pass

def list_students():
    students = session.query(Student).all()
    if len(students)< 1:
        print("No students enrolled yet!")
    else:
        for student in students:
            print(student)

def list_teachers():
    teachers = session.query(Teacher).all()
    if len(teachers)< 1:
        print("No teachers yet!")
    else:
        for teacher in teachers:
            print(teacher)

def students_by_teacher():
    teacher_id = int(input("Enter the teacher ID: "))
    teacher = session.get(Teacher, teacher_id)
    if not teacher:
        print("Invalid teacher ID entered")
        return
    students = teacher.students
    if len(students) < 1:
        print(f"Teacher with ID {teacher_id} has no students yet")
        return
    print(f'The students to teacher id {teacher_id} are ...')
    for student in students:
        print(student)
        
def main_menu():
    while True:
        print('\n Welcome to Student Management CLI!!')
        print('1. create a teacher')
        print('2. update teacher')
        print('3. delete teacher')
        print('4. create student')
        print('5. update student')
        print('6. detele student')
        print('7. create subject')
        print('8. update subject')
        print('9. detele subject')
        print('10. Assign a tm')
        print('11. list teachers')
        print('12. list students')
        print('13. view student by teacher')
        print('14. exit')
        
        try:
            choice = int(input('Enter your choice'))
            if choice ==1:
                create_teacher()
            elif choice == 2:
                update_teacher()
            elif choice ==3:
                delete_teacher()
            elif choice == 4:
                create_student()
            elif choice == 5:
                update_student()
            elif choice == 6:
                delete_student()
            elif choice ==7:
                create_subject()
            elif choice == 8:
                update_subject()
            elif choice == 9:
                delete_subject()
            elif choice == 10:
                assign_student()
            elif choice == 11:
                list_teachers()
            elif choice == 12:
                list_students()
            elif choice == 13:
                students_by_teacher()
            elif choice == 14:
                sys.exit()
                
        except ValueError:
            print('Invalid choice, please try again')
            
if __name__ == '__main__':
    initialize_db()
    main_menu()
    