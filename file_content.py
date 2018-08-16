filename = 'text_files/multi_lines.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

txt_string = ''
for line in lines:
    txt_string += line.strip()

print(txt_string)
print(len(txt_string))