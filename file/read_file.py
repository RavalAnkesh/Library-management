# Reading from a file
#open file
with open('student.txt', 'r') as file:
    #read the open file
    content = file.read()

    #print file content
    print(content)
