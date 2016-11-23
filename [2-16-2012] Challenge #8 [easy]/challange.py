"""
write a program that will print the song "99 bottles of beer on the wall".
for extra credit, do not allow the program to print each loop on a new line.
"""

for x in range(99, -1, -1):
    if x == 0:
        print 'No more bottles of beer on the wall, no more bottles of beer.'
        print 'Go to the store and buy some more, 99 bottles of beer on the wall.'
    else:
        print '%s bottles of beer on the wall, %s bottles of beer.' % (x, x)
        print 'Take one down and pass it around, %s bottles of beer on the wall. \n' % x
