filename = 'text_files/multi_lines.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

txt_string = ''
for line in lines:
    txt_string += line.strip()

the_word = "line"
if the_word in txt_string:
    print("Yes the word 'line' is within this file.")
else:
    print("No 'line' in file.")