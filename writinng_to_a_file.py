filename = 'text_files/empty.txt'

with open(filename, 'w') as file_object:
    file_object.write("This is some text written from the program.")

with open(filename, 'r') as file_object:
    for line in file_object:
        print(line)