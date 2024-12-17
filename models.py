from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()

class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer(), primary_key=True, nullable=False)
    name = Column(String(), nullable=False)
    email = Column(String(), unique=True, nullable=True)
    
    subjects =relationship('Subject', back_populates='teacher')
    students = relationship('Student', back_populates='teacher')
    
    def __repr__(self):
        return f'Teacher[name: {self.name}, email: {self.email}]'
    
class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer(), primary_key=True)
    first_name = Column(String(), nullable=False)
    last_name = Column(String(), nullable=False)
    
    teacher_id = Column(Integer(), ForeignKey('teachers.id'))
    subject_id = Column(Integer(), ForeignKey('subjects.id'))
    
    teacher = relationship('Teacher', back_populates='students')
    subject = relationship('Subject', back_populates='students')
    
    def __repr__(self):
        return f'first_name: {self.first_name}, second_name: {self.last_name}'
    
class Subject(Base):
    __tablename__ = 'subjects'
    
    id = Column(Integer(), primary_key=True)
    subject_name = Column(String(), nullable=False)
    teacher_id = Column(Integer(), ForeignKey('teachers.id'))
    
    teacher = relationship('Teacher', back_populates='subjects')
    students = relationship('Student', back_populates= 'subject')
    
    def __repr__(self):
        return f'Subject[subject_name: {self.subject_name}]'