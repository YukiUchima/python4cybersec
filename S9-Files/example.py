import json
import bcrypt
import logging

filename = 'test.txt'
test_text = "this is a test file"

# ------------------------ #41) Writing to files
# file modes: 
# w: overwrite file
# a: append to file
# r: read from file

# f = open(filename, 'a')
# f.write('1: Adding a new line to the file\n')
# f.write('2: Adding a new line to the file\n')
# f.write('3: Adding a new line to the file\n')
# f.close() # Always close file you are editing

# ------------------------ #42) Files to List
# lines = []
# f = open(filename, 'r')     # read file
# lines = f.readlines()
# f.close()

# for line in lines:
#     print(line)

# ------------------------ #43) Properly using files
# with open(filename, 'w') as f:   # automatically closes after use
#     f.write('Hello!')
#     f.close()
# NEVER PLACE PASSWORDS, KEYS, INSIDE SOURCE CODE

# ------------------------ #44) Hiding Sensitive Information
# with open('credentials.json', 'r') as cred_file:
#     data = json.load(cred_file)
#     print(data)
#     cred_file.close()

# email = data['email_credentials']['email']
# print(email)
# password = data['email_credentials']['password']
# encrypted_password =  bcrypt.hashpw(password.encode(), bcrypt.gensalt())

# print(encrypted_password.decode())

# ------------------------ #45) Logging
# logging levels: debug, info, warning, error, critical
filename = 'example.log'

logging.basicConfig(filename=filename, filemode='a', level=logging.INFO,format="%(asctime)s : %(levelname)s - %(message)s")

#test
logging.info('This is a log message')