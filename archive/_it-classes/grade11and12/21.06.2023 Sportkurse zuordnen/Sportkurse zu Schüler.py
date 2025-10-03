def assign_sport_courses(semester_courses, students):
    assigned_courses = [{'name': student['name'], 'courses': []} for student in students]

    for i in range(len(semester_courses)):
        semester_course = semester_courses[i]

        for student in students:
            available_courses = []

            # Filter courses based on student's preferences and constraints
            for course in semester_course:
                if (student['name'], course) not in assigned_courses[i]['courses'] and \
                        course['name'] not in student['preferences'] and \
                        (not course['is_ballsport'] or student['ballsport_count'] < 3):
                    available_courses.append(course)

            # Sort available courses by the number of assigned students
            available_courses.sort(key=lambda x: len(x['assigned_students']))

            # Find the first course that satisfies the constraints
            assigned_course = None
            for course in available_courses:
                if 15 <= len(course['assigned_students']) <= 25:
                    assigned_course = course
                    break

            if assigned_course is not None:
                assigned_courses[i]['courses'].append((student['name'], assigned_course))
                assigned_course['assigned_students'].append(student['name'])

                if assigned_course['is_ballsport']:
                    student['ballsport_count'] += 1

    return assigned_courses

import random


def assign_students_to_courses(students, sport_courses):
    assigned_courses = []

    for student in students:
        assigned_courses_per_semester = []

        for semester in range(4):
            semester_courses = [course for course in sport_courses if course['semester'] == semester+1]
            available_courses = [course for course in semester_courses if course not in assigned_courses_per_semester]
            valid_courses = []

            for course in available_courses:
                if len(course['assigned_students']) < 25 and \
                        student['name'] not in [s['name'] for s in course['assigned_students']]:
                    valid_courses.append(course)

            if not valid_courses:
                assigned_course = random.choice(available_courses)
            else:
                assigned_course = random.choice(valid_courses)

            assigned_courses_per_semester.append(assigned_course)
            assigned_course['assigned_students'].append(student)

        assigned_courses.append({'name': student['name'], 'courses': assigned_courses_per_semester})

    return assigned_courses


# Print the generated students and their preferences
'''for student in students:
    print(f"Student: {student['name']}, Preferences: {student['preferences']}")

# Print the generated sport courses
for course in sport_courses:
    print(f"Course: {course['name']}, Ballsport: {course['is_ballsport']}")'''

def create_sport_courses(num_courses):
    sport_courses = []
    semesters = [1, 1, 2, 2, 3, 3, 4, 4]  # Define the semesters for the courses
    id = 0
    for i in range(num_courses):
        name = f"Course{i+1}"
        is_ballsport = random.choice([True, False])
        semester = semesters[i % len(semesters)]  # Assign the semester cyclically
        course = f"('{name}', {is_ballsport}, {semester})"
        sport_courses.append(course)
        id += 1
    return sport_courses

# Usage:
#num_courses = 40
#sport_courses = create_sport_courses(num_courses)

# Generate the SQL file
filename = 'sport_courses.sql'
'''with open(filename, 'a') as f:
    f.write('INSERT INTO sport_courses (name, is_ballsport, semester) VALUES\n')
    f.write(',\n'.join(sport_courses))
    f.write(';')'''

import sqlite3

# Connect to the database
conn = sqlite3.connect(':memory:')  # Use an in-memory database or specify a database file name
cursor = conn.cursor()

# Read and execute the SQL statements from the file
with open('sport_courses.sql', 'r') as sql_file:
    sql_script = sql_file.read()
    cursor.executescript(sql_script)

# Execute the query to retrieve all sport courses
cursor.execute("SELECT * FROM sport_courses")

# Fetch all rows from the result set
rows = cursor.fetchall()

# Print the sport courses
"""for row in rows:
    print(row)"""
print(rows)
# Close the database connection
conn.close()

