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
    name = str(input('Enter the name of the teacher'))  
    email = input('Enter a valid email ')
    teacher = Teacher(name= name, email=email)
    session.add(teacher)
    session.commit()
    
def update_teacher():
    id = int(input("Enter the teacher's ID to be updated"))
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
    id = int(input("Enter the teacher ID to be deleted"))
    teacher = session.get(Teacher, id)
    if not teacher:
        print(f'Teacher with ID {id} does not exist. Enter the correct ID')
        return
    session.delete(teacher)
    session.commit()
        
        
    
def create_student():
    name = str(input("Enter the student's name"))
    
    
