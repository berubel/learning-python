import shutil

# Create new file, if the file already exists, your content is overwritten
def write_file(text):
    f = open('test.txt', 'w')
    f.write(text)
    f.close()


# Update the file, appends a new line
def update_file(file_name, text):
    f = open(file_name, 'a')
    f.write(text)
    f.close()


# Read the content of the file
def read_file(file_name):
    f = open(file_name, 'r')
    text = f.read()
    print(text)

# Stores student grades and calculates the average
def grade_average(file_name):
    f = open(file_name, 'r')
    student_grade = f.read()
    student_grade = student_grade.split('\n')
    print(student_grade)
    average_list = []

    for x in student_grade:
        grade_list = x.split(',')
        student = grade_list[0]
        grade_list.pop(0)
        print('\n{}'.format(student))
        print(grade_list)
        average = lambda grades: sum([int(i) for i in grades]) / 3
        print('Average: {:.2f}'.format(average(grade_list)))
        average_list.append({student: average(grade_list)})
    return average_list


# Copy the file to another directory
def copy_file(file_name):
    path = (r'C:\Users\bebel\Downloads')
    shutil.copy(file_name, path)


# Move the file to another directory
def move_file(file_name):
    path = (r'C:\Users\bebel\Downloads')
    shutil.move(file_name, path)


if __name__ == '__main__':
    grade_list = grade_average('grades.txt')
    print('\n{}'.format(grade_list))
    # move_file('grades.txt')
    # copy_file('grades.txt')
    # write_file('First line.\n')
    # student = 'Ana, 40, 45, 40\n'
    # update_file('grades.txt', student)
    # read_file('test.txt')
