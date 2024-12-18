from models import Student, Teacher, Subject
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import random

from faker import Faker
fake = Faker()
if __name__ == '__main__':
    engine = create_engine('sqlite:///students.db')
    Session = sessionmaker(bind=engine)
    session = Session()

students = [
    Student(
        first_name = fake.first_name(),
        last_name = fake.last_name(),
        teacher_id = random.randint(1, 5),
        subject_id = random.randint(1, 5)
    )
    for i in range(6)
]

teachers = [
    Teacher(
        name = fake.name(),
        email = fake.email()
    )
    for i in range(5)
]

subj