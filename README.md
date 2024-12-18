# Student Management System CLI
A Python-based Command Line Interface (CLI) application to manage teachers, students, and subjects. The application leverages SQLAlchemy ORM for database operations and provides functionalities to create, update, delete, and query teachers, students, and subjects.

## Features
- Teacher Management: Add, update, delete, and list teachers.
- Student Management: Add, update, delete, and list students.
- Subject Management: Add, update, delete, and list subjects.
- Querying:
-- View students by their teacher.
-- List all teachers and students.
- Database Initialization: Create the SQLite database with required tables.

## Technologies Used
- Language: Python
- Database: SQLite
- ORM: SQLAlchemy
- Libraries:
sqlalchemy
sys (for exiting the CLI)

## Setup and Installation
### Prerequisites
- Python 3.8 or higher installed on your system.
- Basic understanding of Python and databases.

### Steps to Run the Project
- 1. Clone the Repository
`git clone <repository-url>`
`cd <project-directory>`

- 2. Set Up a Virtual Environment
- `pipenv install`
- `pipenv shell`

- 3. Run the Application
`python3 app.py`

## Usage
- When the application starts, it initializes the database (students.db) if it doesn't already exist.
- You will be presented with a menu of options for managing teachers, students, and subjects.
- Enter the corresponding number to perform an action.

## Menu Options
```
Welcome to Student Management CLI!!
1. Create a teacher
2. Update teacher
3. Delete teacher
4. Create a student
5. Update student
6. Delete student
7. Create a subject
8. Update a subject
9. Delete a subject
10. Assign a student
11. List teachers
12. List students
13. View students by teacher
14. Exit
```
## Future Enhancements
- Add advanced querying features (e.g., filter by specific criteria).
- Improve error handling and validation.
- Add unit tests for core functionalities.

## Contributing
Contributions are welcome! To contribute:

- 1. Fork the repository.
- 2. Create a new branch:
`git checkout -b feature-branch-name`

- 3. Commit your changes:
`git commit -m "Description of changes"`

- 4. Push to your branch:
`git push origin feature-branch-name`

- 5. Submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.