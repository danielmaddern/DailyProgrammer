"""
write a program that will print the song "99 bottles of beer on the wall".
for extra credit, do not allow the program to print each loop on a new line.
"""

for beers in range(99, -1, -1):
    if beers == 0:
        print 'No more bottles of beer on the wall, no more bottles of beer.'
        print 'Go to the store and buy some more, 99 bottles of beer on the wall.'
    elif beers == 1:
        print '%s bottles of beer on the wall, %s bottles of beer.' % (beers, beers)
        print 'Take one down and pass it around, no more bottles of beer on the wall. \n'
    else:
        print '%s bottles of beer on the wall, %s bottles of beer.' % (beers, beers)
        print 'Take one down and pass it around, %s bottles of beer on the wall. \n' % (beers - 1)
