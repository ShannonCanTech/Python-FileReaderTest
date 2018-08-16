filename = 'text_files/multi_lines.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line)