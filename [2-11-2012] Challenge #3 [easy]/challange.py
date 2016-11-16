"""
https://www.reddit.com/r/dailyprogrammer/comments/pkw2m/2112012_challenge_3_easy/
Welcome to cipher day!
write a program that can encrypt texts with an alphabetical caesar cipher. This cipher can ignore numbers, symbols, and whitespace.
for extra credit, add a "decrypt" function to your program!
"""
letters = list('abcdefghijklmnopqrstuvwxyz')

while True:
    # Find out what the user wants to do
    user_choice = raw_input('Would you like to [e]ncrypt, [d]ecrypt or [q]uit?  ')
    if user_choice.lower() == 'e':
        encrypted_text = ''
        while True:
            try:
                shift_by_number_of_letters = int(raw_input('Enter the number of letters you wish to shift by: '))
                break
            except ValueError:
                print "You didn't enter a number, Try again."
        string_to_encrypt = list(raw_input('Enter the string you would like to encrypt: '))

        for x in string_to_encrypt:
            added_to_encrypted_string = False
            for y in letters:
                if x.lower() == y:
                    new_letter = shift_by_number_of_letters + letters.index(y)
                    if new_letter > 25:
                        new_letter -= 26
                    encrypted_text = encrypted_text + letters[new_letter]
                    added_to_encrtyped_string = True
            if added_to_encrypted_string == False:
                encrypted_text = encrypted_text + x

        print "You encrypted text is: %s" % encrypted_text

    elif user_choice.lower() == 'd':
        pass
    elif user_choice.lower() == 'q':
        break
    else:
        print "%s is not a valid option not entered, try again." % user_choice
        user_choice = raw_input('Would you like to [e]ncrypt, [d]ecrypt or [q]uit?  ')
