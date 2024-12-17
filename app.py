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
    
    if not teacher and subject:
        print(f"Either the teacher id ({teacher_id} or subject id {subject_id} does not exist)")
        return
    student =Student(first_name=first_name, last_name= last_name, teacher_id= teacher_id, subject_id = subject_id)
    session.add(student)
    session.commit()
    print(f'The student with the name {first_name} {last_name} has been created with id {student.id}')
    
def update_student():
    student_id = int(input('Enter the student ID to be updated'))
    student = session.get(Student, student_id)
    if not student:
        print(f'THe student with the ID {student_id} doess not exist. Enter correct id')
        return
    
    student.first_name = str(input("Enter student's first name")) or student.first_name
    student.last_name = str(input("Enter student's last name")) or student.last_name
    updated_teacher_id = int(input('Enter the teacher ID')) or student.teacher_id
    teacher = session.get(Teacher, updated_teacher_id)
    
    if not teacher:
        print(f'Teacher with ID {updated_teacher_id} does not exist')
        
    else:
        student.teacher_id = updated_teacher_id
    updated_subject = int(input("Enter the updated subject ID")) or student.subject_id
    subject = session.get(Subject, updated_subject)
    if not subject:
        print("Enter the correct subject ID")
        return
    student.subject = updated_subject
    session.commit()
        
        