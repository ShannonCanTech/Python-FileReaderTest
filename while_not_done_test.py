filename = 'text_files/empty.txt'
prompt = "Enter your full name: "
done = False

while not done:

    full_name = raw_input(prompt)

    answer = raw_input("Do you want to enter more names? (y/n) ")
    if answer == 'n' or answer == 'no':
        break
    else:
        continue

with open(filename, 'a') as file_object:
    file_object.write(full_name)

with open(filename, 'r') as file_object:
    for line in file_object:
        print(line)