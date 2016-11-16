"""
create a program that will ask the users name, age, and reddit username. have it tell them the information back, in the format:
your name is (blank), you are (blank) years old, and your username is (blank)
for extra credit, have the program log this information in a file to be accessed later.
"""

name = raw_input('Enter your name:')
age = raw_input('Enter your age:')
username = raw_input('Enter your Reddit username:')

output = "your name is %s, you are %s years old, and your username is %s" % (name, age, username)
print output

# Extra Credit
with open('output.file', 'w') as f:
    f.write(output)
