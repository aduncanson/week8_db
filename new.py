import sqlite3

connection = sqlite3.connect("college_database.db")

cursor = connection.cursor()

sql_command = """
CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY,
    student_name VARCHAR(255)
);
"""
cursor.execute(sql_command)

sql_command = """
CREATE TABLE IF NOT EXISTS subjects (
    subject_id INTEGER PRIMARY KEY,
    subject_title VARCHAR(255)
);
"""
cursor.execute(sql_command)

sql_command = """
CREATE TABLE IF NOT EXISTS student_subjects (
    student_id INTEGER,
    subject_id INTEGER
);
"""
cursor.execute(sql_command)

sql_command = """
INSERT INTO students (student_id, student_name) VALUES
    (1, 'Adam A'),
    (2, 'Betty B'),
    (3, 'Charlie C'),
    (4, 'David D'),
    (5, 'Emma E')
;
"""
cursor.execute(sql_command)

sql_command = """
INSERT INTO subjects (subject_id, subject_title) VALUES
    (1, 'Maths'),
    (2, 'English'),
    (3, 'Science'),
    (4, 'Art'),
    (5, 'PE')
;
"""
cursor.execute(sql_command)

sql_command = """
INSERT INTO student_subjects (student_id, subject_id) VALUES
    (1, 1),
    (1, 2),
    (2, 1),
    (2, 3),
    (3, 1),
    (3, 4),
    (4, 1),
    (4, 5),
    (5, 1),
    (5, 2),
    (5, 3)
;
"""
cursor.execute(sql_command)

connection.commit()

sql_command = """
SELECT stu.student_name, sub.subject_title FROM students stu
INNER JOIN student_subjects sts ON stu.student_id = sts.student_id
INNER JOIN subjects sub ON sts.subject_id = sub.subject_id
;
"""
cursor.execute(sql_command)

result = cursor.fetchall()
#result = cursor.fetchone()

for row in result:
    print('{0} : {1}'.format(row[0], row[1]))

print(result)
