# Take at a look at the physical text file to see the new text appended (or added) to it
# Adds content to the file instead of writing over it
filename = 'text_files/empty.txt'

with open(filename, 'a') as file_object:
    file_object.write("\nWe're adding this line of text to the file.")

with open(filename, 'r') as file_object:
    for line in file_object:
        print(line)