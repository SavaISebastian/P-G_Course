# # # SQL Server example query

# import pyodbc # type: ignore

# # Connect to SQL Server using Windows Authentication (SSMS)
# conn = pyodbc.connect(
#     'DRIVER={ODBC Driver 17 for SQL Server};'
#     'SERVER=DESKTOP-3SK5E6S;'       # ex: localhost\SQLEXPRESS
#     'DATABASE=school;'                
#     'Trusted_Connection=yes;'        # Windows Authentication
# )

# cursor = conn.cursor()

# # Drop any FK constraints referencing courses, then drop tables in dependency order
# cursor.execute("""
#     DECLARE @sql NVARCHAR(MAX) = ''
#     SELECT @sql = @sql + 'ALTER TABLE [' + OBJECT_NAME(parent_object_id) + '] DROP CONSTRAINT [' + name + ']; '
#     FROM sys.foreign_keys
#     WHERE referenced_object_id = OBJECT_ID('courses')
#     IF LEN(@sql) > 0 EXEC(@sql)
# """)
# cursor.execute("IF OBJECT_ID('courses', 'U') IS NOT NULL DROP TABLE courses")
# cursor.execute("IF OBJECT_ID('students', 'U') IS NOT NULL DROP TABLE students")
# cursor.execute("CREATE TABLE students (id INTEGER PRIMARY KEY IDENTITY(1,1), name VARCHAR(255), dept VARCHAR(255), age INT)")
# cursor.execute("CREATE TABLE courses (courseid INTEGER PRIMARY KEY IDENTITY(1,1), name VARCHAR(255), professor_name VARCHAR(255), studentid INT, FOREIGN KEY (studentid) REFERENCES students(id))")

# cursor.execute("""
#                INSERT INTO students (name, dept, age) values
#                 ('robert','sales',25), 
#                 ('vlad','it',27),
#                 ('andrei','sales',44)
#                """)

# conn.commit()

# cursor.execute("""
#                INSERT INTO courses (name, professor_name, studentid) values
#                 ('maths','zota',1), 
#                 ('physics','popescu',1),
#                 ('sports','ionescu',2)
#                """)

# conn.commit()



# # cursor.execute("INSERT INTO employees values (,'robert','sales',100000)")

# cursor.execute("SELECT * FROM students")

# students = cursor.fetchall()

# print(students)


# conn.close()



# # # SQLite3 example query 2 

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String

# Define the SQL Server database
DATABASE_URL = 'mssql+pyodbc://DESKTOP-3SK5E6S/school?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes'
engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()

# Test connection
try:
    with engine.connect() as connection:
        print("Database connected successfully!")
except Exception as e:
    print(f"Error connecting to database: {e}")

# # Define the Student model
class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)

# Create a new session
Session = sessionmaker(bind=engine)
session = Session()

# Adding sample data
def add_sample_students():
    students = [
        Student(name='Test1', age=30),
        Student(name='Test2', age=22),
        Student(name='Test3', age=26)
    ]
    session.add_all(students)
    session.commit()  # Commit the changes to the database
    print("Sample students added.")

add_sample_students()

# # Querying students with age > 25
students_over_25 = session.query(Student).filter(Student.age > 25).all()


# Display the results
print("Students with age greater than 25:")
for student in students_over_25:
    print(f"ID: {student.id}, Name: {student.name}, Age: {student.age}")

# Close the session
session.close()

