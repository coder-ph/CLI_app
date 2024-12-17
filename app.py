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
    
def create_student():
    name = str(input("Enter the student's name"))
    
    
