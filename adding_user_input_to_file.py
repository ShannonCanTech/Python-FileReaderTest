full_name = raw_input("Enter your full name: ")
email_address = raw_input("Enter your email address: ")
phone_number = raw_input("Enter your phone number: ")

filename = 'text_files/user_input.txt'
with open(filename, 'w') as file_object:
    file_object.write(full_name.title() + '\n')
    file_object.write(email_address + '\n')
    file_object.write(phone_number + '\n')

with open(filename, 'r') as file_object:
    for lines in file_object:
        print lines