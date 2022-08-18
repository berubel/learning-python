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


if __name__ == '__main__':
    # write_file('First line.\n')
    student = 'Gabriele, 85, 95, 90'
    update_file('grades.txt', student)
    # read_file('test.txt')
