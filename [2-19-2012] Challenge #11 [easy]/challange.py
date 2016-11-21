"""
The program should take three arguments.
The first will be a day, the second will be month, and the third will be year.
Then, your program should compute the day of the week that date will fall on.

"""
import datetime

print "This program will tell you what day a particular date falls on."
# Enter a Day:
while True:
    # Find out what the user wants to do
    try:
        day = int(raw_input('Enter the day part of your date: '))
        if 1 <= day <= 31:
            break
        else:
            print 'Day you entered was not between 1 and 31'
    except ValueError:
        print "You didn't enter a number, Try again."
        # day = raw_input('Enter the day part of your date: ')

while True:
    # Find out what the user wants to do
    try:
        month = int(raw_input('Enter the month part of your date: '))
        if 1 <= month <= 12:
            break
        else:
            print 'Month you entered was not between 1 and 12'
    except ValueError:
        print "You didn't enter a number, Try again."
        # month = raw_input('Enter the month part of your date: ')

while True:
    # Find out what the user wants to do
    try:
        year = int(raw_input('Enter the year part of your date: '))
        if 1900 <= year <= 2016:
            break
        else:
            print 'Day you entered was not between 1900 and 2016'
    except ValueError:
        print "You didn't enter a number, Try again."
        # year = raw_input('Enter the year part of your date: ')

date_to_convert = '%s %s %s' % (day, month, year)
day_to_print = datetime.datetime.strptime(date_to_convert, '%d %m %Y').strftime('%A')
print "The day for %s/%s/%s is %s." % (day, month, year, day_to_print)
