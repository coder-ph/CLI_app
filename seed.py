from models import Student, Teacher, Subject
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import random

from faker import Faker
fake = Faker()
if __name__ == '__main__':
    engine = create_engine('sqlite:///students.db', echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()

students = [
    Student(
        first_name = fake.first_name(),
        last_name = fake.last_name(),
        teacher_id = random.randint(1, 5),
        subject_id = random.randint(1, 5)
    )
    for i in range(5)
]

teachers = [
    Teacher(
        name = fake.name(),
        email = fake.email()
    )
    for i in range(5)
]

technology_courses = [
    "Full-Stack Web Development",
    "Data Science and Machine Learning",
    "Cybersecurity",
    "Cloud Computing",
    "Artificial Intelligence and Robotics"
]

subjects =[
    Subject(
        subject_name= random.choice(technology_courses),
        teacher_id = random.randint(1,5)
    )
    for i in range(5)
]

def add_students():
    for student in students:
        session.add(student)    
    session.commit()
    
add_students()

def add_teachers():
    for teacher in teachers:
        session.add(teacher)
    session.commit()
add_teachers()

def add_subjects():
    for subject in subjects:
        session.add(subject)
    session.commit()

add_subjects()
    