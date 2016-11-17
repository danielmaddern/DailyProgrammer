"""
You're challenge for today is to create a random password generator!
For extra credit, allow the user to specify the amount of passwords to generate.
For even more extra credit, allow the user to specify the length of the strings he wants to generate!
"""
import string
import random

character_set = string.ascii_letters + string.digits + string.punctuation
generated_password = ''

while True:
    # Find out what the user wants to do
    try:
        character_length = int(raw_input('This program will generate a random password, how many characters would you like? '))
        break
    except ValueError:
        print "You didn't enter a number, Try again."
        character_length = raw_input('This program will generate a random password, how many characters would you like? ')

for x in range(0, character_length):
    generated_password += random.choice(character_set)

print "Your new password is: %s" % generated_password
